from unittest import TestCase

from DiGraph import DiGraph
from GraphAlgo import GraphAlgo
from numpy import inf


class TestGraphAlgo(TestCase):
    def setUp(self):
        self.graph = None
        self.ga = GraphAlgo()

    def test_load_from_json(self):
        #self.assertTrue(self.ga.load_from_json("A4.json"))
        self.assertTrue(self.ga.load_from_json("100000.json"))
        #self.assertTrue(self.ga.load_from_json("A3.json"))

    def test_save_to_json(self):
        self.ga.load_from_json("A4.json")
        self.assertTrue(self.ga.save_to_json("graph1.json"))
        self.ga.load_from_json("A5.json")
        self.assertTrue(self.ga.save_to_json("graph2.json"))
        self.ga.load_from_json("A3.json")
        self.assertTrue(self.ga.save_to_json("graph3.json"))

    def test_shortest_path(self):
        self.ga.graph = graph_2
        self.assertEqual("(6, [1, 2, 4, 3, 5, 0, 6])", str(self.ga.shortest_path(1, 6)))
        self.assertEqual("(2, [3, 5, 0])", str(self.ga.shortest_path(3, 0)))
        self.assertEqual("(0, [2])", str(self.ga.shortest_path(2, 2)))
        # no path
        no_path = (inf, [])
        self.assertEqual(no_path, self.ga.shortest_path(6, 1))
        self.assertRaises(Exception, self.ga.shortest_path, (10, 1))
        self.assertRaises(Exception, self.ga.shortest_path, (1, 10))
        self.assertRaises(Exception, self.ga.shortest_path, (9, 10))

    def test_plot_graph(self):
        self.ga.graph = graph_2
        self.ga.plot_graph()
        self.ga.graph = graph_3
        self.ga.plot_graph()

    def test_is_connect(self):
        graph_1000 = GraphAlgo()
        #graph_1000.load_from_json("1000Nodes.json")
        graph_10000 = GraphAlgo()
        #graph_10000.load_from_json("10000Nodes.json")
        graph_100000 = GraphAlgo()
        #graph_100000.load_from_json("100000.json")
        graph_g1 = GraphAlgo()
        graph_g1.load_from_json("G1.json")
        graph_g2 = GraphAlgo()
        graph_g2.load_from_json("G2.json")
        graph_g3 = GraphAlgo()
        graph_g3.load_from_json("G3.json")
        #self.assertTrue(graph_1000.is_connect())
        #self.assertTrue(graph_10000.is_connect())
        #self.assertTrue(graph_100000.is_connect())
        #self.assertTrue(graph_g1.is_connect())
        #self.assertTrue(graph_g2.is_connect())
        self.assertTrue(graph_g3.is_connect())

    def test_shortest_path(self):
        graph_1000 = GraphAlgo()
        #graph_1000.load_from_json("1000Nodes.json")
        graph_10000 = GraphAlgo()
        #graph_10000.load_from_json("10000Nodes.json")
        graph_100000 = GraphAlgo()
        graph_100000.load_from_json("100000.json")
        #self.assertEqual("(774.0078942343703, [1, 862, 146, 15])", str(graph_1000.shortest_path(1, 15)))
        #self.assertEqual("(870.6923682519312, [1, 3990, 1160, 1019, 3163, 8714, 15])", str(graph_10000.shortest_path(1, 15)))
        self.assertEqual("(537.5195488123329, [1, 65221, 43448, 80018, 9319, 96684, 29032, 2373, 27009, 72251, 48769, 97983, 15])",str(graph_100000.shortest_path(1, 15)))
        #graph_g1 = GraphAlgo()
        #graph_g1.load_from_json("G1.json")
        #graph_g2 = GraphAlgo()
        #graph_g2.load_from_json("G2.json")
        #graph_g3 = GraphAlgo()
        #graph_g3.load_from_json("G3.json")
        #self.assertEqual("(4.743208031114117, [1, 0, 16, 15])", str(graph_g1.shortest_path(1, 15)))
        #self.assertEqual("(4.743208031114117, [1, 0, 16, 15])", str(graph_g2.shortest_path(1, 15)))
        #self.assertEqual("(5.913721127107312, [1, 9, 11, 13, 14, 15])", str(graph_g3.shortest_path(1, 15)))

    def test_tsp(self):
        graph_1000 = GraphAlgo()
        #graph_1000.load_from_json("1000Nodes.json")
        graph_10000 = GraphAlgo()
        #graph_10000.load_from_json("10000Nodes.json")
        graph_100000 = GraphAlgo()
        graph_100000.load_from_json("100000.json")
        #self.assertEqual("([1, 498, 685, 454, 656, 888, 857, 940, 2, 79, 654, 614, 335, 5], 1844.8834948984238)", str(graph_1000.TSP([1,2,5])))
        #self.assertEqual("([1, 3990, 9861, 3226, 7675, 2008, 547, 9750, 3001, 8120, 5064, 83, 1650, 3420, 4225, 5914, 5, 3900, 2309, 9374, 8889, 2], 2041.2591236559015)", str(graph_10000.TSP([1,2,5])))
        self.assertEqual("([1, 82679, 51097, 58340, 16967, 46872, 23346, 51656, 52335, 2, 70697, 11013, 78028, 51406, 29713, 31406, 37651, 97554, 46963, 70478, 43285, 79691, 5], 939.6605756450049)",str(graph_100000.TSP([1, 2, 5])))
        graph_g1 = GraphAlgo()
        #graph_g1.load_from_json("G1.json")
        graph_g2 = GraphAlgo()
        #graph_g2.load_from_json("G2.json")
        graph_g3 = GraphAlgo()
        #graph_g3.load_from_json("G3.json")

        #self.assertEqual("([1, 2, 6, 5], 5.091901160431474)", str(graph_g1.TSP([1, 2, 5])))
        #self.assertEqual("([1, 2, 6, 5], 5.091901160431474)", str(graph_g2.TSP([1, 2, 5])))
        #self.assertEqual("([1, 9, 2, 3, 13, 5], 4.589204619955602)", str(graph_g3.TSP([1, 2, 5])))

    def test_center(self):
        graph_1000 = GraphAlgo()
        #graph_1000.load_from_json("1000Nodes.json")
        graph_10000 = GraphAlgo()
        # graph_10000.load_from_json("10000Nodes.json")
        graph_100000 = GraphAlgo()
        # graph_100000.load_from_json("100000.json")
        graph_g1 = GraphAlgo()
        graph_g1.load_from_json("G1.json")
        graph_g2 = GraphAlgo()
        graph_g2.load_from_json("G2.json")
        graph_g3 = GraphAlgo()
        graph_g3.load_from_json("G3.json")
        #self.assertEqual("(774.0078942343703, [1, 862, 146, 15])", str(graph_1000.centerPoint()))
        # self.assertEqual("(870.6923682519312, [1, 3990, 1160, 1019, 3163, 8714, 15])", str(graph_10000.shortest_path(1, 15)))
        # self.assertEqual( "(537.5195488123329, [1, 65221, 43448, 80018, 9319, 96684, 29032, 2373, 27009, 72251, 48769, 97983, 15])",str(graph_100000.shortest_path(1, 15)))
        #self.assertEqual("(8, 9.925289024973141)", str(graph_g1.centerPoint()))
        #self.assertEqual("(0, 7.819910602212574)", str(graph_g2.centerPoint()))
        self.assertEqual("(40, 9.291743173960954)", str(graph_g3.centerPoint()))


graph_2 = DiGraph()
for i in range(7):
    graph_2.add_node(i)
graph_2.add_edge(0, 1, 1)
graph_2.add_edge(0, 2, 1)
graph_2.add_edge(0, 3, 1)
graph_2.add_edge(0, 4, 1)
graph_2.add_edge(0, 5, 1)
graph_2.add_edge(0, 6, 1)
graph_2.add_edge(1, 0, 8)
graph_2.add_edge(1, 2, 1)
graph_2.add_edge(1, 6, 9)
graph_2.add_edge(2, 1, 1)
graph_2.add_edge(2, 4, 1)
graph_2.add_edge(3, 4, 1)
graph_2.add_edge(3, 5, 1)
graph_2.add_edge(4, 1, 1)
graph_2.add_edge(4, 2, 1)
graph_2.add_edge(4, 3, 1)
graph_2.add_edge(5, 0, 1)
graph_2.add_edge(5, 2, 1)
graph_2.add_edge(5, 4, 1)

graph_3 = DiGraph()

graph_3.add_node(0, (2, 14, 0))
graph_3.add_node(1, (3, 11, 0))
graph_3.add_node(2, (4, 12, 0))
graph_3.add_node(3, (2, 8, 0))
graph_3.add_node(4, (1, 6, 0))
graph_3.add_node(5, (5, 8, 0))
graph_3.add_node(6, (7, 8, 0))
graph_3.add_node(7, (1, 3, 0))
graph_3.add_node(8, (3, 4, 0))
graph_3.add_node(9, (2, 1, 0))

graph_3.add_edge(0, 2, 1)
graph_3.add_edge(1, 0, 1)
graph_3.add_edge(2, 1, 1)
graph_3.add_edge(1, 3, 1)
graph_3.add_edge(3, 4, 1)
graph_3.add_edge(4, 3, 1)
graph_3.add_edge(5, 6, 1)
graph_3.add_edge(7, 4, 1)
graph_3.add_edge(7, 8, 1)
graph_3.add_edge(8, 9, 1)
graph_3.add_edge(9, 7, 1)
graph_3.add_edge(9, 8, 1)
