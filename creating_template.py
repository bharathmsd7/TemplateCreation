import os
import shutil
import requests
from secrets import GITHUB_TOKEN, GITHUB_USERNAME, SPREADSHEET_ID
from google.oauth2 import service_account
from googleapiclient.discovery import build
import logging as log
from create_html import create_html

log.basicConfig(filename='logs.log', level=log.DEBUG)

inital_count = 1

def getCount():

    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    SERVICE_ACCOUNT_FILE = 'keys.json'

    credentials = None
    credentials = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    # The ID of spreadsheet.
    SAMPLE_SPREADSHEET_ID = SPREADSHEET_ID

    service = build('sheets', 'v4', credentials=credentials)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range="Sheet1!A1:I1000").execute()
    values = result.get('values', [])
    current_count = len(values)

    return current_count

def getValues(current_count):
    first_column = "A"
    last_column = "I"
    
    if current_count > inital_count:

        range = "Sheet1!A"+ str(current_count)+":"+last_column+ str(current_count)
        #print(range)

        SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
        SERVICE_ACCOUNT_FILE = 'keys.json'

        credentials = None
        credentials = service_account.Credentials.from_service_account_file(
                SERVICE_ACCOUNT_FILE, scopes=SCOPES)

        # The ID of spreadsheet.
        SAMPLE_SPREADSHEET_ID = SPREADSHEET_ID

        service = build('sheets', 'v4', credentials=credentials)

        # Call the Sheets API
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range=range).execute()
        values = result.get('values', [])
        
        data = values[0]
        log.info("Data recieved."+ str(data))
        return data

def create_folder(folderName):
    directory = folderName
    directory = directory.replace(' ','')
    folderName = folderName.replace(' ','')
    parent_dir = os.getcwd()
    template_dir = parent_dir + "/Template"
    
    shutil.copytree(template_dir, folderName)
    shutil.copy(directory+".html", folderName)

    # Renaming the HTML file to index.html
    source_path = parent_dir + "/" + directory + "/" + directory+".html"
    destination_path = parent_dir + "/" + directory + "/" + "index.html"
    os.rename(source_path, destination_path)

    remove_file_path = parent_dir + "/"  + directory+".html"
    os.remove(remove_file_path)

    repo_path = parent_dir + "/" + directory
    repo_name = directory

    return repo_path, repo_name 

def create_repo(repo_path, repo_name):
    REPO_PATH = repo_path
    repo_name = repo_name.replace(' ','')
    GITHUB_USER = GITHUB_USERNAME
    GITHUB_URL = "https://api.github.com"

    payload = '{"name": "' + repo_name + '", "private": false }'

    headers = {
        "Authorization": "token " + GITHUB_TOKEN,
        "Accept": "application/vnd.github.v3+json"
    }

    try:
        r = requests.post(GITHUB_URL + "/user/repos", data=payload, headers=headers)
        r.raise_for_status()
        log.info(r)
    except requests.exceptions.RequestException as err:
        raise SystemExit(err)

    try:
        #os.chdir(REPO_PATH)
        #os.system("mkdir " + repo_name)
        os.chdir(REPO_PATH)
        os.system("git init")
        os.system("git remote add origin https://github.com/" + GITHUB_USER + "/" + repo_name + ".git")
        log.info("URL TO BE PUSH === https://github.com/" + GITHUB_USER + "/" + repo_name + ".git")
        os.system("echo '# " + repo_name + "' >> README.md")
        os.system("git add . && git commit -m 'Initial Commit' && git push origin master")
        log.info("trying to push repo")
    except FileExistsError as err:
        log.error(err)
        raise SystemExit(err)
        #return False

    return True

def main():
    
    current_count = getCount()
    data = getValues(current_count)
    date, functionType, bride, groom, time, place, bridePhoto, groomPhoto, invitation = data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8]
    folderName = groom + " Weds " + bride
    
    create_html(folderName, date, bride, groom, place, bridePhoto, groomPhoto, invitation)
    repo_path, repo_name = create_folder(folderName)
    result = create_repo(repo_path, repo_name)

    if result:
        global inital_count 
        inital_count += 1
    print(inital_count)

while(True):
    main()

