# ============================== 📋🍎 SECCIÓN 1: CREACIÓN DE UNA LISTA 🍎📋 ==============================
# 🧾✅ Para crear una lista se usan corchetes []
# 🍎🍌🍒 Creamos la lista myFruitList y dentro de ella guardamos las frutas "apple", "banana" y "cherry"
# 🧠📌 Una lista es una estructura que permite guardar varios valores en una sola variable.
# ✅ Cada elemento se separa con comas.
# 📦 En este caso, guardamos nombres de frutas en formato texto (string).
myFruitList = ["apple", "banana", "cherry"]

# ============================== 🖨️📋 SECCIÓN 2: IMPRIMIR LA LISTA COMPLETA 📋🖨️ ==============================
# 🧠📌 print() muestra en pantalla todo el contenido de la lista.
# 👀 Esto nos permite verificar que la lista fue creada correctamente.
print(myFruitList)

# ============================== 🔎🧠 SECCIÓN 3: VERIFICAR EL TIPO DE DATO 🔎🧠 ==============================
# 🧾📌 type() nos dice qué tipo de dato es la variable.
# ✅ Aquí confirmamos que myFruitList es una lista (list).
print(type(myFruitList))

# ============================== 🔢🍎 SECCIÓN 4: ACCEDER A ELEMENTOS POR POSICIÓN 🔢🍎 ==============================
# 🧠📌 En Python las posiciones comienzan desde 0.
# 0 = primer elemento, 1 = segundo elemento, 2 = tercer elemento.

# 1️⃣🍎 Primer elemento
print(myFruitList[0])

# 2️⃣🍌 Segundo elemento
print(myFruitList[1])

# 3️⃣🍒 Tercer elemento
print(myFruitList[2])

# ============================== 🔁✏️ SECCIÓN 5: MODIFICAR UN ELEMENTO DE LA LISTA ✏️🔁 ==============================
# 🧠📌 Las listas son mutables, eso significa que se pueden modificar después de crearlas.
# 🔄 Cambiamos el valor de la posición 2 (antes era "cherry") por "orange".
myFruitList[2] = "orange"

# 🖨️📋 Imprimimos nuevamente la lista para verificar el cambio
print(myFruitList)

# ============================== 📦🍍 SECCIÓN 6: CREACIÓN DE UNA TUPLA 🍍📦 ==============================
# 🧾✅ Para crear una tupla se usan paréntesis ()
# 🧠📌 Una tupla es parecida a una lista, pero NO se puede modificar después de crearla.
# 🔒 Esto la hace inmutable (más segura si no queremos cambios).
myFinalAnswerTuple = ("apple", "banana", "pineapple")

# 🖨️ Mostramos la tupla completa
print(myFinalAnswerTuple)

# 🔎 Verificamos el tipo de dato
print(type(myFinalAnswerTuple))

# ============================== 🔢🍎 SECCIÓN 7: ACCEDER A VALORES DE LA TUPLA 🔢🍎 ==============================
# 🧠📌 Igual que en las listas, las posiciones comienzan desde 0.

# 1️⃣🍎 Primer elemento
print(myFinalAnswerTuple[0])

# 2️⃣🍌 Segundo elemento
print(myFinalAnswerTuple[1])

# 3️⃣🍍 Tercer elemento
print(myFinalAnswerTuple[2])

# ============================== 📚🍎 SECCIÓN 8: CREACIÓN DE UN DICCIONARIO 🍎📚 ==============================
# 🧾📌 Los diccionarios se crean con llaves {}
# 🧠📌 Guardan información en formato clave : valor
# 🔑 La clave sirve para identificar el dato.
# 📦 El valor es la información asociada a esa clave.
myFavoriteFruitDictionary = {
    "Akua": "apple",
    "Saanvi": "banana",
    "Paulo": "pineapple"
}

# ============================== 🖨️📚 SECCIÓN 9: IMPRIMIR EL DICCIONARIO COMPLETO 📚🖨️ ==============================
# 👀 Mostramos todos los pares clave-valor.
print(myFavoriteFruitDictionary)

# 🔎 Verificamos que sea un diccionario
print(type(myFavoriteFruitDictionary))

# ============================== 🔑🍎 SECCIÓN 10: ACCEDER A VALORES USANDO LA CLAVE 🔑🍎 ==============================
# 🧠📌 Para obtener un valor usamos: diccionario["clave"]

# 🍎 Fruta favorita de Akua
print(myFavoriteFruitDictionary["Akua"])

# 🍌 Fruta favorita de Saanvi
print(myFavoriteFruitDictionary["Saanvi"])

# 🍍 Fruta favorita de Paulo
print(myFavoriteFruitDictionary["Paulo"])