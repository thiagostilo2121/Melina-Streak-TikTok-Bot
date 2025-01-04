# Melina Streak TikTok Bot

![Logo del Proyecto](icon.ico)

**Creado por:** Thiago Valentín Stilo Limarino  
**Fecha de Creación:** 2/1/2025  
**Versión Actual:** 1.0.0 (ALPHA)  

---

## 🔄 Introducción
Melina Streak TikTok Bot es una herramienta automática desarrollada en Python para mantener la racha de mensajes con tus amigos en TikTok. Diseñada para ser fácil de usar y altamente personalizable, este bot se ejecuta diariamente en el horario que elijas y envía mensajes automáticos a tus contactos seleccionados.

---

## 🔧 Características Principales
- • **Automatización diaria:** Envía mensajes automáticos todos los días a una hora predeterminada.
- • **Configuración personalizable:** Selecciona el contacto y el mensaje a enviar mediante archivos de configuración.
- • **Compatible con perfiles de Chrome:** Utiliza perfiles personalizados para evitar verificaciones repetitivas al iniciar sesión.
- • **Soporte múltiple:** Gestiona múltiples contactos usando archivos en la carpeta `USERS`.

---

## ⚡ Requisitos
1. **Python 3.10+**
2. **Google Chrome instalado.**
3. **WebDriver de Chrome** (automáticamente gestionado por el bot).
4. **Sistema operativo compatible:** Windows 10/11.

---

## 📄 Instalación y Configuración
1. **Descargar repositorio**

3. **Instalar las dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Crear el perfil de Chrome**
   - Abre Chrome y crea un nuevo perfil.
   - Inicia sesión en TikTok al menos una vez con tu cuenta principal.

5. **Configurar el archivo `config.py`**
   - Abre el archivo `config.py` y configura el nombre del perfil de Chrome y otros parámetros según tus necesidades.

6. **Crear archivos de usuarios en la carpeta `USERS` (puedes hacerlo con `config.py`)**
   - Crea un archivo de texto con el nombre del contacto objetivo, por ejemplo, `STILO.txt`.
   - Dentro del archivo, escribe el nombre exacto del usuario en TikTok (por ejemplo, `Stilo`).

---

## 💡 Uso
1. **Ejecutar el bot**
   - Abre `start.bat`
3. Selecciona el usuario objetivo desde el menú.
4. El bot enviará automáticamente un mensaje a la hora programada.

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
### 1.0.0 (4/1/2025)
- Primera versión ALPHA.
- Funcionalidad básica implementada:
  - Automatización de mensajes diarios.
  - Soporte para múltiples usuarios.
  - Configuración inicial de perfiles de Chrome.

---

## 🔗 Recursos
- [Documentación oficial de Selenium](https://www.selenium.dev/documentation)
- [Versiones oficiales de Melina STB](https://www.github.com/thiagostilo2121/Melina-Streak-TikTok-Bot/releases)

---

## 🌟 Créditos
Creado con pasión por Thiago Valentín Stilo Limarino. Las pruebas del programa fueron llevadas a cabo por el autor y una persona más.
