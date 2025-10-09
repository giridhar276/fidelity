
# ex_tesserocr_1_basic.py
# pip install tesserocr pillow
from tesserocr import PyTessBaseAPI, PSM, OEM
from PIL import Image

with PyTessBaseAPI(psm=PSM.AUTO, oem=OEM.LSTM_ONLY, lang="eng") as api:
    api.SetImage(Image.open("ocr_demo.png"))
    print(api.GetUTF8Text())
