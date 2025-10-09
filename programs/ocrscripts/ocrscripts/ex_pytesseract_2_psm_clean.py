
# ex_pytesseract_2_psm_clean.py
# pip install pytesseract opencv-python
import pytesseract, cv2
from helper_preprocess import clean_for_ocr

img = clean_for_ocr("ocr_demo_skewed.png")
cfg = "--oem 3 --psm 6"
text = pytesseract.image_to_string(img, lang="eng", config=cfg)
print(text)
