import localDataBaseFolder as db

print("=== MELINA STREAK BOT V1.0.0a1 ===\n\n")

print("[1] Cambiar nombre de perfil Chrome o Windows establecido\n[2] Horario de envio\n[0] Salir")

def option1():
    cname = input("Pon el nombre EXACTO de la cuenta de Google Chrome: ")
    db.setChase("src", "cname", cname, "w")
    wuser = input("Pon el nombre EXACTO de la cuenta de Windows donde se encuentra la cuenta de Google Chrome: ")
    db.setChase("src", "wuser", wuser, "w")
def option2():
    hour = input("Pon la hora en formato 24hs de envio (00:00): ")
    db.setChase("src", "hour", hour, "w")

try:
    choice = int(input("Ingresa el número de la opción: "))
    if choice == 1: option1()
    elif choice == 2: option2()
    if choice < 1 or choice > 2:
        raise ValueError
except ValueError:
    print("Opción no válida.")
    exit()