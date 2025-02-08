from connection import get_neo_driver

def create_genre(driver, name: str) -> None:
    """
    Creates or updates a Genre node and prints a success message in the end.

    Args:
        driver (driver?): driver (?).
        name (string): The genre name.
    """
    label = "Genre"

    query = f"MERGE (m:{label} {{name:$genre_name}} )"

    print(label)
    print(name)

    records, summary, keys = driver.execute_query(
        query,
        genre_name=name,
        database="neo4j"
    )

    print(f"Created/updated node with label: {label} and properties: {name}")

#driver = get_neo_driver()

#create_genre(driver, "Action") # Ejemplo de implementación