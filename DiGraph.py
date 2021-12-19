from abc import ABC

from GraphInterface import GraphInterface


class DiGraph(GraphInterface):
    def __init__(self, **kwargs):
        """
        Each DiGraph contain dictionary of his nodes, and each node contain his edges.
        In addition each DiGraph holds the number of edges in the graph and a mode counter (mc)
        that represent the number of changes (add node, add edge, remove node or remove edge) in the graph.
        """
        self.nodes = dict()
        self.__mc = 0
        self.__num_of_edges = 0

    def get_all_v(self) -> dict:
        return self.nodes

    def all_out_edges_of_node(self, id1: int) -> dict:
        pass

    def all_in_edges_of_node(self, id1: int) -> dict:
        if self.nodes.get(id1) is None:
            raise Exception('Node {} is not exist in the graph'.format(id1))
        return self.nodes.get(id1).get_connections_in()

    def e_size(self) -> int:
        return self.__num_of_edges

    def get_mc(self) -> int:
        return self.__mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        pass

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        pass

    def remove_node(self, node_id: int) -> bool:
        pass

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        pass

    def v_size(self) -> int:
        return len(self.nodes.keys())
