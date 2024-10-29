from datetime import datetime
from DAL.db_autor import listado_autores as lista_autores, obtener_autor_seudonimo as autor_seudonimo
from auxiliares.constantes import servidor_db_biblioteca as servidor,  usuario_db_biblioteca as usuario, contrasena_db_biblioteca as contrasena, db_biblioteca as base_datos
from clases.autor import Autor

def manejo_autor():
        print("""
        Seleccione su Opción:
        1.- Listado Autores
        2.- Buscar Autor por Seudónimo
        3.- Agregar Autor
        """)
        
        accion_autor = input("Ingresa su opción: ")
        if accion_autor == '1':
            obtener_listado_autores()
        elif accion_autor == '2':
            buscar_autor_seudonimo()
        elif accion_autor == '3':
            crear_autor()
        else:
            print("Acción seleccionada es incorrecta")

def obtener_listado_autores():
    lista_autores(servidor, usuario, contrasena, base_datos)

def buscar_autor_seudonimo():
    seudonimo = input("Seudónimo Autor:")
    autor_seudonimo(servidor, usuario, contrasena, base_datos, seudonimo)

def crear_autor():
    nuevo_autor = Autor()
    print("Ingrese los datos del Autor")
    nuevo_autor.nombre_autor = input("Nombre Autor: ")
    nuevo_autor.seudonimo_autor = input("Seudónimo Autor: ")
    fecha_nac = input("Fecha Nacimiento: ")
    fecha_nac_dt = datetime.strptime(fecha_nac, '%d/%m/%Y')
    nuevo_autor.fecha_nac = fecha_nac_dt.strftime('%Y-%m-%d')
    fecha_def = input("Fecha Defunción: ")
    fecha_def_dt = datetime.strptime(fecha_def, '%d/%m/%Y')
    nuevo_autor.fecha_def = fecha_def_dt.strftime('%Y-%m-%d')
    pass