html = ''
for i in range(1, 10):
    display = '' if i == 1 else ' style="display:none;"'
    html += f"""    <!-- Day {i} -->
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

with open('generated_schedule.txt', 'w', encoding='utf-8') as f:
    f.write(html)
