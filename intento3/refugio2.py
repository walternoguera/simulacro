'''campo de la tabla nombre  raza  clase  edad  disponible

Primero mostramos el menu
Atrapamos la opción que ha seleccionado el usuario
Si ha elegido listar, muestrame el contenido del archivo de datos
Si ha elegido buscar, muestrame solo las entradas que coincidan
Si ha elegido insertar, pregunta los datos e inserta
Si ha elegido actualizar, pregunta cual se va a actualizar, pregunta datos, y reemplaza
Si ha elegido eliminar, pregunta criterio y elimina
Si ha elegido salir, sal'''

import sqlite3 as lite
import sys

def db(query,params=()):
    conexion = lite.connect("refugio.sqlite")
    cursor = conexion.cursor()
    cursor.execute(query,params)
    resultado = cursor.fetchall()
    conexion.commit()
    conexion.close()
    return resultado

def listar():
    resultado = db("SELECT * FROM animales")
    for i in resultado:
        print("Id:",i[0],"\tNombre:",i[1],"\tRaza:",i[2],"\tClase:",i[3],"\tEdad:",i[4],"\tDisponible:",i[5])

def buscar():
    buscar = input("Que nombre quieres buscar:")
    resultado = db("SELECT * FROM animales WHERE nombre = '"+buscar+"';")
    if not resultado:
        print("No existen coincidencia")
    else:
        for i in resultado:
            print(i)
def insertar():
    nombre = input("nombre:")
    raza = input("raza:")
    clase = input("clase:")
    edad = input("edad:")
    disponible = input("disponible:")
    resultado = db("INSERT INTO animales (nombre, raza, clase, edad, disponible) VALUES (?, ?, ?, ?, ?);",
                   (nombre, raza, clase, edad, disponible))
    print("Se añadieron nuevos registros.\n")

def actualizar():
    print(db("SELECT * FROM animales"))
    identificador = input("Escribe el identificador del registro que quieras modificar:")
    if not identificador:
        print("Identificador no encontrado")
    else:
        nombre = input("nombre:")
        raza = input("raza:")
        clase = input("clase:")
        edad = input("edad:")
        disponible = input("disponible:")

        cambio = db("UPDATE animales SET nombre = ?, raza = ?, clase = ?, edad = ?, disponible = ? WHERE identificador = ?;",
                (nombre, raza, clase, edad, disponible, identificador))
        print("cambios añadidos")
def eliminar():
    nombre = input("Escribe el nombre del registro que quieras eliminar:")
    cambio = db("DELETE FROM animales WHERE nombre = ?;",(nombre,))
    print("Registro eliminado.")

    
def menu():
    opcion = input("Elige a una de las opciones:\n"+"1.-Listar:\n"+
                   "2.-Buscar:\n"+
                   "3.-Insertar:\n"+
                   "4.-Actualizar:\n"+
                   "5.-Eliminar:\n"+
                   "6.-Salir:\n")
    if opcion == "1":
        listar()
    elif opcion == "2":
        buscar()
    elif opcion == "3":
        insertar()
    elif opcion == "4":
        actualizar()
    elif opcion == "5":
        eliminar()
    elif opcion == "6":
        print("Salimos.")
        sys.exit()
    menu()
menu()
    
