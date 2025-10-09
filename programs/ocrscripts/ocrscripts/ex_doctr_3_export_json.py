
# ex_doctr_3_export_json.py
from doctr.models import ocr_predictor
from doctr.io import DocumentFile
import json

predictor = ocr_predictor(pretrained=True)
result = predictor(DocumentFile.from_images(["ocr_demo.png"]))
as_dict = result.export()
print(json.dumps(as_dict, indent=2)[:2000])  # preview
