import mysql.connector
from mysql.connector import errorcode

def generar_conexion(user,password,server,database, consulta):
    config={
        'user': user,
        'password': password,
        'host': server,
        'database': database
    }
    try:
        conexion = mysql.connector.connect(**config)
        if conexion and conexion.is_connected():
            cursor = conexion.cursor()
            cursor.execute(consulta)
            for registro in cursor:
                print(registro)
            conexion.close()
        else:
            print("Could not connect")
    
    except mysql.connector.Error as error:
        if error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Acceso denegado para el usuario o la contraseña")
        elif error.errno == errorcode.ER_BAD_DB_ERROR:
            print("Su base de datos NO existe")
        else:
            print(error)
    else:
        conexion.close()