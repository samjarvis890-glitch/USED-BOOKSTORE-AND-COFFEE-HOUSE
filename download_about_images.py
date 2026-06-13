import urllib.request
import os
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

images = {
    'about-hero.jpg': 'https://images.unsplash.com/photo-1550399105-c4db5fb85c18?q=80&w=1920&auto=format&fit=crop',
    'about-timeline-1.jpg': 'https://images.unsplash.com/photo-1481627834876-b7833e8f5570?q=80&w=800&auto=format&fit=crop',
    'about-timeline-2.jpg': 'https://images.unsplash.com/photo-1507133759536-415849924976?q=80&w=800&auto=format&fit=crop',
    'about-timeline-3.jpg': 'https://images.unsplash.com/photo-1497935586351-b67a49e012bf?q=80&w=800&auto=format&fit=crop',
    'about-mission.jpg': 'https://images.unsplash.com/photo-1506880018603-83d5b814b5a6?q=80&w=800&auto=format&fit=crop',
    'about-team-1.jpg': 'https://images.unsplash.com/photo-1544005313-94ddf0286df2?q=80&w=800&auto=format&fit=crop',
    'about-team-2.jpg': 'https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?q=80&w=800&auto=format&fit=crop',
    'about-team-3.jpg': 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?q=80&w=800&auto=format&fit=crop',
    'about-cta.jpg': 'https://images.unsplash.com/photo-1463320726281-696a485928c7?q=80&w=1920&auto=format&fit=crop'
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

print("All about images downloaded successfully.")
