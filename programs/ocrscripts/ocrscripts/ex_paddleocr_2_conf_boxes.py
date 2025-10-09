
# ex_paddleocr_2_conf_boxes.py
from paddleocr import PaddleOCR
ocr = PaddleOCR(lang='en', det=True, rec=True, cls=True)
res = ocr.ocr('ocr_demo.png', cls=True)
for box, (txt, conf) in res[0]:
    print(f"{conf:.3f} :: {txt} :: {box}")
