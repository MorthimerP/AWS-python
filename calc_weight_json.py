# ============================== 📦📥 SECCIÓN 1: IMPORTAR EL MÓDULO QUE LEE ARCHIVOS JSON 📥📦 ==============================
# 📦📥 Importo el módulo que creé para leer archivos JSON
# 🧠🗂️ El módulo jsonFileHandler es un archivo Python que contiene funciones para manejar archivos JSON,
# como leer y escribir datos en formato JSON. Al importarlo, puedo usar esas funciones aquí.
import jsonFileHandler

# ============================== 📄🔎 SECCIÓN 2: LEER EL ARCHIVO JSON CON LOS DATOS 🔎📄 ==============================
# 📄🔎 Llamo a la función para leer el archivo JSON
# 📍🗺️ Le paso la ruta donde está guardado
# 🧠📥 La función readJsonFile() abre el archivo 'files/insulin.json', lee su contenido
# y lo convierte en un formato que Python puede manejar (por ejemplo, un diccionario).
# El resultado queda guardado en la variable data para usarlo más adelante.
data = jsonFileHandler.readJsonFile('files/insulin.json')

# ============================== ✅🧪 SECCIÓN 3: CONFIRMAR QUE LA LECTURA SALIÓ BIEN ✅🧪 ==============================
# ✅🧪 Verifico que el archivo sí se haya leído correctamente
# 🧠📌 Si data NO está vacío (no es ""), asumimos que la lectura funcionó.
# 🚫 Si data está vacío, mostramos un error y no seguimos, para evitar fallos después.
if data != "":
    # ============================== 🧬🧩 SECCIÓN 4: SACAR DATOS IMPORTANTES DEL JSON 🧩🧬 ==============================
    # 🧬🅱️ Extraigo la cadena B desde el JSON
    # 🧠📌 La cadena B está guardada dentro de data['molecules']['bInsulin'].
    # ✅ La guardamos en bInsulin para usarla después.
    bInsulin = data['molecules']['bInsulin']

    # 🧬🅰️ Extraigo la cadena A desde el JSON
    # 🧠📌 La cadena A está guardada dentro de data['molecules']['aInsulin'].
    # ✅ La guardamos en aInsulin para usarla después.
    aInsulin = data['molecules']['aInsulin']

    # 🔗🧬 Uno ambas cadenas para formar la insulina completa
    # 🧠📌 La insulina completa se forma uniendo la cadena B y la cadena A.
    # ✅ El símbolo + “pega” textos, por eso funciona para unir secuencias.
    insulin = bInsulin + aInsulin

    # ============================== ⚖️📌 SECCIÓN 5: TOMAR EL VALOR REAL DEL PESO MOLECULAR 📌⚖️ ==============================
    # ⚖️🧾 Extraigo el peso molecular real desde el JSON
    # 🧠📌 Este valor ya está calculado y guardado en el archivo JSON.
    # ✅ Lo usamos para comparar contra nuestro cálculo aproximado.
    molecularWeightInsulinActual = data['molecularWeightInsulinActual']

    # ============================== 🖨️📊 SECCIÓN 6: MOSTRAR LO QUE LEÍMOS (CONFIRMACIÓN VISUAL) 📊🖨️ ==============================
    # 🖨️📊 Imprimo los datos obtenidos
    # 🧠✅ Esto sirve para confirmar que el programa sí encontró las cadenas y el peso real.
    print('bInsulin: ' + bInsulin)
    print('aInsulin: ' + aInsulin)
    print('molecularWeightInsulinActual: ' + str(molecularWeightInsulinActual))

    # ============================== 🧾⚙️ SECCIÓN 7: OBTENER LOS PESOS DE CADA AMINOÁCIDO ⚙️🧾 ==============================
    # 🧾⚙️ Obtengo el diccionario de pesos de aminoácidos
    # 🧠📌 Dentro del JSON existe una “tabla” llamada weights.
    # ✅ Allí cada letra (aminoácido) tiene su peso molecular asociado.
    aaWeights = data['weights']

    # ============================== 🔢🧬 SECCIÓN 8: CONTAR CUÁNTAS VECES APARECE CADA AMINOÁCIDO 🧬🔢 ==============================
    # 🔢🧬 Cuento la cantidad de cada aminoácido en la secuencia de insulina
    # 🧠📌 Para estimar el peso total, primero necesitamos saber cuántas veces aparece cada letra.
    # ✅ upper() pone todo en mayúsculas para contar de forma consistente.
    aaCountInsulin = ({
        # 🔁🧬 Para cada aminoácido (x), contamos cuántas veces aparece en la secuencia.
        # 🧠🔢 count(x) cuenta cuántas veces aparece la letra x.
        x: float(insulin.upper().count(x))
        for x in ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L','M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']
    })

    # ============================== ✖️➕ SECCIÓN 9: CALCULAR EL PESO MOLECULAR APROXIMADO ➕✖️ ==============================
    # ✖️⚖️ Multiplico la cantidad de cada aminoácido por su peso
    # ➕🧮 Luego sumo todos los resultados
    # 🧠📌 Para cada aminoácido:
    # 1) Tomamos su cantidad (aaCountInsulin[x])
    # 2) La multiplicamos por su peso (aaWeights[x])
    # 3) Sumamos todo para obtener un peso total aproximado
    molecularWeightInsulin = sum({
        x: (aaCountInsulin[x] * aaWeights[x])
        for x in ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L','M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']
    }.values())

    # ============================== 🖨️⚖️ SECCIÓN 10: MOSTRAR EL PESO CALCULADO ⚖️🖨️ ==============================
    # 🖨️⚖️ Muestro el peso calculado
    # 🧠📌 Mostramos en pantalla el peso aproximado para poder compararlo con el real.
    print("The rough molecular weight of insulin: " + str(molecularWeightInsulin))

    # ============================== 🧮📉 SECCIÓN 11: CALCULAR Y MOSTRAR EL PORCENTAJE DE ERROR 📉🧮 ==============================
    # 🧮📉 Calculo el porcentaje de error
    # 🧾📌 Fórmula: (calculado - real) / real * 100
    # 🧠📌 Esto nos dice qué tan lejos está nuestro cálculo del valor real.
    percentError = ((molecularWeightInsulin - molecularWeightInsulinActual) / molecularWeightInsulinActual) * 100

    # 🖨️📣 Se imprime el porcentaje de error calculado
    # 🧠📌 Si el porcentaje es pequeño, significa que la aproximación fue buena.
    print("Percent error: " + str(percentError))

# ============================== ⛔📄 SECCIÓN 12: MANEJO DE ERROR (NO SE PUDO LEER EL ARCHIVO) 📄⛔ ==============================
# ⛔📄 Si el archivo no se pudo leer, termina el programa
else:
    # ⛔🧠 Si el archivo no se pudo leer, no podemos seguir porque faltarían los datos.
    # ✅ Mostramos un mensaje claro y terminamos.
    print("Error. Exiting program")