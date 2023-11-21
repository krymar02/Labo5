# main.py

import argparse
import PIL_module
import OpenCV_module

def parse_args():
    parser = argparse.ArgumentParser(description="Procesamiento de Imagenes")
    parser.add_argument("--biblioteca", choices=["PIL", "OpenCV"], required=False, help="Biblioteca para procesamiento de imagenes (PIL o OpenCV)")
    parser.add_argument("--imagen", required=False, help="Ruta de la imagen a procesar")
    return parser.parse_args()

def main():
    args = parse_args()

    if not args.biblioteca:
        args.biblioteca = input("Seleccione una biblioteca (PIL o OpenCV): ")

    if not args.imagen:
        args.imagen = input("Ingrese la ruta de la imagen a procesar: ")

    if args.biblioteca == 'PIL':
        try:
            PIL_module.mostrar_imagen(args.imagen)
        except Exception as e:
            print(f"Error al procesar la imagen con PIL: {e}")
    elif args.biblioteca == 'OpenCV':
        try:
            OpenCV_module.mostrar_imagen(args.imagen)
        except Exception as e:
            print(f"Error al procesar la imagen con OpenCV: {e}")
    else:
        print("Biblioteca no valida. Selecciona PIL o OpenCV.")

if __name__ == "__main__":
    main()

