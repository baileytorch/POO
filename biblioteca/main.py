from pathlib import Path
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import scrolledtext
import tkinter as tkn
from DAL.db import generar_conexion
from DAL.consultas_sql import consulta_1, consulta_3

print("""
    Seleccione su Opción:
    1.- Consultar Libros
    2.- Consultar Editoriales
    3.- Consultar Autores por nombre
    """)
accion = input("Ingresa su opción: ")

if accion == '1':
    generar_conexion('root','','localhost','biblioteca', consulta_1())
elif accion == '2':
    generar_conexion('root','','localhost','biblioteca', consulta_1())
elif accion == '3':
    seudonimo = input("Seudónimo Autor:")
    generar_conexion('root','','localhost','biblioteca', consulta_3(seudonimo))
else:
    print("Saliendo del sistema...")

# Para hace una isntancia de clase
# objeto = MiClase()