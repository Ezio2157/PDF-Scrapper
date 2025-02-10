import os
import PyPDF2
import pdfplumber
import fitz  # PyMuPDF

def extraer_texto_pdf(nombre_archivo):
    """
    Extrae el texto de todas las páginas de un PDF usando PyPDF2.
    Devuelve una lista de strings, uno por página.
    """
    textos_paginas = []
    try:
        with open(nombre_archivo, 'rb') as archivo:
            lector_pdf = PyPDF2.PdfReader(archivo)
            for i, pagina in enumerate(lector_pdf.pages):
                texto = pagina.extract_text()
                textos_paginas.append(texto)
        return textos_paginas
    except Exception as e:
        print("Ocurrió un error al extraer el texto:", e)
        return None

def guardar_texto(textos, nombre_salida):
    """
    Guarda el contenido extraído en un archivo de texto.
    """
    try:
        with open(nombre_salida, 'w', encoding='utf-8') as salida:
            for i, texto in enumerate(textos):
                salida.write(f"--- Página {i+1} ---\n")
                salida.write(texto if texto else "Sin contenido de texto detectado.\n")
                salida.write("\n\n")
        print(f"El contenido ha sido guardado en '{nombre_salida}'.")
    except Exception as e:
        print("Error al guardar el archivo:", e)

def extraer_tablas_pdf(nombre_archivo):
    """
    Utiliza pdfplumber para extraer tablas de cada página del PDF.
    Devuelve una lista de tuplas (número_de_página, tabla), donde 'tabla' es una lista de filas.
    """
    tablas_resultado = []
    try:
        with pdfplumber.open(nombre_archivo) as pdf:
            for i, pagina in enumerate(pdf.pages):
                tabla = pagina.extract_table()
                if tabla:
                    tablas_resultado.append((i+1, tabla))
        return tablas_resultado
    except Exception as e:
        print("Ocurrió un error al extraer tablas:", e)
        return None

def extraer_imagenes_pdf(nombre_archivo, carpeta_salida="imagenes_extraidas"):
    """
    Utiliza PyMuPDF para extraer imágenes de cada página del PDF.
    Las imágenes se guardan en la carpeta especificada.
    """
    try:
        doc = fitz.open(nombre_archivo)
        # Crear carpeta de salida si no existe
        if not os.path.exists(carpeta_salida):
            os.makedirs(carpeta_salida)

        # Iterar sobre las páginas del documento
        for pagina in doc:
            imagenes = pagina.get_images(full=True)
            if imagenes:
                for img_index, img in enumerate(imagenes, start=1):
                    xref = img[0]
                    base_imagen = doc.extract_image(xref)
                    imagen_bytes = base_imagen["image"]
                    extension = base_imagen["ext"]
                    nombre_imagen = f"pagina{pagina.number+1}_img{img_index}.{extension}"
                    ruta_imagen = os.path.join(carpeta_salida, nombre_imagen)
                    with open(ruta_imagen, "wb") as img_file:
                        img_file.write(imagen_bytes)
                    print(f"Imagen guardada: {ruta_imagen}")
            else:
                print(f"No se encontraron imágenes en la página {pagina.number+1}.")
    except Exception as e:
        print("Ocurrió un error al extraer imágenes:", e)

def main():
    nombre_archivo = input("Ingresa el nombre del archivo PDF (incluyendo la extensión .pdf): ")

    # Verificar que el archivo exista en el directorio actual
    if not os.path.isfile(nombre_archivo):
        print("El archivo no se encontró. Asegúrate de que el nombre es correcto y que el archivo se encuentra en el directorio del proyecto.")
        return

    # --- Extracción de texto ---
    textos = extraer_texto_pdf(nombre_archivo)
    if textos is not None:
        print(f"\nEl documento tiene {len(textos)} página(s) de texto.")
        opcion_texto = input("¿Deseas guardar el texto extraído en un archivo? (s/n): ").lower()
        if opcion_texto == 's':
            nombre_salida = input("Ingresa el nombre del archivo de salida (ejemplo: salida.txt): ")
            guardar_texto(textos, nombre_salida)
        else:
            for i, texto in enumerate(textos):
                print(f"\n--- Página {i+1} ---")
                print(texto if texto else "Sin contenido de texto detectado.")

    # --- Extracción de tablas ---
    opcion_tablas = input("\n¿Deseas extraer tablas del documento? (s/n): ").lower()
    if opcion_tablas == 's':
        tablas = extraer_tablas_pdf(nombre_archivo)
        if tablas:
            for num_pagina, tabla in tablas:
                print(f"\n--- Tabla encontrada en la página {num_pagina} ---")
                for fila in tabla:
                    print(fila)
        else:
            print("No se encontraron tablas en el documento.")

    # --- Extracción de imágenes ---
    opcion_imagenes = input("\n¿Deseas extraer imágenes del documento? (s/n): ").lower()
    if opcion_imagenes == 's':
        extraer_imagenes_pdf(nombre_archivo)

if __name__ == '__main__':
    main()
