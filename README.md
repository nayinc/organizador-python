# Organizador de Carpetas en Python

Un script ligero creado en Python para automatizar la limpieza de directorios caóticos (como la carpeta de Descargas o el Escritorio).

## ¿Qué hace?
Lee todos los archivos de una ruta específica, extrae su extensión y los clasifica moviéndolos automáticamente a subcarpetas ordenadas (Documentos, Imágenes, Scripts, etc.).

## Cómo usarlo
1. Abre `main.py` y modifica la variable `ruta` con el directorio que quieras organizar.
2. Ejecuta el script desde la terminal: ``python main.py``
3. Los archivos se moverán a sus respectivas carpetas.

## Tecnologías
- Python 3
- Librerías nativas: `os` y `shutil`