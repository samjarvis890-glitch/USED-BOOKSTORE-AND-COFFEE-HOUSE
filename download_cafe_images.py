import urllib.request
import os
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

images = {
    'cafe_hero.jpg': 'https://images.unsplash.com/photo-1509042239860-f550ce710b93?q=80&w=1920&auto=format&fit=crop',
    'signature_espresso.jpg': 'https://images.unsplash.com/photo-1514432324607-a09d9b4aefdd?q=80&w=800&auto=format&fit=crop',
    'signature_cappuccino.jpg': 'https://images.unsplash.com/photo-1572442388796-11668a67e53d?q=80&w=800&auto=format&fit=crop',
    'signature_nitro.jpg': 'https://images.unsplash.com/photo-1461023058943-07fcbe16d735?q=80&w=800&auto=format&fit=crop',
    'menu_latte.jpg': 'https://images.unsplash.com/photo-1511920170033-f8396924c348?q=80&w=400&auto=format&fit=crop',
    'menu_croissant.jpg': 'https://images.unsplash.com/photo-1530610476181-d83430b64dcd?q=80&w=400&auto=format&fit=crop',
    'menu_pourover.jpg': 'https://images.unsplash.com/photo-1551887196-72e32bfc7bf3?q=80&w=400&auto=format&fit=crop',
    'menu_tea.jpg': 'https://images.unsplash.com/photo-1515823662972-da6a2e4d3002?q=80&w=400&auto=format&fit=crop',
    'gallery_1.jpg': 'https://images.unsplash.com/photo-1442512595331-e89e73853f31?q=80&w=800&auto=format&fit=crop',
    'gallery_2.jpg': 'https://images.unsplash.com/photo-1554118811-1e0d58224f24?q=80&w=800&auto=format&fit=crop',
    'gallery_3.jpg': 'https://images.unsplash.com/photo-1481833761820-0509d3217039?q=80&w=800&auto=format&fit=crop',
    'gallery_4.jpg': 'https://images.unsplash.com/photo-1505682634904-d7c8d95cdc50?q=80&w=800&auto=format&fit=crop',
    'seating_cozy.jpg': 'https://images.unsplash.com/photo-1519681393784-d120267933ba?q=80&w=800&auto=format&fit=crop',
    'seating_study.jpg': 'https://images.unsplash.com/photo-1524995997946-a1c2e315a42f?q=80&w=800&auto=format&fit=crop',
    'seating_lounge.jpg': 'https://images.unsplash.com/photo-1540518614846-7eded433c457?q=80&w=800&auto=format&fit=crop',
    'cafe_cta.jpg': 'https://images.unsplash.com/photo-1525610553991-2bede1a236e2?q=80&w=1920&auto=format&fit=crop'
}

os.makedirs('images', exist_ok=True)

for filename, url in images.items():
    filepath = os.path.join('images', filename)
    print(f"Downloading {filename}...")
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response, open(filepath, 'wb') as out_file:
            data = response.read()
            out_file.write(data)
        print(f"Successfully downloaded {filename}")
    except Exception as e:
        print(f"Failed to download {filename}: {e}")

print("All HD images downloaded successfully.")
