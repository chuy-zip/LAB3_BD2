from connection import get_neo_driver

def create_person(driver, labels_list: list[str], attributes: dict):
    labels = "Person"

    if len(labels_list) > 0:

        labels = labels + ":" + ":".join(labels_list)

    combined_attributes = ", ".join([f"{key}: $q_attributes.{key}" for key in attributes.keys()])

    query = f"MERGE (p:{labels} {{ {combined_attributes} }})"

    print(labels)
    print(combined_attributes)

    records, summary, keys = driver.execute_query(
        query,
        q_attributes=attributes,
        database_="neo4j"
    )
   
    print(f"Created/updated node with labels {labels_list} and properties {attributes}")


#driver = get_neo_driver()

#create_person(driver, ["aYES", "NO2"], {"name": "Bob", "department": "HR"})