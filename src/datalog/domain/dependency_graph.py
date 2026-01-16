import networkx as nx

class DependencyGraph:

    def __init__(self, table_map):
        self._table_map = table_map

        self._graph = nx.DiGraph()

    def generate(self):
        for table_id, table in self._table_map.items():
            print(table_id, table.direct_ancestors)
            self._graph.add_node(table_id)
            self._graph.add_edges_from([(table_id, ancestor) for ancestor in table.direct_ancestors])
        
    def get_upstream(self):
        pass

    def get_downstream(self):
        pass