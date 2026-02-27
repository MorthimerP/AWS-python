# ============================== 🧠🖥️ SECCIÓN 1: INTRODUCCIÓN AL USO DE COMANDOS DEL SISTEMA 🖥️🧠 ==============================
# 🧠🖥️ Este programa muestra cómo ejecutar comandos del sistema operativo desde Python.
# 🧩📦 Utiliza dos módulos importantes:
# 🔹 os → para ejecutar comandos simples.
# 🔹 subprocess → para ejecutar comandos externos de forma más controlada y profesional.
#
# 📌📂 El programa ejecuta comandos como:
# ✅ Listar archivos del directorio actual.
# ✅ Mostrar información del sistema.
# ✅ Mostrar procesos activos.
#
# 🤖📈 Esto es útil para automatizar tareas del sistema usando Python.


# ============================== 📦🧩 SECCIÓN 2: IMPORTAR LOS MÓDULOS NECESARIOS 🧩📦 ==============================
# 🧩🗂️ El módulo os permite interactuar con el sistema operativo.
# 📁 Por ejemplo: ejecutar comandos simples, navegar carpetas, etc.
import os

# 🚀🧾 El módulo subprocess es más potente y flexible que os.system().
# 🔍 Permite:
# ✅ Pasar argumentos como lista
# ✅ Manejar mejor la ejecución
# ✅ Controlar errores
import subprocess


# ============================== 📂🖨️ SECCIÓN 3: EJECUTAR UN COMANDO SIMPLE CON os.system() 🖨️📂 ==============================
# 📂🖨️ Ejecutamos el comando "ls".
# 🧾 Este comando lista los archivos del directorio actual.
# ⚠️ La salida se muestra directamente en la consola, pero no se puede manipular fácilmente desde Python.
os.system("ls")


# ============================== 📂🔎 SECCIÓN 4: EJECUTAR COMANDOS CON ARGUMENTOS USANDO subprocess 🔎📂 ==============================
# 📂🔎 Ejecutamos "ls -l".
# 📄 Muestra información detallada de cada archivo:
# permisos, propietario, tamaño y fecha.
# 🧠 Es mejor usar una lista ["ls", "-l"] en lugar de una sola cadena.
subprocess.run(["ls", "-l"])

# 📄🔍 Ejecutamos "ls -l README.md".
# 📌 Sirve para verificar si el archivo README.md existe.
# 👀 Si existe, muestra sus detalles.
subprocess.run(["ls","-l","README.md"])


# ============================== 🧠🧰 SECCIÓN 5: USAR VARIABLES PARA LOS COMANDOS 🧰🧠 ==============================
# 🧠 Guardar comandos en variables hace el código más organizado.
# ♻️ Permite cambiar el comando fácilmente sin modificar muchas líneas.
# 📌 Mejora la claridad y reutilización.

# 📂 Primero asignamos el comando "ls".
command = "ls"

# ⚠️ Aquí sobrescribimos la variable.
# Ahora command deja de ser "ls" y pasa a ser "uname".
command = "uname"

# 🧾 "-a" es un argumento que muestra información completa del sistema.
# Incluye kernel, versión, arquitectura, etc.
commandArgument = "-a"

# 🖨️ Mostramos un mensaje antes de ejecutar el comando.
print(f'Gathering system information with command: {command} {commandArgument}')

# 🚀 Ejecutamos el comando "uname -a".
subprocess.run([command, commandArgument])


# ============================== 🧾📋 SECCIÓN 6: OBTENER INFORMACIÓN DE PROCESOS ACTIVOS 📋🧾 ==============================
# 🧾🔍 Ahora vamos a ejecutar otro comando del sistema.
# "ps" muestra los procesos que están ejecutándose.
command = "ps"

# ⚙️ "-x" muestra procesos aunque no estén asociados a una terminal.
commandArgument = "-x"

# 🖨️ Mostramos un mensaje informativo antes de ejecutar el comando.
print(f'Gathering active process information with command: {command} {commandArgument}')

# 🚀 Ejecutamos "ps -x".
# 📋 Mostrará en pantalla la lista de procesos activos.
subprocess.run([command, commandArgument])