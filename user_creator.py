from connection import get_neo_driver

def create_user(driver, attributes: dict) -> None:
    """
    Creates or updates a User node and prints a success message in the end.

    Args:
        driver (driver?): driver (?).
        attributes (dictionary): A dictionary that contains the node's attributes.
    """
    label = "User"

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