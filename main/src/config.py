import json
import os
import localDataBaseFolder as db
try:
    from _cmd import config
except ModuleNotFoundError:
    from main.src._cmd import config

prints = config.prints

db.setChase("main/src/interface", "configadtype", "", "w")

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
LANG_CODE = datos.get("language", "en")  # Idioma predeterminado es "es"
translations = load_language(LANG_CODE)

db.setChase("main/src/interface", "configad", "", "w")

# Variables globales
with open("main/app/config/app.json", "r", encoding="utf-8") as file_json:
    datosapp = json.load(file_json)
    version = datosapp["version"]

menutitle = translations["menu_title"].format(version=version)

# Función para limpiar pantalla
def cls(): os.system("cls")

# Guardar preferencias
def save_preferences():
    with open("main/src/preferences.json", "w", encoding="utf-8") as file_json:
        json.dump(datos, file_json, indent=4, ensure_ascii=False)

# Funciones de configuración del bot
def configure_bot():
    configad = db.setChase("main/src/interface", "configad", "", "w")
    configadtype = db.setChase("main/src/interface", "configadtype", "", "w")
    while True:
        cls()
        configad = db.readChase("main/src/interface", "configad")
        configadtype = db.readChase("main/src/interface", "configadtype")
        if configadtype == "error": 
            color = "31"
            prefix = "[ERROR] " 
        else: 
            color = "32" 
            prefix = ""
        prints.print_colored_bold(prefix + configad, color)
        print(menutitle + translations["bot_config_menu"])
        try:
            choice = int(input(translations["option"]))
            if choice == 1:
                optionBot1()
            elif choice == 2:
                optionBot2()
            elif choice == 3:
                optionBot3()
            elif choice == 4:
                optionBot4()
            elif choice == 5:
                optionBot5()
            elif choice == 0:
                configad = db.setChase("main/src/interface", "configad", "", "w")
                configadtype = db.setChase("main/src/interface", "configadtype", "","w")                
                break
            else:
                raise ValueError
        except ValueError:
            db.setChase("main/src/interface", "configad", translations["invalid_option"], "w")
            db.setChase("main/src/interface", "configadtype", "error", "w")

# Funciones de configuración del programa
def configure_program():
    configad = db.setChase("main/src/interface", "configad", "", "w")
    configadtype = db.setChase("main/src/interface", "configadtype", "", "w")
    while True:
        cls()
        configad = db.readChase("main/src/interface", "configad")
        configadtype = db.readChase("main/src/interface", "configadtype")
        if configadtype == "error": 
            color = "31"
            prefix = "[ERROR] " 
        else: 
            color = "32" 
            prefix = ""
        prints.print_colored_bold(prefix + configad, color)
        print(menutitle + translations["program_config_menu"])
        try:
            choice = int(input(translations["option"]))
            if choice == 1:
                option5()
            elif choice == 2:
                option6()
            elif choice == 0:
                configad = db.setChase("main/src/interface", "configad", "", "w")
                configadtype = db.setChase("main/src/interface", "configadtype", "","w")   
                break
            else:
                raise ValueError
        except ValueError:
            db.setChase("main/src/interface", "configad", translations["invalid_option"], "w")
            db.setChase("main/src/interface", "configadtype", "error", "w")

# Funciones de opciones existentes
def optionBot1():
    cname = input(translations["chrome_account_name"])
    datos["cname"] = cname
    wuser = input(translations["windows_account_name"])
    datos["wuser"] = wuser
    save_preferences()
    db.setChase("main/src/interface", "configad", translations.get("action_successful"), "w")
    db.setChase("main/src/interface", "configadtype", "successful", "w")

def optionBot2():
    hour = input(translations["send_schedule"])
    datos["hour"] = hour
    save_preferences()
    db.setChase("main/src/interface", "configad", translations.get("action_successful"), "w")
    db.setChase("main/src/interface", "configadtype", "successful", "w")

def optionBot3():
    nfile = input(translations["file_name"])
    uname = input(translations["tiktok_user"])
    db.createChase("main/src/USERS", nfile)
    with open(f"main/src/USERS/{nfile}.txt", "w", encoding="utf-8") as local:
        local.write(uname)
    db.setChase("main/src/interface", "configad", translations.get("action_successful"), "w")
    db.setChase("main/src/interface", "configadtype", "successful", "w")

def optionBot4():
    message = input(translations["auto_message"])
    datos["message"] = message
    save_preferences()
    db.setChase("main/src/interface", "configad", translations.get("action_successful"), "w")
    db.setChase("main/src/interface", "configadtype", "successful", "w")

def optionBot5():
    del_file = input(translations["delete_file_name"])
    try:
        db.removeChase("main/src/USERS", del_file)
        db.setChase("main/src/interface", "configad", translations.get("action_successful"), "w")
        db.setChase("main/src/interface", "configadtype", "successful", "w")
    except:
        db.setChase("main/src/interface", "configad", translations.get("user_file_no_found"), "w")
        db.setChase("main/src/interface", "configadtype", "error", "w")

def option5():
    global LANG_CODE, translations
    print("[1] Espa\u00f1ol (es)\n[2] English (en)")
    lang_choice = input(translations.get("choose_language", "Choose your language: "))
    if lang_choice == "1" or lang_choice.lower() == "es":
        LANG_CODE = "es"
    elif lang_choice == "2" or lang_choice.lower() == "en":
        LANG_CODE = "en"
    else:
        db.setChase("main/src/interface", "configad", translations.get("invalid_option"), "w")
        db.setChase("main/src/interface", "configadtype", "error", "w")
        return
    datos["language"] = LANG_CODE
    translations = load_language(LANG_CODE)
    save_preferences()
    db.setChase("main/src/interface", "configad", translations.get("action_successful"), "w")
    db.setChase("main/src/interface", "configadtype", "successful", "w")

def option6():
    global datos
    prints.print_colored_bold(
                f"\n[{translations.get('warning')}] " +
                translations.get("background_browser_advice") + "\n",
                "33"
    )
    print("[1] " + translations["background_yes"])
    print("[2] " + translations["background_no"] + "\n")
    try:
        bg_choice = int(input(translations["option"])) 
        if bg_choice == 1:
            datos["headless"] = True
            save_preferences()
        elif bg_choice == 2:
            datos["headless"] = False
            save_preferences()
        else:
            raise ValueError
        db.setChase("main/src/interface", "configad", translations.get("action_successful"), "w")
        db.setChase("main/src/interface", "configadtype", "successful", "w")
    except ValueError:
        db.setChase("main/src/interface", "configad", translations.get("invalid_option"), "w")
        db.setChase("main/src/interface", "configadtype", "error", "w")


# Menú principal
menu = True
while menu:
    cls()
    configad = db.readChase("main/src/interface", "configad")
    configadtype = db.readChase("main/src/interface", "configadtype")
    if configadtype == "error": 
            color = "31"
            prefix = "[ERROR] " 
    else: 
            color = "32" 
            prefix = ""
    prints.print_colored_bold(prefix + configad, color)
    print(menutitle)
    print("[1]", translations["configure_bot"])
    print("[2]", translations["configure_program"])
    print("[0]", translations["exit"], "\n")
    try:
        choice = int(input(translations["option"]))
        if choice == 1:
            configure_bot()
        elif choice == 2:
            configure_program()
        elif choice == 0:
            menu = False
            exit()
        else:
            db.setChase("main/src/interface", "configad", translations["invalid_option"], "w")
            db.setChase("main/src/interface", "configadtype", "error", "w")
    except ValueError:
        db.setChase("main/src/interface", "configad", translations["invalid_option"], "w")
        db.setChase("main/src/interface", "configadtype", "error", "w")