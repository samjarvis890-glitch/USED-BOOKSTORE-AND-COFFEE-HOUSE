from PIL import Image, ImageDraw, ImageFont
import os

# Create images directory if it doesn't exist
os.makedirs('images', exist_ok=True)

images_to_create = [
    ('about-hero.jpg', 1920, 1080, 'Hero Image - Used Bookstore & Coffee House'),
    ('about-timeline-1.jpg', 800, 600, '2012 - Tiny Bookstore Corner'),
    ('about-timeline-2.jpg', 800, 600, '2017 - Specialty Coffee Integration'),
    ('about-timeline-3.jpg', 800, 600, '2023 - The Lounge Expansion'),
    ('about-mission.jpg', 800, 800, 'Open Book and Coffee cup'),
    ('about-team-1.jpg', 800, 1000, 'Clara Vance - Book Curator'),
    ('about-team-2.jpg', 800, 1000, 'Julian Reed - Master Barista'),
    ('about-team-3.jpg', 800, 1000, 'Elena Cross - Events Coordinator'),
    ('about-cta.jpg', 1920, 800, 'Cozy Reading Spot CTA')
]

for filename, width, height, text in images_to_create:
    filepath = os.path.join('images', filename)
    # Background color: warm brown/coffee tone
    img = Image.new('RGB', (width, height), color=(111, 78, 55))
    d = ImageDraw.Draw(img)
    
    # Try to use a default font, otherwise just draw text
    try:
        font = ImageFont.load_default()
        # Scale up text a bit by drawing it larger (simplified approach: just draw text)
        # To make it visible, we'll draw it roughly in the center
        text_bbox = d.textbbox((0,0), text, font=font)
        text_w = text_bbox[2] - text_bbox[0]
        text_h = text_bbox[3] - text_bbox[1]
        
        position = ((width - text_w) / 2, (height - text_h) / 2)
        d.text(position, text, fill=(250, 247, 242), font=font)
    except:
        d.text((10, 10), text, fill=(250, 247, 242))
        
    img.save(filepath, quality=90)
    print(f"Created placeholder: {filepath}")

print("Placeholder generation complete.")
