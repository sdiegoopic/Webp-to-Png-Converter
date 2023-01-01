import os
import glob
from PIL import Image
import tkinter as tk
from tkinter import messagebox

# Función para convertir archivos webp a png
def convertir_webp_a_png():
  # Obtener una lista de todos los archivos con extensión .webp en la carpeta actual
  archivos = glob.glob('*.webp')

  # Bucle para iterar sobre cada nombre de archivo
  for archivo in archivos:
    # Cargar la imagen webp en una imagen de PIL
    image = Image.open(archivo)

    # Convertir la imagen a png y guardarla en un archivo
    nombre, extension = os.path.splitext(archivo)
    image.save(f'{nombre}.png', 'png')

    # Mostrar un mensaje de éxito
    print(f'Archivo {archivo} convertido con éxito')

# Crear una ventana emergente con un botón de "OK"
resultado = messagebox.askokcancel("Convertidor de WebP a PNG", "¿Quieres convertir todos los archivos WebP en la carpeta actual a formato PNG?")

# Si el usuario pulsa "OK", ejecutar la función de conversión
if resultado:
  convertir_webp_a_png()