1. Abrir la carpeta en la terminal:
Debes abrir la terminal o línea de comandos dentro de la carpeta del proyecto.
Windows (Explorador de archivos): Navega a la carpeta, mantén presionada la tecla Shift y haz clic derecho en la carpeta. Selecciona "Abrir ventana de PowerShell aquí" o "Abrir ventana de comandos aquí".
macOS/Linux (Finder/Explorador de archivos): Abre la terminal y usa el comando cd para navegar a la carpeta. Por ejemplo: cd /Users/tu_usuario/Escritorio/mi_proyecto_flask.
2. Crear el entorno virtual (una sola vez por proyecto):
En la terminal, dentro de la carpeta del proyecto, ejecuta el siguiente comando:
Bash
python -m venv .venv
o
si tienes varias versiones de Python y quieres usar una específica (ej. Python 3):
Bash
python3 -m venv .venv
Este comando crea una carpeta llamada .venv (puedes nombrarla como quieras, pero .venv es la convención) que contiene el entorno virtual.
3. Activar el entorno virtual (cada vez que abras una nueva terminal):
Cada vez que abras una nueva ventana de terminal y quieras trabajar en este proyecto, necesitas activar el entorno virtual.
Windows (cmd.exe - Símbolo del sistema):

Bash
.venv\Scripts\activate
Windows (PowerShell):

PowerShell
.venv\Scripts\Activate.ps1

macOS/Linux (bash, zsh, etc.):
Bash
source .venv/bin/activate

Después de activar el entorno, verás el nombre del entorno entre paréntesis o corchetes al principio de la línea de comandos (ej. (.venv) C:\ruta\al\proyecto>).
4. Instalar Flask (dentro del entorno virtual activado):
Una vez que el entorno virtual está activado, ejecuta el siguiente comando para instalar Flask:
Bash
pip install Flask
o
para una instalación más precisa, usando el módulo pip asociado a tu Python actual:
Bash
python -m pip install Flask

Resumen rápido:
python -m venv .venv (crear entorno virtual)

.venv\Scripts\activate (Windows cmd) o .venv\Scripts\Activate.ps1 (Windows PowerShell) o source .venv/bin/activate (macOS/Linux) (activar entorno virtual)

pip install Flask o python -m pip install Flask (instalar Flask)
