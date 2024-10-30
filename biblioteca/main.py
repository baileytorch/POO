from datetime import datetime
from DAL.db import generar_conexion
from DAL.consultas_sql import consulta_1, consulta_3
from interfaces.interfase_autor import manejo_autor

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
    manejo_autor()
else:
    print("Saliendo del sistema...")