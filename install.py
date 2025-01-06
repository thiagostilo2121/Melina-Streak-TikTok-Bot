import os

os.system("pip install -r main/ins.files/requiretements.txt")

import win32com.client
import localDataBaseFolder as db

def sys(command): os.system(command)

shell = win32com.client.Dispatch("WScript.shell")
script_dir = os.path.dirname(os.path.abspath(__file__))

sys("echo Installing...")
sys("echo V = 1.0.0a")

db.findDataCreate("main/src/USERS")

shortcut_main = shell.CreateShortcut(os.path.join(script_dir, "Start.lnk"))
shortcut_main.TargetPath = os.path.join(f"{script_dir}\\main\\src", "main.py")
shortcut_main.IconLocation = os.path.join(f"{script_dir}\\main", "icon.ico")
shortcut_main.Save()

shortcut_config = shell.CreateShortcut(os.path.join(script_dir, "Config.lnk"))
shortcut_config.TargetPath = os.path.join(f"{script_dir}\\main\\ins.files", "config.py")
shortcut_config.IconLocation = os.path.join(f"{script_dir}\\main", "icon.ico")
shortcut_config.Save()

sys("move install.py main/ins.files")
