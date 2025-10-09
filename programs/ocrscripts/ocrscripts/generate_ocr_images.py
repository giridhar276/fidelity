
# generate_ocr_images.py
from PIL import Image, ImageDraw, ImageFont

def make_images(out_clean="ocr_demo.png", out_skew="ocr_demo_skewed.png"):
    w, h = 1000, 600
    img = Image.new("RGB", (w, h), "white")
    draw = ImageDraw.Draw(img)
    try:
        font_big = ImageFont.truetype("DejaVuSans.ttf", 48)
        font_mid = ImageFont.truetype("DejaVuSans.ttf", 36)
        font_small = ImageFont.truetype("DejaVuSans.ttf", 28)
    except:
        font_big = ImageFont.load_default()
        font_mid = ImageFont.load_default()
        font_small = ImageFont.load_default()

    lines = [
        ("INVOICE #12345", font_big),
        ("Date: 2025-10-09", font_mid),
        ("Bill To: Giridhar Sripathi", font_mid),
        ("Items:", font_mid),
        ("1) Data Science Training - 3 days      Qty: 1      Price: 1250.00", font_small),
        ("2) Python Workshop - 1 day             Qty: 1      Price: 350.00", font_small),
        ("Subtotal: 1600.00", font_mid),
        ("Tax (18% GST): 288.00", font_mid),
        ("TOTAL: 1888.00", font_big),
        ("Thank you for your business!", font_mid),
    ]

    y = 40
    for text, font in lines:
        draw.text((40, y), text, fill="black", font=font)
        y += int(getattr(font, "size", 28) * 1.5)

    img.save(out_clean)
    img.rotate(-4, expand=True, fillcolor="white").save(out_skew)
    print("Saved:", out_clean, out_skew)

if __name__ == "__main__":
    make_images()
