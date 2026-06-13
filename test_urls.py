import urllib.request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

urls = [
    'https://images.unsplash.com/photo-1555448248-2571daf6344b?q=80&w=800&auto=format&fit=crop',
    'https://images.unsplash.com/photo-1589998059171-988d887df646?q=80&w=800&auto=format&fit=crop',
    'https://images.unsplash.com/photo-1506880018603-83d5b814b5a6?q=80&w=1920&auto=format&fit=crop',
    'https://images.unsplash.com/photo-1543002588-bfa74002ed7e?q=80&w=800&auto=format&fit=crop',
    'https://images.unsplash.com/photo-1474366521946-c3d4b507abf2?q=80&w=800&auto=format&fit=crop',
    'https://images.unsplash.com/photo-1587876931567-564ce588bfbd?q=80&w=800&auto=format&fit=crop',
    'https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=800&auto=format&fit=crop'
]

for url in urls:
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        response = urllib.request.urlopen(req)
        print(f"Success: {url}")
    except Exception as e:
        print(f"Failed: {url} - {e}")
