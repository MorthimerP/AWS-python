# ============================== 🧮🐍 SECCIÓN 1: OPERACIONES BÁSICAS CON NÚMEROS 🐍🧮 ==============================
# 🧮🐍 Este programa muestra cómo funcionan algunos tipos de datos en Python.
# 🔢📌 En Python existen varios tipos de datos; aquí veremos:
# ✅ int  → números enteros (ej: 1, 20, -3)
# ✅ float → números con decimales (ej: 3.14, 0.5)
# ✅ complex → números complejos (ej: 5j)
# ✅ bool → valores de verdadero o falso (True / False)
#
# ➕➖✖️➗ Primero veremos operaciones matemáticas básicas y luego cómo cambia el “tipo” de una variable.
# 🖨️📣 Usaremos print() para mostrar resultados en pantalla.

# ➕✅ Suma: 2 + 2
print(2+2)

# ➖✅ Resta: 4 - 2
print(4-2)

# ✖️✅ Multiplicación: 2 * 2
print(2*2)

# ➗✅ División: 4 / 2
print(4/2)


# ============================== 🖨️📝 SECCIÓN 2: MENSAJE INFORMATIVO EN PANTALLA 📝🖨️ ==============================
# 🖨️📝 Imprimimos un texto plano.
# 📌🔢 Este mensaje solo sirve para avisar de qué trata el ejemplo.
print("Python has three numeric types: int, float, and complex")


# ============================== 🧱🔢 SECCIÓN 3: VARIABLE CON UN NÚMERO ENTERO (INT) 🔢🧱 ==============================
# 🧱🔢 Creamos una variable llamada myValue y guardamos el número 1.
# 🧠📌 Una variable es como una “cajita” donde guardamos un valor para usarlo después.
myValue = 1

# 🖨️🔎 Imprimimos el valor guardado en myValue.
print(myValue)

# 🧬🔍 Para saber el tipo de dato de una variable usamos type().
# 📌🧠 En este caso, debería decir que es un entero: int.
print(type(myValue))

# 🔤🧾 str() convierte un valor a texto para poder unirlo en un mensaje.
# 📌🧠 Así imprimimos un mensaje más explicativo (valor + tipo).
print(str(myValue) + " is of the data type " + str(type(myValue)))


# ============================== 🔄💧 SECCIÓN 4: CAMBIAR A NÚMERO DECIMAL (FLOAT) 💧🔄 ==============================
# 🔄🧠 En Python una misma variable puede cambiar de valor (y hasta de tipo).
# 📌🧪 Ahora myValue guardará 3.14, que es un número decimal (float).
myValue = 3.14

# 🖨️🔎 Imprimimos el nuevo valor de myValue.
print(myValue)

# 🧬🔍 Verificamos el tipo: ahora debería ser float.
print(type(myValue))

# 🔤🧾 Convertimos a texto para imprimir un mensaje completo.
print(str(myValue) + " is of the data type " + str(type(myValue)))


# ============================== 🌀➕ SECCIÓN 5: CAMBIAR A NÚMERO COMPLEJO (COMPLEX) ➕🌀 ==============================
# 🔄🧠 Ahora myValue guardará 5j.
# 📌🧿 Ese “j” indica que es un número complejo (se usa en matemáticas avanzadas).
myValue = 5j

# 🖨️🔎 Imprimimos el valor actual.
print(myValue)

# 🧬🔍 Verificamos el tipo: debería ser complex.
print(type(myValue))

# 🔤🧾 Imprimimos valor + tipo en un solo mensaje.
print(str(myValue) + " is of the data type " + str(type(myValue)))


# ============================== ✅❌ SECCIÓN 6: CAMBIAR A VERDADERO (BOOL) ❌✅ ==============================
# 🔄🧠 Ahora myValue guardará True.
# 📌✅ True significa “verdadero” y es un tipo de dato booleano (bool).
myValue = True

# 🖨️🔎 Imprimimos el valor actual.
print(myValue)

# 🧬🔍 Verificamos el tipo: debería ser bool.
print(type(myValue))

# 🔤🧾 Imprimimos valor + tipo en un solo mensaje.
print(str(myValue) + " is of the data type " + str(type(myValue)))


# ============================== ❌✅ SECCIÓN 7: CAMBIAR A FALSO (BOOL) ✅❌ ==============================
# 🔄🧠 Ahora myValue guardará False.
# 📌❎ False significa “falso” y también es un booleano (bool).
myValue = False

# 🖨️🔎 Imprimimos el valor actual.
print(myValue)

# 🧬🔍 Confirmamos el tipo: sigue siendo bool.
print(type(myValue))

# 🔤🧾 Imprimimos valor + tipo en un solo mensaje.
print(str(myValue) + " is of the data type " + str(type(myValue)))