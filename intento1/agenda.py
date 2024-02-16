#Intento 1, Agenda por Walter Morel
import sqlite3 as lite


#Definimos funciones
def consulta(consulta, parametros=None):
    conexion = lite.connect("agenda.sqlite")
    cursor = conexion.cursor()
    if parametros is not None:
        cursor.execute(consulta, parametros)
    else:
        cursor.execute(consulta)
    conexion.commit()
    datos = cursor.fetchall()
    cursor.close()
    conexion.close()
    return datos

def listar(tabla):
    resultado = consulta("SELECT * FROM " + tabla + ";")
    for i in resultado:
        print("id;",i[0],"\tNombre",i[1],"\tContraseña",i[2],"\tnombre propio",i[3],"\tApellido",i[4],"\temail",i[5],"\ttelefono",i[6])

def buscar(nombre):
    resultados = consulta("SELECT * FROM usuarios WHERE nombre = ?;", (nombre,))
    if resultados:
        print("Se encontraron los siguientes usuarios con el nombre:", nombre + ":")
        for i in resultados:
            print("id:", i[0], "\tNombre:", i[1], "\tContraseña:", i[2], "\tNombre propio:", i[3], "\tApellido:", i[4], "\tEmail:", i[5], "\tTeléfono:", i[6])
    else:
        print("No se encontraron usuarios con el nombre:", nombre)
            
def insertar(nombre, contrasena, nombrePropio, apellido, email, telefono, tabla):
    consulta("INSERT INTO " + tabla + " VALUES (NULL, ?, ?, ?, ?, ?, ?);", (nombre, contrasena, nombrePropio, apellido, email, telefono))
    

def menu():
    opcion = input("Elige una de las opciones:\n"+"1-Listar\n"+
                   "2-Buscar\n"+
                   "3-Insertar\n"+
                   "4-Actualizar\n"+
                   "5-Eliminar\n"+
                   "6-Salir\n")
    if opcion == "1":
        listar("usuarios")
        
    elif opcion == "2":
        nombre = input("ingresa el nombre a buscar:")
        buscar(nombre)
    elif opcion == "3":
        nombre = input("Ingresa el nombre:")
        contrasena = input("Ingresa la contraseña:")
        nombrePropio = input("Ingresa el nombre propio:")
        apellido = input("Ingresa el apellido:")
        email = input("Ingresa el email:")
        telefono = input("Ingresa el teléfono:")
        insertar(nombre, contrasena, nombrePropio, apellido, email, telefono, "usuarios")
    menu()
menu()
