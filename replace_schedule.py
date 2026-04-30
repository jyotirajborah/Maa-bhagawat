import re

html_to_insert = ''
for i in range(1, 10):
    display = '' if i == 1 else ' style="display:none;"'
    html_to_insert += f"""    <!-- Day {i} -->
    <div class="schedule-day-panel" id="day-{i}"{display}>
      <div class="schedule-day-title">
        <h3>Day {i}</h3>
        <p>Divine Discourse</p>
      </div>
      <div class="schedule-timeline">
        <div class="timeline-item" style="animation-delay:0s"><div class="timeline-time">06:30 PM</div><div class="timeline-dot"></div><div class="timeline-content"><div class="timeline-content-inner"><h4>Mangalacharan</h4><p>Sacred Invocation</p></div></div></div>
        <div class="timeline-item" style="animation-delay:0.1s"><div class="timeline-time">06:45 PM</div><div class="timeline-dot"></div><div class="timeline-content"><div class="timeline-content-inner"><h4>Shrimad Bhagwat Mahapuran Pravachan</h4><p>Divine Discourse by Raseshwari Devi Ji</p></div></div></div>
        <div class="timeline-item" style="animation-delay:0.2s"><div class="timeline-time">08:15 PM</div><div class="timeline-dot"></div><div class="timeline-content"><div class="timeline-content-inner"><h4>Aarti</h4><p>Evening Conclusion</p></div></div></div>
      </div>
    </div>
"""

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# We need to replace everything from <!-- Day 1 --> to the end of <!-- Day 9 --> panel.
# We can find <!-- Day 1 --> and then the end of the day-9 panel.
start_idx = content.find('<!-- Day 1 -->')
end_idx = content.find('<!-- SNEAK PEEK VIDEOS -->')

# Actually, the days are inside `<div class="schedule-day-panel"` blocks.
# Let's find exactly the range:
if start_idx != -1 and end_idx != -1:
    # We want to replace from start_idx up to the last `</div>\n    </div>\n  </div>\n</section>\n\n\n<!-- SNEAK PEEK VIDEOS -->`
    # Let's find the `</div>\n  </div>\n</section>` before SNEAK PEEK
    end_of_schedule = content.rfind('  </div>\n</section>', start_idx, end_idx)
    
    # Actually the panels are wrapped in `<div class="schedule-days-container">` which has a closing `</div>`?
    # No, wait, looking at my view_file output:
    # 1457:     </div>
    # 1458:   </div>
    # 1459: </section>
    
    # We just need to replace from `<!-- Day 1 -->` up to `<!-- Day 9 -->`'s closing `</div>`
    
    # Let's use regex to replace `<!-- Day 1 -->.*?(?=  </div>\n</section>)` with `html_to_insert`
    # The container ends at `  </div>\n</section>`
    pattern = re.compile(r'    <!-- Day 1 -->.*?    </div>\n(?=  </div>\n</section>)', re.DOTALL)
    new_content = pattern.sub(html_to_insert, content)
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Replaced successfully")
else:
    print("Could not find start/end indices")
