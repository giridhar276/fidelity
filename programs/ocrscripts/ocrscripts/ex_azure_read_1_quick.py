
# ex_azure_read_1_quick.py
# pip install azure-ai-formrecognizer
# Set AZURE_FORMRECOGNIZER_ENDPOINT and AZURE_FORMRECOGNIZER_KEY in env
import os
from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential

endpoint = os.environ.get("AZURE_FORMRECOGNIZER_ENDPOINT")
key = os.environ.get("AZURE_FORMRECOGNIZER_KEY")
client = DocumentAnalysisClient(endpoint=endpoint, credential=AzureKeyCredential(key))

with open("ocr_demo.png","rb") as f:
    poller = client.begin_analyze_document("prebuilt-read", document=f)
result = poller.result()
for page in result.pages:
    for line in page.lines:
        print(" ".join([w.content for w in line.words]))
