#importamos librerias
import sqlite3 as lite

# Primero mostramos el menu
print("Agenda - por Walter Morel(c)")

# definimos funciones
def consulta(query):
    conexion = lite.connect("agenda.sqlite")
    cursor = conexion.cursor()
    cursor.execute(query)
    datos = cursor.fetchall()
    return datos
#funciones CRUD
def listar(tabla):
    resultado = consulta("SELECT * FROM " + tabla + ";")
    for i in resultado:
        print("id",i[0],"\tnombre",i[1],"\tcontraseña",i[2],"\tapodo",i[3],"\tapellidos",i[4],"\temail",i[5],"\ttelefono",i[6])

def buscar(nombre,tabla):
    resultado = consulta("SELECT * FROM " + tabla + " WHERE nombre = '" + nombre + "';")
    return resultado

def insertar(datos, tabla):
    query = f"INSERT INTO "+tabla+" VALUES (NULL, ?, ?, ?, ?, ?, ?);"
    consulta(query,datos)

def menu():
    # Atrapamos la opción que ha seleccionado el usuario
    opcion = input("Por favor, elige una opción:\n"+"1.-Listar\n"+
                   "2.-Buscar\n"+
                   "3.-Insertar\n"+
                   "4.-Actualizar\n"+
                   "5.-Eliminar\n"+
                   "6.-Salir\n")
    ##CRUD
    # Si ha elegido listar, muestrame el contenido del archivo de datos
    if opcion == "1":
        listar("usuarios")
    # Si ha elegido buscar, muestrame solo las entradas que coincidan
    elif opcion == "2":
        nombre = input("Que nombre quieres buscar?:")
        resultado = buscar(nombre, "usuarios")
        if resultado:
            print(resultado)
        else:
            print("no hay coincidencia")
        
    # Si ha elegido insertar, pregunta los datos e inserta
    elif opcion == "3":
        
    # Si ha elegido actualizar, pregunta cual se va a actualizar, pregunta datos, y reemplaza

    # Si ha elegido eliminar, pregunta criterio y elimina

    # Si ha elegido salir, sal
    menu()
menu()
