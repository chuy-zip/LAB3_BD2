def create_relation(driver, firstNodeType: str, firstNode: str, secondNodeType: str, secondNode: str, relation: str, attributes: dict) -> None:
    """
    Creates or updates a relation between two given nodes.

    Args:
        driver (driver): driver.
        firstNode (str): The node at the start.
        secondNode (str): The node at the end.
        relation (str): The relation between two nodes.
        role (str): The first node's relation's attributes.
    """
    if attributes:
        combined_attrbutes = ", ".join([f"{key}: $q_attributes.{key}" for key in attributes.keys()])

        query = f"MATCH (a:{firstNodeType}), (b:{secondNodeType}) WHERE a.name = '{firstNode}' and b.name = '{secondNode}' MERGE (a)-[r:{relation} {{{combined_attrbutes}}}]->(b)"
        
    else:
        query = f"MATCH (a:{firstNodeType}), (b:{secondNodeType}) WHERE a.name = '{firstNode}' and b.name = '{secondNode}' MERGE (a)-[r:{relation}]->(b)"
    
    records, summary, keys = driver.execute_query(
        query,
        q_attributes=attributes,
        database_="neo4j"
    )

    print(f"Created/updated relation with label {relation} between {firstNode} and {secondNode}")