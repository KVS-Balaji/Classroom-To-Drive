from login import login

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ['https://www.googleapis.com/auth/drive']

def create_sem5():
    folders_in_drive = service.files().list(q="mimeType='application/vnd.google-apps.folder'",
                                     corpora='user', 
                                     includeItemsFromAllDrives=False,
                                    ).execute()
    create_sem5 = 1

    print('='*75)
    for folder in folders_in_drive['files']:
        if 'Sem 5' in folder['name']:
            print('Sem 5 exists')
            sem5_id = folder['id']
            print(sem5_id)
            create_sem5 = 0

    if create_sem5 == 1:
        file_metadata = {'name': 'OS (Lab)',
                    'mimeType': 'application/vnd.google-apps.folder'}

        file = service.files().create(body=file_metadata, fields='id').execute()
        sem5_id = file["id"]
        print(f'Folder ID: "{sem5_id}."')

    return sem5_id

def create_folder(folder_name, parent_id):
    folders_in_drive = service.files().list(q="mimeType='application/vnd.google-apps.folder'",
                                     corpora='user', 
                                     includeItemsFromAllDrives=False,
                                    ).execute()

    folder_exists = 1

    for folder in folders_in_drive['files']:
        if folder_name in folder['name']:
            print(f'{folder_name} Exists')
            folder_id = folder['id']
            folder_exists = 0

    if folder_exists == 1:
        file_metadata = {'name': folder_name,
                    'mimeType': 'application/vnd.google-apps.folder',
                    'parents': [parent_id]}

        file = service.files().create(body=file_metadata, fields='id').execute()
        folder_id = file["id"]
        print(f'Folder ID: "{file["id"]}".')

    return folder_id

def folder_creation():
    try:
        credentials = login(SCOPES, 'drive_token')

        global service 
        service = build('drive', 'v3', credentials=credentials)

        sem5ID = create_sem5()
        folder_list = ['DBMS', 'ML', 'OOP', 'OS']
        folder_ids = [{'name': 'Sem 5', 'id': sem5ID}]

        for new_folder in folder_list:
            new_folder_id = create_folder(new_folder, sem5ID)
            folder_ids.append({'name':new_folder, 'id':new_folder_id})
        return folder_ids

    except HttpError as err:
        print(err)