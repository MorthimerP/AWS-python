# ============================== 🧵🧠 MANEJO DE STRINGS (TEXTO) EN PYTHON 🧠🧵 ==============================

# ============================== 🧵📝 CREAMOS UNA CADENA (STRING) Y LA GUARDAMOS EN UNA VARIABLE ==============================
# 🧵📝 CREAMOS UNA CADENA (STRING) Y LA GUARDAMOS EN UNA VARIABLE
# 📌 Creamos una variable myString y dentro de ella se guarda el texto "This is a string"
# 🧠 En Python, las cadenas de texto se representan utilizando comillas simples (' ') o comillas dobles (" ").
# ✅ En este caso, se utilizan comillas dobles para definir la cadena de texto "This is a string".
# 📦 La variable myString ahora contiene esta cadena de texto y puede ser utilizada posteriormente en el código.
# 🔤 Esto es útil para hacer operaciones como concatenar, buscar palabras, contar letras, etc.
myString = "This is a string."

# ============================== 🖨️📤 MOSTRAMOS EN PANTALLA EL CONTENIDO DE UNA VARIABLE ==============================
# 🖨️📤 IMPRIMIMOS EL CONTENIDO DE LA VARIABLE
# 📌 Imprimimos el valor de la variable myString
# 🧾 La función print() se utiliza para mostrar el valor de la variable myString en la consola.
# 👀 Al ejecutar esta línea de código, se imprimirá el texto "This is a string." en la salida estándar (consola).
# ✅ Esto permite verificar rápidamente qué contiene la variable.
print(myString)

# ============================== 🧪🔍 REVISAMOS QUÉ TIPO DE DATO ES (STRING, NÚMERO, ETC.) ==============================
# 🧪🔍 VERIFICAMOS EL TIPO DE DATO
# 📌 Imprimimos el tipo de dato de la  variable myString
# 🧠 La función type() se utiliza para determinar el tipo de dato de la variable myString.
# ✅ En este caso, como myString contiene una cadena de texto, type(myString) devolverá <class 'str'>.
# 🧾 Esto confirma que myString es un string.
print(type(myString))

# ============================== 🧾🔗 UNIMOS TEXTO CON INFORMACIÓN (CONVERSIÓN A STRING) ==============================
# 🧾🔗 IMPRIMIMOS VALOR + TEXTO + TIPO (CONVERSIÓN A STR)
# 📌 Imprimimos el valor de la variable myString, un texto y finalmente el tipo de dato de la variable myString
# 🧠 En esta línea se imprime un mensaje combinado (concatenado) usando el operador +.
# 🔁 Como type(myString) no es texto, usamos str(...) para convertirlo a string y poder unirlo sin error.
# ✅ Resultado: muestra el contenido de myString y el tipo de dato en una sola línea.
print(myString + " is of the data type " + str(type(myString)))

# ============================== 🔗✨ CONCATENACIÓN DE STRINGS (UNIR PALABRAS) ==============================
# 🌊🧩 CREAMOS STRINGS PARA CONCATENAR
# 📌 Creamos la variable firstString y dentro de ella guardamos el valor de "water"
# 🧠 En esta línea de código, se crea una variable llamada firstString y se le asigna el valor de la cadena de texto "water".
# ✅ firstString queda guardando la palabra "water" para usarla después.
firstString = "water"

# 🍂🧩 SEGUNDA CADENA PARA UNIR
# 📌 Creamos la variable secondString y dentro de ella guardamos el valor de "fall"
# 🧠 En esta línea de código, se crea una variable llamada secondString y se le asigna el valor de la cadena de texto "fall".
# ✅ secondString queda guardando la palabra "fall" para luego combinarla.
secondString = "fall"

# 🔗✨ CONCATENAMOS DOS STRINGS PARA CREAR UNO NUEVO
# 📌 Creamos la variable thirdString y dentro de ella guardamos el valor concatenado (unido) de las variable firstString y secondString
# 🧠 El operador + se utiliza para concatenar (unir) dos cadenas.
# ✅ Al unir "water" + "fall" obtenemos "waterfall".
# 📦 Ese resultado se guarda en thirdString.
thirdString = firstString + secondString

# ============================== 🖨️✅ MOSTRAMOS EL RESULTADO DE LA UNIÓN DE TEXTOS ==============================
# 🖨️🌊 IMPRIMIMOS EL RESULTADO DE LA CONCATENACIÓN
# 📌 Imprimimos el valor de la variable thirdString
# 🧾 print() muestra en la consola el valor actual de thirdString.
# ✅ Aquí veremos: waterfall
print(thirdString)

# ============================== 🙋‍♂️⌨️ ENTRADAS DEL USUARIO (INPUT) ==============================
# 🙋‍♂️⌨️ ENTRADA DE USUARIO: PEDIMOS EL NOMBRE
# 📌 Creamos la variable name y usando la funcion input() vamos a almacenar lo que escriba el usuario por consola
# 🧠 input() muestra un mensaje y espera a que el usuario escriba algo y presione Enter.
# 📥 Todo lo que se escribe entra como texto (tipo str), incluso si parecen números.
# ✅ Lo que el usuario escriba se guarda en la variable name.
name = input("What is your name? ")

# ============================== 🖨️👤 MOSTRAMOS LO QUE EL USUARIO ESCRIBIÓ ==============================
# 🖨️👤 IMPRIMIMOS LO QUE ESCRIBIÓ EL USUARIO
# 📌 Imprimimos el valor de la variable name
# 👀 Así podemos verificar qué fue lo que el usuario ingresó.
print(name)

# ============================== 🎨🐾 PEDIMOS MÁS DATOS AL USUARIO (COLOR Y ANIMAL) ==============================
# 🎨⌨️ ENTRADA DE USUARIO: COLOR FAVORITO
# 📌 Creamos la variable color y usando la funcion input() vamos a almacenar lo que escriba el usuario por consola
# 🧠 Se solicita al usuario su color favorito y se guarda como texto en la variable color.
# ✅ La respuesta queda almacenada para usarla en el mensaje final.
color = input("What is your favorite color?  ")

# 🐾⌨️ ENTRADA DE USUARIO: ANIMAL FAVORITO
# 📌 Creamos la variable animal y usando la funcion input() vamos a almacenar lo que escriba el usuario por consola
# 🧠 Se solicita al usuario su animal favorito y se guarda como texto en la variable animal.
# ✅ La respuesta queda almacenada para usarla en el mensaje final.
animal = input("What is your favorite animal?  ")

# ============================== 🧩🧾 MENSAJE FINAL CON TEXTO FORMATEADO ==============================
# 🧩🧾 SALIDA FORMATEADA CON format()
# 📌 Para imprimir usando format() vamos a poner un {} por cada variable y el format() va a poner el valor de las variables en el orden que se estan usando
# 🧠 Los {} son "huecos" donde se insertarán los valores que se pasan en format(...).
# ✅ El orden importa: primero name, luego color, luego animal.
# 🖨️ Resultado ejemplo: "Carlos, you like a blue dog!"
print("{}, you like a {} {}!".format(name,color,animal))