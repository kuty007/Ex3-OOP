import queue
import random
from typing import List
import json
from DiGraph import DiGraph
from GraphAlgoInterface import GraphAlgoInterface
from GraphInterface import GraphInterface
import heapq
from numpy import inf


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
        path_nodes = []
        path = []
        start_node = node_lst[0]
        path.append(start_node)
        node_lst.remove(start_node)
        total_distance = 0
        while len(node_lst) > 0:
            closet = -1
            min_value = inf
            for i in node_lst:
                short_path = self.shortest_path(start_node, i)
                min_dis = short_path[0]
                if min_dis == inf:
                    raise Exception("the nodes on the list are not connected can't find TSP")
                else:
                    if min_dis < min_value:
                        min_value = min_dis
                        path_nodes = short_path[1]
                        closet = i
            path_nodes.remove(start_node)
            path.extend(path_nodes)
            start_node = closet
            node_lst.remove(start_node)
            total_distance += min_value
        return path, total_distance

    def centerPoint(self) -> (int, float):
        if not self.is_connect():
            return (-1, inf),
        dictionary = {}
        for i in self.graph.get_all_v():
            mx = -inf
            for j in self.graph.get_all_v():
                if i != j:
                    max_dis = self.shortest_path(i, j)[0]
                    if max_dis > mx:
                        mx = max_dis

            dictionary.update({i: mx})
        x = min(dictionary, key=dictionary.get)
        return x, dictionary.get(x)

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
                else:
                    x = random.uniform(0, 100)
                    y = random.uniform(0, 100)
                    gr.add_node(int(i.get("id")), (x, y, 0))
            for i in graph_dict.get("Edges"):
                gr.add_edge(int(i.get("src")), int(i.get("dest")), float(i.get("w")))
        self.graph = gr
        return True

    def save_to_json(self, file_name: str) -> bool:
        try:
            with open(file_name, "w") as f:
                json.dump(self.graph, default=lambda o: o.graph_dict(), indent=4, fp=f)
        except IOError as e:
            print(e)
            return False
        return True

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        if self.graph.nodes.get(id1) is None:
            raise Exception('Node {} is not exist in the graph'.format(id1))
        if self.graph.nodes.get(id2) is None:
            raise Exception('Node {} is not exist in the graph'.format(id2))
        if id1 == id2:
            return 0, [id1]
        return self.dijkstra(id1, id2)

    def plot_graph(self) -> None:
        pass

    def dijkstra(self, src, dest):
        distances = {node: inf for node in self.graph.nodes.keys()}
        previous_nodes = {src: -1}
        distances[src] = 0
        queue = []
        heapq.heappush(queue, (0, src))
        while queue:
            current_node = heapq.heappop(queue)[1]
            if distances[current_node] == inf:
                break
            for neighbour, w in self.graph.nodes.get(current_node).get_edge_out().items():
                alternative_route = distances[current_node] + w
                if alternative_route < distances[neighbour]:
                    distances[neighbour] = alternative_route
                    previous_nodes[neighbour] = current_node
                    heapq.heappush(queue, (distances[neighbour], neighbour))
                if current_node == dest:
                    break
        path, current_node = [], dest
        if distances[dest] == inf:
            return inf, []
        while current_node != -1:
            path.insert(0, current_node)
            current_node = previous_nodes[current_node]
        return distances[dest], path

    def is_connect(self):
        vertex_size = self.graph.v_size()
        for i in self.graph.get_all_v():
            src = self.graph.get_node(i)
            list1 = self.is_connected_bfs(src.get_key())
            len_list_vertex = len(list1)
            if len_list_vertex != vertex_size:
                return False

        return True

    def is_connected_bfs(self, src: int):
        visited = []
        q = queue.Queue()
        current = self.graph.get_node(src)
        visited.append(current)
        q.put(current)
        while not q.empty():
            current = q.get()
            for ed in current.get_edge_out():
                nod = self.graph.get_node(ed)
                if nod not in visited:
                    q.put(nod)
                    visited.append(nod)
        return visited


g_algo = GraphAlgo()  # init an empty graph - for the GraphAlgo
file = "A4.json"
g_algo.load_from_json(file)
print(g_algo.centerPoint())
