import os
from PIL import Image, ImageDraw

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

bg_path = os.path.join(BASE_DIR, 'output', 'demo', 'thumbnail-bg.jpg')
portrait_path = os.path.join(BASE_DIR, 'entities', 'demo', 'photos', 'avatar-portrait.png')
out_path = os.path.join(BASE_DIR, 'output', 'demo', 'thumbnail-final.jpg')

if not os.path.exists(bg_path):
    print(f"Background image not found: {bg_path}")
    print("Please generate a background first using the /thumbnail-generator skill or place an image.")
    exit(1)

if not os.path.exists(portrait_path):
    print(f"Portrait photo not found: {portrait_path}")
    print("Please place a transparent PNG portrait photo in your entity folder.")
    exit(1)

bg = Image.open(bg_path).convert('RGBA')
bg_w, bg_h = bg.size  # 1280x720 standard

portrait = Image.open(portrait_path).convert('RGBA')

# Portrait circle: standard diameter for high CTR visibility
diameter = 380
portrait_resized = portrait.resize((diameter, diameter), Image.LANCZOS)

# Circular alpha mask
mask = Image.new('L', (diameter, diameter), 0)
ImageDraw.Draw(mask).ellipse((0, 0, diameter, diameter), fill=255)

portrait_circle = Image.new('RGBA', (diameter, diameter), (0, 0, 0, 0))
portrait_circle.paste(portrait_resized, (0, 0), mask)

# Cyan border and luminous outer glow
border = 5
total = diameter + border * 2
bordered = Image.new('RGBA', (total, total), (0, 0, 0, 0))
d = ImageDraw.Draw(bordered)

# Subtle outer glow effect
for i in range(6, 0, -1):
    d.ellipse((border - i, border - i, total - border + i, total - border + i),
              outline=(0, 229, 255, int(60 * i / 6)), width=2)

# Main cyan solid border
d.ellipse((1, 1, total - 2, total - 2), outline=(0, 229, 255, 255), width=border)

bordered.paste(portrait_circle, (border, border), portrait_circle)

# Position: bottom-right corner, snug to edges
x = bg_w - total - 20
y = bg_h - total - 15

bg.paste(bordered, (x, y), bordered)

os.makedirs(os.path.dirname(out_path), exist_ok=True)
bg.convert('RGB').save(out_path, 'JPEG', quality=92)
print('Final thumbnail saved successfully:', out_path)
