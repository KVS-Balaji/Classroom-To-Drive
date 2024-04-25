import os
from login import login
from create_folder import folder_creation

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload

SCOPES = ['https://www.googleapis.com/auth/drive']

def upload(file_list, folder_name):
    credentials = login(SCOPES, 'drive_token')
    
    folder_name_id_dict = folder_creation()

    try:
        service = build('drive', 'v3', credentials=credentials)
        parent_id = None

        for folders in folder_name_id_dict:
            if folders['name'] == 'OS' and folder_name == '5':
                parent_id = folders['id']
            elif folders['name'] == 'DBMS' and folder_name == 'PMCO-Sec-C':
                parent_id = folders['id']
            elif folders['name'] == 'ML' and folder_name == '2023_Probability & Statistics':
                parent_id = folders['id']
            elif folders['name'] == 'OOP' and folder_name == 'FAFL 4':
                parent_id = folders['id']

        if parent_id is None:
            parent_id = folder_name_id_dict[0]['id']

        #UPLOAD/CREATE FILE IN DRIVE IF NOT PRESENT
        for file_name in file_list:
            print(os.getcwd() + f'\\{folder_name}\\{file_name}')
            response = service.files().list(q=f"name contains '{file_name}'",
                                                spaces='drive').execute()

            if response['files'] == []:
                print(f'Uploading file {file_name} to ID {parent_id}')
                file_metadata = {'name': f'{file_name}',
                                'parents': [parent_id]
                                } 
                media = MediaFileUpload(os.getcwd() + f'\\{folder_name}\\{file_name}',
                                        mimetype='file/pdf',
                                        resumable=True)
                file = service.files().create(body=file_metadata, 
                                            media_body=media,
                                            fields='id').execute()
                print(str(file) + '\n')
        print('='*100)
        return 1
    except HttpError as err:
        print(err)