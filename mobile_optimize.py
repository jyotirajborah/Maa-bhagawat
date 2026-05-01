import re

def optimize_html(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Replace inline grids with CSS classes
    content = content.replace(
        '<div style="display:grid;grid-template-columns:1fr 1fr;gap:32px;align-items:start;">',
        '<div class="why-listen-grid">'
    )
    content = content.replace(
        '<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:24px;margin-top:48px;">',
        '<div class="benefits-grid">'
    )
    content = content.replace(
        '<div style="display:grid;grid-template-columns:1fr 1fr;gap:50px;align-items:start;">',
        '<div class="unique-grid">'
    )
    
    # 2. Add the new classes to the main CSS block (before @media)
    new_css_classes = """
  .why-listen-grid { display:grid; grid-template-columns:1fr 1fr; gap:32px; align-items:start; }
  .benefits-grid { display:grid; grid-template-columns:repeat(3,1fr); gap:24px; margin-top:48px; }
  .unique-grid { display:grid; grid-template-columns:1fr 1fr; gap:50px; align-items:start; }
"""
    # Insert new classes right before the @media (max-width: 768px) block
    content = content.replace('  @media (max-width: 768px) {', new_css_classes + '  @media (max-width: 768px) {')
    
    # 3. Update @media (max-width: 768px)
    media_query_addition = """
    .section-container { padding: 60px 20px; }
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
    # Find the opening brace of @media (max-width: 768px) { and insert additions right after
    content = content.replace(
        '  @media (max-width: 768px) {',
        '  @media (max-width: 768px) {' + media_query_addition
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print("Optimization applied successfully.")

if __name__ == '__main__':
    optimize_html('index.html')
