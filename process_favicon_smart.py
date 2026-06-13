from PIL import Image, ImageChops

try:
    img = Image.open('images/logo.png').convert('RGBA')
    bg = Image.new('RGBA', img.size, img.getpixel((0,0)))
    diff = ImageChops.difference(img, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    
    if bbox:
        print(f"Content bounding box: {bbox}")
        # Crop the content
        content = img.crop(bbox)
        c_width, c_height = content.size
        print(f"Cropped content size: {c_width}x{c_height}")
        
        # Take the left square of the content for the favicon
        icon_size = c_height
        icon_box = (0, 0, icon_size, icon_size)
        icon = content.crop(icon_box)
        
        # Add a little padding back and a transparent background or rounded corners?
        # Let's just resize it to 128x128
        if hasattr(Image, 'Resampling'):
            icon = icon.resize((128, 128), Image.Resampling.LANCZOS)
        else:
            icon = icon.resize((128, 128), Image.LANCZOS)
            
        icon.save('images/favicon.png')
        print("Successfully created square favicon.png.")
    else:
        print("Could not find content bounding box.")
        
except Exception as e:
    print(f"Error processing image: {e}")
