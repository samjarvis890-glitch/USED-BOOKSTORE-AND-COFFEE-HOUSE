import urllib.request
import os
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

images = {
    'tradein-hero.jpg': 'https://images.unsplash.com/photo-1491841550275-ad7854e35ca6?q=80&w=1920&auto=format&fit=crop',
    'tradein-step-1.jpg': 'https://images.unsplash.com/photo-1526243741027-444d633d7365?q=80&w=800&auto=format&fit=crop',
    'tradein-step-2.jpg': 'https://images.unsplash.com/photo-1456513080510-7bf3a84b82f8?q=80&w=800&auto=format&fit=crop',
    'tradein-step-3.jpg': 'https://images.unsplash.com/photo-1509042239860-f550ce710b93?q=80&w=800&auto=format&fit=crop',
    'tradein-category-textbook.jpg': 'https://images.unsplash.com/photo-1532012197267-da84d127e765?q=80&w=800&auto=format&fit=crop',
    'tradein-category-fiction.jpg': 'https://images.unsplash.com/photo-1544947950-fa07a98d237f?q=80&w=800&auto=format&fit=crop',
    'tradein-category-collectible.jpg': 'https://images.unsplash.com/photo-1589829085413-56de8ae18c73?q=80&w=800&auto=format&fit=crop',
    'tradein-benefits.jpg': 'https://images.unsplash.com/photo-1490806843957-31f4c9a91c65?q=80&w=800&auto=format&fit=crop',
    'tradein-cta.jpg': 'https://images.unsplash.com/photo-1495446815901-a7297e633e8d?q=80&w=1920&auto=format&fit=crop'
}

os.makedirs('images/tradein', exist_ok=True)

for filename, url in images.items():
    filepath = os.path.join('images/tradein', filename)
    print(f"Downloading {filename}...")
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response, open(filepath, 'wb') as out_file:
            data = response.read()
            out_file.write(data)
        print(f"Successfully downloaded {filename}")
    except Exception as e:
        print(f"Failed to download {filename}: {e}")

print("All trade-in HD images downloaded successfully.")
