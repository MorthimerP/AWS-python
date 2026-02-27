# ============================== 📚📦 SECCIÓN 1: IMPORTACIÓN DE LIBRERÍAS 📦📚 ==============================
# 📄➗ La librería csv nos permite trabajar con archivos donde los datos están separados por comas (,).
# 🧠📌 En este caso, se va a trabajar con un archivo llamado car_fleet.csv que contiene información de una flota de vehículos.
# ✅ csv facilita leer y recorrer la información fila por fila, como si fuera una tabla.
import csv

# 🧬📋 La librería copy nos permite copiar estructuras de datos (como diccionarios) sin “mezclar” la información.
# 🧠📌 Usaremos deepcopy para crear copias independientes del diccionario myVehicle.
# ✅ Esto evita que al modificar un vehículo se cambien los demás por accidente.
import copy


# ============================== 🚗🧾 SECCIÓN 2: CREAR UNA “PLANTILLA” DE VEHÍCULO (DICCIONARIO) 🧾🚗 ==============================
# 🚗🧾 Se crea el diccionario myVehicle
# 🧠📌 Este diccionario funciona como una plantilla para describir un vehículo.
# ✅ Tiene “claves” (como vin, make, model...) y valores iniciales vacíos o en cero.
# 📌 Luego, al leer el archivo CSV, se llenarán estos espacios con datos reales.
myVehicle = {
    # 🆔 "vin": "<empty>" - Identificador único del vehículo (Vehicle Identification Number).
    "vin": "<empty>",
    # 🏷️ "make": "<empty>" - Marca del vehículo.
    "make": "<empty>",
    # 🚘 "model": "<empty>" - Modelo del vehículo.
    "model": "<empty>",
    # 🗓️ "year": 0 - Año del vehículo.
    "year": 0,
    # 🛣️ "range": 0 - Autonomía (cuánto puede recorrer).
    "range": 0,
    # 🏎️ "topSpeed": 0 - Velocidad máxima.
    "topSpeed": 0,
    # ⏱️ "zeroSixty": 0.0 - Tiempo de 0 a 60 (aceleración).
    "zeroSixty": 0.0,
    # 🧮 "mileage": 0 - Kilometraje.
    "mileage": 0
}


# ============================== 🖨️🔎 SECCIÓN 3: MOSTRAR LA PLANTILLA EN PANTALLA 🔎🖨️ ==============================
# 🔁🖨️ Se crea un ciclo for para imprimir cada clave:valor que hay dentro del diccionario
# 🧠📌 Esto sirve para ver qué campos tiene el vehículo y sus valores iniciales.
for key, value in myVehicle.items():
    # 🖨️🔑 Se imprime la clave : valor
    print("{} : {}".format(key, value))


# ============================== 📦🚗 SECCIÓN 4: CREAR EL INVENTARIO (LISTA DE VEHÍCULOS) 🚗📦 ==============================
# 📦🚗 Se crea la lista myInventoryList
# 🧠📌 Aquí vamos a guardar TODOS los vehículos leídos desde el CSV.
# ✅ Cada vehículo será un diccionario independiente dentro de esta lista.
myInventoryList = []


# ============================== 📂📖 SECCIÓN 5: ABRIR Y LEER EL ARCHIVO CSV 📖📂 ==============================
# 📂📖 Se abre el archivo car_fleet.csv y se guarda dentro de la variable csvFile
# 🧠📌 Abrimos el archivo para poder leer sus filas.
with open('car_fleet.csv') as csvFile:
    # 📑🔍 Se crea un lector de CSV donde el separador es la coma.
    csvReader = csv.reader(csvFile, delimiter=',')

    # 🔢🧾 Se crea la variable lineCount para contar cuántas líneas se procesan.
    lineCount = 0

    # ============================== 🔁📄 SECCIÓN 6: RECORRER FILA POR FILA EL CSV 📄🔁 ==============================
    # 🔁📄 Este ciclo for lee cada fila (row) del archivo.
    for row in csvReader:

        # ============================== 🏷️📌 SECCIÓN 7: LEER LA PRIMERA FILA (NOMBRES DE COLUMNAS) 📌🏷️ ==============================
        # 🧾🔎 Si lineCount es 0, significa que estamos en la primera fila.
        # 🧠📌 Normalmente esa fila trae los títulos de las columnas.
        if lineCount == 0:
            # 🖨️🧾 Se imprime el nombre de las columnas.
            print(f'Column names are: {", ".join(row)}')

            # ➕🔢 Aumentamos el conteo para pasar a las filas con datos reales.
            lineCount += 1

        # ============================== 🚗📄 SECCIÓN 8: LEER LAS FILAS CON DATOS DE VEHÍCULOS 📄🚗 ==============================
        # 🚗📄 Si NO es la primera línea, entonces aquí vienen los datos de cada vehículo.
        else:
            # 🖨️🚘 Imprimimos los datos de la fila actual para ver qué estamos leyendo.
            print(
                f'vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, '
                f'range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}'
            )

            # ============================== 🧬🧾 SECCIÓN 9: CREAR UN VEHÍCULO NUEVO A PARTIR DE LA PLANTILLA 🧾🧬 ==============================
            # 🧠📌 Hacemos una copia COMPLETA de la plantilla para que sea un vehículo independiente.
            currentVehicle = copy.deepcopy(myVehicle)

            # 🧾📌 Llenamos el diccionario con los datos de la fila (row).
            currentVehicle["vin"] = row[0]
            currentVehicle["make"] = row[1]
            currentVehicle["model"] = row[2]
            currentVehicle["year"] = row[3]
            currentVehicle["range"] = row[4]
            currentVehicle["topSpeed"] = row[5]
            currentVehicle["zeroSixty"] = row[6]
            currentVehicle["mileage"] = row[7]

            # ============================== ➕📦 SECCIÓN 10: GUARDAR EL VEHÍCULO EN LA LISTA (INVENTARIO) 📦➕ ==============================
            # 🚗➕ Agregamos este vehículo a la lista de inventario.
            myInventoryList.append(currentVehicle)

            # ➕🔢 Contamos esta línea como procesada.
            lineCount += 1

    # ============================== ✅📊 SECCIÓN 11: RESUMEN DE PROCESO (TOTAL DE LÍNEAS) 📊✅ ==============================
    # 🧾✅ Se imprime el total de líneas procesadas.
    print(f'Processed {lineCount} lines.')


# ============================== 🖨️🚗 SECCIÓN 12: IMPRIMIR EL INVENTARIO COMPLETO 🚗🖨️ ==============================
# 🔁🚗 Se crea un for para imprimir cada vehículo de la lista
# 🧠📌 Aquí recorremos la lista y mostramos las propiedades guardadas de cada vehículo.
for myCarProperties in myInventoryList:

    # 🖨️📣 Mensaje para organizar la salida en pantalla
    print("Printing each car's properties:")

    # 🔁📌 Recorremos cada clave y valor dentro del diccionario del vehículo actual
    for key, value in myCarProperties.items():
        # 🖨️🔑 Se imprime la llave : valor
        print("{} : {}".format(key, value))

    # ➖➖➖ Separador para distinguir un vehículo del siguiente
    print("-----")