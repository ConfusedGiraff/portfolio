import os
from pathlib import Path # import all the path functions
import pyinputplus as pyip
import send2trash
import shutil #import shell utilities
import zipfile

folder = Path.cwd() / 'fileorg'
source_file = Path(folder) / 'source_file.txt'
destination_folder = Path(folder) / 'destination_folder'
backup_folder = Path.cwd() / 'fileorg_backup'

shutil.copy(source_file, destination_folder) #copies the source file to the destination folder

shutil.copy(source_file, Path(destination_folder) / 'new_filename.txt') #copies the source file to the destination folder and renames it to 'new filename.txt'

shutil.copytree(folder, backup_folder) #creates the backup folder if it doesn't exist and copies folder and all its contents to it

shutil.move(source_file, Path(destination_folder) / 'source_file.txt') #moves the source file to the destination folder
##If the destination includes a filename and a file with that name already exists in the destination folder, shutil.move overwrites that file

shutil.move(source_file, destination_folder)
##If the destination does not include a filename and a file with that name already exists in the destination folder, shutil.move throws an error

shutil.move(source_file, Path.cwd() / 'not_exist' / 'fileorg') #If the folders that make up the destination don't exist, Python throws an exception

shutil.move(source_file, Path(destination_folder) / 'not_exist' ) #If the destination folder doesn't exist, Python assumes it's a filename and creates a txt file with that name

shutil.move(source_file, Path(destination_folder) / 'new_filename.txt') #moves the source file to the destination folder and renames it to 'new filename.txt'

os.unlink(Path(folder) / 'delete_file.txt') #deletes the file specified

os.rmdir(Path(folder) / 'delete_empty') #deletes the folder specified if the folder is empty

x = pyip.inputYesNo(f'Are you sure you want to permanently delete {(Path(folder) / "delete_folder")}? ')
if x == 'yes':
    shutil.rmtree(Path(folder) / 'delete_folder') #permanently deletes the specified folder and all contents
else:
    print('That was a close one!')
#Use a print statement to check what files will be deleted before actually using this function

send2trash.send2trash(Path(folder) / 'safe_delete.txt') #sends files and folders to the recycle bin instead of deleting them permanently

for folderName, subfolders, filenames in os.walk(folder): #returns lists of all the objects in the folder specified
    print(folderName) #prints the folder name
    print(subfolders) #prints a list of the subfolder names
    print(filenames) #prints a list of the filenames
    for filename in filenames:
        print(Path(folderName) / filename) #prints the path to each file


with zipfile.ZipFile(Path(folder) / 'new.zip', 'w') as newZip:
    newZip.write('input.py', compress_type=zipfile.ZIP_DEFLATED) #creates a zip folder of the backup folder

with zipfile.ZipFile(Path(folder) / 'new.zip') as newZip:
    newZip.extractall(Path.cwd() / 'extracted') #extracts the contents of new.zip to the extracted folder

with zipfile.ZipFile(Path(folder) / 'new.zip') as newZip:
    print(newZip.namelist())
    newZip.extract('input.py') #extracts source_file.txt from new.zip and saves it in new_dest 

with zipfile.ZipFile(Path(folder) / 'new.zip', 'a') as newZip:
    newZip.write('lorem.txt', compress_type=zipfile.ZIP_DEFLATED) #adds lorem.txt to new.zip

with zipfile.ZipFile(Path(folder) / 'new.zip') as newZip:
    newZip.extractall(Path.cwd() / 'extracted') #extracts the contents of new.zip to the extracted folder






