import sqlite3 as lite

conexion = lite.connect('agenda.sqlite')
cursor = conexion.cursor()
cursor.execute("SELECT * FROM usuarios;")
resultado = cursor.fetchall()
conexion.close()

print(resultado)