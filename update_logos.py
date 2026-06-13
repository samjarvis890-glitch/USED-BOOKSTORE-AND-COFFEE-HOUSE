import os
import glob

directory = r"d:\USED BOOKSTORE AND COFFEE HOUSE"
html_files = glob.glob(os.path.join(directory, "*.html"))

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = content.replace('logo.png', 'logo.svg').replace('favicon.png', 'favicon.svg')
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {os.path.basename(filepath)}")

print("Done updating logo references.")
