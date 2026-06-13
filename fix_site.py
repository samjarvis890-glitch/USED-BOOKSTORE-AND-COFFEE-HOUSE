import os
import glob
import re

html_files = glob.glob('*.html')

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Fix favicon
    # <link rel="icon" type="image/png" href="assets/images/logo/favicon.png"> -> <link rel="icon" type="image/png" href="images/logo.png">
    content = re.sub(
        r'<link\s+rel="icon"\s+type="image/png"\s+href="(?:assets/)?images/logo/(?:favicon\.png|logo\.svg)">',
        '<link rel="icon" type="image/png" href="images/logo.png">',
        content
    )
    # Just in case there's another variation
    content = re.sub(
        r'<link rel="icon" type="image/png" href="assets/images/logo/favicon.png">',
        '<link rel="icon" type="image/png" href="images/logo.png">',
        content
    )

    # 2. Fix navbar logo
    nav_logo_old = r'<a class="navbar-brand d-flex align-items-center" href="index\.html">\s*<img src="assets/images/logo/logo\.svg" alt="Folio & Froth Logo" style="height: 55px; width: auto;">\s*</a>'
    nav_logo_new = """<a class="navbar-brand d-flex align-items-center" href="index.html">
        <img src="images/logo.png" alt="Folio & Froth Logo" style="height: 55px; width: 55px; object-fit: contain;">
      </a>"""
    content = re.sub(nav_logo_old, nav_logo_new, content)

    # 3. Fix footer logo
    footer_logo_old = r'<div class="bg-white/5 p-4 rounded-xl inline-block backdrop-blur-sm border border-white/10">\s*<img src="assets/images/logo/logo\.svg" alt="Folio & Froth" class="h-16" style="filter: drop-shadow\(0 4px 6px rgba\(0,0,0,0\.3\)\);">\s*</div>'
    footer_logo_new = """<div class="inline-block">
            <img src="images/logo.png" alt="Folio & Froth" class="h-16 w-16 object-contain" style="filter: drop-shadow(0 4px 6px rgba(0,0,0,0.3));">
          </div>"""
    content = re.sub(footer_logo_old, footer_logo_new, content)

    # 4. Fix footer book icon alignment
    # "footer above round side inside book icon have alignment center fix"
    # Old:
    # <div class="absolute top-0 bg-[#6F4E37] text-[#EADBC8] w-20 h-20 rounded-full flex items-center justify-center shadow-lg border-4 border-[#EADBC8]" style="left: 50%; transform: translate(-50%, -50%);">
    # New:
    # <div class="absolute top-0 bg-[#6F4E37] text-[#EADBC8] w-20 h-20 rounded-full d-flex align-items-center justify-content-center shadow-lg border-4 border-[#EADBC8]" style="left: 50%; transform: translate(-50%, -50%); display: flex; align-items: center; justify-content: center;">
    
    icon_div_old = r'<div class="absolute top-0 bg\[#6F4E37\] text\[#EADBC8\] w-20 h-20 rounded-full flex items-center justify-center shadow-lg border-4 border\[#EADBC8\]" style="left: 50%; transform: translate\(-50%, -50%\);">\s*<i class="fas fa-book-open text-2xl"></i>\s*</div>'
    icon_div_new = """<div class="absolute top-0 bg-[#6F4E37] text-[#EADBC8] w-20 h-20 rounded-full d-flex align-items-center justify-content-center shadow-lg border-4 border-[#EADBC8]" style="left: 50%; transform: translate(-50%, -50%); display: flex; align-items: center; justify-content: center;">
      <i class="fas fa-book-open text-2xl" style="display: block; text-align: center; margin: auto;"></i>
    </div>"""
    
    # We will just do a simpler string replace for the div opening tag
    div_old_str = '<div class="absolute top-0 bg-[#6F4E37] text-[#EADBC8] w-20 h-20 rounded-full flex items-center justify-center shadow-lg border-4 border-[#EADBC8]" style="left: 50%; transform: translate(-50%, -50%);">'
    div_new_str = '<div class="absolute top-0 bg-[#6F4E37] text-[#EADBC8] w-20 h-20 rounded-full d-flex align-items-center justify-content-center shadow-lg border-4 border-[#EADBC8]" style="left: 50%; transform: translate(-50%, -50%); display: flex; align-items: center; justify-content: center;">'
    
    content = content.replace(div_old_str, div_new_str)

    # Let's also do a second pass for the `<i>` tag just in case it needs fixing too:
    # Actually wait, adding `margin: auto;` or `display: block` inside the `<i>` can fix any FontAwesome weirdness if it's not perfectly centered. Let's replace the inner tag too.
    i_old = '<i class="fas fa-book-open text-2xl"></i>'
    i_new = '<i class="fas fa-book-open text-2xl" style="margin: auto;"></i>'
    # we only want to replace it inside that specific div!
    # Let's use regex for the whole block:
    
    block_pattern = r'<div class="absolute top-0 bg\[#6F4E37\] text\[#EADBC8\] w-20 h-20 rounded-full flex items-center justify-center shadow-lg border-4 border\[#EADBC8\]" style="left: 50%; transform: translate\(-50%, -50%\);">\s*<i class="fas fa-book-open text-2xl"></i>\s*</div>'
    block_replacement = """<div class="absolute top-0 bg-[#6F4E37] text-[#EADBC8] w-20 h-20 rounded-full d-flex align-items-center justify-content-center shadow-lg border-4 border-[#EADBC8]" style="left: 50%; transform: translate(-50%, -50%); display: flex; align-items: center; justify-content: center;">
      <i class="fas fa-book-open text-2xl" style="margin-top: 2px;"></i>
    </div>"""
    # Wait, the user said "inside book icon have alignment center fix"
    # Actually, FontAwesome icons sometimes appear slightly off-center vertically. `margin-top: 2px` or just relying on `d-flex align-items-center justify-content-center` might work. Let's just use `d-flex align-items-center justify-content-center`.
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
print("Done fixing site.")
