from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow

import sys
import os
import pickle

def upload_basic(file_path, client_secrets_file):
    """Insert new file.
    Returns : Id's of the file uploaded

    Load pre-authorized user credentials from the environment.
    TODO(developer) - See https://developers.google.com/identity
    for guides on implementing OAuth2 for the application.
    """
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    else:
        SCOPES = ['https://www.googleapis.com/auth/drive'] 
        flow = InstalledAppFlow.from_client_secrets_file(client_secrets_file , SCOPES)
        creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('drive', 'v3', credentials=creds)

    file_metadata = {'name': file_path}
    media = MediaFileUpload(file_path)
    file = service.files().create(body=file_metadata, media_body=media,
                                    fields='id').execute()
    print(F'File ID: {file.get("id")}')
    return file.get('id')


if __name__ == '__main__':
    file_path = sys.argv[1]
    client_secrets_file = 'client_secret_xxxxxxxxxxxx.json'
    upload_basic(file_path, client_secrets_file)
