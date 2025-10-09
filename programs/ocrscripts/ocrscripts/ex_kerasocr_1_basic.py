
# ex_kerasocr_1_basic.py
# pip install keras-ocr tensorflow
import keras_ocr

pipeline = keras_ocr.pipeline.Pipeline()
images = [keras_ocr.tools.read("ocr_demo.png")]
prediction_groups = pipeline.recognize(images)

for text, box in prediction_groups[0]:
    print(text, "::", box)
