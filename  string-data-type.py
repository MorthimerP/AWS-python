# Creamos una variable myString y dentro de ella se guarda el texto "This is a string"
myString = "This is a string."

# Imprimimos el valor de la variable myString
print(myString)

# Imprimimos el tipo de dato de la  variable myString
print(type(myString))

# Imprimimos el valor de la variable myString, un texto y finalmente el tipo de dato de la variable myString
print(myString + " is of the data type " + str(type(myString)))

# Creamos la variable firstString y dentro de ella guardamos el valor de "water"
firstString = "water"

# Creamos la variable secondString y dentro de ella guardamos el valor de "fall"
secondString = "fall"

# Creamos la variable thirdString y dentro de ella guardamos el valor concatenado (unido) de las variable firstString y secondString
thirdString = firstString + secondString

# Imprimimos el valor de la variable thirdString
print(thirdString)

# Creamos la variable name y usando la funcion input() vamos a almacenar lo que escriba el usuario por consola
name = input("What is your name? ")

# Imprimimos el valor de la variable name
print(name)

# Creamos la variable color y usando la funcion input() vamos a almacenar lo que escriba el usuario por consola
color = input("What is your favorite color?  ")

# Creamos la variable animal y usando la funcion input() vamos a almacenar lo que escriba el usuario por consola
animal = input("What is your favorite animal?  ")

# Para imprimir usando format() vamos a poner un {} por cada variable y el format() va a poner el valor de las variables en el orden que se estan usando
print("{}, you like a {} {}!".format(name,color,animal))