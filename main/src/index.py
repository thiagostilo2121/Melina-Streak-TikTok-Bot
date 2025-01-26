print("Cargando/Loading...")
import os
import json
import time
import pyperclip
import schedule
import logging
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException
try:
    from _cmd.config import prints
except ModuleNotFoundError:
    from main.src._cmd.config import prints
import localDataBaseFolder as db

# Configuración del logger para guardar los logs en un archivo
db.setChase("main/logs", "index_log", "--- CLEARED ---\n\n", "w")
LOG_FILE = "main/logs/index_log.txt"
logging.basicConfig(filename=LOG_FILE, level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Constantes
PREFERENCES_FILE = "main/src/preferences.json"
LOCALES_DIR = "main/locales/"
USERS_DIR = "main/src/USERS/"

# Inicializar base de datos
db.setChase("main/src/interface", "indexcls", "False", "w")

# Función para cargar idioma desde un archivo JSON
def load_language(lang_code):
    try:
        with open(os.path.join(LOCALES_DIR, f"{lang_code}.json"), "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        logging.error(f"Archivo de idioma no encontrado, usando inglés: {lang_code}")
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
        logging.error(f"Error al leer el archivo de preferencias {PREFERENCES_FILE}")
        prints.print_colored_bold("[ERROR]" + translations["error_reading_prefereces_file"], "31")
        time.sleep(3)
        exit()
    except json.JSONDecodeError:
        logging.error("Error al analizar el archivo JSON de preferencias.")
        prints.print_colored_bold("[ERROR]" + translations["no_preferences_found"], "31")
        time.sleep(3)
        exit()

# Iniciar sesión en Chrome con perfil de usuario
def iniciar_sesion(cname, headless):
    try:
        USERDATADIR = os.path.dirname(os.path.abspath(f"main/data/User Data/{cname}/"))
        print(USERDATADIR)
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        options.add_argument(
            rf"user-data-dir={USERDATADIR}\\{cname}"
            #rf"user-data-dir=C:\\Users\\{user_windows}\\AppData\\Local\\Google\\Chrome\\User Data\\{cname}"
        )

        options.add_argument("--log-level=3")
        
        # Configurar modo headless si está habilitado en las preferencias
        if headless:
            options.add_argument("--headless")
            options.add_argument("--disable-gpu")
            options.add_argument("--window-size=1920,1080")


        try:
           driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        except:
            try:
                driver =  webdriver.Chrome(service=Service("main\data\drivers\chromedriver-win64_132\chromedriver.exe"), options=options)
            except:
                try:
                    driver =  webdriver.Chrome(service=Service("main/data/drivers/chromedriver-win64_133/chromedriver.exe"), options=options)
                except:
                    driver =  webdriver.Chrome(service=Service("main/data/drivers/chromedriver-win64_134/chromedriver.exe"), options=options)
        return driver
    except Exception as e:
        logging.error(f"Error al iniciar sesión en Chrome: {str(e)}")
        prints.print_colored_bold("[ERROR] " + translations["error_occurred"].format(error=str(e)), "31")
        time.sleep(3)
        exit()

# Listar usuarios disponibles
def listar_usuarios():
    try:
        files = [f for f in os.listdir(USERS_DIR) if f.endswith(".txt")]
        if not files:
            logging.warning("No se encontraron usuarios.")
            prints.print_colored_bold("[ERROR] " + translations["no_users_found"], "31")
            time.sleep(3)
            exit()
        return files
    except FileNotFoundError as e:
        logging.error(f"Error al listar usuarios: {str(e)}")
        prints.print_colored_bold(f"[ERROR] {str(e)}", "31")
        time.sleep(3)
        exit()

# Función para enviar mensaje a un usuario
def enviar_mensaje(user_files, message, headless, driver):
    logging.info(f"Enviando mensaje a {len(user_files)} usuarios.")
    try:

        if headless:
            driver = iniciar_sesion(datos["cname"], headless=False)  
        
        driver.get("https://www.tiktok.com/messages")

        cls()

        for user_file in user_files:

            indexcls = bool(db.readChase("main/src/interface", "indexcls"))

            with open(os.path.join(USERS_DIR, user_file), "r", encoding="utf-8") as file:
                username = file.read().strip()

            try:
                element = WebDriverWait(driver, 20).until(
                    EC.visibility_of_element_located((By.XPATH, f"//p[contains(@class, 'css-1mez8np-PInfoNickname eii3f6d9') and text()='{username}']"))
                )
            except TimeoutException:
                prints.print_colored_bold("[ERROR] " + translations["user_not_found_timeout"].format(user=username), "31")
                continue  # Saltar al siguiente usuario

            # Buscar la conversación con el usuario
            conversaciones = driver.find_elements(By.XPATH, f"//p[contains(@class, 'PInfoNickname') and text()='{username}']")
            if not conversaciones:
                prints.print_colored_bold("[ERROR] " + translations["user_not_found"].format(user=username), "31")
                continue

            conversaciones[0].click()

            # Enviar el mensaje
            campo_mensaje = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//div[@contenteditable='true']"))
            )
            driver.execute_script(""" 
                let campo = arguments[0];
                campo.focus();
            """, campo_mensaje)  
            pyperclip.copy(message)
            campo_mensaje.send_keys(Keys.CONTROL, "v")
            time.sleep(1)
            campo_mensaje.send_keys(Keys.RETURN)

            logging.info(f"Mensaje enviado a {username}")

            if indexcls == False:
                cls()
                db.setChase("main/src/interface", "indexcls", "True", "w")

            print(translations["message_sent"].format(user=username))

        if headless:
            driver.quit()
        
        print("\n Proceso de envio de mensaje finalizado.")

    except Exception as e:
        logging.error(f"Error al enviar mensaje: {str(e)}")
        prints.print_colored_bold("[ERROR] " + translations["error_occurred"].format(error=str(e)), "31")

# Programar tarea para enviar mensajes a todos los usuarios
def programar_envio(user_files, message: str, hour: str, headless: bool, driver):
    #schedule.every().day.at(hour).do(enviar_mensaje, user_files, message, headless, driver)
    logging.info(f"Tarea programada para enviar mensaje a las {hour}")
    print(translations["scheduler_started"])
    enviar_mensaje(user_files, message, headless, driver) # <-- For testing
    while True:
        schedule.run_pending()
        time.sleep(1)

# Main
if __name__ == "__main__":
    try:
        cls()
        datos = load_preferences()
        LANG_CODE = datos.get("language", "en")
        translations = load_language(LANG_CODE)

        if not datos["cname"] or not datos["hour"] or not datos["message"]: 
            logging.error("Preferencias incompletas.")
            prints.print_colored_bold("[ERROR] " + translations.get("empty_preferences_error"), "31")
            time.sleep(3)
            exit()

        # Obtener el valor de 'headless' desde las preferencias
        headless = datos.get("headless", False)
        if headless == False: driver = iniciar_sesion(datos["cname"], False)
        else: driver = None

        # Listar todos los usuarios disponibles
        user_files = listar_usuarios()

        # Confirmar que el mensaje está programado
        cls()
        print(translations["message_scheduled"].format(hour=datos["hour"]))

        # Programar envío de mensaje a todos los usuarios
        programar_envio(user_files=user_files, message=datos["message"], hour=datos["hour"], headless=headless, driver=driver)

    except Exception as e:
        logging.error(f"Error general: {str(e)}")
        try:
            errormsj = translations.get("error_ocurred")
        except: errormsj = "An error occurred: {error}"
        prints.print_colored_bold("[ERROR] " + errormsj.format(error=str(e)), color_code="31")
        time.sleep(3)
        exit()
