# Proyecto PDF Scrapping

Este proyecto es una herramienta desarrollada en Python para extraer información de archivos PDF. La herramienta permite extraer **texto**, **tablas** e **imágenes** de un documento PDF utilizando las siguientes bibliotecas:

- **PyPDF2**: Para la extracción de texto.
- **pdfplumber**: Para la detección y extracción de tablas.
- **PyMuPDF (fitz)**: Para la extracción de imágenes.

## Requisitos

- Python 3.6 o superior.
- Las siguientes librerías:
  - PyPDF2
  - pdfplumber
  - PyMuPDF


### **Instalar dependencias**
Ejecuta el siguiente comando para instalar las librerías necesarias:
```bash
pip install -r requirements.txt
```

**Contenido del `requirements.txt`**
```
PyPDF2
pdfplumber
PyMuPDF
```

## Uso

1. Coloca el archivo PDF que deseas procesar en el mismo directorio que el script.
2. Ejecuta el script "pdf_scrapper.py"
3. Sigue las instrucciones en la consola:
   - Ingresa el nombre del archivo PDF.
   - Decide si deseas extraer y guardar el texto, tablas e imágenes.

## Funcionalidades

- **Extracción de Texto**:  
  Se utiliza PyPDF2 para extraer el contenido textual de cada página del PDF.

- **Extracción de Tablas**:  
  Se emplea pdfplumber para detectar y extraer tablas presentes en el documento.

- **Extracción de Imágenes**:  
  Se utiliza PyMuPDF para extraer imágenes de cada página del PDF y guardarlas en una carpeta.

## Estructura del Proyecto

- `pdf_scrapper.py`: Script principal que contiene el código de extracción.
- `imagenes_extraidas/`: Carpeta donde se guardarán las imágenes extraídas (se crea automáticamente al ejecutar el script).

## Notas

- El script procesa PDFs con contenido textual nativo.
- Para PDFs escaneados, se recomienda utilizar OCR (por ejemplo, combinando `pdf2image` y `pytesseract`).
- La detección de tablas depende de la estructura del PDF.
- Si tienes sugerencias o encuentras algún problema, no dudes en abrir un issue en el repositorio.

## Licencia

Este proyecto está licenciado bajo los términos de la licencia MIT. Consulta el archivo [LICENSE](./LICENSE) para más detalles.

