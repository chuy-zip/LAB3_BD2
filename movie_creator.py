from connection import get_neo_driver

def create_movie(driver, attributes: dict) -> None:
    """
    Creates or updates a Movie node and prints a success message in the end.

    Args:
        driver (driver?): driver (?).
        attributes (dictionary): A dictionary that contains the node's attributes.
    """
    label = "Movie"

    combined_attributes = ", ".join([f"{key}: $q_attributes.{key}" for key in attributes.keys()])

    query = f"MERGE (m:{label} {{{combined_attributes}}})"

    print(label)
    print(combined_attributes)

    records, summary, keys = driver.execute_query(
        query,
        q_attributes=attributes,
        database="neo4j"
    )

    print(f"Created/updated node with label: {label} and properties: {attributes}")

#driver = get_neo_driver()

#create_movie(driver, {"name": "Kingsman: The Secret Service", "year": 2015}) # Ejemplo de implementación

#P.D.: Si vi esa película jaja. Dejo la escena más divertida:
# https://youtu.be/90OFZQx_7xI?si=j28zEp963x3_zmJ4