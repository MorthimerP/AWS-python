🐍 PROYECTO DE FUNDAMENTOS DE PYTHON

Este repositorio contiene varios ejemplos prácticos para aprender los conceptos básicos de Python.
Cada archivo demuestra un tema diferente como variables, condicionales, ciclos, manejo de archivos, uso del sistema operativo y cálculos científicos.

El objetivo es entender qué hace cada parte del código de manera clara y sencilla.

📌 CONTENIDO DEL PROYECTO

Este proyecto incluye ejemplos de:

✅ Impresión en pantalla (print)

✅ Variables y tipos de datos

✅ Operaciones matemáticas

✅ Condicionales (if, elif, else)

✅ Ciclos (for, while)

✅ Listas y diccionarios

✅ Lectura de archivos CSV

✅ Lectura de archivos JSON

✅ Ejecución de comandos del sistema

✅ Cálculos científicos (insulina, pH, peso molecular)

🧮 TIPOS DE DATOS NUMÉRICOS
🔢 OPERACIONES MATEMÁTICAS BÁSICAS

Se muestran ejemplos de:

Suma

Resta

Multiplicación

División

Esto ayuda a entender cómo Python maneja los números.

🔎 VERIFICAR EL TIPO DE UNA VARIABLE

Se usa la función:

type(variable)

Para saber si un valor es:

int (entero)

float (decimal)

complex (complejo)

bool (booleano)

También se demuestra cómo una variable puede cambiar de tipo dinámicamente en Python.

📝 VARIABLES Y MENSAJES EN PANTALLA
🌎 IMPRIMIR TEXTO Y VARIABLES

Se muestra cómo:

Crear una variable

Guardar un nombre

Imprimir mensajes en pantalla

Ejemplo:

print("Hola mundo")
print(name)

Esto es fundamental para interactuar con el usuario.

🔁 CICLOS (LOOPS)
🔢 CICLO FOR

Se utiliza for junto con range() para repetir acciones varias veces.

Ejemplo:

Contar del 0 al 10

Recorrer listas

Procesar datos

🔄 CICLO WHILE

Se usa cuando queremos repetir algo mientras se cumpla una condición.

Ejemplo:

Calcular la carga neta de una proteína variando el pH.

🔍 CONDICIONALES (IF - ELSE)
🎉 VALIDACIÓN DE EDAD

Se muestra cómo:

Pedir datos al usuario

Convertir texto a número con int()

Evaluar condiciones

Ejemplo:

Permitir entrar a una fiesta si es mayor de 18 años.

💵 VALIDACIÓN CON MÚLTIPLES CONDICIONES

Se combinan condiciones usando:

and

Ejemplo:

Debe ser mayor de edad y tener suficiente dinero.

🛍️ MÚLTIPLES DECISIONES CON elif

Permite evaluar varios escenarios:

Si tiene poco dinero → compra galletas

Si tiene más → chocolates

Si tiene aún más → picafresas

Si tiene mucho → peluche

📂 MANEJO DE ARCHIVOS CSV
🚗 INVENTARIO DE VEHÍCULOS

Se trabaja con un archivo car_fleet.csv.

El programa:

Abre el archivo

Lee cada línea

Guarda la información en diccionarios

Almacena todos los vehículos en una lista

Se usan:

csv.reader

Diccionarios

copy.deepcopy()

Esto permite estructurar datos reales en memoria.

📦 MANEJO DE ARCHIVOS JSON
📖 FUNCIÓN PARA LEER JSON

Se crea una función que:

Intenta abrir un archivo JSON

Si funciona → devuelve los datos

Si falla → muestra un error

Se usa:

try

except

json.load()

Esto enseña manejo básico de errores.

🖥️ EJECUCIÓN DE COMANDOS DEL SISTEMA
🧩 USO DEL MÓDULO os

Permite ejecutar comandos simples como:

os.system("ls")
🚀 USO DEL MÓDULO subprocess

Es más flexible y seguro.

Permite:

Pasar argumentos como lista

Ejecutar comandos como uname -a

Ver procesos activos con ps -x

Es útil para automatizar tareas del sistema.

🧬 PROYECTO CIENTÍFICO: INSULINA
🧪 SECUENCIAS DE AMINOÁCIDOS

Se guarda la secuencia de:

Preproinsulina

Cadena A

Cadena B

Cadena C

Luego se une la cadena A y B para formar la insulina activa.

⚖️ CÁLCULO DEL PESO MOLECULAR

El programa:

Cuenta cuántos aminoácidos hay

Multiplica por su peso molecular

Suma todo

Calcula el porcentaje de error

Esto demuestra cómo usar:

Diccionarios

Comprensiones de diccionarios

Fórmulas matemáticas

🌡️ CÁLCULO DE CARGA NETA SEGÚN EL PH

Se evalúa cómo cambia la carga de la insulina cuando el pH varía de 0 a 14.

Se usan:

Diccionarios

Fórmulas químicas

Ciclo while

Este ejemplo combina programación y biología.

🎯 OBJETIVO DEL PROYECTO

Este conjunto de programas tiene como finalidad:

Comprender los fundamentos de Python.

Aprender a estructurar código correctamente.

Entender cómo funcionan los tipos de datos.

Practicar lógica con condicionales y ciclos.

Trabajar con archivos reales.

Aplicar programación a problemas científicos.

🚀 REQUISITOS

Python 3 instalado

No se requieren librerías externas adicionales

📚 RECOMENDADO PARA

Personas que están empezando en programación.

Estudiantes de informática.

Estudiantes de ciencias que quieren aplicar Python.

Cualquier persona que quiera entender cómo funciona Python desde lo básico hasta ejemplos más aplicados.