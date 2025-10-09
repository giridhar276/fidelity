

from office365.runtime.auth.token_response import TokenResponse
from office365.sharepoint.client_context import ClientContext
import msal

TENANT = "giridharsripathi.onmicrosoft.com"
CLIENT_ID = "bbc90079-29a7-472b-8972-5995592340f5"
CERT_THUMBPRINT = "C66DBBF4966CB4151DE95A7721A571BE4A1608C3"
CERT_PATH = "my_certificate.pem"
RESOURCE = "https://giridharsripathi.sharepoint.com"
SITE_URL = f"{RESOURCE}/sites/training"
LIST_NAME = "Tasks"
ITEM_ID = 1  # ID of the list item to update

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
sp_list = ctx.web.lists.get_by_title(LIST_NAME)
item = sp_list.get_item_by_id(ITEM_ID)
item.set_property('Status', 'Completed')
item.update()
ctx.execute_query()

print(f"List item ID {ITEM_ID} updated.")
