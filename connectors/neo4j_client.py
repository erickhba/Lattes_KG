from neo4j import GraphDatabase

class client_graph:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def print_greeting(self, message):
        with self.driver.session() as session:
            greeting = session.execute_write(self._create_and_return_greeting, message)
            print(greeting)

    @staticmethod
    def _create_and_return_greeting(tx, message):
        result = tx.run("MATCH (pesquisador:Pesquisador { Nome: 'Gisele da Silva Craveiro' })-[:orienta]->(orientacao:Orientacoes) RETURN pesquisador,  orientacao", message=message)
        return result.single()[0]


if __name__ == "__main__":
    greeter = client_graph("bolt://localhost:7687", "username", "***")
    greeter.print_greeting("hello, world")
    greeter.close()