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
