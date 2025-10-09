
# ex_cloud_textract_1_quick.py
# pip install boto3
# Requires AWS credentials in environment or ~/.aws/credentials
import boto3, json

textract = boto3.client('textract', region_name='us-east-1')
with open('ocr_demo.png','rb') as f:
    resp = textract.detect_document_text(Document={'Bytes': f.read()})
for block in resp.get('Blocks', []):
    if block.get('BlockType') == 'LINE':
        print(block.get('Text'))
