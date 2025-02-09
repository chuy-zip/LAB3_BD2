###########################################
#       LABORATORIO 3 - BASE DE DATOS 2
#       AUTORES:
#           Eunice Mata......21231
#           Ricardo Chuy.....221007
#           Héctor Penedo....22217
###########################################

from connection import get_neo_driver
from search import search_user, search_movie, search_person
from genre_creator import create_genre
from movie_creator import create_movie
from person_creator import create_person
from user_creator import create_user
from relation_creator import create_relation

driver = get_neo_driver()

def getInfo(property):
    return input(f"Porfavor ingrese la información {str(property)}: ")

# menu
print("\n\n--------------------------------------------------\n|   Bienvenido al creador de Nodos de Neo4js     |\n--------------------------------------------------")
stay = True

while(stay):
    print("\n\n--------------------------------------------------")
    print("|                MENU PRINCIPAL                  |")
    print("--------------------------------------------------")
    print("|   Seleccione una de las siguientes opciones    |")
    print("--------------------------------------------------")
    print("   1. Crear nodo")
    print("   2. Crear relación entre nodos")
    print("   3. Buscar en el grafo")
    print("   4. Listar todos los nodos")
    print("   5. Salir")
    op1 = input("   -> ")
    
    if op1 == "1":
        print("\n\n--------------------------------------------------")
        print("                 CREAR NODO")
        print("--------------------------------------------------")
        print("        Seleccione el tipo de nodo a crear")
        print("--------------------------------------------------")
        print("   1. Crear un nodo person")
        print("   2. Crear un nodo user")
        print("   3. Crear un nodo movie")
        print("   4. Crear un nodo genre")
        sub_op1 = input("   -> ")

        if sub_op1 == "1":
            print("Crear un nodo person")
            keyLoop = True
            labels = []
            attributes = {}

            while keyLoop:
                label = input("\nIngresa la(s) etiqueta(s) del nodo. Escribe 'Salir' para terminar: ")
                if label.lower() != "salir":
                    labels.append(label)

                else:
                    keyLoop = False

            keyLoop = True
            while keyLoop:
                dictionaryKey = input("\nIngresa el nombre del atributo. Escribe 'Salir' para terminar: ")

                if dictionaryKey.lower() != 'salir':
                    dictionaryValue = input("\nIngresa el valor del atributo: ")
                    try:
                        attributes[dictionaryKey.lower()] = int(dictionaryValue)
                    except ValueError:
                        try:
                            attributes[dictionaryKey.lower()] = float(dictionaryValue)
                        except ValueError:
                            attributes[dictionaryKey.lower()] = dictionaryValue

                    print(attributes)

                else:
                    keyLoop = False

            create_person(driver, labels, attributes)
            
        elif sub_op1 == "2":
            print("Crear un nodo user")
            keyLoop = True
            label = "User"
            attributes = {}

            keyLoop = True
            while keyLoop:
                dictionaryKey = input("\nIngresa el nombre del atributo. Escribe 'Salir' para terminar: ")

                if dictionaryKey.lower() != 'salir':
                    dictionaryValue = input("\nIngresa el valor del atributo: ")
                    try:
                        attributes[dictionaryKey.lower()] = int(dictionaryValue)
                    except ValueError:
                        try:
                            attributes[dictionaryKey.lower()] = float(dictionaryValue)
                        except ValueError:
                            attributes[dictionaryKey.lower()] = dictionaryValue

                    print(attributes)

                else:
                    keyLoop = False

            create_user(driver, attributes)

        elif sub_op1 == "3":
            print("Crear un nodo movie")
            keyLoop = True
            label = "User"
            attributes = {}

            keyLoop = True
            while keyLoop:
                dictionaryKey = input("\nIngresa el nombre del atributo. Escribe 'Salir' para terminar: ") # Utilizar 'name' en lugar de 'title'

                if dictionaryKey.lower() != 'salir':
                    dictionaryValue = input("\nIngresa el valor del atributo: ")
                    try:
                        attributes[dictionaryKey.lower()] = int(dictionaryValue)
                    except ValueError:
                        try:
                            attributes[dictionaryKey.lower()] = float(dictionaryValue)
                        except ValueError:
                            attributes[dictionaryKey.lower()] = dictionaryValue

                    print(attributes)

                else:
                    keyLoop = False

            create_movie(driver, attributes)

        elif sub_op1 == "4":
            print("Crear un nodo genre")
            label = "Genre"

            name = input("\nIngresa el nombre del género: ")

            create_genre(driver, name)

        else:
            print("Opción no válida.")

    elif op1 == "2":
        print("\n\n--------------------------------------------------")
        print("            CREAR RELACIÓN ENTRE NODOS")
        print("--------------------------------------------------")
        print("          Seleccione el tipo de relación")
        print("--------------------------------------------------")
        print("   1. Rating (user - movie)")
        print("   2. Directed (person - movie)")
        print("   3. Acted in (person - movie)")
        print("   4. In genre (movie - genre)")
        sub_op2 = input("   -> ")

        if sub_op2 == "1":
            print("Rating (user - movie)")
            # Aquí iria la funcion para crear la relación Rating
        elif sub_op2 == "2":
            print("Directed (person - movie)")
            # Aquí iria la funcion para crear la relación Directed
        elif sub_op2 == "3":
            print("Acted in (person - movie)")
            # Aquí iria la funcion para crear la relación Acted in
        elif sub_op2 == "4":
            print("In genre (movie - genre)")
            # Aquí iria la funcion para crear la relación In genre
        else:
            print("Opción no válida.")

    elif op1 == "3":
        print("\n\n--------------------------------------------------")
        print("                BUSCAR EN EL GRAFO")
        print("--------------------------------------------------")
        print("        Seleccione la opción de búsqueda")
        print("--------------------------------------------------")
        print("   1. Encontrar un usuario")
        print("   2. Encontrar una película")
        print("   3. Encontrar usuarios con relaciones a película")
        sub_op3 = input("   -> ")

        if sub_op3 == "1":
            print("Encontrar un usuario")
            # Aquí iria la funcion para buscar un usuario
        elif sub_op3 == "2":
            print("Encontrar una película")
            # Aquí iria la funcion para buscar una película
        elif sub_op3 == "3":
            print("Encontrar usuarios con relaciones a película")
            # Aquí iria la funcion para buscar peliculas relacionados a un usuarip
        else:
            print("Opción no válida.")

    elif op1 == "4":
        print("\n\n--------------------------------------------------")
        print("                 LISTAR TODOS LOS NODOS")
        print("--------------------------------------------------")
        print("              Listar todos los nodos")
        print("--------------------------------------------------")
        # Aquí iria la funcion para listar todos los nodos

    elif op1 == "5":
        print("Saliendo del programa. ¡Hasta luego!")
        stay = False

    else:
        print("Opción no válida. Por favor, intente de nuevo.")
