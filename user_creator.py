from connection import get_neo_driver

def create_user(driver, attributes: dict):
    label = "User"

    combined_attributes = ", ".join([f"{key}: $q_attributes.{key}" for key in attributes.keys()])

    query = f"MERGE (u:{label} {{ {combined_attributes} }})"

    print(combined_attributes)

    records, summary, keys = driver.execute_query(
        query,
        q_attributes=attributes,
        database_="neo4j"
    )
   
    print(f"Created/updated node with properties {attributes}")

