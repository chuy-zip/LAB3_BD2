def print_node_properties(node_type: str, properties: dict):

    print(f"Propiedades del nodo tipo {node_type}: ")

    for prop, value in properties.items():

        print(f"- {prop}: {value}")
    print()



def search_user(driver, person_name:str):
    records, summary, keys = driver.execute_query(
        "MATCH (n:User) WHERE n.name = $q_name RETURN n",
        q_name=person_name,
        database_="neo4j"
    )

    if not records:
        print(f"No se encontro un usario con el nombre '{person_name}'.")
        return None

    users = []
    for record in records:
        user_node = record["n"]  
        users.append(user_node) 

    print(f"\nSe encontraron: {len(users)} nodo(s) 'User' con el nombre: '{person_name}'.")

    for user in users:
        print_node_properties("User", user._properties)
    return users

def search_person(driver, person_name:str):
    records, summary, keys = driver.execute_query(
        "MATCH (n:Person) WHERE n.name = $q_name RETURN n",
        q_name=person_name,
        database_="neo4j"
    )

    if not records:
        print(f"No se encontro una persona con el nombre '{person_name}'.")
        return None

    users = []
    for record in records:
        user_node = record["n"]  
        users.append(user_node) 

    print(f"\nSe encontraron: {len(users)} nodo(s) 'Person' con el nombre: '{person_name}'.")

    for user in users:
        print_node_properties("Person", user._properties)

    return users

def search_genre(driver, genre_name: str):
    records, summary, keys = driver.execute_query(
        "MATCH (g:Genre) WHERE g.name = $q_name RETURN g",
        q_name=genre_name,
        database_="neo4j"
    )

    if not records:
        print(f"No se encontro un genero con el nombre: '{genre_name}'.")
        return None

    genres = []
    for record in records:
        user_node = record["g"]  
        genres.append(user_node) 
    
    print(f"\nSe encontraron: {len(genres)} nodo(s) 'Genre' con el nombre: '{genre_name}'.")

    for genre in genres:
        print_node_properties("Genre", genres._properties)
    return genres

def search_movie(driver, movie_title:str):
    records, summary, keys = driver.execute_query(
        "MATCH (n:Movie) WHERE n.name = $q_title RETURN n",
        q_title=movie_title,
        database_="neo4j"
    )

    if not records:
        print(f"No se encontro una pelicula con el nombre:'{movie_title}'.")
        return None

    movies = []
    for record in records:
        user_node = record["n"]  
        movies.append(user_node) 
    
    print(f"\nSe encontraron: {len(movies)} nodo(s) 'Movie' con el nombre: '{movie_title}'.")
    
    for movie in movies:
        print_node_properties("Movie", movie._properties)

    return movies

def search_relation(driver, person_name: str) -> list:
    """
    Function that searches the relations between a given user and all the movies.

    Args:
        driver (driver): driver
        person_name: The person's name

    Returns:
        (list): A list containing the relations between the user and all the movies.
    """
    records, summary, keys = driver.execute_query(
        "MATCH (p:Person)-[r]->(m:Movie) WHERE p.name = $q_name RETURN m",
        q_name=person_name,
        database_="neo4j"
    )

    if not records:
        print(f"No se encontro una relacion con el nombre' {person_name}'.")
        return None

    relations = []
    for record in records:
        relation_node = record["m"]  
        relations.append(relation_node) 

    print(f"Se encontraron {len(relations)} relacion(es) relacionadas al nombre '{person_name}'.")
    for relation in relations:
        print(f"{relation}")
    return relations    

def search_person_movie(driver, person_name: str, movie_name: str) -> list:
    """
    Function that searches the relations between a person and a movie. Both of them are given.

    Args:
        driver (driver): driver
        person_name (string): The person's name
        movie_title (string): The movie's title 

    Returns:
        (list): A list containing the whole relations.
    """

    records, summary, keys = driver.execute_query(
        f"MATCH (u:Person)-[r]->(b:Movie) WHERE u.name = '{person_name}' AND b.name = '{movie_name}' RETURN r",
        q_name = person_name,
        q_title = movie_name,
        database = "neo4j"
    )

    if not records:
        print(f"No se encontraron relaciones entre '{person_name}' y '{movie_name}'.")
        return None
    
    relations = []
    for record in records:
        relation_node = record["r"]
        relations.append(relation_node)

    print(f"Found {len(relations)} relation(s):")
    for relation in relations:
        print(f"'{person_name}' {relation.type} '{movie_name}'")
    return relations

def search_user_movie(driver, user_name: str, movie_name: str) -> list:
    """
    Function that searches the relations between a user and a movie. Both of them are given.

    Args:
        driver (driver): driver
        user_name (string): The person's name
        movie_title (string): The movie's title 

    Returns:
        (list): A list containing the whole relations.
    """

    records, summary, keys = driver.execute_query(
        f"MATCH (u:User)-[r]->(b:Movie) WHERE u.name = '{user_name}' AND b.name = '{movie_name}' RETURN r",
        q_name = user_name,
        q_title = movie_name,
        database = "neo4j"
    )

    if not records:
        print(f"No se encontraron relaciones entre '{user_name}' y '{movie_name}'.")
        return None
    
    relations = []
    for record in records:
        relation_node = record["r"]
        relations.append(relation_node)

    print(f"Se encontraron {len(relations)} relacion(es):")
    for relation in relations:
        print(f"'{user_name}' {relation.type} '{movie_name}'")
    return relations

def search_all(driver) -> list:
    """
    Function that searches and returns all nodes.

    Args:
        driver (driver): driver

    Returns:
        (list): A list containing all nodes.
    """

    records = driver.execute_query(
        f"MATCH (n) RETURN n",
        database = "neo4j"
    )

    if not records:
        print(f"No nodes found.")
        return None

    nodes = []
    for record in records:
        nodes.append(record)

    print(f"Se encontraron {len(nodes)} nodo(s):")
    for node in nodes:
        print_node_properties("Todos", node._properties)
    return nodes