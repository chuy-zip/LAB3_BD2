from connection import get_neo_driver

driver = get_neo_driver()

try:
    records, summary, keys = driver.execute_query(
        "MERGE (p:Person {name: 'Call2'})",
        database_="neo4j"
    )
    print("Query executed successfully")
finally:
    driver.close()