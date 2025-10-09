
# ex_easyocr_2_with_boxes.py
# pip install easyocr opencv-python numpy
import easyocr, cv2, numpy as np

reader = easyocr.Reader(['en'])
res = reader.readtext("ocr_demo.png")  # [ [box, text, conf], ... ]

for (box, txt, conf) in res:
    print(f"{conf:.2f} :: {txt} :: {box}")

# Optional annotate image
img = cv2.imread("ocr_demo.png")
for (box, txt, conf) in res:
    pts = np.array(box, dtype=np.int32)
    cv2.polylines(img, [pts], True, (0,0,0), 2)
# cv2.imwrite("ocr_demo_annotated.png", img)
