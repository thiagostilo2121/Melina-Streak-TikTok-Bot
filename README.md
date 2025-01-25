# Melina Streak TikTok Bot

## Español

![Logo del Proyecto](main/icon.ico)

**Creado por:** Thiago Valentín Stilo Limarino  
**Fecha de Creación:** 2/1/2025  
**Fecha de lanzamiento:** 11/1/2025   
**Versión Actual:** 1.3.0 (UNDER DEV)   
**Redes Sociales:** [Twitter/X](https://x.com/melina_stbot)   

---

## 🔄 Introducción
Melina Streak TikTok Bot es una herramienta automática desarrollada en Python para mantener la racha de mensajes con tus amigos en TikTok. Diseñada para ser fácil de usar y altamente personalizable, este bot se ejecuta diariamente en el horario que elijas y envía mensajes automáticos a tus contactos seleccionados.

---

## 🔧 Características Principales
- • **Automatización diaria:** Envía mensajes automáticos todos los días a una hora predeterminada.
- • **Configuración personalizable:** Selecciona el contacto y el mensaje a enviar mediante archivos de configuración.
- • **Compatible con perfiles de Chrome:** Utiliza perfiles personalizados para evitar verificaciones repetitivas al iniciar sesión.
- • **Soporte múltiple:** Gestiona múltiples contactos usando archivos en la carpeta `USERS`.
- • **Mejoras en la gestión de errores y excepciones.**

---

## ⚡ Requisitos
1. **Python 3.10+**
2. **Google Chrome instalado.**
3. **WebDriver de Chrome** (automáticamente gestionado por el bot).
4. **Sistema operativo compatible:** Windows 10/11.
---

## 📄 Instalación y Configuración
1. **Descargar repositorio**

2. **Instalar las dependencias (instrucciones en el archivo [INSTRUCCIONES.txt](INSTRUCCIONES.txt))**
   Abra `install.py`

   o ejecute

   ```bash
   cd RUTA/A/LA/CARPETA/DE/MELINASTB
   pip install -r main/ins.files/requirements.txt
   ```

3. **Configurar el archivo `Config`**
   - Abre el archivo `Config` y configura el nombre del perfil de Chrome y otros parámetros según tus necesidades.

4. **Crear archivos de usuarios en la carpeta `main/src/USERS` (puedes hacerlo con `Config`)**
   - Crea un archivo de texto con el nombre del contacto objetivo, por ejemplo, `STILO.txt`.
   - Dentro del archivo, escribe el nombre exacto del usuario en TikTok (por ejemplo, `Stilo`).
  
5. **Configurar el perfil de Chrome**
   - Abra el programa (con el modo primer plano).
   - Inicia sesión en TikTok al menos una vez con tu cuenta principal (con iniciar una vez no deberá hacerlo más y ya podrá usar el modo segundo plano).

---

## 💡 Uso
1. **Ejecutar el bot**
   - Abre `Start`
2. Selecciona el usuario objetivo desde el menú.
3. El bot enviará automáticamente un mensaje a la hora programada.

---

## 🔧 Contribuir
Si deseas contribuir al desarrollo de este proyecto:
1. Haz un fork del repositorio.
2. Crea una rama para tus cambios.
   ```bash
   git checkout -b mi-nueva-funcionalidad
   ```
3. Envía un pull request detallando tus cambios.

---

## 🔧 Licencia
Este proyecto está licenciado bajo la [Licencia MIT](LICENSE).

---

## 🎉 Changelog

Mira los cambios [aquí](doc/changelog.md).

---

## 🔗 Recursos
- [Documentación oficial de Selenium](https://www.selenium.dev/documentation)
- [Versiones oficiales de Melina STB](https://www.github.com/thiagostilo2121/Melina-Streak-TikTok-Bot/releases)
- [LICENCIA](doc/LICENSE)
- [Codigo de conducta](doc/CODE-OF-CONDUCT.md)

---

## ⚠️ Advertencia
Este programa es relativamente nuevo y, por lo tanto, se encuentra sujeto a constantes cambios. También contiene errores o bugs que serán solucionados en cada actualización.

Le pido disculpas por el largo y tedioso proceso de instalación y configuración manual del programa (cual se especifica en [INSTRUCCIONES.txt](INSTRUCCIONES.txt)) que es debido a que: 1. Deseo procurar la seguridad del usuario para que no crea que su cuenta de TikTok es vulnerada 2. El programa NO puede iniciar sesión en cuentas de TikTok debido a la verificación solicitada por la plataforma. A pesar de esto, trataré de mejorar el proceso de instalación y configuración en el futuro.

---

## 🌟 Créditos
Creado con pasión por Thiago Valentín Stilo Limarino. Las pruebas del programa fueron llevadas a cabo por el autor y una persona más.

Here is the translated text into English:  

---

## English

![Project Logo](main/icon.ico)

**Created by:** Thiago Valentín Stilo Limarino  
**Creation Date:** 1/2/2025  
**Release Date:** 1/11/2025  
**Current Version:** 1.3.0 (UNDER DEV)
**Social Media:** [Twitter/X](https://x.com/melina_stbot)   

---

## 🔄 Introduction
Melina Streak TikTok Bot is an automated tool developed in Python to maintain streaks of messages with your friends on TikTok. Designed to be user-friendly and highly customizable, this bot runs daily at your chosen time and sends automatic messages to your selected contacts.

---

## 🔧 Key Features
- • **Daily automation:** Sends automatic messages every day at a pre-set time.
- • **Customizable configuration:** Select the contact and message to send through configuration files.
- • **Chrome profile compatibility:** Uses personalized profiles to avoid repetitive login verifications.
- • **Multiple support:** Manage multiple contacts using files in the `USERS` folder.
- • **Improved error and exception handling.**

---

## ⚡ Requirements
1. **Python 3.10+**
2. **Google Chrome installed.**
3. **Chrome WebDriver** (automatically managed by the bot).
4. **Compatible operating system:** Windows 10/11.

---

## 📄 Installation and Configuration
1. **Download the repository.**

2. **Install dependencies (instructions in the file [INSTRUCTIONS.txt](INSTRUCTIONS.txt))**
   Open `install.py`

   or execute

   ```bash
   cd PATH/TO/MELINASTB/FOLDER
   pip install -r main/ins.files/requirements.txt
   ```

3. **Configure the `Config` file.**
   - Open the `Config` file and set up the Chrome profile name and other parameters as needed.

4. **Create user files in the `main/src/USERS` folder (this can be done with `Config`).**
   - Create a text file named after the target contact, e.g., `STILO.txt`.
   - Inside the file, write the exact name of the user on TikTok (e.g., `Stilo`).
  
5. **Set up the Chrome profile.**
   - Open the program (make sure you are with the foreground mode activated).
   - Log in to TikTok at least once with your main account (you won't need to do this again after the first time and now you can use the background mode).

---

## 💡 Usage
1. **Run the bot.**
   - Open `Start`.
2. Select the target user from the menu.
3. The bot will automatically send a message at the scheduled time.

---

## 🔧 Contributing
If you’d like to contribute to this project:
1. Fork the repository.
2. Create a branch for your changes.
   ```bash
   git checkout -b my-new-feature
   ```
3. Submit a pull request detailing your changes.

---

## 🔧 License
This project is licensed under the [MIT License](LICENSE).

---

## 🎉 Changelog

See the changelog [here](doc/changelog.md).

---

## 🔗 Resources
- [Official Selenium Documentation](https://www.selenium.dev/documentation)
- [Official Melina STB Releases](https://www.github.com/thiagostilo2121/Melina-Streak-TikTok-Bot/releases)
- [LICENSE](doc/LICENSE)
- [Code of Conduct](doc/CODE-OF-CONDUCT.md)

---

## ⚠️ Disclaimer
This program is relatively new and, therefore, subject to constant changes. It also contains bugs or errors that will be fixed in future updates.

I apologize for the long and tedious manual installation and configuration process (specified in [INSTRUCTIONS.txt](INSTRUCTIONS.txt)), which is due to: 1. Ensuring user security so they do not feel their TikTok account is at risk. 2. The program CANNOT log in to TikTok accounts due to verification required by the platform. Despite this, I will strive to improve the installation and configuration process in the future.

---

## 🌟 Credits
Created with passion by Thiago Valentín Stilo Limarino. Program testing was conducted by the author and one other person.