from PIL import Image

try:
    img = Image.open('images/logo.png')
    # get bounding box of non-zero alpha
    bbox = img.getbbox()
    print(f"Bounding box: {bbox}")
    
    if bbox:
        # Crop to the bounding box
        cropped = img.crop(bbox)
        c_width, c_height = cropped.size
        print(f"Cropped size: {c_width}x{c_height}")
        
        # If it's a wide rectangle, the icon is likely on the left.
        # Let's crop a square from the left of the cropped image.
        icon_size = c_height
        icon_box = (0, 0, icon_size, icon_size)
        icon = cropped.crop(icon_box)
        
        if hasattr(Image, 'Resampling'):
            icon = icon.resize((64, 64), Image.Resampling.LANCZOS)
        else:
            icon = icon.resize((64, 64), Image.LANCZOS)
            
        icon.save('images/favicon.png')
        print("Successfully created square favicon.png from the left side of the actual logo content.")
    else:
        print("Image is entirely transparent.")
except Exception as e:
    print(f"Error processing image: {e}")
