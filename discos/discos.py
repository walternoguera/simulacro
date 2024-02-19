'''Pseudocodigo
MODELO DE DATOS DE BBDD: identificador, artista, anio, titulo'''

import sqlite3 as lite
import sys

def db(query,params=()):
    conexion = lite.connect("discos.sqlite")
    cursor = conexion.cursor()
    cursor.execute(query,params)
    resultado = cursor.fetchall()
    conexion.commit()
    conexion.close()
    return resultado

#funcion listar
def listar():
    resultado = db("SELECT * FROM discos;")
    for i in resultado:
        print("Identificador:",i[0],"\tArtista:",i[1],"\tAño:",i[2],"\tTitulo:",i[3])

#funcion buscar
def buscar():
    item = input("Que artista quieres buscar:")
    resultado = db("SELECT * FROM discos WHERE artista = ?;",(item,))
    if not resultado:
        print("No se encontraron coincidencias")
    else:
        print("El artista que buscas es")
        for i in resultado:
            print("Identificador:",i[0],"\tArtista:",i[1],"\tAño:",i[2],"\tTitulo:",i[3])
        

#funcion insertar
def insertar():
    artista = input("artista:")
    anio = input("año:")
    titulo = input("titulo:")

    resultado = db("INSERT INTO discos (artista, anio, titulo) VALUES (?, ?, ?);",
                   (artista, anio, titulo))
    print("Se añadieron nuevos registros")

#funcion actualizar
def actualizar():
    print(db("SELECT * FROM discos;\n"))
    item = input("Escribe el ID del registro que quieras modificar:")
    if not item:
        print("Escribe el identificador correcto")
    else:
        artista = input("artista:")
        anio = input("año:")
        titulo = input("titulo:")
        db("UPDATE discos SET artista = ?, anio = ?, titulo = ?;",(artista, anio, titulo))
        print("Cambios añadidos")
        
#funcion eliminar
def eliminar():
    print(db("SELECT * FROM discos;\n"))
    item = input("Escribe el ID del registro que quieras borrar:")
    if not item:
        print("Escribe el identificador correcto")
    else:
        db("DELETE FROM discos WHERE identificador = ?;",(item,))
        print("Registro eliminado")
        
    
def menu():
    opcion = input("Elige a una de las opciones:\n"+"1.-Listar:\n"+
                   "2.-Buscar.\n"+
                   "3.-Insertar.\n"+
                   "4.-Actualizar.\n"+
                   "5.-Eliminar.\n"+
                   "6.-Salir.\n"+
                   "prompt$ ")
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
        sys.exit()

    menu() #ejecutamos el menú de forma recursiva
menu()
