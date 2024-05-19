import os
from PIL import Image
import tkinter as tk
from tkinter import filedialog, messagebox

# Función para convertir múltiples archivos seleccionados de WebP a PNG
def convertir_webp_a_png():
    # Abrir el cuadro de diálogo para seleccionar múltiples archivos de entrada
    archivos_entrada = filedialog.askopenfilenames(
        title="Selecciona archivos WebP",
        filetypes=(("WebP files", "*.webp"),)
    )
    
    if not archivos_entrada:
        messagebox.showwarning("Advertencia", "No se ha seleccionado ningún archivo.")
        return

    # Abrir el cuadro de diálogo para seleccionar la carpeta de exportación
    carpeta_exportacion = filedialog.askdirectory(
        title="Selecciona la carpeta de exportación"
    )
    
    if not carpeta_exportacion:
        messagebox.showwarning("Advertencia", "No se ha seleccionado ninguna carpeta de exportación.")
        return

    for archivo_entrada in archivos_entrada:
        try:
            # Cargar la imagen
            image = Image.open(archivo_entrada)
            
            # Obtener el nombre del archivo sin la extensión
            nombre_archivo = os.path.splitext(os.path.basename(archivo_entrada))[0]
            
            # Crear la ruta completa del archivo de salida
            archivo_salida = os.path.join(carpeta_exportacion, f"{nombre_archivo}.png")
            
            # Guardar la imagen en formato PNG
            image.save(archivo_salida, 'png')
            
            # Mostrar un mensaje de éxito
            print(f"Archivo {archivo_entrada} convertido con éxito a {archivo_salida}")
        except Exception as e:
            messagebox.showerror("Error", f"Se ha producido un error al convertir {archivo_entrada}: {e}")

    messagebox.showinfo("Conversión Completa", "Todos los archivos seleccionados se han convertido a formato PNG.")

# Crear la ventana principal
root = tk.Tk()
root.title("Convertidor de WebP a PNG")

# Configurar el botón para seleccionar archivos y convertir
btn_convertir = tk.Button(root, text="Seleccionar archivos y convertir a PNG", command=convertir_webp_a_png)
btn_convertir.pack(pady=20)

# Ejecutar el bucle principal de Tkinter
root.mainloop()
