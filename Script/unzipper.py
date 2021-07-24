import os
import zipfile
from pathlib import Path
import shutil
import datetime
from tkinter import Tk, filedialog

downloadDir = str(os.path.join( os.getenv('USERPROFILE'), 'Downloads'))

archiveDirPath = downloadDir + "\ziparchive"
fileExtension = ".zip"
initialDirCounter = 1

def selectFolder():
    # always create a Tkinter instance
    root = Tk()
    # pop-up window is on top of other windows
    root.attributes("-topmost", True)
    root.iconbitmap("D:/PythonScripts/Unzipper1.1/Icon/UnzipperFavicon_256.ico")
    root.withdraw()
    newFolderPath = filedialog.askdirectory(title='Choose directory for ' + folderName)
    # When user hits cancel or terminates pop-up
    if not newFolderPath:
        newFolderPath = downloadDir
    return newFolderPath

# timestamp for like-named folders 
timeStamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-")

# loop through items in downloads directory
for item in os.listdir(downloadDir):
    # check for ".zip"-files in downloads directory
    if item.endswith(fileExtension):
        # .zip-extension gets stripped of at the end, leaving only the foldername
        folderName = Path(item).stem
        # new folder directory gets set
        newFolderDir = selectFolder() + "\\" + folderName

        # for the case that the new folder directory already exists
        while os.path.exists(newFolderDir):
            # append counter inside parentheses
            folderName = folderName.strip() [0]
            print(folderName)
            newFolderDir = newFolderDir + " (" + str(initialDirCounter) + ")"
            initialDirCounter += 1

        # Path to zip-file
        zipFilePath = downloadDir + "\\" + item
        # create zipfile object
        zip_ref = zipfile.ZipFile(zipFilePath)  

        # extract zip into the choosen location
        zip_ref.extractall(newFolderDir)
        # close file
        zip_ref.close()  

        # open the unzipped folder
        os.startfile(newFolderDir)
        # archive folder is created if it doesnt exist yet
        if not os.path.exists(archiveDirPath):
            os.mkdir(archiveDirPath)
        
        zipForArchive = zipFilePath
        
        # zip-file
        archiveFolderPath = archiveDirPath + "\\" + item
        if os.path.exists(archiveFolderPath):
            zipForArchive = downloadDir + "\\" + timeStamp + Path(item).stem + ".zip"
            # you have to specific rename the zip.file, which is stored in zipFilePath
            os.rename(zipFilePath, zipForArchive)

        shutil.move(zipForArchive, archiveDirPath)
