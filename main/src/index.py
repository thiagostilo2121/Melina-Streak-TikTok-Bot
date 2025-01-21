print("Cargando/Loading...")
import os
import json
import time
import pyperclip
import schedule
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from _cmd.config import prints
import localDataBaseFolder as db

# Constantes
PREFERENCES_FILE = "main/src/preferences.json"
LOCALES_DIR = "main/locales/"
USERS_DIR = "main/src/USERS/"

# Inicializar base de datos
db.setChase("main/src/interface", "indexad", "", "w")
db.setChase("main/src/interface", "indexadtype", "", "w")

# Función para cargar idioma desde un archivo JSON
def load_language(lang_code):
    try:
        with open(os.path.join(LOCALES_DIR, f"{lang_code}.json"), "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        with open(os.path.join(LOCALES_DIR, "en.json"), "r", encoding="utf-8") as file:
            return json.load(file)

# Función para limpiar pantalla
def cls():
    os.system("cls" if os.name == "nt" else "clear")

# Cargar preferencias
def load_preferences():
    try:
        with open(PREFERENCES_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        prints.print_colored_bold("[ERROR]" + translations["error_reading_prefereces_file"], "31")
        exit()
    except json.JSONDecodeError:
        prints.print_colored_bold("[ERROR]" + translations["no_preferences_found]"], "31")
        exit()

# Iniciar sesión en Chrome con perfil de usuario
def iniciar_sesion(user_windows, cname):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument(
        rf"user-data-dir=C:\\Users\\{user_windows}\\AppData\\Local\\Google\\Chrome\\User Data\\{cname}"
    )
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Listar usuarios disponibles
def listar_usuarios():
    try:
        files = [f for f in os.listdir(USERS_DIR) if f.endswith(".txt")]
        if not files:
            raise FileNotFoundError(translations["no_users_found"])
        return files
    except FileNotFoundError as e:
        prints.print_colored_bold(f"[ERROR] {str(e)}", "31")
        exit()

# Seleccionar usuario
def seleccionar_usuario(user_files):
    print(translations["select_target"])
    for idx, file in enumerate(user_files, start=1):
        print(f"[{idx}] {file[:-4]}")

    while True:
        try:
            choice = int(input(translations["input_option"]))
            if 1 <= choice <= len(user_files):
                return user_files[choice - 1]
            raise ValueError
        except ValueError:
            prints.print_colored_bold("[ERROR] " + translations["invalid_option"], "31")

# Enviar mensaje al usuario seleccionado
def enviar_mensaje(driver, user_file, message):
    print(translations["sending_message"])
    try:
        driver.get("https://www.tiktok.com/messages")
        time.sleep(20)

        with open(os.path.join(USERS_DIR, user_file), "r", encoding="utf-8") as file:
            username = file.read().strip()

        conversaciones = driver.find_elements(By.XPATH, f"//p[contains(@class, 'PInfoNickname') and text()='{username}']")
        if not conversaciones:
            raise Exception(translations["user_not_found"])

        conversaciones[0].click()
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

# Programar tarea
def programar_envio(driver, user_file, message, hour):
    schedule.every().day.at(hour).do(enviar_mensaje, driver, user_file, message)
    print(translations["scheduler_started"])
    while True:
        schedule.run_pending()
        time.sleep(1)

# Main
if __name__ == "__main__":
    cls()
    datos = load_preferences()
    LANG_CODE = datos.get("language", "en")
    translations = load_language(LANG_CODE)

    driver = iniciar_sesion(datos["wuser"], datos["cname"])
    user_files = listar_usuarios()
    selected_user = seleccionar_usuario(user_files)
    cls()
    print(translations["message_scheduled"].format(hour=datos["hour"]))
    programar_envio(driver, selected_user, datos["message"], datos["hour"])
