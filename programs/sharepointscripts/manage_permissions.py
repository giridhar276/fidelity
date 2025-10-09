

from office365.runtime.auth.token_response import TokenResponse
from office365.sharepoint.client_context import ClientContext
import msal

TENANT = "giridharsripathi.onmicrosoft.com"
CLIENT_ID = "bbc90079-29a7-472b-8972-5995592340f5"
CERT_THUMBPRINT = "C66DBBF4966CB4151DE95A7721A571BE4A1608C3"
CERT_PATH = "my_certificate.pem"
RESOURCE = "https://giridharsripathi.sharepoint.com"
SITE_URL = f"{RESOURCE}/sites/training"
USER_EMAIL = "user@example.com"
ROLE_DEFINITION_NAME = "Read"  # Could also be "Contribute" or "Full Control"

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

# Get the file/folder by server relative URL
target_url = "/sites/training/Shared Documents/example.txt"
resource = ctx.web.get_file_by_server_relative_url(target_url)

# Break role inheritance if necessary
resource.break_role_inheritance(False, True).execute_query()  # False=copyRoleAssignments, True=clearSubscopes

user = ctx.web.site_users.get_by_email(USER_EMAIL)
ctx.load(user)
ctx.execute_query()

role_def = ctx.web.role_definitions.get_by_name(ROLE_DEFINITION_NAME)
ctx.load(role_def)
ctx.execute_query()

resource.role_assignments.add_role_assignment(user.properties['Id'], role_def.properties['Id']).execute_query()

print(f"Granted '{ROLE_DEFINITION_NAME}' permission to {USER_EMAIL} on {target_url}")
