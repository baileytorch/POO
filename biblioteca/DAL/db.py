import mysql.connector

def usar_db(consulta_sql):
    conexion_db = mysql.connector.connect(
        host="localhost", 
        user="root", 
        passwd="",
        database="biblioteca"
        )
    
    cursor = conexion_db.cursor()
    cursor.execute(f"{consulta_sql}")
    # cursor.execute("SHOW DATABASES") # Comando usado para testear la conexión, OK
    for base in cursor:
        print(base)
    conexion_db.close()