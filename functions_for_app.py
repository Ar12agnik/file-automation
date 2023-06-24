import os
import winshell
def create_desktop_shortcut(name, target_path, icon_path=None):
    shortcut_path = os.path.join(winshell.desktop(), f'{name}.lnk')
    
    with winshell.shortcut(shortcut_path) as shortcut:
        shortcut.path = target_path
        if icon_path:
            shortcut.icon_location = (icon_path, 0)
def organise_files(file_extension,files):
    path=f"C:\\Users\\Agnik and Ahana\\Documents\\{file_extension}"
    if os.path.exists(path):
        for file in files:
            if file_extension in file.lower():
                os.rename(f"C:\\Users\\Agnik and Ahana\\Documents\\organizing folder\\{file}",f"C:\\Users\\Agnik and Ahana\\Documents\\{file_extension}\\{file}")
                if 'important' in file.lower():
                    create_desktop_shortcut(file,f"C:\\Users\\Agnik and Ahana\\Documents\\{file_extension}\\{file}")
    else:
        os.mkdir(path=path)
        organise_files(file_extension=file_extension,files=files)
        