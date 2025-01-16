print("Cargando/Loading...")
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import schedule
import localDataBaseFolder as db
import os
import json
import time
import pyperclip

# Cargar idioma desde preferencias
def load_language(lang_code):
    try:
        with open(f"main/locales/{lang_code}.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        with open("main/locales/en.json", "r", encoding="utf-8") as file:
            return json.load(file)

# Función para limpiar pantalla
def cls():
    os.system("cls")

cls()

# Cargar preferencias
json_pref = "main/src/preferences.json"
with open(json_pref, "r", encoding="utf-8") as json_file:
    datos = json.load(json_file)

LANG_CODE = datos.get("language", "es")
translations = load_language(LANG_CODE)

user_windows = datos["wuser"]
cname = datos["cname"]
message = datos["message"]
hour = datos["hour"]

# Ruta de archivos
script_dir = os.path.dirname(os.path.abspath(__file__))
users_folder = os.path.join(script_dir, "USERS")

# Iniciar sesión en Chrome con perfil de usuario
def iniciar_sesion():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument(
        r"user-data-dir=C:\\Users\\" + user_windows + r"\\AppData\\Local\\Google\\Chrome\\User Data\\" + cname
    )
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

driver = iniciar_sesion()

# Listar usuarios desde la carpeta USERS
user_files = [f for f in os.listdir(users_folder) if f.endswith('.txt')]
if not user_files:
    print(translations["no_users_found"])
    exit()

print(translations["select_target"])
for idx, file in enumerate(user_files, start=1):
    print(f"[{idx}] {file[:-4]}")

try:
    choice = int(input(translations["input_option"]))
    if choice < 1 or choice > len(user_files):
        raise ValueError
except ValueError:
    print(translations["invalid_option"])
    exit()

cls()
print(translations["message_scheduled"].format(hour=hour))

# Enviar mensaje al usuario seleccionado
def enviar_mensaje():
    print(translations["sending_message"])
    try:
        driver.get('https://www.tiktok.com/messages')
        time.sleep(20)  

        selected_file = user_files[choice - 1]
        with open(os.path.join(users_folder, selected_file), 'r', encoding='utf-8') as file:
            photo = file.read().strip()

        conversaciones = driver.find_elements(By.XPATH, f"//p[contains(@class, 'PInfoNickname') and text()='{photo}']")
        if conversaciones:
            conversaciones[0].click()
        else:
            print(translations["user_not_found"])
            driver.quit()
            return

        time.sleep(5)  
        
        campo_mensaje = driver.find_element(By.XPATH, "//div[@contenteditable='true']")
        pyperclip.copy(message)
        campo_mensaje.send_keys(Keys.CONTROL, "v")
        time.sleep(1)  

        campo_mensaje.send_keys(Keys.RETURN)
        cls()
        print(translations["message_sent"])

    except Exception as e:
        cls()
        print(translations["error_occurred"].format(error=str(e)))

# Programar envío del mensaje
schedule.every().day.at(hour).do(enviar_mensaje)

print(translations["scheduler_started"])
while True:
    schedule.run_pending()
    time.sleep(1)