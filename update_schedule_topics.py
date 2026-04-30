import re

themes = [
    "The Quest for Profit and Internal Awakening",
    "Authentication — Myth vs. Reality",
    "Shravan Vidhi — The Methodology of Listening",
    "The Art of Inquiry and the Role of the Guru",
    "The Supreme Gift — Value of Kathamrit over Amrit",
    "Understanding and Overcoming the Fear of Death",
    "The Three Tapa — Identifying the Sources of Suffering",
    "Sachchidananda — Exploring our Divine Identity",
    "The Role of God and the Ultimate Grace of Radha"
]

html_to_insert = ''
for i in range(1, 10):
    display = '' if i == 1 else ' style="display:none;"'
    theme = themes[i-1]
    html_to_insert += f"""    <!-- Day {i} -->
    <div class="schedule-day-panel" id="day-{i}"{display}>
      <div class="schedule-day-title">
        <h3>Day {i}</h3>
        <p>{theme}</p>
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

pattern = re.compile(r'    <!-- Day 1 -->.*?    </div>\n(?=  </div>\n</section>)', re.DOTALL)
new_content = pattern.sub(html_to_insert, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
print("Updated topics successfully")
