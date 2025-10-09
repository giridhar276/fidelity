

from office365.runtime.auth.token_response import TokenResponse
from office365.sharepoint.client_context import ClientContext
import msal

TENANT = "giridharsripathi.onmicrosoft.com"
CLIENT_ID = "bbc90079-29a7-472b-8972-5995592340f5"
CERT_THUMBPRINT = "C66DBBF4966CB4151DE95A7721A571BE4A1608C3"
CERT_PATH = "my_certificate.pem"
RESOURCE = "https://giridharsripathi.sharepoint.com"
SITE_URL = f"{RESOURCE}/sites/training"

with open(CERT_PATH, "r") as f:
    private_key = f.read()

def acquire_token():
    app = msal.ConfidentialClientApplication(
        CLIENT_ID,
        authority=f"https://login.microsoftonline.com/{TENANT}",
        client_credential={"thumbprint": CERT_THUMBPRINT, "private_key": private_key}
    )
    result = app.acquire_token_for_client(scopes=[f"{RESOURCE}/.default"])
    return TokenResponse.from_json(result)

ctx = ClientContext(SITE_URL).with_access_token(acquire_token)

source_url = "/sites/training/Shared Documents/example.txt"
target_url = "/sites/training/Shared Documents/example_renamed.txt"

file = ctx.web.get_file_by_server_relative_url(source_url)
file.move_to(target_url, 1).execute_query()  # 1 = Overwrite if target exists

print(f"Moved/Renamed file from {source_url} to {target_url}")
