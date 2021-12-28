import queue
import random
from typing import List
import json
from DiGraph import DiGraph
from GraphAlgoInterface import GraphAlgoInterface
from GraphInterface import GraphInterface
import heapq
from numpy import inf
import matplotlib.pyplot as plt


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
        """
          TSP:
              :param node_lst: list of nodes to go through
              @return: The shortest path between all the nodes in the list and the weight of this course
          """
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
                    return inf, []
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
        """
         centerPoint:
             @return:returns the id of the node that is most distance node form him is the closest and the weight of the
             distance between them
        """

        dictionary = {}  # this will contain each node and the value of the longest shortest_path from him to node
        # in the graph
        for i in self.graph.get_all_v():
            mx = -inf
            for j in self.graph.get_all_v():
                if i != j:
                    max_dis = self.shortest_path(i, j)[0]
                    if max_dis == inf:
                        return -1, inf
                        # if the graph not connected we can't find a center
                    elif max_dis > mx:
                        mx = max_dis
            dictionary.update({i: mx})
        x = min(dictionary, key=dictionary.get)
        return (x, dictionary.get(x))

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
        """
        Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm
         @param id1: The start node id
         @param id2: The end node id
         @return: The distance of the path, a list of the nodes ids that the path goes through
          """
        if self.graph.nodes.get(id1) is None:
            raise Exception('Node {} is not exist in the graph'.format(id1))
        if self.graph.nodes.get(id2) is None:
            raise Exception('Node {} is not exist in the graph'.format(id2))
        if id1 == id2:
            return 0, [id1]
        return self.dijkstra(id1, id2)

    """
        plot of the graph in matplotlib
    """

    def plot_graph(self) -> None:
        for node in self.graph.get_all_v().values():
            if node.get_location() is None:
                loc_x = random.uniform(0, 100)
                loc_y = random.uniform(0, 100)
                location = (loc_x, loc_y, 0)
                node.set_location(location)
            x, y, z = node.get_location()
            plt.plot(x, y, markersize=15, marker="*", color='blue')
            plt.text(x, y, str(node.get_key()), color="#FFDF00", fontsize=10)
            for dest_id, w in self.graph.all_out_edges_of_node(node.get_key()).items():
                dest = self.graph.get_node(dest_id)
                if dest.get_location() is None:
                    loc_x2 = random.uniform(0, 100)
                    loc_y2 = random.uniform(0, 100)
                    location = (loc_x2, loc_y2, 0)
                    dest.set_location(location)
                x2, y2, z2 = dest.get_location()
                plt.annotate("", xy=(x, y), xytext=(x2, y2), arrowprops=dict(arrowstyle="->"))
        plt.show()

    def dijkstra(self, src, dest):
        """
           dijkstra implementation:
                 Returns the shortest path from node id1 to node id2
                 @param src: The start node id(src)
                 @param dest: The end node id(dst)
                 @return: The distance of the path, a list of the nodes ids that the path goes through
            """
        distances = {node: inf for node in self.graph.nodes.keys()}
        previous_nodes = {src: -1}
        distances[src] = 0
        qu = []
        heapq.heappush(qu, (0, src))
        while qu:
            current_node = heapq.heappop(qu)[1]
            if distances[current_node] == inf:
                break
            for neighbour, w in self.graph.nodes.get(current_node).get_edge_out().items():
                alternative_route = distances[current_node] + w
                if alternative_route < distances[neighbour]:
                    distances[neighbour] = alternative_route
                    previous_nodes[neighbour] = current_node
                    heapq.heappush(qu, (distances[neighbour], neighbour))
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
        """
         is_connect:
             Returns if the graph is strongly connected
             @param self graph
             @return: True if the graph is strongly connected and False if not
             """
        graph = self.graph
        for nodes in self.graph.nodes:
            node = self.get_graph().get_node(nodes)
            node.reset_visited()
        gre = self.transpose()
        vertex_size = self.graph.v_size()
        src = self.graph.get_node(0)
        list1 = self.is_connected_bfs(src.get_key())
        len_list_vertex = len(list1)
        if len_list_vertex != vertex_size:
            return False
        self.graph = gre
        list2 = self.is_connected_bfs(src.get_key())
        len_list_vertex2 = len(list2)
        if len_list_vertex2 != vertex_size:
            self.graph = graph
            return False
        self.graph = graph
        return True
    def is_connected_bfs(self, src: int):
        """
         is_connected_bfs:
              Returns list with all the nodes that we visited when we start from specific node
              @param src node id
              @return: list with all the nodes we visited
               """
        visited = []
        q = queue.Queue()
        current = self.graph.get_node(src)
        visited.append(current)
        current.visited = True
        q.put(current)
        while not q.empty():
            current = q.get()
            for ed in current.get_edge_out():
                nod = self.graph.get_node(ed)
                if not nod.get_visited():
                    nod.visited = True
                    q.put(nod)
                    visited.append(nod)
        return visited

    def transpose(self):
        """
        Return transpose graph.
        Meaning each edge in the original graph transpose (src-->dest)-->(src<--dest).
        :return:
        """
        gra = DiGraph()
        for k, v in self.graph.get_all_v().items():
            gra.add_node(k, v.get_location())
        for k, v in gra.get_all_v().items():
            for dest, w in self.graph.all_in_edges_of_node(k).items():
                gra.add_edge(k, dest, w)
        return gra


g_algo = GraphAlgo()  # init an empty graph - for the GraphAlgo
file = "A4.json"
g_algo.load_from_json(file)
g_algo.is_connect()
g_algo.save_to_json("ro.json")
