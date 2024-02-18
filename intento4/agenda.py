import sqlite3 as lite

def db(query):
    conexion = lite.connect('agenda.sqlite')
    cursor = conexion.cursor()
    cursor.execute(query)
    resultado = cursor.fetchall()
    conexion.close()
    return resultado

def menu():
    opcion = input("elige una opcion de agenda:\n"+"1.listar\n"+
                   "2.insertar")
    if opcion == "1":
        resultado = db("SELECT * FROM usuarios")
        print(resultado)
menu()