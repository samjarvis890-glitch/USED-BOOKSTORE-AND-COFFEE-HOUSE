import urllib.request
import os
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

images = {
    # UI Layout Images (Unsplash HD)
    'home_hero.jpg': 'https://images.unsplash.com/photo-1506880018603-83d5b814b5a6?q=80&w=1920&auto=format&fit=crop',
    'coffee_experience.jpg': 'https://images.unsplash.com/photo-1497935586351-b67a49e012bf?q=80&w=1920&auto=format&fit=crop',
    'cta_banner.jpg': 'https://images.unsplash.com/photo-1507842217343-583bb7270b66?q=80&w=1920&auto=format&fit=crop',
    
    # Book Cover Images (Open Library Cover API)
    'book_midnight_library.jpg': 'https://covers.openlibrary.org/b/isbn/9780525559474-L.jpg',
    'book_circe.jpg': 'https://covers.openlibrary.org/b/isbn/9780316556347-L.jpg',
    'book_silent_patient.jpg': 'https://covers.openlibrary.org/b/isbn/9781250301697-L.jpg',
    'book_sapiens.jpg': 'https://covers.openlibrary.org/b/isbn/9780062316097-L.jpg',
    'book_name_wind.jpg': 'https://covers.openlibrary.org/b/isbn/9780756404741-L.jpg',
    'book_pride_prejudice.jpg': 'https://covers.openlibrary.org/b/isbn/9780141439518-L.jpg',
    'book_alchemist.jpg': 'https://covers.openlibrary.org/b/isbn/9780062315007-L.jpg',
    'book_atomic_habits.jpg': 'https://covers.openlibrary.org/b/isbn/9780735211292-L.jpg'
}

os.makedirs('images', exist_ok=True)

print("Starting download of homepage and book cover images...")
for filename, url in images.items():
    filepath = os.path.join('images', filename)
    print(f"Downloading {filename} from {url[:60]}...")
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'})
        with urllib.request.urlopen(req, timeout=30) as response, open(filepath, 'wb') as out_file:
            data = response.read()
            out_file.write(data)
        print(f"Successfully downloaded {filename} ({len(data)} bytes)")
    except Exception as e:
        print(f"Failed to download {filename}: {e}")

print("Image download process complete.")
