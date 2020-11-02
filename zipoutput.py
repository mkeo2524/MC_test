import os
from zipfile import *
from os.path import basename
from pathlib import Path

DEFAULT_PATH = os.getcwd()
VTP_PATH = Path(DEFAULT_PATH + "/geom/output/geom")
OSIM_PATH = Path(DEFAULT_PATH + "/muscle/output")

def output_zip():
    with ZipFile('MapClient.zip', 'w') as zipObj:
        for folderName, subfolders, filenames in os.walk(str(VTP_PATH)):
            for filename in filenames:
                #create complete filepath of file in directory
                filePath = os.path.join(folderName, filename)
                # Add file to zip
                zipObj.write(filePath, os.path.join("geom",basename(filePath)))
        osimFilePath = str(Path(str(OSIM_PATH) + "/gait2392_simbody.osim"))
        zipObj.write(osimFilePath, basename(osimFilePath))
        zipObj.close()


