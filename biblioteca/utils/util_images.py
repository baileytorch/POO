from PIL import ImageTk, Image

def controlar_imagen(ruta,tamano,nombre):
    return ImageTk.PhotoImage(Image.open(ruta).resize(tamano, Image.ADAPTIVE))