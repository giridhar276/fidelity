
# ex_pytesseract_3_pdf_pages.py
# pip install pytesseract pdf2image
from pdf2image import convert_from_path
import pytesseract

# Replace with your scanned PDF path
pdf_path = "sample_scanned.pdf"

pages = convert_from_path(pdf_path, dpi=300)
for i, page in enumerate(pages, 1):
    text = pytesseract.image_to_string(page, lang="eng")
    print(f"\n--- PAGE {i} ---\n{text}")
