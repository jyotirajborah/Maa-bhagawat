import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the duplicated injected grid classes
dup_classes = """  .why-listen-grid { display:grid; grid-template-columns:1fr 1fr; gap:32px; align-items:start; }
  .benefits-grid { display:grid; grid-template-columns:repeat(3,1fr); gap:24px; margin-top:48px; }
  .unique-grid { display:grid; grid-template-columns:1fr 1fr; gap:50px; align-items:start; }
"""
content = content.replace(dup_classes, '', 1) # remove the first occurrence (at line 616)

dup_media = """    .section-container { padding: 60px 20px; }
    .why-listen-grid, .benefits-grid, .unique-grid, .venue-grid { grid-template-columns: 1fr; }
    .hero { padding: 120px 20px 80px; }
    .schedule-tabs { 
      justify-content: flex-start; 
      overflow-x: auto; 
      white-space: nowrap; 
      -webkit-overflow-scrolling: touch; 
      padding-bottom: 10px;
    }
    .schedule-tab { flex: 0 0 auto; }
"""
content = content.replace(dup_media, '', 1) # remove first occurrence (at line 620)

# Now fix the mobile navigation
content = content.replace(
    '    .nav-links { display: none; }',
    '''    .nav-links { 
      display: flex; 
      overflow-x: auto; 
      white-space: nowrap; 
      -webkit-overflow-scrolling: touch; 
      padding-bottom: 10px;
      scrollbar-width: none;
      width: 100%;
      margin-top: 12px;
    }
    .nav-links::-webkit-scrollbar { display: none; }
    nav { flex-wrap: wrap; justify-content: space-between; }'''
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Cleanup applied")
