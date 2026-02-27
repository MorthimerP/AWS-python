# ============================== 🧬🚀 SECCIÓN 1: DEFINIR SECUENCIAS DE INSULINA (TEXTO) 🚀🧬 ==============================
# 🧬📌 Voy a guardar las secuencias de insulina como texto (strings).
# 🔤🧫 Cada letra representa un aminoácido.
# 🧪🧍‍♂️ Guardo la secuencia completa de la preproinsulina humana en una variable.
# 🧠🔬 La preproinsulina es la forma inicial de la insulina que produce el cuerpo humano. Luego se procesa para formar la insulina activa.
# 🧾🧬 La secuencia de la preproinsulina humana es una cadena de letras (aminoácidos). Cada letra corresponde a un aminoácido específico.
# 🩸⚙️ Esta secuencia es importante porque contiene la “receta” para producir insulina, hormona clave para regular la glucosa en la sangre.
# 🧪🔎 También se usa en investigación y en procesos donde se produce insulina sintética.
preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"


# ============================== 🧩🧬 SECCIÓN 2: SEPARAR LAS PARTES DE LA INSULINA 🧬🧩 ==============================
# 🧩🧬 Guardo las partes principales de la insulina en variables separadas.
# 🧠🔍 La insulina se compone de varias partes: cadena A, cadena B y cadena C.
# ✅🧬 La cadena A y la cadena B son las partes “activas” que forman la insulina final.
# ✂️🧬 La cadena C es un tramo intermedio que se elimina durante el procesamiento.
# ✅🧾 Al guardar cada parte en su propia variable, es más fácil trabajar con ellas (por ejemplo, para cálculos posteriores).
lsInsulin = "malwmrllpllallalwgpdpaaa"
bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"
aInsulin = "giveqcctsicslyqlenycn"
cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"


# ============================== 🔗🧬 SECCIÓN 3: CONSTRUIR LA INSULINA ACTIVA (B + A) 🧬🔗 ==============================
# 🔗🧬 Junto la cadena B y la cadena A para formar la insulina final.
# 🧪⚗️ La insulina activa se forma cuando se elimina la cadena C y quedan unidas las cadenas B y A.
# ➕🔤 Para obtener la secuencia activa, uno la cadena B con la cadena A usando el operador +.
# 🔡✅ Además uso .lower() para dejar todo en minúsculas y evitar diferencias por mayúsculas/minúsculas.
# 🧾✅ El resultado se guarda en la variable insulin, que se usará más adelante para calcular la carga neta.
insulin = (bInsulin + aInsulin).lower()


# ============================== 🗂️📊 SECCIÓN 4: CREAR TABLA DE VALORES pKR (DICCIONARIO) 📊🗂️ ==============================
# 🗂️📊 Aquí creo un diccionario (como una “tablita”) con valores pKR.
# 💡🔤 La idea es: cada letra (aminoácido) tiene un número asociado.
# ⚖️🧪 El pKR indica en qué pH ese aminoácido cambia su carga (mitad cargado / mitad sin carga).
# 📌🧮 Esto sirve para calcular la carga neta de la insulina en diferentes valores de pH.
# 🧾🧪 Ejemplo: 'y' tiene pKR 10.07, así que cerca de ese pH su carga cambia de forma importante.
# 🧬🩺 Estos valores ayudan a entender cómo se comporta la insulina en ambientes más ácidos o más básicos.
pKR = {'y':10.07,'c': 8.18,'k':10.53,'h':6.00,'r':12.48,'d':3.65,'e':4.25}


# ============================== 🔎🔤 SECCIÓN 5: CONTAR AMINOÁCIDOS IMPORTANTES EN LA INSULINA 🔤🔎 ==============================
# 🔎🔤 Aquí cuento cuántas veces aparecen y, c, k, h, r, d, e dentro de la insulina.
# 🧾📌 Lo guardo en un diccionario llamado seqCount.
# 🧮🔁 La función count() cuenta cuántas veces aparece una letra dentro del texto.
# 🧬📊 El resultado queda así: cada letra es una “clave” y su valor es la cantidad de veces que aparece en la secuencia.
# ⚡🧠 Esto es importante porque cada aminoácido aporta carga positiva o negativa dependiendo del pH.
seqCount = ({x: float(insulin.count(x)) for x in ['y','c','k','h','r','d','e']})


# ============================== 🧪📈 SECCIÓN 6: PROBAR pH DE 0 A 14 (BARRIDO DE ACIDEZ) 📈🧪 ==============================
# 🧪📈 Voy a probar distintos valores de pH desde 0 hasta 14 y calcular la carga neta.
# 🌡️⚗️ El pH mide qué tan ácida o qué tan básica es una solución.
# 🧾📉 pH 0 = muy ácido, pH 14 = muy básico.
# 👀🔍 Esto me permite observar cómo cambia la carga de la insulina en diferentes condiciones.
pH = 0


# ============================== 🔁⚡ SECCIÓN 7: CALCULAR CARGA NETA PARA CADA pH ⚡🔁 ==============================
# 🔁🧪 El ciclo while se ejecutará mientras el valor de pH sea menor o igual a 14.
# 🧮⚡ En cada vuelta se calcula la carga neta usando una fórmula basada en:
# 1) cuántas veces aparece cada aminoácido (seqCount)
# 2) su valor pKR (pKR)
# 3) el pH actual
# 🖨️📊 Después se imprime el pH (con dos decimales) y la carga neta calculada.
# ➕🔄 Al final se aumenta pH en 1 para probar el siguiente valor.
while (pH <= 14):

    # ============================== 🧾🧮 SECCIÓN 8: FÓRMULA DE CARGA NETA (POSITIVOS - NEGATIVOS) 🧮🧾 ==============================
    # 🧾🧮 Esta es la fórmula que nos dieron para calcular la carga neta.
    # 🔁📌 Está dentro del while porque se recalcula para cada pH.
    #
    # ➕✅ Parte positiva: aminoácidos que aportan carga positiva (k, h, r)
    # ➖✅ Parte negativa: aminoácidos que aportan carga negativa (y, c, d, e)
    #
    # 📊🧠 Cada término usa el conteo (seqCount), el pKR del aminoácido y el pH actual.
    # 🎯✅ El resultado final es la carga neta estimada de la insulina a ese pH.
    netCharge = (
        # ➕🧮 Sumamos contribuciones positivas (k, h, r)
        (sum({x: ((seqCount[x]*(10**pKR[x]))/((10**pH)+(10**pKR[x])))
        for x in ['k','h','r']}.values()))
        # ➖🧮 Restamos contribuciones negativas (y, c, d, e)
        - (sum({x: ((seqCount[x]*(10**pH))/((10**pH)+(10**pKR[x])))
        for x in ['y','c','d','e']}.values()))
    )

    # ============================== 🖨️📌 SECCIÓN 9: MOSTRAR RESULTADOS EN PANTALLA 📌🖨️ ==============================
    # 🖨️📌 Imprimo el pH con 2 decimales y luego la carga neta calculada.
    # 🧾🔢 format() deja el pH con dos decimales (por ejemplo: 7.00).
    # 📊👀 Así puedo ver cómo cambia la carga neta conforme cambia el pH.
    print('{0:.2f}'.format(pH), netCharge)

    # ============================== ➕🔁 SECCIÓN 10: AUMENTAR EL pH Y REPETIR 🔁➕ ==============================
    # ➕🔁 Aumento el pH en 1 para la siguiente vuelta del ciclo.
    # 📈✅ Esto permite recorrer todo el rango desde 0 hasta 14.
    pH += 1