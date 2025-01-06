import json
import localDataBaseFolder as db
print("=== MELINA STREAK TIKTOK BOT V1.0.0 [ALPHA] ===\n\nEl programa se encuentra en su versión ALPHA, está sujeto a constantes cambios y puede contener errores o bugs.\n\n")

print("[1] Cambiar nombre de perfil Chrome o Windows establecido\n[2] Horario de envio\n[3] Agregar usuario objetivo\n[4] Establecer mensaje automático\n[0] Salir")

with open("main/src/preferences.json", "r", encoding="utf-8") as file_json:
    datos = json.load(file_json)

def option1():
    cname = input("Pon el nombre EXACTO de la cuenta de Google Chrome: ")
    datos["cname"] = cname
    wuser = input("Pon el nombre EXACTO de la cuenta de Windows donde se encuentra la cuenta de Google Chrome: ")
    datos["wuser"] = wuser
    with open("main/src/preferences.json", "w", encoding="utf-8") as file_json:
        json.dump(datos, file_json, indent=4, ensure_ascii=False)
def option2():
    hour = input("Pon la hora en formato 24hs de envio (00:00): ")
    datos["hour"] = hour
    with open("main/src/preferences.json", "w", encoding="utf-8") as file_json:
        json.dump(datos, file_json, indent=4, ensure_ascii=False)
def option3():
    nfile = input("Establece un nombre al archivo: ")
    uname = input("Introduce el nombre de TikTok EXACTO del usuario objetivo: ")
    db.createChase("main/src/USERS", nfile)
    with open(f"main/src/USERS/{nfile}.txt", "w") as local:
        local.write(uname)
def option4():
    message = input("Establece un mensaje automático: ")
    datos["message"] = message
    with open("main/src/preferences.json", "w", encoding="utf-8") as file_json:
        json.dump(datos, file_json, indent=4, ensure_ascii=False)

try:
    choice = int(input("Ingresa el número de la opción: "))
    if choice == 1: option1()
    elif choice == 2: option2()
    elif choice == 3: option3()
    elif choice == 4: option4()
    elif choice == 0: exit()
    if choice < 0 or choice > 4:
        raise ValueError
except ValueError:
    print("Opción no válida.")
    exit()
