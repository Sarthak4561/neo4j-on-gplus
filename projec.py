# from neo4j import GraphDatabase

# # Connect to the Neo4j database
# uri = "bolt://localhost:7687"
# driver = GraphDatabase.driver(uri, auth=("neo4j", "12345678"))

# # Define the query to create a node with a given name
# create_node_query = "CREATE (:Node {name: $name})"

# # Define the query to create a relationship between two nodes
# create_relationship_query = """
#     MATCH (a:Node {name: $source})
#     MATCH (b:Node {name: $target})
#     CREATE (a)-[:FRIEND]->(b)
# """

# # Open the text file and iterate through each line
# with open("gplus_combined.txt", "r") as file:
#     for line in file:
#         # Split the line into two nodes
#         source, target = line.strip().split()

#         # Create a node for the source and target if they don't exist already
#         with driver.session() as session:
#             session.execute_write(
#                 lambda tx: tx.run(create_node_query, name=source))
#             session.execute_write(
#                 lambda tx: tx.run(create_node_query, name=target))

#         # Create a relationship between the source and target
#         with driver.session() as session:
#             session.execute_write(lambda tx: tx.run(
#                 create_relationship_query, source=source, target=target))


# from neo4j import GraphDatabase

# # Connect to the Neo4j database
# uri = "bolt://localhost:7687"
# username = "neo4j"
# password = "12345678"
# driver = GraphDatabase.driver(uri, auth=(username, password))

# # Read in the text file
# filename = "gplus_combined.txt"
# with open(filename, "r") as file:
#     lines = file.readlines()

# # Create the graph database
# with driver.session() as session:
#     for line in lines:
#         # Extract the two nodes from the line
#         node1, node2 = line.strip().split(" ")

#         # Determine the label based on even or odd node value
#         if int(node1) % 2 == 0:
#             label1 = "MALE"
#         elif int(node1) % 2 == 1:
#             label1 = "FEMALE"
#         else:
#             label1 = "OTHER"
#         if int(node2) % 2 == 0:
#             label2 = "MALE"
#         elif int(node2) % 2 == 1:
#             label2 = "FEMALE"
#         else:
#             label2 = "OTHER"

#         # Determine the status based on even or odd node value
#         if int(node1) % 2 == 0 and int(node2) % 2 == 0:
#             status = "better"
#         elif int(node1) % 2 == 1 and int(node2) % 2 == 1:
#             status = "good"
#         else:
#             status = "bad"

#         # Create the nodes and their relationship with the label and status properties
#         session.run(
#             "MERGE (n1:Node {name: $node1, label: $label1})"
#             "MERGE (n2:Node {name: $node2, label: $label2})"
#             "MERGE (n1)-[r:CONNECTED_TO {status: $status}]->(n2)",
#             node1=node1,
#             node2=node2,
#             label1=label1,
#             label2=label2,
#             status=status,
#         )

# # Output the number of nodes and relationships created
# with driver.session() as session:
#     result = session.run("MATCH (n) RETURN count(n) as num_nodes")
#     num_nodes = result.single()["num_nodes"]
#     result = session.run(
#         "MATCH ()-[r]->() RETURN count(r) as num_relationships")
#     num_relationships = result.single()["num_relationships"]
# print(f"Created {num_nodes} nodes and {num_relationships} relationships.")


# from neo4j import GraphDatabase

# # Connect to the Neo4j database
# uri = "bolt://localhost:7687"
# username = "neo4j"
# password = "12345678"
# driver = GraphDatabase.driver(uri, auth=(username, password))

# # Read in the text file
# filename = "gplus_combined.txt"
# with open(filename, "r") as file:
#     lines = file.readlines()

# # Create the graph database
# with driver.session() as session:
#     for line in lines:
#         # Extract the two nodes from the line
#         node1, node2 = line.strip().split(" ")

#         # Determine the node labels and relationship status based on the node IDs
#         node1_label = "MALE" if int(node1) % 2 == 0 else "FEMALE" if int(
#             node1) % 2 == 1 else "OTHER"
#         node2_label = "MALE" if int(node2) % 2 == 0 else "FEMALE" if int(
#             node2) % 2 == 1 else "OTHER"
#         rel_status = "good" if (int(node1) + int(node2)) % 2 == 1 else "better" if (
#             int(node1) + int(node2)) % 2 == 0 else "bad"

#         # Create the nodes and their relationship with the appropriate labels and status
#         session.run(
#             "MERGE (n1:" + node1_label + " {name: $node1})"
#             "MERGE (n2:" + node2_label + " {name: $node2})"
#             "MERGE (n1)-[r:CONNECTED_TO {status: $status}]->(n2)",
#             node1=node1,
#             node2=node2,
#             status=rel_status,
#         )

# # Output the number of nodes and relationships created
# with driver.session() as session:
#     result = session.run("MATCH (n) RETURN count(n) as num_nodes")
#     num_nodes = result.single()["num_nodes"]
#     result = session.run(
#         "MATCH ()-[r]->() RETURN count(r) as num_relationships")
#     num_relationships = result.single()["num_relationships"]
# print(f"Created {num_nodes} nodes and {num_relationships} relationships.")


# from neo4j import GraphDatabase

# # Connect to the Neo4j database
# uri = "bolt://localhost:7687"
# username = "neo4j"
# password = "12345678"
# driver = GraphDatabase.driver(uri, auth=(username, password))

# # Read in the text file
# filename = "gplus_combined.txt"
# with open(filename, "r") as file:
#     lines = file.readlines()

# # Create the graph database
# with driver.session() as session:
#     for line in lines:
#         # Extract the two nodes from the line
#         node1, node2 = line.strip().split(" ")

#         # Determine the node labels and relationship status based on the node IDs
#         node1_label = "MALE" if int(node1) % 2 == 0 else "FEMALE" if int(
#             node1) % 2 == 1 else "OTHER"
#         node2_label = "MALE" if int(node2) % 2 == 0 else "FEMALE" if int(
#             node2) % 2 == 1 else "OTHER"
#         rel_status = "good" if (int(node1) + int(node2)) % 2 == 1 else "better" if (
#             int(node1) + int(node2)) % 2 == 0 else "bad"

#         # Create the nodes and their relationship with the appropriate labels and status
#         session.run(
#             "MERGE (n1:" + node1_label + " {name: $node1})"
#             "MERGE (n2:" + node2_label + " {name: $node2})"
#             "MERGE (n1)-[r:CONNECTED_TO {status: $status}]->(n2)",
#             node1=node1,
#             node2=node2,
#             status=rel_status,
#         )

# # Output the number of nodes and relationships created
# with driver.session() as session:
#     result = session.run("MATCH (n) RETURN count(n) as num_nodes")
#     num_nodes = result.single()["num_nodes"]
#     result = session.run(
#         "MATCH ()-[r]->() RETURN count(r) as num_relationships")
#     num_relationships = result.single()["num_relationships"]
# print(f"Created {num_nodes} nodes and {num_relationships} relationships.")


from neo4j import GraphDatabase

# Connect to the Neo4j database
uri = "bolt://localhost:7687"
username = "neo4j"
password = "12345678"
driver = GraphDatabase.driver(uri, auth=(username, password))

# Read in the text file
filename = "gplus_combined.txt"
with open(filename, "r") as file:
    lines = file.readlines()

# Create the graph database
with driver.session() as session:
    for line in lines:
        # Extract the two nodes from the line
        node1, node2 = line.strip().split(" ")

        # Determine the node labels and relationship status based on the node IDs
        node1_label = "MALE" if int(node1) % 2 == 0 else "FEMALE" if int(
            node1) % 2 == 1 else "OTHER"
        node2_label = "MALE" if int(node2) % 2 == 0 else "FEMALE" if int(
            node2) % 2 == 1 else "OTHER"
        rel_status = "good" if (int(node1) + int(node2)) % 2 == 1 else "better" if (
            int(node1) + int(node2)) % 2 == 0 else "bad"

        # Create the nodes and their relationship with the appropriate labels and status
        session.run(
            "MERGE (n1:" + node1_label + " {id: $node1_id})"
            "MERGE (n2:" + node2_label + " {id: $node2_id})"
            "MERGE (n1)-[r:" + rel_status.upper() + "]->(n2)",
            node1_id=node1,
            node2_id=node2,
        )

# Output the number of nodes and relationships created
with driver.session() as session:
    result = session.run("MATCH (n) RETURN count(n) as num_nodes")
    num_nodes = result.single()["num_nodes"]
    result = session.run(
        "MATCH ()-[r]->() RETURN count(r) as num_relationships")
    num_relationships = result.single()["num_relationships"]
print(f"Created {num_nodes} nodes and {num_relationships} relationships.")
