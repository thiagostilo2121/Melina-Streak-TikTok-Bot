import os
import subprocess
import sys
import time

# Verificar la versión de Python
required_version = (3, 10)
if sys.version_info < required_version:
    print(f"[ERROR] Python {required_version[0]}.{required_version[1]} or better required.")
    print(f"You have Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}.")
    print("\n>>> To update it, go to https://www.python.org/ <<<")
    time.sleep(5)
    exit(1)

def run_command(command, success_msg=None, error_msg=None):
    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if success_msg:
            print(success_msg)
        return result
    except subprocess.CalledProcessError as e:
        if error_msg:
            print(f"{error_msg}\n{e.stderr}")
        else:
            print(e.stderr)
        time.sleep(3)
        exit(1)

def install_win(script_dir):
    # Create shortcuts
    shortcut_main = shell.CreateShortcut(os.path.join(script_dir, "Start.lnk"))
    shortcut_main.TargetPath = os.path.join(f"{script_dir}\\main\\src", "index.py")
    shortcut_main.IconLocation = os.path.join(f"{script_dir}\\main", "icon.ico")
    shortcut_main.Save()

    shortcut_config = shell.CreateShortcut(os.path.join(script_dir, "Config.lnk"))
    shortcut_config.TargetPath = os.path.join(f"{script_dir}\\main\\src", "config.py")
    shortcut_config.IconLocation = os.path.join(f"{script_dir}\\main", "icon.ico")
    shortcut_config.Save()

    # Move installation script
    install_script_path = os.path.join(script_dir, "install.py")
    destination_path = "main/ins.files"
    os.makedirs(destination_path, exist_ok=True)
    os.replace(install_script_path, os.path.join(destination_path, "install.py"))

def install_no_win(script_dir):
    install_script_path = os.path.join(f"{script_dir}/main/src", "index.py")
    destination_path = script_dir
    os.makedirs(destination_path, exist_ok=True)
    os.replace(install_script_path, os.path.join(destination_path, "index.py"))

    install_script_path = os.path.join(f"{script_dir}/main/src", "config.py")
    destination_path = script_dir
    os.makedirs(destination_path, exist_ok=True)
    os.replace(install_script_path, os.path.join(destination_path, "config.py"))

    install_script_path = os.path.join(script_dir, "install.py")
    destination_path = "main/ins.files"
    os.makedirs(destination_path, exist_ok=True)
    os.replace(install_script_path, os.path.join(destination_path, "install.py"))

if not os.access(os.curdir, os.W_OK):
    print("[ERROR] Insufficient permissions to write to the installation directory.")
    time.sleep(3)
    exit(1)

# Install requirements
requirements_path = "main/ins.files/requirements.txt"
run_command(
    f"pip install -r {requirements_path} --quiet",
    success_msg="[INFO] Requirements installed successfully.",
    error_msg="[ERROR] Failed to install requirements."
)

import win32com.client
import json
import localDataBaseFolder as db

# Initialize COM shell
shell = win32com.client.Dispatch("WScript.shell")
script_dir = os.path.dirname(os.path.abspath(__file__))

# Load app version
try:
    with open("main/app/config/app.json", "r", encoding="utf-8") as file_json:
        datosapp = json.load(file_json)
        version = datosapp["version"]
except FileNotFoundError:
    print("[ERROR] Configuration file not found.")
    time.sleep(3)
    exit(1)
except json.JSONDecodeError:
    print("[ERROR] Configuration file is invalid.")
    time.sleep(3)
    exit(1)

# Display installation messages
print("Installing...")
print(f"V = {version}")

# Create necessary directories
dirs = ["main/src/USERS/", "main/logs/", "main/data/", "main/data/User Data/"]
for dir in dirs:
    db.findDataCreate(dir)
db.findChaseCreate("main/logs/", "index_log")

if os.name != "nt":
    print("[INFO] Shortcut creation is only supported on Windows.")
    install_no_win(script_dir)
else: install_win(script_dir)

print("[INFO] Installation completed.")

time.sleep(3)