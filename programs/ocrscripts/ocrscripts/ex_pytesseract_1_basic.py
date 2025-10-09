
# ex_pytesseract_1_basic.py
# pip install pytesseract pillow
import pytesseract
from PIL import Image

img = Image.open("ocr_demo.png")
text = pytesseract.image_to_string(img, lang="eng")
print(text)
