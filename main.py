# importacionn de librerias
import os


ruta = r"C:\Users\Naiara\Desktop\organizadorPython"
archivos = os.listdir(ruta)

print("Archivos en la carpeta:", archivos)


# diccionario
categorias = {
    ".py": "Scripts de Python",
    ".txt": "Archivos de texto",
    ".jpg": "Imágenes JPEG",
    ".png": "Imágenes PNG",
    ".exe": "Archivos ejecutables",
    ".pdf": "Documentos PDF"
}

# bucle
for archivo in archivos:
    if archivo == "main.py" or archivo == ".git":
        continue  # saltar el archivo main.py y la carpeta .git
    # extension
    extension = os.path.splitext(archivo)[1]
    print(f"Archivo: {archivo}, Extensión: {extension}")

    categoria = categorias.get(extension, "Otros")
    print(f"El archivo {archivo} con extensión {extension} pertenece a la categoría: {categoria}")
