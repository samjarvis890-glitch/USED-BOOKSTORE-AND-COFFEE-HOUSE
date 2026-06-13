import urllib.request
import os
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

images = {
    'loyalty-hero.jpg': 'https://images.unsplash.com/photo-1554118811-1e0d58224f24?q=80&w=1920&auto=format&fit=crop',
    'reward-coffee.jpg': 'https://images.unsplash.com/photo-1497935586351-b67a49e012bf?q=80&w=800&auto=format&fit=crop',
    'reward-book.jpg': 'https://images.unsplash.com/photo-1481627834876-b7833e8f5570?q=80&w=800&auto=format&fit=crop',
    'reward-vip.jpg': 'https://images.unsplash.com/photo-1544947950-fa07a98d237f?q=80&w=800&auto=format&fit=crop',
    'testimonial-1.jpg': 'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?q=80&w=400&auto=format&fit=crop',
    'testimonial-2.jpg': 'https://images.unsplash.com/photo-1494790108377-be9c29b29330?q=80&w=400&auto=format&fit=crop',
    'cta.jpg': 'https://images.unsplash.com/photo-1524813686514-a57563d77965?q=80&w=1920&auto=format&fit=crop',
    'faq-image.jpg': 'https://images.unsplash.com/photo-1461280360983-bd93eaa5051b?q=80&w=800&auto=format&fit=crop'
}

os.makedirs(os.path.join('images', 'loyalty'), exist_ok=True)

for filename, url in images.items():
    filepath = os.path.join('images', 'loyalty', filename)
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
