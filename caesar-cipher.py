# ============================== 🧩🛠️ SECCIÓN 1: ¿QUÉ SON LAS FUNCIONES Y PARA QUÉ SIRVEN? 🛠️🧩 ==============================
# 🧩🛠️ Funciones
# 🧠📌 Las funciones son bloques de código que realizan una tarea específica.
# 🧾🔑 Se definen con la palabra clave def, seguida del nombre de la función y paréntesis que pueden contener parámetros.
# ▶️ El código dentro de la función se ejecuta únicamente cuando “llamamos” (usamos) esa función.
# 📤 Algunas funciones pueden devolver un resultado usando la palabra return.
# 🧰✅ Las funciones ayudan a organizar el código, evitar repetir lo mismo y hacerlo más fácil de entender.
# 🎯📥 Una funcion recibe parametros o variables para realizar una tarea especifica

# ============================== ➕🧮 SECCIÓN 2: FUNCIÓN SIMPLE (SUMAR DOS NÚMEROS) ➕🧮 ==============================
# ➕🧮 Creamos una funcion llamada suma
# 🧠🧾 La función suma recibe dos parámetros, numero1 y numero2, que son los dos números que queremos sumar.
# 💾➕ Dentro de la función se hace la suma y se guarda en la variable resultado.
# 📤✅ Finalmente, la función devuelve el resultado con return para poder usarlo fuera de la función.
# 🔁✅ Esta función se puede usar muchas veces con números diferentes, sin reescribir el cálculo.
def suma (numero1, numero2):
    # 💾➕ Guardamos en la variable resultado el valor de la suma
    # 🧠➕ La operación de suma se realiza con el operador +, que suma numero1 y numero2.
    resultado = numero1 + numero2
    # 📤✅ Devolvemos el valor del proceso
    # 🧠🔙 return devuelve el resultado al lugar donde se llamó la función.
    return resultado

# ============================== ⌨️🔢 SECCIÓN 3: PEDIR DATOS AL USUARIO (NÚMERO A) ⌨️🔢 ==============================
# 🧾⌨️ Creamos una variable a con lo que diga el usuario
# 🧠📥 input() le pide al usuario que escriba algo y lo guarda como texto (string).
# ✅ Aunque la persona escriba un número, input() lo guarda como texto.
a = input("Escriba un numero: ")

# 🔄🔢 Convertimos la variable a numero
# 🧠✅ int() convierte el texto a un número entero, para poder hacer operaciones matemáticas.
# ⚠️ Si el usuario escribe letras en vez de un número, esta conversión dará error.
a = int(a)

# ============================== ⌨️🔢 SECCIÓN 4: PEDIR DATOS AL USUARIO (NÚMERO B) ⌨️🔢 ==============================
# 🧾⌨️ Creamos una variable b con lo que diga el usuario
# 🧠📥 Volvemos a pedir otro número para sumarlo con el anterior.
# ✅ Luego lo convertiremos a entero igual que hicimos con “a”.
b = input("Escriba otro numero: ")

# 🔄🔢 Convertimos la variable a numero
# 🧠✅ Convertimos b a entero para poder sumarlo sin errores.
b = int(b)

# ============================== 🧮🖨️ SECCIÓN 5: USAR LA FUNCIÓN Y MOSTRAR EL RESULTADO 🧮🖨️ ==============================
# 🧮🖨️ Llamamos a la funcion suma para obtener el resultado y lo imprimimos
# 🧠📌 Aquí se llama a suma(a, b): se envían los dos números a la función.
# 📤 La función devuelve el resultado, y print(...) lo muestra en pantalla.
print(suma(a, b))

# ============================== 🧪🔐 SECCIÓN 6: INTRODUCCIÓN AL CIFRADO CÉSAR (LABORATORIO) 🔐🧪 ==============================
#-------------------------Laboratorio---------------------------------------

# 🧪🔐 La idea es “mover” cada letra del mensaje un número de posiciones (la clave).
# 🧠➡️ Por ejemplo, si la clave es 3: A -> D, B -> E, C -> F, etc.

# ============================== 🔁🔤 SECCIÓN 7: PREPARAR EL ALFABETO PARA PODER “MOVER” LETRAS 🔤🔁 ==============================
# 🔁🔤 Esta función recibe un alfabeto (un texto) y lo pega consigo mismo.
# 🧠🧩 Lo hacemos para poder “movernos” hacia adelante sin quedarnos sin letras.
# 🧾📌 Ejemplo: "ABC" se vuelve "ABCABC".
# ✅🔐 Esto facilita el desplazamiento en el cifrado César.
def getDoubleAlphabet(alphabet):
    # 🔗🔤 Concatenamos el alfabeto consigo mismo para crear un alfabeto duplicado
    # 🧠📌 Esto evita problemas cuando la clave “pasa” del final del alfabeto.
    doubleAlphabet = alphabet + alphabet
    # 📤✅ Al final devolvemos el alfabeto duplicado completo
    return doubleAlphabet

# ============================== 🧾⌨️ SECCIÓN 8: PEDIR EL MENSAJE QUE SE QUIERE ENCRIPTAR ⌨️🧾 ==============================
# 🧾⌨️ Esta función le pide al usuario que escriba un mensaje.
# 💾📝 Lo que el usuario escriba se guarda y luego se devuelve para usarlo después.
def getMessage():
    # 🧠⌨️ Pedimos al usuario el mensaje y lo guardamos como texto.
    stringToEncrypt = input("Please enter a message to encrypt: ")
    # 📤✅ Devolvemos el mensaje para que otras partes del programa lo usen.
    return stringToEncrypt

# ============================== 🔑🔢 SECCIÓN 9: PEDIR LA CLAVE (CUÁNTO SE MUEVEN LAS LETRAS) 🔢🔑 ==============================
# 🔑🧾 Esta función le pide al usuario una clave.
# 🔢➡️ La clave es un número (normalmente del 1 al 25) que indica cuántas posiciones se moverán las letras.
def getCipherKey():
    # 🧠⌨️ Pedimos la clave al usuario. Se guarda como texto (string).
    shiftAmount = input("Please enter a key (whole number from 1-25): ")
    # 📤✅ Devolvemos la clave para usarla después al encriptar/desencriptar.
    return shiftAmount

# ============================== 🔐🧠 SECCIÓN 10: FUNCIÓN PRINCIPAL (ORQUESTA TODO EL PROGRAMA) 🧠🔐 ==============================
# 🔐⚙️ Esta función es la “jefa”: prepara todo, pide datos al usuario, encripta y luego desencripta.
# ✅ Así comprobamos que el proceso funciona (que al desencriptar vuelve el mensaje original).
def runCaesarCipherProgram():
    # 🔤📌 Definimos el alfabeto
    myAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # 🖨️👀 Imprimimos el alfabeto para que el usuario lo vea
    print(f'Alphabet: {myAlphabet}')

    # 🔁🔤 Duplico el alfabeto para poder desplazar letras sin problemas
    myAlphabet2 = getDoubleAlphabet(myAlphabet)
    # 🖨️👀 Imprimimos el alfabeto duplicado para que el usuario lo vea
    print(f'Alphabet2: {myAlphabet2}')

    # 🧾⌨️ Pido el mensaje al usuario
    myMessage = getMessage()
    # 🖨️👀 Imprimimos el mensaje original antes de encriptarlo
    print(myMessage)

    # 🔑⌨️ Pido la clave al usuario
    myCipherKey = getCipherKey()
    # 🖨️👀 Imprimimos la clave para confirmar cuál se usará
    print(myCipherKey)

    # 🔐🧮 Encripto el mensaje
    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)
    # 🖨️🔐 Imprimimos el mensaje encriptado
    print(f'Encrypted Message: {myEncryptedMessage}')

    # 🔓✅ Desencripto el mensaje (para comprobar que vuelve al original)
    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)
    # 🖨️🔓 Imprimimos el mensaje desencriptado para confirmar que coincide con el original
    print(f'Decypted Message: {myDecryptedMessage}')

# ============================== 🔐🔤 SECCIÓN 11: ENCRIPTAR MENSAJE (MOVER LETRAS HACIA ADELANTE) 🔤🔐 ==============================
# 🔐🛠️ Funcion encriptar
# 🧠📌 Esta función recorre el mensaje letra por letra.
# 🔎 Busca cada letra en el alfabeto, le suma la clave y toma la nueva letra.
# 🚫 Si encuentra espacios o símbolos, los deja igual.
def encryptMessage(message, cipherKey, alphabet):
    # 🧱🔐 Inicializamos la variable que va a contener el mensaje encriptado
    encryptedMessage = ""
    # 🔠⬆️ Convertimos el mensaje a mayúsculas para que coincida con el formato del alfabeto
    uppercaseMessage = ""
    # 🧠⬆️ upper() convierte el mensaje a mayúsculas para que coincida con "ABCDEFGHIJKLMNOPQRSTUVWXYZ".
    uppercaseMessage = message.upper()

    # 🔁🔤 Recorremos cada caracter del mensaje
    for currentCharacter in uppercaseMessage:
        # 🔎🔤 Busco en qué posición está la letra dentro del alfabeto
        position = alphabet.find(currentCharacter)

        # ➕➡️ Calculo la nueva posición sumando la clave
        newPosition = position + int(cipherKey)

        # ✅🔤 Si la letra sí está en el alfabeto, la cambiamos por la “movida”
        if currentCharacter in alphabet:
            encryptedMessage = encryptedMessage + alphabet[newPosition]
        # 🚫🔤 Si no es letra (por ejemplo espacio, número o símbolo), la dejo igual
        else:
            encryptedMessage = encryptedMessage + currentCharacter

    # 📤✅ Devolvemos el texto encriptado completo
    return encryptedMessage

# ============================== 🔓🔤 SECCIÓN 12: DESENCRIPTAR MENSAJE (MOVER LETRAS HACIA ATRÁS) 🔤🔓 ==============================
# 🔓🛠️ Funcion desencriptar
# 🧠📌 Para desencriptar, usamos la misma lógica, pero con la clave en negativo.
# 🔙 Esto hace que las letras vuelvan a su posición original.
def decryptMessage(message, cipherKey, alphabet):
    # 🔙🔑 Invertimos la clave: si encriptamos con +3, desencriptamos con -3
    decryptKey = -1 * int(cipherKey)
    # 🔓🧩 Reutilizamos encryptMessage porque el proceso es el mismo con la clave invertida
    return encryptMessage(message, decryptKey, alphabet)

# ============================== 🚀▶️ SECCIÓN 13: ARRANQUE DEL PROGRAMA (EJECUCIÓN) ▶️🚀 ==============================
# 🚫🧠 Si no llamamos la función principal, no pasa nada.
# 🚀▶️ Esta línea es la que “arranca” el programa.
runCaesarCipherProgram()