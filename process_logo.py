from PIL import Image

try:
    img = Image.open('images/logo.png')
    width, height = img.size
    print(f"Original logo size: {width}x{height}")
    
    # Assuming the icon is on the left, crop a square from the left edge
    box = (0, 0, height, height)
    icon = img.crop(box)
    
    # Resize to 128x128 for favicon
    if hasattr(Image, 'Resampling'):
        icon = icon.resize((128, 128), Image.Resampling.LANCZOS)
    else:
        icon = icon.resize((128, 128), Image.LANCZOS)
        
    icon.save('images/favicon.png')
    print("Successfully created images/favicon.png by cropping the left square.")
    
except Exception as e:
    print(f"Error processing image: {e}")
