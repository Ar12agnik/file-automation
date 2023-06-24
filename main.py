import os
import winshell
import functions_for_app as f
os.chdir("C:\\Users\\Agnik and Ahana\\Documents\\organizing folder")
directories=os.listdir()#checks for files in the cwd
for dir in directories:
    extention=str(dir.split('.')[1])
    f.organise_files(extention,directories)
print("done")