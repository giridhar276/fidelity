
# ex_easyocr_1_basic.py
# pip install easyocr
import easyocr
reader = easyocr.Reader(['en'])
lines = reader.readtext("ocr_demo.png", detail=0)
print("\n".join(lines))
