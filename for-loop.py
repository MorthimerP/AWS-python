# ============================== 🔢🚀 SECCIÓN 1: MENSAJE DE INICIO 🚀🔢 ==============================
# 🔁🔢 Vamos a crear un ciclo for que imprime los números hasta 10.
# 📏➡️ Para lograrlo, usaremos range() para generar una lista de números.
# 🖨️💬 Primero mostraremos un mensaje en pantalla para avisar que vamos a empezar a contar.
print("Count to 10!")

# ============================== 🔁📌 SECCIÓN 2: CICLO FOR PARA CONTAR DEL 0 AL 10 📌🔁 ==============================
# 🧮📌 Creamos una variable llamada x que irá tomando valores desde 0 hasta 10.
# 📏➡️ range(0, 11) significa:
# ✅ Empieza en 0
# ✅ Termina en 11, pero OJO: el 11 NO se incluye
# 🎯 Por eso, el último número que veremos será 10.
# 🔁📍 El ciclo for repite el bloque de abajo una vez por cada número del rango.
# ⏱️🔟 En total, se repite 11 veces: 0, 1, 2, ..., 10
for x in range(0, 11):
    # ============================== 🖨️🔢 SECCIÓN 3: IMPRIMIR EL NÚMERO ACTUAL 🔢🖨️ ==============================
    # 🖨️🔢 En cada vuelta del ciclo, se imprime el número actual guardado en x.
    # 🔄➕ En la siguiente vuelta, x cambia automáticamente al siguiente número del rango.
    print(x)