# ============================== 🧬🚀 INICIO DEL PROGRAMA: LIMPIEZA Y PROCESAMIENTO DE PREPROINSULINA 🚀🧬 ==============================

# ============================== 📚🔧 IMPORTACIÓN DE LIBRERÍAS 🔧📚 ==============================
# Importamos la librería "re", que sirve para trabajar con expresiones regulares.
# Las expresiones regulares nos permiten buscar, eliminar o modificar partes específicas de un texto.
# En este programa la usamos para limpiar la secuencia de preproinsulina eliminando palabras y caracteres que no pertenecen a la secuencia real de aminoácidos.
import re

# ============================== 📂📖 LECTURA DEL ARCHIVO ORIGINAL 📖📂 ==============================
# Abrimos el archivo de texto que contiene la secuencia original.
# El archivo debe estar en la misma carpeta que este programa o se debe indicar la ruta completa.
# Usamos "r" (read) para abrirlo en modo lectura.
with open("preproinsulin-seq.txt", "r") as f:
    # Leemos TODO el contenido del archivo y lo guardamos en la variable raw_data.
    # En este momento el texto puede contener palabras, números y símbolos que debemos limpiar.
    raw_data = f.read()

# ============================== 🧽🧹 LIMPIEZA DEL TEXTO (ELIMINAR PALABRAS Y SÍMBOLOS INNECESARIOS) 🧹🧽 ==============================
# Eliminamos la palabra "ORIGIN" del texto.
# No importa si está en mayúsculas o minúsculas.
# Esto se hace porque esa palabra no forma parte de la secuencia de aminoácidos.
clean_data = re.sub(r"\bORIGIN\b", "", raw_data, flags=re.IGNORECASE)

# Eliminamos los símbolos "//" que indican el final del registro.
# Tampoco forman parte de la secuencia real.
clean_data = clean_data.replace("//", "")

# ============================== 🔤✂️ FILTRAR SOLO LETRAS (DEJAR ÚNICAMENTE AMINOÁCIDOS) ✂️🔤 ==============================
# Ahora eliminamos cualquier cosa que NO sea una letra.
# Esto quita números, espacios y otros símbolos.
# Al final solo quedarán letras, que representan los aminoácidos.
clean_data = re.sub(r"[^A-Za-z]", "", clean_data)

# ============================== 🔡✅ NORMALIZACIÓN DE LA SECUENCIA (TODO EN MINÚSCULAS) ✅🔡 ==============================
# Convertimos toda la secuencia a minúsculas.
# Esto garantiza que todas las letras tengan el mismo formato
# y evita problemas al procesarlas más adelante.
clean_data = clean_data.lower()

# ============================== 💾📝 GUARDAR EL ARCHIVO YA LIMPIO 📝💾 ==============================
# Volvemos a abrir el archivo, pero ahora en modo escritura ("w").
# Esto reemplaza completamente el contenido anterior.
with open("preproinsulin-seq.txt", "w") as f:
    # Guardamos la secuencia limpia en el archivo.
    # Ahora el archivo solo contiene letras válidas.
    f.write(clean_data)

# ============================== 📏🔍 VALIDACIÓN DE LONGITUD (CONTROL DE CALIDAD) 🔍📏 ==============================
# Verificamos cuántos caracteres tiene la secuencia limpia.
# La preproinsulina humana debe tener exactamente 110 aminoácidos.
print("Longitud preproinsulina: ", len(clean_data))

# Si la secuencia no tiene 110 caracteres, el programa se detiene.
# Esto es una medida de seguridad para evitar trabajar con datos incorrectos.
if len(clean_data) != 110:
    print("Error: la secuencia no tiene 110 caracteres")
    exit()

# ============================== ✂️🧬 EXTRACCIÓN DE SEGMENTOS (DIVISIÓN DE LA SECUENCIA) 🧬✂️ ==============================
# Ahora dividimos la secuencia en sus partes biológicas.

# Extraemos los primeros 24 caracteres (cadena señal).
lsinsulin = clean_data[0:24]

# Extraemos del carácter 25 al 54 (cadena B).
binsulin = clean_data[24:54]

# Extraemos del carácter 55 al 89 (cadena C).
cinsulin = clean_data[54:89]

# Extraemos del carácter 90 al 110 (cadena A).
ainsulin = clean_data[89:110]

# ============================== 🗃️🧾 CREACIÓN DE ARCHIVOS SEPARADOS PARA CADA SEGMENTO 🧾🗃️ ==============================
# Creamos un archivo independiente para cada parte.
# Esto facilita el análisis individual de cada segmento.

with open("lsinsulin-seq-clean.txt", "w") as f:
    f.write(lsinsulin)

with open("binsulin-seq-clean.txt", "w") as f:
    f.write(binsulin)

with open("cinsulin-seq-clean.txt", "w") as f:
    f.write(cinsulin)

with open("ainsulin-seq-clean.txt", "w") as f:
    f.write(ainsulin)

# ============================== ✅📏 VERIFICACIÓN FINAL DE TAMAÑOS 📏✅ ==============================
# Confirmamos que cada segmento tenga la longitud correcta.
print("lsinsulin: ", len(lsinsulin))
print("binsulin: ", len(binsulin))
print("cinsulin: ", len(cinsulin))
print("ainsulin: ", len(ainsulin))

# ============================== 🔗🧬 CONSTRUCCIÓN DE INSULINA FINAL (UNIÓN DE B + A) 🧬🔗 ==============================
# La insulina activa se forma uniendo la cadena B con la cadena A.
insulin = binsulin + ainsulin

# ============================== 🧾📌 RESULTADOS FINALES (LONGITUD Y SECUENCIA) 📌🧾 ==============================
# Mostramos cuántos aminoácidos tiene la insulina procesada.
print("Insulina procesada: ", len(insulin))

# Mostramos la secuencia final completa.
print("Secuencia de la insulina: ", insulin)

# ============================== ✅🏁 FIN DEL PROGRAMA 🏁✅ ==============================