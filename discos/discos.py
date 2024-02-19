'''Pseudocodigo
MODELO DE DATOS DE BBDD: artista, anio, titulo'''



def menu():
    opcion = input("Elige a una de las opciones:\n"+"1.-Listar:\n"+
                   "2.-Buscar.\n"+
                   "3.-Insertar.\n"+
                   "4.-Actualizar.\n"+
                   "5.-Eliminar.\n"+
                   "6.-Salir.\n"+
                   "prompt$ ")
    menu() #ejecutamos el menú de forma recursiva
menu()
