import os
import subprocess

def convert_to_pdf(course_title):
    try:
        print(f'Converting files in "{course_title}" to pdf!')
        path_to_office = r"C:\Program Files\LibreOffice\program\soffice.exe"

        source_folder = os.getcwd() + '\\' + course_title
        output_folder = os.getcwd() + '\\' + course_title

        os.chdir(source_folder)

        files = os.listdir(os.getcwd())

        for file in files:
            if '.pdf' in file:
                files.remove(file)

        command = f"\"{path_to_office}\" --convert-to pdf  --outdir \"{output_folder}\" *.*"
        subprocess.run(command)

        for file in files:
            os.remove(file)

        print(f'Converted files in "{course_title}" to pdf!')

        os.chdir(os.getcwd().removesuffix(rf'\{course_title}'))

        return os.listdir(os.getcwd() + '\\' + course_title)
    except:
        print('*****Error in converting files to PDF*****')