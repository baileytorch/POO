from datetime import datetime
import mysql.connector

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
            A.nombre_autor,
            A.seudonimo_autor,
            P.gentilicio_pais,
            A.fecha_nac,
            A.fecha_def
        FROM autor A
        JOIN paises P ON A.codigo_pais = P.codigo_pais
        """)
    
    print(f"Nombre    -    Sudónimo    -    Nacionalidad    -    Fecha Nacimiento    -    Fecha Defunción")
    print("""=============================================================================================""")
    for (nombre_autor,seudonimo_autor,gentilicio_pais,fecha_nac,fecha_def) in cursor:
        print(f"{nombre_autor} - {seudonimo_autor} - {gentilicio_pais} - {datetime.strftime(fecha_nac, '%d/%m/%Y')} - {datetime.strftime(fecha_def, '%d/%m/%Y')}")
        print("---------------------------------------------------------------------------------------------")
                    
    cursor.close()
    conexion.close()

def obtener_autor_seudonimo(servidor, usuario, contrasena, base_datos, seudonimo):
    conexion = generar_conexion(servidor, usuario, contrasena, base_datos)
    cursor = conexion.cursor()
    cursor.execute(f"""
        SELECT 
            A.nombre_autor,
            A.seudonimo_autor,
            P.gentilicio_pais,
            A.fecha_nac,
            A.fecha_def
        FROM autor A
        JOIN paises P ON A.codigo_pais = P.codigo_pais
        WHERE A.seudonimo_autor LIKE '%{seudonimo}%'
        """)
    
    for (nombre_autor,seudonimo_autor,gentilicio_pais,fecha_nac,fecha_def) in cursor:
        print(f"""
            Nombre: {nombre_autor}
            Seudónimo: {seudonimo_autor}
            Nacionalidad: {gentilicio_pais}
            Fecha de Nacimiento: {datetime.strftime(fecha_nac, '%d/%m/%Y')}
            Fecha de Defunción: {datetime.strftime(fecha_def, '%d/%m/%Y')}
        """)
                    
    cursor.close()
    conexion.close()

def crear_autor(user,password,server,database,autor):
    conexion = generar_conexion(user,password,server,database)
    cursor = conexion.cursor()
    cursor.execute(f"""
        INSERT INTO autor (nombre_autor,seudonimo_autor,codigo_pais) VALUES (
            'Federico De las Mercedew',
            'Quico',
            'AFG'
        )
        """)
