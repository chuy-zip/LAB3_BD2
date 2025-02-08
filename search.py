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

def search_movie(driver, movie_title:str):
    records, summary, keys = driver.execute_query(
        "MATCH (n:Movie) WHERE n.title = $q_title RETURN n",
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
    records, summary, keys = driver.execute_query(
        "MATCH (p:User)-[r]->(m:Movie) WHERE n.name = $q_name RETURN r",
        q_name=person_name,
        database_="neo4j"
    )

    if not records:
        print(f"No user found with the name '{person_name}'.")
        return None

    relations = []
    for record in records:
        relation_node = record["r"]  
        relations.append(relation_node) 

    print(f"Found {len(relations)} relation(s) related to the name '{person_name}'.")
    for relation in relations:
        print(f"{relation}")
    return relations    

def search_user_movie(driver, person_name: str, movie_title: str) -> list:
    """
    Function that searches the relations between a person and a movie. Both of them are given by the user.

    Args:
        driver (driver): driver
        person_name (string): The person's name
        movie_title (string): The movie's title 

    Returns:
        (list): A list containing the whole relations.
    """

    records, summary, keys = driver.execute_query(
        "MATCH (p:User)-[r]->(m:Movie) WHERE p.name = $q_name AND m:title = $q_title RETURN p, r, m",
        q_name = person_name,
        q_title = movie_title,
        database = "neo4j"
    )

    if not records:
        print(f"No relationships found between '{person_name}' and '{movie_title}'.")
        return None
    
    relations = []
    for record in records:
        user_node = record["p"]
        movie_node = record["m"]
        relation_node = record["r"]
        relations.append(user_node)
        relations.append(relation_node)
        relations.append(movie_node)

    print(f"Found {len(relations)/3} relation(s) between '{person_name}' and '{movie_title}'.")
    return relations