######################################################
#       LABORATORIO 3 - BASE DE DATOS 2
#       AUTORES:
#           Eunice Mata......21231
#           Ricardo Chuy.....221007
#           Hector Penedo....22217
######################################################

from connection import get_neo_driver
from search import search_user, search_movie, search_person, search_person_movie, search_genre, search_all, search_relation
from neo import graph_exercise_2, graph_exersice_4

driver = get_neo_driver()

# menu
print("\n\n--------------------------------------------------\n|   Bienvenido al creador de Nodos de Neo4js     |\n--------------------------------------------------")
stay = True

while(stay):
    print("\n\n--------------------------------------------------")
    print("|                MENU PRINCIPAL                  |")
    print("--------------------------------------------------")
    print("|   Seleccione una de las siguientes opciones    |")
    print("--------------------------------------------------")
    print("   1. Crear grafo del ejercicio 2")
    print("   2. Crear grafo del ejercicio 4")
    print("   3. Buscar en el grafo")
    print("   4. Listar todos los nodos")
    print("   5. Salir")
    op1 = input("   -> ")
    
    if op1 == "1":
        print("\n\n--------------------------------------------------")
        print("             CREANDO GRAFO DEL EJ 2")
        print("--------------------------------------------------")
        graph_exercise_2()

    elif op1 == "2":
        print("\n\n--------------------------------------------------")
        print("            CREANDO GRAFO DEL EJ 4")
        print("--------------------------------------------------")
        graph_exersice_4()

    elif op1 == "3":
        print("\n\n--------------------------------------------------")
        print("                BUSCAR EN EL GRAFO")
        print("--------------------------------------------------")
        print("        Seleccione la opción de búsqueda")
        print("--------------------------------------------------")
        print("   1. Encontrar un usuario")
        print("   2. Encontrar una persona")
        print("   3. Encontrar una película")
        print("   4. Encontrar un género")
        print("   5. Encontrar personas con relaciones a película")
        print("   6. Encontrar usuarios con relaciones a película")
        sub_op3 = input("   -> ")

        if sub_op3 == "1":
            print("Encontrar un usuario")
            userName = input("\nIngresa el nombre del usuario que deseas encontrar: ")
            search_user(driver, userName)

        elif sub_op3 == "2":
            print("Encontrar una persona")
            personName = input("\nIngresa el nombre de la persona que deseas encontrar: ")
            search_person(driver, personName)

        elif sub_op3 == "3":
            print("Encontrar una película")
            movieName = input("\nIngresa el nombre de la película que deseas encontrar: ")
            search_movie(driver, movieName)

        elif sub_op3 == "4":
            print("Encontrar un género")
            genreName = input("\nIngresa el nombre del género que deseas encontrar: ")
            search_genre(driver, genreName)

        elif sub_op3 == "5":
            print("Encontrar personas con relaciones a película")
            personName = input("\nIngresa el nombre de la persona que deseas encontrar: ")
            movieName = input("\nIngresa el nombre de la película relacionada con la persona ingresada: ")
            search_person_movie(driver, personName, movieName)

        elif sub_op3 == "6":
            print("Encontrar usuarios con relaciones a película")
            userName = input("\nIngresa el nombre del usuario que deseas encontrar: ")
            movieName = input("\nIngresa el nombre de la película relacionada con el usuario ingresado: ")
            search_person_movie(driver, userName, movieName)

        else:
            print("Opción no válida.")

    elif op1 == "4":
        print("\n\n--------------------------------------------------")
        print("                 LISTAR TODOS LOS NODOS")
        print("--------------------------------------------------")
        print("              Listar todos los nodos")
        print("--------------------------------------------------")
        search_all(driver)

    elif op1 == "5":
        print("Saliendo del programa. ¡Hasta luego!")
        stay = False

    else:
        print("Opción no válida. Por favor, intente de nuevo.")