
# ex_mmocr_1_det_rec.py
# pip install mmocr
# NOTE: First run may download models.
from mmocr.apis import MMOCR

ocr = MMOCR(det='DB_r18', rec='CRNN', device='cpu')
res = ocr.readtext('ocr_demo.png', print_result=True)
# 'res' is a list of dicts with boxes and text
