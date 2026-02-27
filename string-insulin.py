# ============================== 🧬📌 SECCIÓN 1: GUARDAR LA SECUENCIA COMPLETA (PREPROINSULINA) 📌🧬 ==============================
# 🧬📌 Guardo la secuencia completa de la preproinsulina en una variable.
# 📏🔤 Uso \ para dividir la línea porque es muy larga y así el código es más fácil de leer.
# 🧪🧍‍♂️ La preproinsulina es la forma inicial de la insulina que produce el cuerpo humano.
# 🧬 Contiene varias partes: cadena A, cadena B y cadena C.
# ✂️🧩 Durante el procesamiento biológico, la cadena C se elimina.
# 🧾 Cada letra representa un aminoácido específico dentro de la proteína.
preproInsulin = (
"malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktr" \
"reaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"
)


# ============================== 🧩🔬 SECCIÓN 2: SEPARAR LAS PARTES DE LA INSULINA 🔬🧩 ==============================
# 🧠 Guardar cada parte en variables separadas facilita el análisis.
# 🧬🅰️ Cadena A → parte activa de la insulina.
# 🧬🅱️ Cadena B → también parte activa.
# 🧬🅲 Cadena C → se elimina durante el proceso de activación.
# 🏗️ Separarlas permite hacer cálculos más específicos después.
lsInsulin = "malwmrllpllallalwgpdpaaa"
bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"
aInsulin = "giveqcctsicslyqlenycn"
cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"


# ============================== 🔗➕ SECCIÓN 3: FORMAR LA INSULINA ACTIVA (B + A) ➕🔗 ==============================
# 🔗➕ Unimos la cadena B y la cadena A.
# 🧾 El símbolo + sirve para concatenar (pegar) textos.
# ⚙️ La insulina activa se obtiene eliminando la cadena C y uniendo A + B.
# 🧬 El resultado es la secuencia funcional de la hormona.
insulin = bInsulin + aInsulin


# ============================== 🖥️📤 SECCIÓN 4: MOSTRAR SECUENCIAS EN PANTALLA 📤🖥️ ==============================
# 📢🖨️ print() se usa para mostrar información al usuario.

# 📜 Imprimo un mensaje descriptivo.
print("La secuencia de la preproinsulina humana es: ")

# 🔎 Imprimo la secuencia completa.
print(preproInsulin)

# 🧬🅰️ Imprimo solo la cadena A para verla por separado.
print("La secuencia de la insulina humana, cadena A: " + aInsulin)


# ============================== 📊⚖️ SECCIÓN 5: CREAR TABLA DE PESOS MOLECULARES ⚖️📊 ==============================
# 📊🧮 Creo un diccionario donde cada letra (aminoácido) tiene su peso molecular.
# 🗂️ Es como una tabla: letra → peso.
# ⚖️ Estos valores permiten calcular el peso total de la proteína.
aaWeights = {
    'A': 89.09, 'C': 121.16, 'D': 133.10, 'E': 147.13, 'F': 165.19,
    'G': 75.07, 'H': 155.16, 'I': 131.17, 'K': 146.19, 'L': 131.17, 'M': 149.21,
    'N': 132.12, 'P': 115.13, 'Q': 146.15, 'R': 174.20, 'S': 105.09,
    'T': 119.12, 'V': 117.15, 'W': 204.23, 'Y': 181.19
}


# ============================== 🔎🔠 SECCIÓN 6: CONTAR AMINOÁCIDOS EN LA INSULINA 🔠🔎 ==============================
# 🔎🔠 Cuento cuántas veces aparece cada aminoácido en la secuencia.
# ⬆️ upper() convierte todo a mayúsculas para que coincida con el diccionario.
# 🔁 count(x) cuenta cuántas veces aparece cada letra.
# 📦 El resultado se guarda en aaCountInsulin.
# 🧮 Esto es necesario para calcular el peso molecular total.
aaCountInsulin = ({
    x: float(insulin.upper().count(x))
    for x in ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L',
              'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']
})


# ============================== ⚖️🧬 SECCIÓN 7: CALCULAR PESO MOLECULAR APROXIMADO 🧬⚖️ ==============================
# 🔢 Multiplico la cantidad de cada aminoácido por su peso.
# ➕ Luego sumo todos los resultados con sum().
# 📊 values() obtiene solo los valores numéricos del cálculo.
# 🎯 El resultado es una estimación del peso total de la insulina.
molecularWeightInsulin = sum({
    x: (aaCountInsulin[x] * aaWeights[x])
    for x in ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L',
              'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']
}.values())


# ============================== 🖨️📊 SECCIÓN 8: MOSTRAR EL PESO CALCULADO 📊🖨️ ==============================
# 🔤 Uso str() para convertir el número a texto y poder imprimirlo junto con el mensaje.
print("El peso molecular aproximado de la insulina es: " +
      str(molecularWeightInsulin))


# ============================== 🧪📏 SECCIÓN 9: DEFINIR EL VALOR REAL EXPERIMENTAL 📏🧪 ==============================
# 🔬 Este valor fue determinado experimentalmente en laboratorio.
# 📊 Nos servirá para comparar qué tan preciso fue nuestro cálculo.
molecularWeightInsulinActual = 5807.63

# 🖨️ Muestro nuevamente el valor aproximado.
print("El peso molecular aproximado de la insulina es: " +
      str(molecularWeightInsulin))


# ============================== 📉📈 SECCIÓN 10: CALCULAR PORCENTAJE DE ERROR 📈📉 ==============================
# 🧮 Fórmula del porcentaje de error:
# ((valor_calculado - valor_real) / valor_real) * 100
# 📊 Esto indica qué tan lejos estamos del valor real.
# 🎯 Cuanto menor sea el porcentaje, más preciso fue el cálculo.
print("Porcentaje de error: " +
      str(((molecularWeightInsulin - molecularWeightInsulinActual)
           / molecularWeightInsulinActual) * 100))