
# ex_paddleocr_1_basic.py
# pip install "paddleocr>=2.6"
from paddleocr import PaddleOCR
ocr = PaddleOCR(lang='en')
res = ocr.ocr('ocr_demo.png', cls=True)
print("\n".join([line[1][0] for line in res[0]]))
