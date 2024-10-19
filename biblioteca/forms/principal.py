from pathlib import Path
import tkinter as tk
from tkinter import Tk
from tkinter import ttk
from tkinter.ttk import Frame, Separator
from ttkbootstrap import Style
from PIL import Image, ImageTk
# from tkinter import font
from config import directorio_base #COLOR_BARRA_LATERAL, COLOR_BARRA_SUPERIOR, COLOR_CUERPO, COLOR_CURSOR_MENU, directorio_base
import utils.util_images as util_image
# import utils.util_ventana as util_ventana
from forms.listado_libros import FormularioLibros
from forms.info import FormularioInfo

class FormularioPrincipal(Tk):
    def __init__(self):
        super().__init__()
        
        self.logo = tk.PhotoImage(name='logo', file= directorio_base/'assets/images/icons/023-university.png')
        self.title('Gestión Biblioteca')
        self.estilo = Style(theme='darkly')
        self.contenedor_principal = ContenedorPrincipal()
        self.contenedor_principal.pack(fill='both', expand='yes')

class ContenedorPrincipal(Frame):
    def __init__(self):
        super().__init__()
        
        cabecera = ttk.Frame(self, padding=20)
        cabecera.grid(row=0, column=0, columnspan=3, sticky='ew')
        ttk.Label(cabecera, image= 'logo', style='header.TLabel').pack(side='left')
        texto_cabecera = ttk.Label(cabecera, text='Gestión Biblioteca', font=('TkDefaultFixed', 30), style='header.TLabel')
        texto_cabecera.pack(side='left', padx=10)
        Separator(bootstyle='secondary')
        
        barra_lateral = ttk.Frame(self)
        barra_lateral.grid(row=1, column=0, sticky='nsew')
        boton_libros = ttk.Button(barra_lateral, text='Libros', compound='top', style='dark-outline.TButton')
        boton_libros.pack(side='top', fill='both', ipadx=10, ipady=10)
        boton_prestamo = ttk.Button(barra_lateral, text='Préstamo', compound='top', style='dark-outline.TButton')
        boton_prestamo.pack(side='top', fill='both', ipadx=10, ipady=10)
        boton_lectores = ttk.Button(barra_lateral, text='Lectores', compound='top', style='dark-outline.TButton')
        boton_lectores.pack(side='top', fill='both', ipadx=10, ipady=10)
        boton_info = ttk.Button(barra_lateral, text='Información', compound='top', style='dark-outline.TButton')
        boton_info.pack(side='top', fill='both', ipadx=10, ipady=10)
        
        contenedor_principal = ttk.Notebook(self)
        contenedor_principal.grid(row=1, column=1, sticky='nsew', )

if __name__=="__main__":
    FormularioPrincipal().mainloop()

# class FormularioPrincipal(tk.Tk):
#     def __init__(self):        
    #     super().__init__()
    #     self.logo = util_image.controlar_imagen(directorio_base.joinpath("assets/images/hipercubo_logo.png"), (400,200))
    #     self.perfil = util_image.controlar_imagen(directorio_base.joinpath("assets/images/hipercubo_logo_circulo.png"), (100, 100))
    #     self.config_ventana()
    #     self.paneles()
    #     self.contenedor_superior()
    #     self.contenedor_lateral()
    #     self.cuerpo()
    
    # def config_ventana(self):
    #     self.title("Gestión Biblioteca")
    #     self.iconbitmap(directorio_base.joinpath("assets/images/hipercubo_logo.ico"))
    #     ancho, alto = 1000, 600
    #     util_ventana.centrar_ventana(self, ancho, alto)
    
    # def paneles(self):
    #     self.menu_superior = tk.Frame(self, bg= COLOR_BARRA_SUPERIOR, height= 50)
    #     self.menu_superior.pack(side= tk.TOP, fill= "both")
        
    #     self.menu_lateral = tk.Frame(self, bg= COLOR_BARRA_LATERAL, width= 150)
    #     self.menu_lateral.pack(side= tk.LEFT, fill= "both", expand= False)
        
    #     self.contenedor_principal = tk.Frame(self, bg= COLOR_CUERPO)
    #     self.contenedor_principal.pack(side= tk.RIGHT, fill= "both", expand= True)
    
    # def contenedor_superior(self):
    #     font_awesome = font.Font(family= "FontAwesome", size= 15)
        
    #     self.etiqueta_menu_superior = tk.Label(self.menu_superior, text= ("Biblioteca").upper())
    #     self.etiqueta_menu_superior.config(fg= "#fff", font=("Roboto", 15), bg= COLOR_BARRA_SUPERIOR, pady= 10, width= 15)
    #     self.etiqueta_menu_superior.pack(side= tk.LEFT)
        
    #     self.boton_menu_superior = tk.Button(
    #         self.menu_superior,
    #         text= "\uf109",
    #         font= font_awesome,
    #         command= self.toggle_panel,
    #         bd= 0,
    #         bg= COLOR_BARRA_SUPERIOR,
    #         fg= "white"
    #     )
    #     self.boton_menu_superior.pack(side= tk.LEFT)
        
    #     self.etiqueta_menu_superior = tk.Label(self.menu_superior, text= "baileytorch@hotmail.com")
    #     self.etiqueta_menu_superior.config(fg= "#fff", font=("Roboto", 10), bg= COLOR_BARRA_SUPERIOR, padx= 10, width= 20)
    #     self.etiqueta_menu_superior.pack(side= tk.RIGHT)
    
    # def contenedor_lateral(self):
    #     ancho_menu = 20
    #     alto_menu = 2
    #     font_awesome = font.Font(family= "FontAwesome", size= 15)
        
    #     self.etiqueta_perfil = tk.Label(self.menu_lateral, image=self.perfil, bg= COLOR_BARRA_LATERAL)
    #     self.etiqueta_perfil.pack(side= tk.TOP, pady= 10)
        
    #     self.boton_libros = tk.Button(self.menu_lateral)
    #     self.boton_perfil = tk.Button(self.menu_lateral)
    #     self.boton_imagen = tk.Button(self.menu_lateral)
    #     self.boton_info = tk.Button(self.menu_lateral)
    #     self.boton_configuracion = tk.Button(self.menu_lateral)
        
    #     configuracion_botones = [
    #         ("Libros", "\uf0db", self.boton_libros, self.abrir_form_libros),
    #         ("Perfil", "\uf007", self.boton_perfil, self.abrir_form_info),
    #         ("Imagen", "\uf03e", self.boton_imagen, self.abrir_form_info),
    #         ("Información", "\uf129", self.boton_info, self.abrir_form_info),
    #         ("Configuración", "\uf013", self.boton_configuracion, self.abrir_form_info)
    #     ]
        
    #     for texto, icono, boton, comando in configuracion_botones:
    #         self.configurar_botones_menu(boton, texto, icono, font_awesome, ancho_menu, alto_menu, comando)
            
    # def configurar_botones_menu(self, boton, texto, icono, font_awesome, ancho_menu, alto_menu, comando):
    #     boton.config(
    #         text= f" {icono} {texto}",
    #         anchor= "w",
    #         font= font_awesome,
    #         bd= 0,
    #         bg= COLOR_BARRA_LATERAL,
    #         fg= "white",
    #         width= ancho_menu,
    #         height= alto_menu,
    #         command= comando
    #     )
    #     boton.pack(side=tk.TOP)
    #     self.bind_hover_events(boton)
    
    # def bind_hover_events(self, boton):
    #     boton.bind("<Enter>", lambda event: self.on_enter(event, boton))
    #     boton.bind("<Leave>", lambda event: self.on_leave(event, boton))
    
    # def on_enter(self, evento, boton):
    #     boton.config(bg= COLOR_CURSOR_MENU, fg= "white")
    
    # def on_leave(self, evento, boton):
    #     boton.config(bg= COLOR_BARRA_LATERAL, fg= "white")
    
    # def toggle_panel(self):
    #     if self.menu_lateral.winfo_ismapped():
    #         self.menu_lateral.pack_forget()
    #     else:
    #         self.menu_lateral.pack(side=tk.LEFT, fill="y")
    
    # def cuerpo(self):
    #     label= tk.Label(self.contenedor_principal, image= self.logo, bg= COLOR_CUERPO)
    #     label.place(x= 0, y= 0, relwidth=1, relheight=1)
    
    # def abrir_form_info(self):
    #     FormularioInfo()
    
    # def abrir_form_libros(self):
    #     self.limpiar_panel(self.contenedor_principal)
    #     FormularioLibros(self.contenedor_principal)
        
    # def limpiar_panel(self, panel):
    #     for widget in panel.winfo_children():
    #         widget.destroy()