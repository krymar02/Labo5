import cv2

def mostrar_imagen(ruta):
    try:
        imagen = cv2.imread(ruta)
        if imagen is not None:
            cv2.imshow('Imagen', imagen)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        else:
            print("Error al abrir la imagen. Asegúrate de que la ruta sea correcta.")
    except Exception as e:
        print(f"Error al procesar la imagen: {e}")

