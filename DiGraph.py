from Node import Node
from GraphInterface import GraphInterface


class DiGraph(GraphInterface):
    def __init__(self, **kwargs):
        """
        Each DiGraph contain dictionary of his nodes, and each node contain his edges.
        In addition each DiGraph holds the number of edges in the graph and a mode counter (mc)
        that represent the number of changes (add node, add edge, remove node or remove edge) in the graph.
        """
        self.nodes = dict()
        self.__changes = 0
        self.__num_of_edges = 0

    def __repr__(self) -> str:
        return f"Graph: |V| = {len(self.nodes)},  |E|={self.__num_of_edges}   "



    def get_all_v(self) -> dict:
        return self.nodes

    def all_out_edges_of_node(self, id1: int) -> dict:
        if self.nodes.get(id1) is None:
            raise Exception(f"Node {id1} is not exist in the graph")
        return self.nodes.get(id1).get_edge_out()

    def all_in_edges_of_node(self, id1: int) -> dict:
        if self.nodes.get(id1) is None:
            raise Exception(f"Node {id1} is not exist in the graph")
        return self.nodes.get(id1).get_edge_in()

    def e_size(self) -> int:
        return self.__num_of_edges

    def get_mc(self) -> int:
        return self.__changes

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if self.nodes.get(id1) is None or self.nodes.get(id2) is None:
            return False
        if id2 in self.get_node(id1).get_edge_out().keys():
            return False
        if weight < 0:
            raise Exception('Edge weight must be positive')
        if id1 == id2:
            return False
        self.nodes.get(id1).add_edge_out(id2, weight)
        self.nodes.get(id2).add_edge_in(id1, weight)
        self.__changes += 1
        self.__num_of_edges += 1
        return True

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if node_id in self.nodes:
            return False
        n = Node(node_id, pos)
        self.nodes[node_id] = n
        self.__changes += 1
        return True

    def remove_node(self, node_id: int) -> bool:
        if node_id not in self.nodes.keys():
            return False
        removed_node = self.nodes[node_id]
        keys = ()
        for x in removed_node.get_edge_out().keys():
            keys += (x,)
        [self.remove_edge(node_id, x) for x in keys]
        keys = ()
        for x in removed_node.get_edge_in().keys():
            keys += (x,)
        [self.remove_edge(x, node_id) for x in keys]
        del self.nodes[node_id]
        self.__changes += 1
        return True

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if self.nodes.get(node_id1) is None or self.nodes.get(node_id2) is None:
            return False
        if node_id2 not in self.nodes.get(node_id1).get_edge_out():
            return False
        del self.nodes.get(node_id1).get_edge_out()[node_id2]
        del self.nodes.get(node_id2).get_edge_in()[node_id1]
        self.__changes += 1
        self.__num_of_edges -= 1
        return True

    def v_size(self) -> int:
        return len(self.nodes.keys())

    def get_node(self, node_id: int) -> Node:
        """
        Return node by key (node_id).
        :param node_id: this node key
        :return: the node by his key.
        """
        if node_id not in self.nodes.keys():
            raise Exception(f"Node {node_id} is not exist in the graph")
        return self.nodes[node_id]

    def graph_dict(self):
        """
        Return the graph as dictionary {"Edges": ...., "Nodes": ....}
        :return: the graph as dictionary
        """
        g_dict = {}
        list_of_edges = []
        list_of_nodes = []
        for k, v in self.nodes.items():
            list_of_nodes.append(v.as_dict_node())
            for i in range(len(v.as_dict_edge())):
                list_of_edges.append(v.as_dict_edge()[i])
        g_dict["Edges"] = list_of_edges
        g_dict["Nodes"] = list_of_nodes

        return g_dict
