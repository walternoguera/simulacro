import sqlite3
import json
from xml.etree.ElementTree import Element, SubElement, ElementTree

def obtener_estructura_bd(nombre_bd):
    conexion = sqlite3.connect(nombre_bd)
    cursor = conexion.cursor()

    # Obtener los nombres de las tablas
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tablas = [tabla[0] for tabla in cursor.fetchall()]

    estructura = {}

    for tabla in tablas:
        # Obtener los nombres de los campos de cada tabla
        cursor.execute(f"PRAGMA table_info({tabla});")
        campos = [campo[1] for campo in cursor.fetchall()]
        estructura[tabla] = campos

    conexion.close()
    return estructura

def guardar_estructura_en_json(estructura, archivo):
    with open(archivo, "w") as f:
        json.dump(estructura, f, indent=4)

def guardar_estructura_en_xml(estructura, archivo):
    root = Element("estructura")
    for tabla, campos in estructura.items():
        tabla_element = SubElement(root, "tabla", nombre=tabla)
        for campo in campos:
            SubElement(tabla_element, "campo", nombre=campo)
    
    tree = ElementTree(root)
    tree.write(archivo, encoding="utf-8", xml_declaration=True)

def main(nombre_bd, formato):
    estructura = obtener_estructura_bd(nombre_bd)
    if formato == "json":
        guardar_estructura_en_json(estructura, "estructura_bd.json")
    elif formato == "xml":
        guardar_estructura_en_xml(estructura, "estructura_bd.xml")
    else:
        print("Formato no válido. Por favor, elige 'json' o 'xml'.")

if __name__ == "__main__":
    nombre_bd = "agenda.sqlite"  # Nombre de tu base de datos
    formato = "xml"  # Formato deseado ('json' o 'xml')
    main(nombre_bd, formato)
