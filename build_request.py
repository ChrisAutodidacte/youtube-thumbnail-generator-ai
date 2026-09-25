import io, base64, json, os
from PIL import Image

# Default prompt sample for standalone testing
prompt = (
    "Create a modern professional YouTube thumbnail image, 1280x720 pixels, 16:9 ratio.\n\n"
    "BACKGROUND: Dark gradient (deep black #0d0d14 to dark navy #0d1b2a). "
    "Subtle thin geometric lines as filigree in the corners only, very discreet.\n\n"
    "COMPOSITION LAYOUT:\n"
    "- TITLE ZONE: Top area, spanning full width (upper 40%). Title centered and very large, subtitle centered below.\n"
    "- ILLUSTRATION ZONE: Bottom-left area (lower 50%, left 60%). The illustration fills this area.\n"
    "- BOTTOM-RIGHT (lower 50%, right 40%): Leave this as plain dark background, no elements, no frame, no border.\n\n"
    "TEXT STYLE:\n"
    "- Main title \"AI AUTOMATION\" in very bold, extra-black, uppercase font. "
    "Use white (#FFFFFF) for \"AI\" and bright electric cyan (#00E5FF) for \"AUTOMATION\". "
    "Title must be HUGE.\n"
    "- Subtitle \"The only real secret to 10x your productivity.\" in bold font, "
    "bright yellow (#FFD700), clearly visible, medium size.\n\n"
    "ILLUSTRATION (bottom-left only):\n"
    "- Draw a sleek glowing 3D futuristic AI robotic brain core with luminous data circuits and glowing holographic gears. "
    "Keep it CLEAN and IMPACTFUL with high visual contrast.\n\n"
    "STYLE: Clean, professional, high contrast. No watermark, no logo, no distorted human figures. "
    "Mood: serious, futuristic, authoritative.\n\n"
    "CRITICAL: Bottom-right area must remain clean dark background — absolutely no frame, no border, no box outline."
)

payload = {
    "contents": [{
        "role": "user",
        "parts": [{"text": prompt}]
    }],
    "generationConfig": {
        "responseModalities": ["IMAGE", "TEXT"],
        "imageConfig": {
            "aspectRatio": "16:9",
            "imageSize": "1K"
        }
    }
}

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
out_path = os.path.join(BASE_DIR, 'request.json')
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(payload, f, ensure_ascii=False, indent=2)

print('Payload request.json created successfully, size:', os.path.getsize(out_path))
