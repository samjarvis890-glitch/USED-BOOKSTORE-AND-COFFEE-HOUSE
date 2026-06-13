import os
import glob
import re

html_files = glob.glob('*.html')

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Navbar logo
    # Current: <img src="images/logo.png" alt="Folio & Froth Logo" style="height: 55px; width: 55px; object-fit: contain;">
    content = re.sub(
        r'<img src="images/logo\.png" alt="Folio & Froth Logo" style="height: 55px; width: 55px; object-fit: contain;">',
        '<img src="images/logo.png" alt="Folio & Froth Logo" style="height: 65px; width: auto; max-width: 250px; object-fit: contain; mix-blend-mode: multiply;" class="transition-transform duration-300 hover:scale-105">',
        content
    )

    # 2. Footer logo
    # Current: <div class="inline-block">\s*<img src="images/logo\.png" alt="Folio & Froth" class="h-16 w-16 object-contain" style="filter: drop-shadow\(0 4px 6px rgba\(0,0,0,0\.3\)\);">\s*</div>
    footer_logo_pattern = r'<div class="inline-block">\s*<img src="images/logo\.png" alt="Folio & Froth" class="h-16 w-16 object-contain" style="filter: drop-shadow\(0 4px 6px rgba\(0,0,0,0\.3\)\);">\s*</div>'
    footer_logo_new = """<div class="bg-[#F8F5F0] p-3 rounded-2xl inline-block shadow-lg border-2 border-[#C4A484]/50 transition-transform duration-300 hover:-translate-y-1">
            <img src="images/logo.png" alt="Folio & Froth" style="height: 50px; width: auto; object-fit: contain;">
          </div>"""
    content = re.sub(footer_logo_pattern, footer_logo_new, content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated logo display settings in all HTML files.")
