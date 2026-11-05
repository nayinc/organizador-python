# importacionn de librerias
import os
import shutil # libreria para mover archivos

ruta = r"C:\Users\Naiara\Downloads"  # ruta de la carpeta a organizar
archivos = os.listdir(ruta)

print("Archivos en la carpeta:", archivos)


# diccionario
categorias = {
    ".py": "Scripts de Python",
    ".txt": "Archivos de texto",
    ".jpg": "Imágenes JPEG",
    ".png": "Imágenes PNG",
    ".exe": "Archivos ejecutables",
    ".pdf": "Documentos PDF",
    ".zip": "Archivos comprimidos",
}

# bucle
for archivo in archivos:
    ruta_origen = os.path.join(ruta, archivo)

    if os.path.isdir(ruta_origen):
        continue

    if archivo == "main.py" or archivo == ".git":
        continue

    # obtener la extensión del archivo
    extension = os.path.splitext(archivo)[1]
    categoria = categorias.get(extension, "Otros")
    print(f"Archivo: {archivo} | Categoría: {categoria}")

    ruta_carpeta = os.path.join(ruta, categoria)
    if not os.path.exists(ruta_carpeta):
        os.makedirs(ruta_carpeta)
        print(f"Carpeta creada: {ruta_carpeta}")

    ruta_destino = os.path.join(ruta_carpeta, archivo)
    shutil.move(ruta_origen, ruta_destino)