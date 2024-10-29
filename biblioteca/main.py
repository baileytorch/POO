from datetime import datetime
# from pathlib import Path
# from tkinter import *
# from tkinter import ttk
# from tkinter import messagebox
# from tkinter import scrolledtext
# import tkinter as tkn
from DAL.db import generar_conexion
from DAL.consultas_sql import consulta_1, consulta_3
from DAL.db_autor import listado_autores, crear_autor
#from clases.autor import Autor

print("""
    Seleccione su Opción:
    1.- Consultar Libros
    2.- Consultar Editoriales
    3.- Consultar Autores
    """)
accion = input("Ingresa su opción: ")

if accion == '1':
    generar_conexion('root','','localhost','biblioteca', consulta_1())
elif accion == '2':
    generar_conexion('root','','localhost','biblioteca', consulta_1())
elif accion == '3':
    pass
else:
    print("Saliendo del sistema...")

# Para hace una instancia de clase
# objeto = MiClase()