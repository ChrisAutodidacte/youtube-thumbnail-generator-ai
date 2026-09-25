import json, base64, os
from PIL import Image
import io

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
resp_path = os.path.join(BASE_DIR, 'response.json')

if not os.path.exists(resp_path):
    print(f"File response.json not found: {resp_path}")
    print("Please generate an image via the Claude skill or API call first.")
    exit(1)

with open(resp_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

image_data = None

def find_image(obj):
    global image_data
    if isinstance(obj, dict):
        if 'inlineData' in obj and 'data' in obj['inlineData']:
            image_data = obj['inlineData']['data']
            return
        if 'inline_data' in obj and 'data' in obj['inline_data']:
            image_data = obj['inline_data']['data']
            return
        for v in obj.values():
            find_image(v)
    elif isinstance(obj, list):
        for item in obj:
            find_image(item)

find_image(data)

if image_data:
    img_bytes = base64.b64decode(image_data)
    img = Image.open(io.BytesIO(img_bytes)).convert('RGB')
    out_dir = os.path.join(BASE_DIR, 'output', 'demo')
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, 'thumbnail-bg.jpg')
    img.save(out_path, 'JPEG', quality=92)
    print('Background saved successfully:', out_path)
else:
    print('No image found in response payload.')
