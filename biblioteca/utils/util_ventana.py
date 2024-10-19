def centrar_ventana(ventana, ancho, alto):
    ancho_pantalla = ventana.winfo_screenwidth()
    alto_pantalla = ventana.winfo_screenheight()
    x = int((ancho_pantalla/2) - (ancho/2))
    y = int((alto_pantalla/2) - (alto/2))
    return ventana.geometry(f"{ancho}x{alto}+{x}+{y}")