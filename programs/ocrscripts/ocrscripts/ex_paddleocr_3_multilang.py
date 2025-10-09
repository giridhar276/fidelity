
# ex_paddleocr_3_multilang.py
# Run with different lang codes as needed
from paddleocr import PaddleOCR
ocr = PaddleOCR(lang='en')  # swap to 'hi','te','ta','bn', etc. for Indic scripts
res = ocr.ocr('ocr_demo.png', cls=True)
print("\n".join([x[1][0] for x in res[0]]))
