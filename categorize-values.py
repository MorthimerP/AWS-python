# ============================== 📋🧩 SECCIÓN 1: CREACIÓN DE UNA LISTA CON DATOS MEZCLADOS 🧩📋 ==============================
# 📋🧩 Se crea la lista myMixedTypeList en la cual se guardan diferentes tipos de datos
# 🧠📌 Aquí creamos una lista llamada myMixedTypeList que guarda varios valores juntos, en una sola “cajita”.
# ✅ Esta lista es especial porque mezcla diferentes tipos de datos para mostrar que Python lo permite.
# 🧾🔎 La lista myMixedTypeList contiene los siguientes elementos:
# 🔢 - 45: un número entero (int)
# 🔢 - 290578: otro número entero (int)
# 🔣 - 1.02: un número decimal (float)
# ✅ - True: un valor de verdadero/falso (bool)
# 📝 - "My dog is on the bed.": una frase (str)
# 🧾 - "45": texto que se ve como número, pero sigue siendo texto (str)
myMixedTypeList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]

# ============================== 🔁👀 SECCIÓN 2: RECORRER LA LISTA ELEMENTO POR ELEMENTO 🔁👀 ==============================
# 🔁👀 El ciclo for se encarga de mirar cada uno de los elementos de la lista
# 🧠📌 Un ciclo for sirve para repetir una acción con cada elemento de la lista, uno por uno.
# ✅ En cada vuelta del ciclo, la variable item toma el valor del siguiente elemento de la lista.
# 🔄📍 Así podemos trabajar con cada elemento sin escribir código repetido para cada uno.
for item in myMixedTypeList:
    # ============================== 🖨️🧾 SECCIÓN 3: MOSTRAR EL VALOR Y EL TIPO DE DATO 🧾🖨️ ==============================
    # 🖨️🧾 En esta impresión se va a mostrar el valor del elemento y el tipo de dato que tiene
    # 🧠📌 print() muestra un mensaje en pantalla.
    # 🔎 type(item) nos dice qué tipo de dato es (número entero, decimal, texto, etc.).
    # 🧩 format(...) coloca el valor y el tipo dentro del texto usando {} como “espacios” para rellenar.
    print("{} is of the data type {}".format(item, type(item)))