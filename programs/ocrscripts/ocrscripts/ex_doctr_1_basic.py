
# ex_doctr_1_basic.py
# pip install "python-doctr[torch]" pillow
from doctr.models import ocr_predictor
from doctr.io import DocumentFile

predictor = ocr_predictor(pretrained=True)
doc = DocumentFile.from_images(["ocr_demo.png"])
res = predictor(doc)
print(res.render())
