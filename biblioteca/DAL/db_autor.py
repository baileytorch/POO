from datetime import datetime
import mysql.connector
from prettytable import from_db_cursor
from clases.autor import Autor as aut

def generar_conexion(servidor, usuario, contrasena, base_datos):
    config = {
        'host': servidor,
        'user': usuario,
        'password': contrasena,
        'database': base_datos
    }
    conexion = mysql.connector.connect(**config)
    return conexion

def listado_autores(servidor, usuario, contrasena, base_datos):
    conexion = generar_conexion(servidor, usuario, contrasena, base_datos)
    cursor = conexion.cursor()
    cursor.execute(f"""
        SELECT 
            A.nombre_autor 'Nombre Autor',
            A.seudonimo_autor 'Seudónimo',
            P.gentilicio_pais 'Nacionalidad',
            DATE_FORMAT(A.fecha_nac, '%d/%m/%Y') 'Fecha Nacimiento',
            DATE_FORMAT(A.fecha_def, '%d/%m/%Y') 'Fecha Defunción'
        FROM autor A
        JOIN paises P ON A.codigo_pais = P.codigo_pais
        """)

    tabla = from_db_cursor(cursor)
    print(tabla)                    
    cursor.close()
    conexion.close()

def obtener_autor_seudonimo(servidor, usuario, contrasena, base_datos, seudonimo):
    conexion = generar_conexion(servidor, usuario, contrasena, base_datos)
    cursor = conexion.cursor()
    cursor.execute(f"""
        SELECT 
            A.nombre_autor 'Nombre Autor',
            A.seudonimo_autor 'Seudónimo',
            P.gentilicio_pais 'Nacionalidad',
            DATE_FORMAT(A.fecha_nac, '%d/%m/%Y') 'Fecha Nacimiento',
            DATE_FORMAT(A.fecha_def, '%d/%m/%Y') 'Fecha Defunción'
        FROM autor A
        JOIN paises P ON A.codigo_pais = P.codigo_pais
        WHERE A.seudonimo_autor LIKE '%{seudonimo}%'
        """)
    
    tabla = from_db_cursor(cursor)
    print(tabla)                    
    cursor.close()
    conexion.close()

def crear_autor(user, password, server, database, autor:aut):
    id_autor = 0
    conexion = generar_conexion(user, password, server, database)
    
    sql_agregar_autor = ("INSERT INTO autor "
               "(nombre_autor, seudonimo_autor, fecha_nac, fecha_def) "
               "VALUES (%s, %s, %s, %s)")
    data_autor = (autor.nombre_autor, autor.seudonimo_autor, autor.fecha_nac, autor.fecha_def)
    
    cursor = conexion.cursor()
    cursor.execute(sql_agregar_autor, data_autor)
    if cursor.rowcount > 0:
        id_autor = cursor.lastrowid
        print(f"Autor con ID: {id_autor} agregado correctamente.")
    else:
        print("No ha sido posible agregar al autor")
    conexion.commit()                
    cursor.close()
    conexion.close()
    obtener_autor_por_id(user, password, server, database, id_autor)
        
def obtener_autor_por_id(servidor, usuario, contrasena, base_datos, id_autor):
    conexion = generar_conexion(servidor, usuario, contrasena, base_datos)
    
    sql_obtener_autor = ("SELECT "
               "A.nombre_autor 'Nombre Autor', A.seudonimo_autor 'Seudónimo', P.gentilicio_pais 'Nacionalidad', "
               "DATE_FORMAT(A.fecha_nac, '%d/%m/%Y') 'Fecha Nacimiento', DATE_FORMAT(A.fecha_def, '%d/%m/%Y') 'Fecha Defunción' "
               "FROM autor A JOIN paises P ON A.codigo_pais = P.codigo_pais "
               f"WHERE A.id_autor = {id_autor}")
    
    cursor = conexion.cursor()
    cursor.execute(sql_obtener_autor)
    
    tabla = from_db_cursor(cursor)
    print(tabla)                    
    cursor.close()
    conexion.close()
    
