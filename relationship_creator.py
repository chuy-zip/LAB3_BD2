from connection import get_neo_driver
import datetime

def create_relationship(driver, relationship_name: str, relationship_properties: dict, from_node: dict, to_node: dict):
    """
    Crea una relación entre dos nodos en Neo4j.

    driver: Neo4j driver
    relationship_name: Nombre de la relación (e.g., "KNOWS")
    relationship_properties: Diccionario con propiedades de la relación
    from_node: Diccionario con propiedades del nodo origen (e.g., {"labels": "Person", "attributes": {"name": "Alice"}})
    to_node: Diccionario con propiedades del nodo destino (e.g., {"labels": "User", "attributes": {"username": "Bob"}})
    """
    # Preparar las etiquetas y atributos de los nodos
    from_labels = from_node.get("labels", "Node")
    from_attributes = ", ".join([f"{key}: $from_attributes.{key}" for key in from_node["attributes"].keys()])

    to_labels = to_node.get("labels", "Node")
    to_attributes = ", ".join([f"{key}: $to_attributes.{key}" for key in to_node["attributes"].keys()])

    # Preparar las propiedades de la relación
    rel_properties = ", ".join([f"{key}: $rel_properties.{key}" for key in relationship_properties.keys()])

    # Consulta Cypher para crear la relación
    query = f"""
    MATCH (a:{from_labels} {{ {from_attributes} }}), (b:{to_labels} {{ {to_attributes} }})
    MERGE (a)-[r:{relationship_name} {{ {rel_properties} }}]->(b)
    RETURN a, r, b
    """

    # Debug prints para verificar la consulta
    print("Cypher Query:")
    print(query)

    # Ejecutar la consulta
    records, summary, keys = driver.execute_query(
        query,
        from_attributes=from_node["attributes"],
        to_attributes=to_node["attributes"],
        rel_properties=relationship_properties,
        database_="neo4j"
    )

    print(f"Created/updated relationship '{relationship_name}' with properties {relationship_properties}")
    return records, summary, keys

