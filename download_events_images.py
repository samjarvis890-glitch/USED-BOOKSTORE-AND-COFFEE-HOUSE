import urllib.request
import os
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

images = {
    'events-hero.jpg': 'https://images.unsplash.com/photo-1543269865-cbf427effbad?q=80&w=1920&auto=format&fit=crop',
    'author-reading-1.jpg': 'https://images.unsplash.com/photo-1521714161819-15534968fc5f?q=80&w=800&auto=format&fit=crop',
    'author-reading-2.jpg': 'https://images.unsplash.com/photo-1524995997946-a1c2e315a42f?q=80&w=800&auto=format&fit=crop',
    'workshop-1.jpg': 'https://images.unsplash.com/photo-1516321497487-e288fb19713f?q=80&w=800&auto=format&fit=crop',
    'workshop-2.jpg': 'https://images.unsplash.com/photo-1522202176988-66273c2fd55f?q=80&w=800&auto=format&fit=crop',
    'community-openmic.jpg': 'https://images.unsplash.com/photo-1511192336575-5a79af67a629?q=80&w=800&auto=format&fit=crop',
    'events-extra-1.jpg': 'https://images.unsplash.com/photo-1544928147-79a2dbc1f389?q=80&w=800&auto=format&fit=crop',
    'events-extra-2.jpg': 'https://images.unsplash.com/photo-1528605248644-14dd04022da1?q=80&w=800&auto=format&fit=crop'
}

os.makedirs('images/events', exist_ok=True)

for filename, url in images.items():
    filepath = os.path.join('images', 'events', filename)
    print(f"Downloading {filename}...")
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response, open(filepath, 'wb') as out_file:
            data = response.read()
            out_file.write(data)
        print(f"Successfully downloaded {filename}")
    except Exception as e:
        print(f"Failed to download {filename}: {e}")

print("All event images downloaded successfully.")
