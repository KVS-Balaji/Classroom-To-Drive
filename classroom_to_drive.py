import os.path
import io

#Necessary functions imported from other files
from pdf_converter import convert_to_pdf
from upload_files import upload
from login import login

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseDownload


SCOPES_CLASSROOM = ['https://www.googleapis.com/auth/classroom.courses.readonly', 
                    'https://www.googleapis.com/auth/classroom.announcements', 
                    'https://www.googleapis.com/auth/classroom.courseworkmaterials']

SCOPES_DRIVE = ['https://www.googleapis.com/auth/drive']

#Returns the list of courses user is part of
def course_list():
    creds = login(SCOPES_CLASSROOM, 'classroom_token')
    try:
        service = build('classroom', 'v1', credentials=creds)
        courses = []
        page_token = None

        while True:
            response = service.courses().list(pageToken=page_token,
                                              pageSize=2).execute()
            courses.extend(response.get('courses', []))
            page_token = response.get('nextPageToken', None)
            if not page_token:
                break

        if not courses:
            print("NO COURSES FOUND")
            return
        
        print("COURSES FOUND")
        return courses
    except HttpError as error:
        print(f"An error occurred: {error}")
        return error

#Returns a list of course work from the specified course
def courseWork(cid):
    creds = login(SCOPES_CLASSROOM, 'classroom_token')
    try:
        service = build('classroom', 'v1', credentials=creds)
        ids = list()
        titles = list()
        response = service.courses().courseWorkMaterials().list(courseId=cid).execute()
        response = response['courseWorkMaterial']
        for course_work in response:
            for material in course_work['materials']:
                file_data = material['driveFile']['driveFile']
                ids.append(file_data['id'])
                titles.append(file_data['title'])
        print("="*100)
        print(titles)
        print("="*100)
        return list(zip(ids, titles))
    except HttpError as err:
        print(err)
        return err
    except KeyError:
        print('No CourseWork available')
        return 'NCA'

#Returns a list announcements from specified course
def course_announcements(cid):
    creds = login(SCOPES_CLASSROOM, 'classroom_token')
    try:
        ids = list()
        titles = list()
        service = build('classroom', 'v1', credentials=creds)
        course = service.courses().announcements().list(courseId=cid).execute()
        for announcement in course['announcements']:
            for material in announcement['materials']:
                file_data = material['driveFile']['driveFile']
                ids.append(file_data['id'])
                titles.append(file_data['title'])
        print('='*100)
        print(titles)
        print('='*100)
        return list(zip(ids, titles))
    except HttpError as err:
        print(f'An error occured: {err}')
        return err
    except KeyError:
        print('No Announcements available')
        return 'NAA'
    
#Download annoucements/coursework from classroom and store locally
def file_download(zip_obj, course_name):
    creds = login(SCOPES_DRIVE, 'drive_token')
    try:
        folder_dir = os.getcwd() + '\\' + course_name
        try:
            os.mkdir(folder_dir)
        except FileExistsError:
            print('Course folder already exists!')
        
        service = build('drive', 'v3', credentials=creds)
        for file_id, title in zip_obj:
            print(f'Downloading file: "{title}"')
            request = service.files().get_media(fileId=file_id)
            file = io.BytesIO()
            downloader = MediaIoBaseDownload(file, request)
            done = False
            while done is False:
                status, done = downloader.next_chunk()
                print(f'Download {int(status.progress() * 100)}%')
            
            file.seek(0)
            
            path = folder_dir  + '\\' + title
            with open(path, 'wb') as f:
                f.write(file.read())
                f.close()
    except HttpError as err:
        print(f'An error occurred: {err}')
        file = None
        return err

#Delete locally downloaded files
#Uncomment line 162 to not delete them
def delete_files(course_name):
    path = os.getcwd() + rf'\{course_name}'
    files = os.listdir(path)

    for file in files:
        os.remove(path + rf'\{file}')
    os.rmdir(path)

def main():
    #GATHER LIST OF COURSES
    available_courses = course_list()
    for available_course in available_courses:
        print("Course ID:", available_course['id'] + '\t' +
              "Course Title:", available_course['name'])
        
        #READ SPECIFIC COURSE DETAILS
        id_title_iterable = course_announcements(available_course['id'])

        if id_title_iterable == 'NAA':
            id_title_iterable = courseWork(available_course['id'])
            if id_title_iterable == 'NCA':
                continue
            
        #DOWNLOAD FILES FROM COURSE
        file_download(id_title_iterable, available_course['name'])
        
        pdf_files = os.listdir(os.getcwd() + '\\' + available_course['name'])
        #CONVERT ANY OFFICE FILE TO PDF
        pdf_files = convert_to_pdf(available_course['name'])

        # UPLOAD THE PDF FILES TO RESPECTIVE DRIVE FOLDER
        ret_val = 0
        # ret_val = upload(pdf_files, available_course['name'])
        
        delete_files(available_course['name']) if ret_val else print('='*100 + 'DOWNLOADED FILES LOCALLY!' + '='*100)

if __name__ == '__main__':
    main()