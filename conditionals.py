# ============================== 🎉🛂 SECCIÓN 1: VALIDAR ENTRADA A LA FIESTA (SOLO EDAD) 🛂🎉 ==============================
# 🎉🛂 Vamos a crear un validador para saber si una persona puede entrar a una fiesta.
# ✅ Requisito: para entrar, debe ser mayor de edad (18 años o más).

# 🧾👤 Se crea la variable edad y en ella se guarda lo que escriba el usuario.
# 🧠📌 input() muestra un mensaje y espera a que el usuario escriba algo en la consola.
# ✅ Lo que se escribe se guarda como texto (str), aunque parezca un número.
edad = input("Escriba su edad: ")

# ============================== 🔄🔢 SECCIÓN 2: CONVERTIR LA EDAD A NÚMERO 🔢🔄 ==============================
# 🔁🔢 Convertimos la edad a número entero.
# 🧠📌 Esto es necesario porque para comparar edades (mayor, menor, igual) se deben usar números.
edad = int(edad)

# ============================== ✅🔍 SECCIÓN 3: DECIDIR SI PUEDE ENTRAR (IF / ELSE) 🔍✅ ==============================
# ✅🔍 Comparamos si la edad es mayor o igual a 18.
# 🧠📌 Si cumple, entra. Si no cumple, no entra.
if edad >= 18:
    # ✅🟢 Si es mayor de edad, se le permite entrar.
    print("Puede entrar")
else:
    # ⛔🔴 Si es menor de edad, no se le permite entrar.
    print("No puede entrar")


# ============================== 🎉💵 SECCIÓN 4: VALIDAR ENTRADA A LA FIESTA (EDAD + DINERO) 💵🎉 ==============================
# 🎉💵 Ahora validamos DOS condiciones:
# ✅ Debe tener 18 años o más
# ✅ Y además debe tener 600 o más (dinero suficiente)

# 🧾👤 Volvemos a pedir la edad.
# 🧠📌 De nuevo, lo que se escribe se guarda como texto al principio.
edad = input("Escriba su edad: ")

# 🔁🔢 Convertimos la edad a número entero para poder compararla.
edad = int(edad)

# ============================== 💰🧾 SECCIÓN 5: PEDIR Y CONVERTIR EL DINERO 💰🧾 ==============================
# 💰🧾 Se crea la variable dinero y se guarda lo que escriba el usuario.
# 🧠📌 input() también devuelve texto, por eso luego debemos convertirlo.
dinero = input("Escriba su dinero: ")

# 🔁🔢 Convertimos el dinero a entero para poder compararlo con 600.
dinero = int(dinero)

# ============================== ✅🔍 SECCIÓN 6: VALIDACIÓN CON IF ANIDADO (PASO A PASO) 🔍✅ ==============================
# ✅🔍 Primero verificamos si cumple la edad.
if edad >= 18:
    # 💵✅ Si cumple la edad, verificamos si tiene suficiente dinero.
    if dinero >= 600:
        # ✅🟢 Cumple ambas condiciones: entra.
        print("Puede entrar")
    else:
        # ⛔💵 Cumple la edad, pero NO tiene suficiente dinero.
        print("No puede entrar")
else:
    # ⛔🔞 No cumple la edad, así tenga dinero, NO entra.
    print("No puede entrar")


# ============================== ✅🧩 SECCIÓN 7: VALIDACIÓN EN UNA SOLA LÍNEA (VERSIÓN 2) 🧩✅ ==============================
# ✅🧩 Esta versión hace lo mismo, pero en una sola condición:
# 🧠📌 “and” significa: ambas condiciones deben ser verdaderas al mismo tiempo.
if edad >= 18 and dinero >= 600:
    # ✅🟢 Si cumple edad Y dinero, entra.
    print("v2 Puede entrar")
else:
    # ⛔🚫 Si falla cualquiera (edad o dinero), no entra.
    print("v2 No puede entrar")


# ============================== 🧩🛍️ SECCIÓN 8: DECIDIR QUÉ COMPRAR SEGÚN EL DINERO 🛍️🧩 ==============================
# 🧩🔍 Ahora haremos varias comparaciones para sugerir qué comprar.
# 💰🧾 Pedimos el dinero otra vez (para este ejemplo de compras).
dinero = input("Esccriba el dinero con el que cuenta: ")

# 🔁🔢 Lo convertimos a número entero para comparar.
dinero = int(dinero)

# 🧮🛍️ Comparamos el dinero con diferentes rangos para decidir qué comprar.
if dinero < 100:
    # 🍪🟢 Si tiene menos de 100, sugerimos algo económico.
    print("Le compro unas galletas")

elif dinero >= 100 and dinero <= 200:
    # 🍫🟡 Si tiene entre 100 y 200, sugerimos chocolates.
    print("Le compro unos chocolates")

elif dinero > 200 and dinero <= 300:
    # 🍓🟠 Si tiene entre 201 y 300, sugerimos picafresas.
    print("Le compro unas 300 picafresas")

else:
    # 🧸🔵 Si tiene más de 300, sugerimos algo más costoso.
    print("Le compro un peluche")


# ============================== 📦📮 SECCIÓN 9: SERVICIO DE ENVÍO (RESPUESTA SÍ / NO) 📮📦 ==============================
# 📦❓ Guardamos en userReply lo que escriba el usuario.
# 🧠📌 El usuario debe responder "yes" o "no".
userReply = input("Do you need to ship a package? (Enter yes or no) ")

# ✅🧾 Si escribió exactamente "yes", damos una respuesta positiva.
if userReply == "yes":
    # 📦✅ Mensaje de ayuda.
    print("We can help you ship that package!")
else:
    # 🙏👋 Si no escribió "yes", mostramos un mensaje de despedida amable.
    print("Please come back when you need to ship a package. Thank you.")


# ============================== 🛒🧾 SECCIÓN 10: ELEGIR UN SERVICIO (STAMPS / ENVELOPE / COPY) 🧾🛒 ==============================
# 🛒📮📄 El usuario debe escribir una opción:
# stamps, envelope o copy
# 🧠📌 Guardamos su respuesta en userReply.
userReply = input("Would you like to buy stamps, buy an envelope, or make a copy? (Enter stamps, envelope, or copy) ")

# 🧾✅ Si eligió "stamps", mostramos opciones de sellos.
if userReply == "stamps":
    # 🟦📮 Mensaje sobre sellos.
    print("We have many stamp designs to choose from.")

# ✉️✅ Si eligió "envelope", mostramos opciones de sobres.
elif userReply == "envelope":
    # ✉️📏 Mensaje sobre sobres.
    print("We have many envelope sizes to choose from.")

# 🖨️✅ Si eligió "copy", pedimos cuántas copias quiere.
elif userReply == "copy":
    # 🧾🔢 Pedimos el número de copias.
    copies = input("How many copies would you like? (Enter a number) ")

    # 🖨️📄 Mostramos el resultado usando format() para insertar el número.
    print("Here are {} copies.".format(copies))

else:
    # 🙏👋 Si no eligió ninguna opción válida, despedimos al usuario.
    print("Thank you, please come again.")