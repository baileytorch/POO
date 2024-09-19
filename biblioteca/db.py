import mysql.connector

def usar_db(consulta_sql):
    conexion_db = mysql.connector.connect(host="localhost", user="root", passwd="")
    cursor1 = conexion_db.cursor()
    cursor1.execute(consulta_sql)
    for base in cursor1:
        print(base)
    conexion_db.close()