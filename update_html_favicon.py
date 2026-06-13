import glob
import re

html_files = glob.glob('*.html')

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Change favicon link from logo.png to favicon.png
    content = re.sub(
        r'<link rel="icon" type="image/png" href="images/logo\.png">',
        '<link rel="icon" type="image/png" href="images/favicon.png">',
        content
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated favicon link in all HTML files.")
