
# helper_preprocess.py
import cv2
import numpy as np

def clean_for_ocr(path):
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    img = cv2.fastNlMeansDenoising(img, h=10)
    img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]
    # deskew (estimate by moments)
    m = cv2.moments(img)
    if abs(m['mu02']) < 1e-2:
        return img
    skew = m['mu11'] / m['mu02']
    h, w = img.shape
    M = np.float32([[1, skew, -0.5*skew*h], [0, 1, 0]])
    img = cv2.warpAffine(img, M, (w, h), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)
    return img
