
# ex_easyocr_3_batch_folder.py
# pip install easyocr
import os, easyocr

reader = easyocr.Reader(['en'])
for f in os.listdir("."):
    if f.lower().endswith((".png",".jpg",".jpeg",".bmp",".tif",".tiff")):
        print(f"\n== {f} ==")
        print("\n".join(reader.readtext(f, detail=0)))
