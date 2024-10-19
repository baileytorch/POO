import tkinter as tk
import utils.util_ventana as util_ventana
from config import directorio_base

class FormularioInfo(tk.Toplevel):
    def __init__(self) -> None:
        super().__init__()
        self.config_ventana()
        self.control_Widget()
    
    def config_ventana(self):
        self.title('Gestión Biblioteca: Info')
        self.iconbitmap(directorio_base.joinpath("assets/images/hipercubo_logo.ico"))
        ancho, alto = 400, 200
        util_ventana.centrar_ventana(self, ancho, alto)
        
    def control_Widget(self):
        self.etiqueta_version = tk.Label(self, text="Versión 1.0")
        self.etiqueta_version.config(
            fg= "#000000",
            font=("Roboto", 15),
            pady=15,
            width= 20
        )
        self.etiqueta_version.pack()
    
        self.etiqueta_autor = tk.Label(self, text="Autor: Erick Bailey R.")
        self.etiqueta_autor.config(
            fg= "#000000",
            font=("Roboto", 15),
            pady= 10,
            width= 20
        )
        self.etiqueta_autor.pack()