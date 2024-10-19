import tkinter as tk
import ttkbootstrap as ttk
from config import COLOR_CUERPO, COLOR_BARRA_SUPERIOR

class FormularioLibros():
    def __init__(self, panel_principal):
        self.barra_superior = tk.Frame(panel_principal, bg= COLOR_BARRA_SUPERIOR)
        self.barra_superior.pack(side= tk.TOP, fill= tk.X, expand= False)
        
        self.etiqueta_titulo = tk.Label(self.barra_superior, text= "Listado Libros")
        self.etiqueta_titulo.config(
            fg= "white",
            font=("Roboto", 15),
            bg= COLOR_CUERPO
        )
        self.etiqueta_titulo.pack(side= tk.TOP, fill= "both", expand= True)
        
        self.barra_inferior = tk.Frame(panel_principal)
        self.barra_inferior.pack(side= tk.TOP, fill= "both", expand= True)
        
        ttk.LabelFrame(bootstyle="secondary")