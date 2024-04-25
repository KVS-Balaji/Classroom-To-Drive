# Classroom_To_Drive

## Table of Contents

1. [Project Description](#project-description)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Contribution and Usage](#getting-involved-and-usage)

## Project Description

**Classroom To Drive** is a Python-based utility made to simplify the management of Google Classroom files. 

### Key Features

- **Course Scanning**: Quickly and efficiently scan through all your Google Classroom courses.
- **File Management**: Download files attached to assignments and announcements from your courses to your local computer.
- **Optional Google Drive Integration**: Seamlessly upload downloaded files to your Google Drive for cloud storage and easy access.

### Why It Matters

Google Classroom is a widely-used platform in educational settings, but managing files within it can be cumbersome. **Classroom To Drive** aims to streamline this process, making it easier for educators and students to access and organize their course materials.

Whether you're a teacher managing multiple classes or a student trying to keep track of your coursework, **Classroom To Drive** is here to simplify your Google Classroom experience.

Please proceed to the "Installation" section to get started with using **Classroom To Drive** for your own needs.

## Installation

To get **Classroom To Drive** up and running on your system, follow these simple steps:

1. **Clone the Repository**: 
   Clone this repository to your local machine using the following command:

   ```bash
   git clone https://github.com/KVS-Balaji/Classroom_To_Drive.git
   ```
   Note: If git is not installed on your system, you can simply download the repository as a zip file.
   
2. **Google Cloud Project Setup**:
   Before running the script, you'll need to create a Google Cloud project and set up authentication credentials. Follow the instructions in the [Google Workspace Developer Guide](https://developers.google.com/docs/api/quickstart/python)
 to create your project and obtain the required credentials.
   When prompted to download your OAuth client json file, please rename that file to `credentials.json`.   
  Note: You need not do the steps "Configure the sample" and "Run the sample".

4. **Optional: Install LibreOffice (for PDF Conversion, Windows)**:
   If you plan to convert files from Google Classroom into PDF format before uploading to drive, you can download and install LibreOffice by following this [link](https://www.libreoffice.org/download/download-libreoffice/). This step is optional, and you can skip it if you don't need PDF conversion.

## Usage

To use **Classroom To Drive**, follow these steps:

1. **Prerequisites**:
   - Ensure you have completed the installation steps mentioned in the [Installation](#installation) section.

2. **Credentials File**:
   - Make sure you have the `credentials.json` file in the same directory as the main file (`classroom_to_drive.py`). You can obtain this file by following the instructions in the [Google Workspace Developer Guide](https://developers.google.com/docs/api/quickstart/python).

3. **First Run**:
   - The first time you run `classroom_to_drive.py`, you will be prompted to grant access to your Google Classroom and Google Drive. Follow the prompts to provide access.

4. **Token Files**:
   - After granting access, two token files, `classroom_token.json` and `drive_token.json`, will be created in the same directory. Do not share these files with anyone, as they contain your authentication tokens.

5. **File Conversion (Optional)**:
   - By default, the script converts files from Google Classroom to PDF format before uploading to Google Drive. If you wish to skip the conversion step, you can comment out the line that says:
   
     ```python
     pdf_files = convert_to_pdf(available_course['name'])
     ```

6. **File Upload (Optional)**:
   - If you want to keep the downloaded files on your local hard disk and not upload them to Google Drive, comment out the line that says:

     ```python
     ret_val = upload(pdf_files, available_course['name'])
     ```

7. **Customization**:
    When using **Classroom To Drive**, you may need to customize the script to match your specific Google Classroom folder names and conditions for file uploads. The script provides flexibility to determine where files are uploaded based on these folder names. Follow these steps to customize the script:
    
    1. **Open the Script**:
       - Open the `upload_files.py` script in your preferred text editor or code editor.
    
    2. **Locate the `if-elif` Blocks**:
       - Find the section of code in `upload_files.py` that contains `if-elif` blocks. These blocks define conditions based on folder names and determine the `parent_id` for file uploads.
    
       ```python
       for folders in folder_name_id_dict:
           if folders['name'] == 'OS' and folder_name == '5':
               parent_id = folders['id']
           elif folders['name'] == 'DBMS' and folder_name == 'PMCO-Sec-C':
               parent_id = folders['id']
           elif folders['name'] == 'ML' and folder_name == '2023_Probability & Statistics':
               parent_id = folders['id']
           elif folders['name'] == 'OOP' and folder_name == 'FAFL 4':
               parent_id = folders['id']
    Customize the Conditions:
    
    Replace the folder names in the if-elif statements with the names of your actual Google Classroom folders.
    Adjust the conditions to match your specific requirements.
    For example, if your Google Classroom folder names are 'Biology', 'Math', 'History', and 'Chemistry', and you want files to be uploaded to corresponding folders, you can adjust the conditions accordingly.  
    **folder_name corresponds to the name of the classroom, aka, name of the folder the classroom files are downloaded in**  
    **modify the folders['name'] condition to the name of the folder you want to be displayed in your google drive**
    
    Save Your Changes:
    
    Save the modified upload_files.py script.
    With these customizations, the script will upload files to the specified folders based on the actual folder names you've defined in your Google Classroom.
    
    If you have any questions or encounter issues while customizing the script, don't hesitate to reach out for assistance.

9. **Running the Script**:
   - Finally, run the main script by executing `classroom_to_drive.py`. Your files will be managed according to the configurations you've set.

That's it! You're now ready to use **Classroom To Drive** to simplify your Google Classroom file management. If you encounter any issues or have questions during usage, don't hesitate to reach out for assistance.

## Getting Involved and Usage
**Start Using**:

You're welcome to use this code for your personal needs, whether it's for school or just simplifying your Google Classroom experience. If you ever run into questions or need assistance, don't hesitate to reach out. I'm here to help you get the most out of it.

**Get Involved**:

Even though it's a solo project, I genuinely appreciate your input! If you have suggestions, come across a bug, or dream up exciting features, please feel free to share. You can create an issue or drop me a message with your ideas. Together, we can make this code even better and more helpful for everyone.

Your feedback is invaluable, and I'm grateful for your support on this journey.

