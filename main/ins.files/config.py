import json
import os
import localDataBaseFolder as db

# Cargar traducciones
def load_language(lang_code):
    try:
        with open(f"main/locales/{lang_code}.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        with open("main/locales/en.json", "r", encoding="utf-8") as file:
            return json.load(file)

# Cargar configuración de preferencias
with open("main/src/preferences.json", "r", encoding="utf-8") as file_json:
    datos = json.load(file_json)
LANG_CODE = datos.get("language", "es")  # Idioma predeterminado es "es"
translations = load_language(LANG_CODE)

db.setChase("main/ins.files", "configad", "", "w")

# Variables globales
with open("main/src/config/app.json", "r", encoding="utf-8") as file_json:
    datosapp = json.load(file_json)
    version = datosapp["version"]

menutitle = translations["menu_title"].format(version=version)
menuad = translations["menu_options"]

def cls(): os.system("cls")

def save_preferences():
    with open("main/src/preferences.json", "w", encoding="utf-8") as file_json:
        json.dump(datos, file_json, indent=4, ensure_ascii=False)

# Funciones de opciones
def option1():
    cname = input(translations["chrome_account_name"])
    datos["cname"] = cname
    wuser = input(translations["windows_account_name"])
    datos["wuser"] = wuser
    save_preferences()

def option2():
    hour = input(translations["send_schedule"])
    datos["hour"] = hour
    save_preferences()

def option3():
    nfile = input(translations["file_name"])
    uname = input(translations["tiktok_user"])
    db.createChase("main/src/USERS", nfile)
    with open(f"main/src/USERS/{nfile}.txt", "w", encoding="utf-8") as local:
        local.write(uname)

def option4():
    message = input(translations["auto_message"])
    datos["message"] = message
    save_preferences()

def option5():
    global LANG_CODE, translations
    print("[1] Español (es)\n[2] English (en)")
    lang_choice = input(translations.get("choose_language", "Choose your language: "))
    if lang_choice == "1" or lang_choice.lower() == "es":
        LANG_CODE = "es"
    elif lang_choice == "2" or lang_choice.lower() == "en":
        LANG_CODE = "en"
    else:
        print(translations.get("invalid_option", "Invalid option."))
        return
    datos["language"] = LANG_CODE
    translations = load_language(LANG_CODE)
    save_preferences()

menu = True

def loadMenu(): 
    cls()
    menutxt = db.readChase("main/ins.files", "configad")
    print(menutxt + menutitle + menuad)
    _a = input("\n" + translations["option"])
    print("\n")
    return _a

# Menú principal
while menu: 
    try:
        choice = int(loadMenu())
        if choice == 1: option1()
        elif choice == 2: option2()
        elif choice == 3: option3()
        elif choice == 4: option4()
        elif choice == 5: option5()
        elif choice == 0: 
            menu = False
            exit()
        db.setChase("main/ins.files", "configad", translations["action_successful"], "w")
        if choice < 0 or choice > 5:
            raise ValueError
    except ValueError:
        print(translations["invalid_option"])
        exit()