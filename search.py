def search_user(driver, person_name:str):
    records, summary, keys = driver.execute_query(
        "MATCH (n:User) WHERE n.name = $q_name RETURN n",
        q_name=person_name,
        database_="neo4j"
    )

    if not records:
        print(f"No user found with the name '{person_name}'.")
        return None

    users = []
    for record in records:
        user_node = record["n"]  
        users.append(user_node) 

    print(f"Found {len(users)} user(s) with the name '{person_name}'.")
    for user in users:
        print(f"{user._properties}")
    return users

def search_person(driver, person_name:str):
    records, summary, keys = driver.execute_query(
        "MATCH (n:Person) WHERE n.name = $q_name RETURN n",
        q_name=person_name,
        database_="neo4j"
    )

    if not records:
        print(f"No user found with the name '{person_name}'.")
        return None

    users = []
    for record in records:
        user_node = record["n"]  
        users.append(user_node) 

    print(f"Found {len(users)} person(people) with the name '{person_name}'.")
    for user in users:
        print(f"{user._properties}")
    return users

def search_genre(driver, genre_name: str):
    records, summary, keys = driver.execute_query(
        "MATCH (g:Genre) WHERE g.name = $q_name RETURN g",
        q_name=genre_name,
        database_="neo4j"
    )

    if not records:
        print(f"No genre found with the name '{genre_name}'.")
        return None

    genres = []
    for record in records:
        user_node = record["g"]  
        genres.append(user_node) 

    print(f"Found {len(genres)} genre(s) with the name '{genre_name}'.")
    for genre in genres:
        print(f"{genre._properties}")
    return genres

def search_movie(driver, movie_title:str):
    records, summary, keys = driver.execute_query(
        "MATCH (n:Movie) WHERE n.name = $q_title RETURN n",
        q_title=movie_title,
        database_="neo4j"
    )

    if not records:
        print(f"No movie found with the title '{movie_title}'.")
        return None

    movies = []
    for record in records:
        user_node = record["n"]  
        movies.append(user_node) 

    print(f"Found {len(movies)} user(s) with the name '{movie_title}'.")
    for user in movies:
        print(f"{user._properties}")
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
        print(f"No user found with the name '{person_name}'.")
        return None

    relations = []
    for record in records:
        relation_node = record["m"]  
        relations.append(relation_node) 

    print(f"Found {len(relations)} relation(s) related to the name '{person_name}'.")
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
        print(f"No relationships found between '{person_name}' and '{movie_name}'.")
        return None
    
    relations = []
    for record in records:
        relation_node = record["r"]
        relations.append(relation_node)

    print(f"Found {len(relations)} relation(s):")
    for relation in relations:
        print(f"'{person_name}' {relation.type} '{movie_name}'")
    return relations

def search_person_movie(driver, user_name: str, movie_name: str) -> list:
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
        print(f"No relationships found between '{user_name}' and '{movie_name}'.")
        return None
    
    relations = []
    for record in records:
        relation_node = record["r"]
        relations.append(relation_node)

    print(f"Found {len(relations)} relation(s):")
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
        nodes.append(record.keys)

    print(f"Found {len(nodes)} node(s):")
    for node in nodes:
        print(f"{node}")
    return nodes