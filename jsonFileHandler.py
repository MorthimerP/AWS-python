# ============================== 📦📄 SECCIÓN 1: IMPORTAR LA LIBRERÍA JSON 📄📦 ==============================
# 📦📄 Importamos la librería json.
# 🧠📌 Esta librería nos permite trabajar con archivos en formato JSON.
# ✅ JSON es un formato muy común para guardar información estructurada.
# 🔄 Con json podemos convertir archivos JSON en estructuras de Python como diccionarios y listas.
import json


# ============================== 🧩🛠️ SECCIÓN 2: CREAR LA FUNCIÓN PARA LEER EL ARCHIVO 🛠️🧩 ==============================
# 🧩📖 Creamos una función llamada readJsonFile.
# 📌 Esta función recibe un parámetro llamado fileName (el nombre o ruta del archivo).
# 🎯 Su objetivo es intentar abrir el archivo y devolver su contenido.
# ✅ Si todo sale bien, devuelve los datos.
# ❌ Si ocurre un error, muestra un mensaje y devuelve un valor vacío.
def readJsonFile(fileName):


    # ============================== 📄🧾 SECCIÓN 3: INICIALIZAR VARIABLE DE RESULTADO 🧾📄 ==============================
    # 🧾 Creamos la variable data y la dejamos vacía.
    # 🧠📌 Si ocurre un error, esta será la que se devolverá.
    # ✅ Si el archivo se lee correctamente, aquí se guardarán los datos.
    data = ""


    # ============================== 🔍📂 SECCIÓN 4: INTENTAR ABRIR EL ARCHIVO 📂🔍 ==============================
    # 🔍 Usamos un bloque try para intentar abrir el archivo.
    # 🧠📌 Esto nos permite manejar errores sin que el programa se detenga.
    try:
        # 📂 with open(...) abre el archivo.
        # ✅ El bloque "with" garantiza que el archivo se cierre automáticamente.
        # 📌 Esto es una buena práctica para evitar problemas con archivos abiertos.
        with open(fileName) as json_file:


            # ============================== 🔄📊 SECCIÓN 5: CONVERTIR JSON A DICCIONARIO 📊🔄 ==============================
            # 🔄 json.load() lee el contenido del archivo.
            # 🧠📌 Convierte el archivo JSON en un diccionario de Python.
            # ✅ Ahora podremos trabajar con esos datos fácilmente en el programa.
            data = json.load(json_file)


    # ============================== ❌⚠️ SECCIÓN 6: MANEJO DE ERRORES ⚠️❌ ==============================
    # ❌ Si ocurre un error al abrir el archivo (por ejemplo, no existe),
    # el programa no se detiene, sino que entra aquí.
    except IOError:
        # 🖨️ Mostramos un mensaje indicando que no se pudo leer el archivo.
        # 📌 Esto ayuda a entender qué salió mal.
        print("Could not read file")


    # ============================== 🔁📤 SECCIÓN 7: DEVOLVER EL RESULTADO 📤🔁 ==============================
    # 🔁 Finalmente, devolvemos la variable data.
    # ✅ Si todo salió bien, será un diccionario con la información del JSON.
    # ❌ Si hubo un error, será una cadena vacía.
    return data