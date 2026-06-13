import urllib.request
import os
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

images = {
    'books-hero.jpg': 'https://images.unsplash.com/photo-1507842217343-583bb7270b66?q=80&w=1920&auto=format&fit=crop',
    'genre-fiction.jpg': 'https://images.unsplash.com/photo-1512820790803-83ca734da794?q=80&w=800&auto=format&fit=crop',
    'genre-mystery.jpg': 'https://images.unsplash.com/photo-1626618012641-bfbca5a31239?q=80&w=800&auto=format&fit=crop',
    'genre-nonfiction.jpg': 'https://images.unsplash.com/photo-1456513080510-7bf3a84b82f8?q=80&w=800&auto=format&fit=crop',
    'genre-history.jpg': 'https://images.unsplash.com/photo-1461360370896-922624d12aa1?q=80&w=800&auto=format&fit=crop',
    'genre-fantasy.jpg': 'https://images.unsplash.com/photo-1618666012174-83b441c0bc76?q=80&w=800&auto=format&fit=crop',
    'genre-classics.jpg': 'https://images.unsplash.com/photo-1555448248-2571daf6344b?q=80&w=800&auto=format&fit=crop',
    'bestseller-1.jpg': 'https://images.unsplash.com/photo-1544947950-fa07a98d237f?q=80&w=800&auto=format&fit=crop',
    'bestseller-2.jpg': 'https://images.unsplash.com/photo-1589829085413-56de8ae18c73?q=80&w=800&auto=format&fit=crop',
    'bestseller-3.jpg': 'https://images.unsplash.com/photo-1589998059171-988d887df646?q=80&w=800&auto=format&fit=crop',
    'rare-1.jpg': 'https://images.unsplash.com/photo-1550399105-c4db5fb85c18?q=80&w=800&auto=format&fit=crop',
    'rare-2.jpg': 'https://images.unsplash.com/photo-1535905557558-afc4877a26fc?q=80&w=800&auto=format&fit=crop',
    'search-bg.jpg': 'https://images.unsplash.com/photo-1481627834876-b7833e8f5570?q=80&w=1920&auto=format&fit=crop',
    'cta.jpg': 'https://images.unsplash.com/photo-1506880018603-83d5b814b5a6?q=80&w=1920&auto=format&fit=crop',
    'book-search-1.jpg': 'https://images.unsplash.com/photo-1543002588-bfa74002ed7e?q=80&w=800&auto=format&fit=crop',
    'book-search-2.jpg': 'https://images.unsplash.com/photo-1474366521946-c3d4b507abf2?q=80&w=800&auto=format&fit=crop',
    'book-search-3.jpg': 'https://images.unsplash.com/photo-1587876931567-564ce588bfbd?q=80&w=800&auto=format&fit=crop',
    'book-search-4.jpg': 'https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=800&auto=format&fit=crop'
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
