
# ex_cloud_vision_1_quick.py
# pip install google-cloud-vision
# Set GOOGLE_APPLICATION_CREDENTIALS to your service account JSON
from google.cloud import vision

client = vision.ImageAnnotatorClient()
with open('ocr_demo.png','rb') as f:
    content = f.read()
image = vision.Image(content=content)
resp = client.text_detection(image=image)
if resp.text_annotations:
    print(resp.text_annotations[0].description)
