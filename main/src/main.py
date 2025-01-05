print("Cargando...")
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
options = webdriver.ChromeOptions()
# Configuración para usar el perfil de Chrome de "BOT"
def cls(): os.system("cls")
cls()

json_pref = "preferences.json"

script_dir = os.path.dirname(os.path.abspath(__file__))
users_folder = os.path.join(script_dir, "USERS")

with open(json_pref, "r", encoding="utf-8") as json_file:
    datos = json.load(json_file)

user_windows = datos["wuser"]
cname = datos["cname"]
message = datos["message"]
hour = datos["hour"]

def iniciar_sesion():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument(r"user-data-dir=C:\\Users\\"+ user_windows +r"\\AppData\\Local\\Google\\Chrome\\User Data\\" + cname)  # Ruta a tu perfil "BOT"
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

driver = iniciar_sesion()

user_files = [f for f in os.listdir(users_folder) if f.endswith('.txt')]

if not user_files:
    print("No se encontraron archivos en la carpeta USERS. Crea al menos un archivo.")
    exit()

# Mostrar opciones al usuario
print("Seleccione un objetivo:")
for idx, file in enumerate(user_files, start=1):
    print(f"[{idx}] {file[:-4]}")  # Muestra el nombre sin la extensión .txt

# Obtener la selección del usuario
try:
    choice = int(input("Ingresa el número de la opción: "))
    if choice < 1 or choice > len(user_files):
        raise ValueError
except ValueError:
    print("Opción no válida.")
    exit()

cls()
print(f"\nSe enviará el mensaje al usuario seleccionado a las {hour}hs")

# Función para enviar el mensaje
def enviar_mensaje():
    print("Iniciando proceso de envío de mensaje...")
    try:
        # Abre la página de mensajes de TikTok
        driver.get('https://www.tiktok.com/messages')
        time.sleep(20)  # Espera a que cargue la página

        # Localiza la conversación y haz click
        selected_file = user_files[choice - 1]
        with open(os.path.join(users_folder, selected_file), 'r', encoding='utf-8') as file:
            photo = file.read().strip()   
        conversaciones = driver.find_elements(By.XPATH, f"//p[contains(@class, 'PInfoNickname') and text()='{photo}']")  # Ajusta el nombre según sea necesario
        if conversaciones:
            conversaciones[0].click()
        else:
            print("No se encontró la conversación con el usuario especificado.")
            driver.quit()
            return

        time.sleep(5)  # Espera a que se abra la conversación

        # Encuentra el campo de texto de mensaje y escribe
        campo_mensaje = driver.find_element(By.XPATH, "//div[@contenteditable='true']")  # Ajusta el XPath del campo
        pyperclip.copy(message)
        campo_mensaje.send_keys(Keys.CONTROL, "v")
        time.sleep(1)  # Pequeño retardo para simular escritura humana

        # Presiona Enter para enviar el mensaje
        campo_mensaje.send_keys(Keys.RETURN)
        cls()
        print("Mensaje enviado correctamente.")

    except Exception as e:
        cls()
        print(f"Ocurrió un error: {e}")


# Programar el envío diario a las 00:00 (GMT-3)
schedule.every().day.at(hour).do(enviar_mensaje)

print("Programador iniciado. Esperando la hora programada...")
while True:
    schedule.run_pending()
    time.sleep(1)