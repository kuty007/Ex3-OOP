from typing import List
import random
import json
from DiGraph import DiGraph
from GraphAlgoInterface import GraphAlgoInterface
from GraphInterface import GraphInterface


class GraphAlgo(GraphAlgoInterface):
    def __init__(self, digraph: DiGraph = None):
        """
        Each GraphAlgo contain a DiGraph on which the algorithm works on.
        :param digraph:
        """
        self.graph = digraph

    def get_graph(self) -> GraphInterface:
        return self.graph

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        pass

    def centerPoint(self) -> (int, float):
        pass

    def load_from_json(self, file_name: str) -> bool:
        gr = DiGraph()
        with open(file_name, "r") as f:
            graph_dict = json.load(f)
            for i in graph_dict.get("Nodes"):
                if "pos" in i and len(i.get("pos")) > 0:
                    pos = []
                    pos_as_str = i.get("pos")
                    arr = pos_as_str.split(',')
                    for j in arr:
                        pos.append(float(j))
                    gr.add_node(int(i.get("id")), tuple(pos))
            for i in graph_dict.get("Edges"):
                gr.add_edge(int(i.get("src")), int(i.get("dest")), float(i.get("w")))
        self.graph = gr
        return True

    def save_to_json(self, file_name: str) -> bool:
        try:
            with open(file_name, "w") as f:
                json.dump(self.graph, default=lambda o: o.as_dict(), indent=4, fp=f)
        except IOError as e:
            print(e)
            return False
        return True

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        pass

    def plot_graph(self) -> None:
        pass
