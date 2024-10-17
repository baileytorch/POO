import mysql.connector

# Connect to server
cnx = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="",
    database="biblioteca")

# Get a cursor
cur = cnx.cursor()

# Execute a query
cur.execute("SELECT * FROM autor")

# Fetch one result
#row = cur.fetchone()
for filas in cur:
    print(filas)

# Close connection
cnx.close()