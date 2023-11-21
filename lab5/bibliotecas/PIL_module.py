from PIL import Image

def mostrar_imagen(ruta):
    try:
        imagen = Image.open(ruta)
        imagen.show()
    except FileNotFoundError:
        print("Archivo no encontrado.")
    except IOError:
        print("Error al abrir la imagen.")

