import os

def es_primo(numero):
    if numero < 2:
        return False

    for divisor in range(2, int(numero ** 0.5) + 1):
        if numero % divisor == 0:
            return False

    return True

def main():
    primos = []

    for numero in range(1, 251):
        if es_primo(numero):
            primos.append(numero)

    # Guardar en results.txt (en la misma carpeta del script)
    ruta_carpeta = os.path.dirname(os.path.abspath(__file__))
    ruta_archivo = os.path.join(ruta_carpeta, "results.txt")

    with open(ruta_archivo, "w", encoding="utf-8") as archivo:
        for primo in primos:
            archivo.write(str(primo) + "\n")

    # Mostrar en pantalla
    print("Números primos entre 1 y 250:")
    print(primos)

    # Mostrar rutas absolutas (para que las anotes)
    print("\nRuta absoluta del script:")
    print(os.path.abspath(__file__))

    print("\nRuta absoluta del archivo results.txt:")
    print(ruta_archivo)

    # Verificación rápida
    print(f"\nSe guardaron {len(primos)} números primos en results.txt.")

if __name__ == "__main__":
    main()