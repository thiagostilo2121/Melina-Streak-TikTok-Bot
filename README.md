# Melina Streak TikTok Bot

![Logo del Proyecto](main/icon.ico)

**Creado por:** Thiago Valentín Stilo Limarino  
**Fecha de Creación:** 2/1/2025  
**Fecha de lanzamiento:** 11/1/2025   
**Versión Actual:** 1.0.0 (ALPHA)   
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

---

## ⚡ Requisitos
1. **Python 3.10+**
2. **Google Chrome instalado.**
3. **WebDriver de Chrome** (automáticamente gestionado por el bot).
4. **Sistema operativo compatible:** Windows 10/11.

---

## 📄 Instalación y Configuración
1. **Descargar repositorio**

3. **Instalar las dependencias (instrucciones en el archivo [INSTRUCCIONES.txt](INSTRUCCIONES.txt))**
   ```bash
   pip install -r main/ins.files/requirements.txt
   ```
   o abra `install.py`

4. **Crear el perfil de Chrome**
   - Abre Chrome y crea un nuevo perfil o usa uno existente.
   - Inicia sesión en TikTok al menos una vez con tu cuenta principal.

5. **Configurar el archivo `Config`**
   - Abre el archivo `Config` y configura el nombre del perfil de Chrome y otros parámetros según tus necesidades.

6. **Crear archivos de usuarios en la carpeta `main/src/USERS` (puedes hacerlo con `Config`)**
   - Crea un archivo de texto con el nombre del contacto objetivo, por ejemplo, `STILO.txt`.
   - Dentro del archivo, escribe el nombre exacto del usuario en TikTok (por ejemplo, `Stilo`).

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
### 1.0.0 ALPHA (11/1/2025)
- Lanzamiento
- Primera versión ALPHA.

---

## 🔗 Recursos
- [Documentación oficial de Selenium](https://www.selenium.dev/documentation)
- [Versiones oficiales de Melina STB](https://www.github.com/thiagostilo2121/Melina-Streak-TikTok-Bot/releases)

---

## ⚠️ Advertencia
Este programa se encuentra en su versión ALPHA, por lo tanto, se encuentra sujeto a constantes cambios. También contiene errores o bugs que serán solucionados en cada actualización.

Le pido disculpas por el largo y tedioso proceso de instalación y configuración manual del programa (cual se especifica en [INSTRUCCIONES.txt](INSTRUCCIONES.txt)) que es debido a que: 1. Deseo procurar la seguridad del usuario para que no crea que su cuenta de TikTok es vulnerada 2. El programa NO puede iniciar sesión en cuentas de TikTok debido a la verificación solicitada por la plataforma. A pesar de esto, trataré de mejorar el proceso de instalación y configuración en el futuro.

---

## 🌟 Créditos
Creado con pasión por Thiago Valentín Stilo Limarino. Las pruebas del programa fueron llevadas a cabo por el autor y una persona más.
