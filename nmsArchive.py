import os
import datetime
import shutil

sourceDirectory = os.getenv('APPDATA') + "\\HelloGames\\NMS\\"
targetDirectory = os.getenv('HOMEPATH') + "\\Documents\\NMSBackups\\"
archiveFileName = "NMSBackup " + datetime.datetime.now().strftime("%m-%d-%Y--%H-%M-%S-%f")
try:
    if not os.path.exists(targetDirectory):
        os.mkdir(targetDirectory)
except Exception as e:
    print("The destination folder {} could not be created.  The following error occured: {}".format(targetDirectory , str(e)))
    exit()
else:
    os.chdir(targetDirectory)
try:
    shutil.make_archive(archiveFileName, 'zip', base_dir=sourceDirectory)
except Exception as e:
    print("The archive was not created correctly.  The following error occurred {}".format(e))