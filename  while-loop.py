# ============================== ✅📚 IMPORTACIÓN DE LIBRERÍAS (SIEMPRE ARRIBA) 📚✅ ==============================
# ✅📚 Siempre que se importe una libreria debe ir al principio del codigo
# 🎲📦   En este caso se importa la libreria random para generar numeros aleatorios
import random

# ============================== 🔁🧠 IDEA CLAVE: ¿QUÉ ES UN WHILE? 🧠🔁 ==============================
# 🔁🧠 Un ciclo while es un bucle que va a recorrer hasta que no se cumpla la condicion

# ============================== 🔢⌨️ PARTE 1: CONTAR DESDE UN NÚMERO HASTA LLEGAR A 10 🔢⌨️ ==============================
# 🧾⌨️ Se crea la variable numero y se le pide al usuario que escriba el numero 0
# 🧠📝 En esta línea de código, se crea una variable llamada numero y se le asigna el valor que el usuario ingresa a través de la función input(). La función input() muestra un mensaje en la consola ("Escriba el numero 0: ") y espera a que el usuario escriba su respuesta. Una vez que el usuario ingresa un número y presiona Enter, el valor ingresado se almacena en la variable numero, lo que permite que el programa utilice este valor posteriormente para realizar operaciones relacionadas con este número.
numero = input("Escriba el numero 0: ")

# 🔄🔢 Convertimos la variable numero de str a int
# ✅🧩 La función int() se utiliza para convertir el valor almacenado en la variable numero, que inicialmente es una cadena de texto (str) debido a la función input(), en un número entero (int). Esto es necesario para poder realizar operaciones matemáticas o comparaciones numéricas con la variable numero en el código posterior. Después de esta conversión, la variable numero contendrá un valor numérico que puede ser utilizado en cálculos o condiciones dentro del programa.
numero = int(numero)

# 🔍✅ Se verifica que lo que hay en la variable numero sea menor que 10
# 🔁📌 En esta línea de código, se inicia un ciclo while que continuará ejecutándose mientras la condición numero < 10 sea verdadera. Esto significa que el bloque de código dentro del ciclo while se repetirá continuamente hasta que el valor de numero sea igual o mayor a 10. El ciclo while es útil para realizar tareas repetitivas o iterativas basadas en una condición específica, en este caso, la comparación de numero con el valor 10.
while numero < 10 :
    # ➕📈 Se incrementa el valor de numero
    # 🧠⬆️ En esta línea de código, se incrementa el valor de la variable numero en 1 utilizando la operación de suma. Esto significa que cada vez que se ejecute esta línea dentro del ciclo while, el valor de numero aumentará en 1. Este incremento es importante para asegurar que eventualmente la condición del ciclo while (numero < 10) deje de ser verdadera, lo que permitirá que el ciclo termine y el programa continúe con las siguientes instrucciones después del ciclo.
    numero = numero + 1
    # 🖨️📣 Si numero es menor que 10 se imprime su valor
    # 👀🧾 En esta línea de código, se utiliza la función print() para mostrar el valor actual de la variable numero en la consola. Esto se ejecutará cada vez que el ciclo while se repita, lo que permitirá al usuario ver cómo el valor de numero cambia a medida que se incrementa en cada iteración del ciclo. La impresión del valor de numero es útil para monitorear el progreso del ciclo y entender cómo se está modificando la variable durante la ejecución del programa.
    print(numero)

# ============================== ✖️📋 PARTE 2: TABLA DE MULTIPLICAR (DEL 1 AL 10) 📋✖️ ==============================
# -------------------------------------------------------------------
# ✖️📋 Vamos a construir la tabla de multiplicar de un numero
# 🧾⌨️ Se crea la variable numero y se le pide al usuario que escriba el numero 0
# 🧠📝 En esta línea de código, se crea una variable llamada numero y se le asigna el valor que el usuario ingresa a través de la función input(). La función input() muestra un mensaje en la consola ("Escriba un numero: ") y espera a que el usuario escriba su respuesta. Una vez que el usuario ingresa un número y presiona Enter, el valor ingresado se almacena en la variable numero, lo que permite que el programa utilice este valor posteriormente para realizar operaciones relacionadas con este número.
numero = input("Escriba un numero: ")

# 🔄🔢 Convertimos la variable numero de str a int
# ✅🧩 La función int() se utiliza para convertir el valor almacenado en la variable numero, que inicialmente es una cadena de texto (str) debido a la función input(), en un número entero (int). Esto es necesario para poder realizar operaciones matemáticas o comparaciones numéricas con la variable numero en el código posterior. Después de esta conversión, la variable numero contendrá un valor numérico que puede ser utilizado en cálculos o condiciones dentro del programa.
numero = int(numero)

# 🔢🧮 multiplicador
# 🧠🧾 Se crea la variable multiplicador y se le asigna el valor de 0. Esta variable se utilizará como contador para generar la tabla de multiplicar del número ingresado por el usuario. A medida que el ciclo while se ejecute, el valor de multiplicador se incrementará en cada iteración, lo que permitirá calcular y mostrar los resultados de la multiplicación del número con los valores del multiplicador.
multiplicador = 0

# 🔍✅ Se verifica que lo que hay en la variable numero sea menor que 10
# 🔁📌 En esta línea de código, se inicia un ciclo while que continuará ejecutándose mientras la condición multiplicador < 10 sea verdadera. Esto significa que el bloque de código dentro del ciclo while se repetirá continuamente hasta que el valor de multiplicador sea igual o mayor a 10. El ciclo while es útil para realizar tareas repetitivas o iterativas basadas en una condición específica, en este caso, la comparación de multiplicador con el valor 10, lo que permitirá generar la tabla de multiplicar del número ingresado por el usuario.
while multiplicador < 10 :
    # ➕📈 Se incrementa el valor de multiplicador
    # 🧠⬆️ En esta línea de código, se incrementa el valor de la variable multiplicador en 1 utilizando la operación de suma. Esto significa que cada vez que se ejecute esta línea dentro del ciclo while, el valor de multiplicador aumentará en 1. Este incremento es importante para asegurar que eventualmente la condición del ciclo while (multiplicador < 10) deje de ser verdadera, lo que permitirá que el ciclo termine y el programa continúe con las siguientes instrucciones después del ciclo. Además, este incremento es esencial para generar la tabla de multiplicar, ya que se utilizará el valor de multiplicador para calcular los resultados de la multiplicación con el número ingresado por el usuario.
    multiplicador = multiplicador + 1
    # ✖️🧾 Valor de multiplicacion
    # 🧠🧮 En esta línea de código, se calcula el valor de multiplicacion al multiplicar la variable numero (que contiene el número ingresado por el usuario) por la variable multiplicador (que se incrementa en cada iteración del ciclo while). El resultado de esta multiplicación se almacena en la variable multiplicacion, lo que permitirá mostrar el resultado de la tabla de multiplicar para cada valor del multiplicador. Este cálculo es fundamental para generar la tabla de multiplicar del número ingresado por el usuario.
    multiplicacion = numero * multiplicador
    # 🖨️📣 Si numero es menor que 10 se imprime su valor
    # 🚫📝print(numero, " * ", multiplicador, " = ", multiplicacion)
    # 🧠📌 En esta línea de código, se utiliza la función print() para mostrar el resultado de la multiplicación en un formato específico. Se utiliza una cadena de formato (f-string) para insertar los valores de numero, multiplicador y multiplicacion directamente dentro del texto que se imprimirá. Al ejecutar esta línea, se mostrará un mensaje que indica la operación de multiplicación realizada, por ejemplo, "5  *  1  =  5", lo que permite al usuario ver claramente el resultado de cada paso en la tabla de multiplicar.
    print(f"{numero}  *  {multiplicador}  =  {multiplicacion}")

# ============================== 🎮🎯 PARTE 3: JUEGO “ADIVINA EL NÚMERO” 🎯🎮 ==============================
#---------------------Laboratorio--------------------------------

# 🎮🧠 Vamos a construir un juego de adivinar el numero
# 🧾⌨️ Se crea la variable numero y se le pide al usuario que escriba el numero 0
# 🧠📝 En esta línea de código, se crea una variable llamada numero y se le asigna el
# 🧾🧠 valor que el usuario ingresa a través de la función input(). La función input() muestra un mensaje en la consola ("Escriba un numero: ") y espera a que el usuario escriba su respuesta. Una vez que el usuario ingresa un número y presiona Enter, el valor ingresado se almacena en la variable numero, lo que permite que el programa utilice este valor posteriormente para realizar operaciones relacionadas con este número.
print("Welcome to Guess the Number!")

# 🖨️👋 En esta línea de código, se utiliza la función print() para mostrar un mensaje de bienvenida al usuario en la consola. El mensaje "Welcome to Guess the Number!" indica que el programa es un juego de adivinar el número, lo que ayuda a establecer el contexto y las expectativas para el usuario antes de comenzar a jugar.
print("The rules are simple. I will think of a number, and you will try to guess it.")

# 🎲🔢 La libreria random genera numero aleatorios desde un numero inicial hasta un numero final
# 🧠📌 En esta línea de código, se utiliza la función randint() de la librería random para generar un número aleatorio entre 1 y 10 (inclusive). El número generado se almacena en la variable number, lo que permitirá que el programa tenga un número secreto que el usuario intentará adivinar durante el juego. Cada vez que se ejecute esta línea, se generará un nuevo número aleatorio, lo que hace que el juego sea diferente cada vez que se juegue.
number = random.randint(1,10)

# ✅❌ Se crea la variable isGuessRight y se guarda un valor booleano (False)
# 🧠🏳️ En esta línea de código, se crea una variable llamada isGuessRight y se le asigna el valor booleano False. Esta variable se utilizará como una bandera para indicar si el usuario ha adivinado correctamente el número secreto. Mientras isGuessRight sea False, el juego continuará solicitando al usuario que ingrese sus conjeturas. Una vez que el usuario adivine correctamente el número, isGuessRight se establecerá en True, lo que permitirá que el ciclo while termine y el juego finalice.
isGuessRight = False

# 🔁🎯 Mientras la variable isGuessRight sea diferente de verdadero se ejecuta el codigo
# 🧠📌 En esta línea de código, se inicia un ciclo while que continuará ejecutándose mientras la condición isGuessRight != True sea verdadera. Esto significa que el bloque de código dentro del ciclo while se repetirá continuamente hasta que isGuessRight sea igual a True. El ciclo while es útil para mantener el juego en ejecución hasta que el usuario adivine correctamente el número secreto, momento en el cual isGuessRight se establecerá en True y el ciclo terminará, finalizando el juego.
while isGuessRight != True:
    # 🧾⌨️ Se crea la variable guess y se guarda dentro de ella lo que escriba el usuario
    # 🧠📝 En esta línea de código, se crea una variable llamada guess y se le asigna el valor que el usuario ingresa a través de la función input(). La función input() muestra un mensaje en la consola ("Guess a number between 1 and 10: ") y espera a que el usuario escriba su respuesta. Una vez que el usuario ingresa un número y presiona Enter, el valor ingresado se almacena en la variable guess, lo que permite que el programa utilice este valor posteriormente para comparar con el número secreto almacenado en la variable number. Este proceso es fundamental para el juego de adivinar el número, ya que permite al usuario hacer conjeturas y recibir retroalimentación sobre si su conjetura es correcta o no.
    guess = input("Guess a number between 1 and 10: ")
    # 🔍✅ Mientras el valor de la variable guess sea un entero exactamente igual al valor de la variable number
    # 🧠⚖️ En esta línea de código, se utiliza una estructura condicional if para comparar el valor ingresado por el usuario (guess) con el número secreto generado por el programa (number). La función int() se utiliza para convertir la variable guess, que inicialmente es una cadena de texto (str) debido a la función input(), en un número entero (int) para poder realizar la comparación numérica. Si el valor de guess convertido a entero es exactamente igual al valor de number, entonces se ejecutará el bloque de código dentro del if, lo que indicará que el usuario ha adivinado correctamente el número secreto.
    if int(guess) == number:
        # 🏆🎉 Imprime que ganamos
        # 🧠📣 En esta línea de código, se utiliza la función print() para mostrar un mensaje de felicitación al usuario en la consola, indicando que ha adivinado correctamente el número secreto. El mensaje "You guessed {}. That is correct! You win!" incluye un marcador de posición {} que se reemplaza con el valor de guess utilizando el método format(). Al ejecutar esta línea, se mostrará un mensaje personalizado que confirma que la conjetura del usuario es correcta y que ha ganado el juego.
        print("You guessed {}. That is correct! You win!".format(guess))
        # ✅🔚 La variable isGuessRight se pasa a verdadero para terminar el ciclo while
        # 🧠🏁 En esta línea de código, se asigna el valor booleano True a la variable isGuessRight. Esto es importante porque isGuessRight se utiliza como una bandera para controlar la ejecución del ciclo while. Al establecer isGuessRight en True, se cumplirá la condición para salir del ciclo while (isGuessRight != True), lo que permitirá que el juego termine después de que el usuario adivine correctamente el número secreto.
        isGuessRight = True
    # ❌🔁 Si la variable guess no es exactamente igual a la variable isGuessRight imprime
    # 🧠📌 En esta línea de código, se utiliza la estructura condicional else para manejar el caso en el que la conjetura del usuario (guess) no sea igual al número secreto (number). Si la condición del if anterior no se cumple, es decir, si el usuario no adivina correctamente el número, entonces se ejecutará el bloque de código dentro del else, lo que proporcionará retroalimentación al usuario indicando que su conjetura es incorrecta y lo alentará a intentarlo nuevamente.
    else:
        # 🔁💪 Intentalo de nuevo
        # 🧠📣 En esta línea de código, se utiliza la función print() para mostrar un mensaje de retroalimentación al usuario en la consola, indicando que su conjetura es incorrecta y animándolo a intentarlo nuevamente. El mensaje "You guessed {}. Sorry, that isn’t it. Try again." incluye un marcador de posición {} que se reemplaza con el valor de guess utilizando el método format(). Al ejecutar esta línea, se mostrará un mensaje personalizado que informa al usuario que su conjetura no es correcta y lo motiva a seguir intentando adivinar el número secreto.
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))