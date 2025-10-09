
# ex_doctr_2_iter_blocks.py
from doctr.models import ocr_predictor
from doctr.io import DocumentFile

predictor = ocr_predictor(pretrained=True)
res = predictor(DocumentFile.from_images(["ocr_demo.png"]))
for page in res.pages:
    for block in page.blocks:
        for line in block.lines:
            print(" ".join([w.value for w in line.words]))
