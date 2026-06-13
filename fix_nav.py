import os

directory = r"d:\USED BOOKSTORE AND COFFEE HOUSE"

target = '<li class="nav-item dropdown"><a class="nav-link dropdown-toggle" href="#" id="navbarDropdownHome" role="button" data-bs-toggle="dropdown" aria-expanded="false">Home</a><ul class="dropdown-menu border-0 shadow-sm" aria-labelledby="navbarDropdownHome"><li><a class="dropdown-item" href="index.html">Home 1</a></li><li><a class="dropdown-item" href="home2.html">Home 2</a></li></ul></li>'

replacement = '<li class="nav-item"><a class="nav-link" href="index.html">Home 1</a></li>\n          <li class="nav-item"><a class="nav-link" href="home2.html">Home 2</a></li>'

for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if target in content:
            content = content.replace(target, replacement)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated {filename}")
