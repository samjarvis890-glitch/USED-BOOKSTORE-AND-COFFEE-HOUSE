import urllib.request
import os
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

images = {
    'contact-hero.jpg': 'https://images.unsplash.com/photo-1524995997946-a1c2e315a42f?q=80&w=1920&auto=format&fit=crop',
    'contact-form-bg.jpg': 'https://images.unsplash.com/photo-1481627834876-b7833e8f5570?q=80&w=1920&auto=format&fit=crop',
    'contact-map.jpg': 'https://images.unsplash.com/photo-1524661135-423995f22d0b?q=80&w=1920&auto=format&fit=crop',
    'contact-extra.jpg': 'https://images.unsplash.com/photo-1511882150382-421056c89033?q=80&w=1920&auto=format&fit=crop'
}

os.makedirs(os.path.join('images', 'contact'), exist_ok=True)

for filename, url in images.items():
    filepath = os.path.join('images', 'contact', filename)
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response, open(filepath, 'wb') as out_file:
            data = response.read()
            out_file.write(data)
        print(f"Successfully downloaded {filename}")
    except Exception as e:
        print(f"Failed to download {filename}: {e}")
