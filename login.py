import os

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

def login(SCOPES, file_name):
    os.chdir(os.getcwd())
    credentials = None
    if os.path.exists(file_name + '.json'):
        credentials = Credentials.from_authorized_user_file(file_name + '.json', SCOPES)
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            credentials = flow.run_local_server(port=0)
        with open(file_name + '.json', 'w') as token:
            token.write(credentials.to_json())
    return credentials