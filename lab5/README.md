# Laboratorio 5: Manipulación de Imágenes en Python

## Descripción
Este proyecto corresponde al Laboratorio 5 del curso IE-0117 - Programación Bajo Plataformas Abiertas de la Universidad de Costa Rica. El objetivo es implementar la manipulación de imágenes utilizando diferentes bibliotecas en Python, con un enfoque en el diseño modular del programa.

### Participantes del proyecto y datos del curso:
- Universidad de Costa Rica
- Facultad de Ingeniería
- Escuela de Ingeniería Eléctrica
- IE-0117 - Programación Bajo Plataformas Abiertas
- II ciclo 2023
- Laboratorio 05: Manipulación de imágenes usando lenguaje de programación Python
- Participantes:
  - Dilana Rodríguez Jiménez (Carne C06660)
  - Kryssia Martínez Martínez (Carne B84636)
- Profesora: Carolina Trejos
- Fecha: 21 de Noviembre del 2023

## Estructura de Carpetas
El proyecto tiene la siguiente estructura de carpetas:
lab5/
├── biblioteca/
│ ├── OpenCV_module.py
│ └── PIL_module.py
├── imagenes/
│ └── imagen.jpg
├── main.py
└── README.md
## Diagrama de Diseño
Aqui se incluyo un diagrama de diseño creado en draw.io el cual se incluyo en el repositorio y ademas adjuntamos el link de drive. 

https://drive.google.com/file/d/1v9nACPrvrM_7R6o6JTYocS426lbZ6m5O/view?usp=sharing

## Dependencias del Proyecto
Este proyecto requiere las siguientes bibliotecas de Python:
- `Pillow` (PIL): Para manejar imágenes con la biblioteca PIL.
- `opencv-python`: Biblioteca OpenCV para el procesamiento de imágenes.

### Instalación de Dependencias:
```bash
pip install Pillow
pip install opencv-python

## Instrucciones de Uso
El programa se ejecuta desde la línea de comandos. Para utilizarlo, se siguen los siguientes pasos:

1.Ejecutar main.py desde la terminal especificando la biblioteca y la ruta de la imagen a procesar.

Ejemplo utilizando PIL:
python main.py --biblioteca PIL --imagen imagenes/imagen.jpg

Ejemplo utilizando OpenCV:
python main.py --biblioteca OpenCV --imagen imagenes/imagen.jpg

##Notas adicionales
Para este laboratorio se requirio informacion acerca de las bibliotecas a utilizar, adicional a eso se agrego una estructura modular que funciona de manera ordenada, se probo el programa en la maquina virtual y en VSCODE por lo cual funciona con la imagen guardada en la carpeta de imagenes segun lo esperado. 


