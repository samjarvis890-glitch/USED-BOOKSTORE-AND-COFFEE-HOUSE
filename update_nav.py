import os
import re

directory = r'd:\USED BOOKSTORE AND COFFEE HOUSE'
target_dropdown = """<li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" id="navbarDropdownHome" role="button" data-bs-toggle="dropdown" aria-expanded="false">
              Home
            </a>
            <ul class="dropdown-menu border-0 shadow-sm" aria-labelledby="navbarDropdownHome">
              <li><a class="dropdown-item" href="index.html">Home 1</a></li>
              <li><a class="dropdown-item" href="home2.html">Home 2</a></li>
            </ul>
          </li>"""

for filename in os.listdir(directory):
    if filename.endswith('.html'):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        original_content = content
        
        # Replace Home 1 / Home 2
        pattern1 = r'<li class="nav-item">\s*<a class="nav-link" href="index\.html">Home 1</a>\s*</li>\s*<li class="nav-item">\s*<a class="nav-link" href="home2\.html">Home 2</a>\s*</li>'
        content = re.sub(pattern1, target_dropdown, content)
        
        # Replace single Home (if it doesn't already have dropdown)
        pattern2 = r'<li class="nav-item">\s*<a class="nav-link" href="index\.html">Home</a>\s*</li>'
        content = re.sub(pattern2, target_dropdown, content)
        
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f'Updated {filename}')
