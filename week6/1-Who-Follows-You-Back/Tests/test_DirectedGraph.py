from DirectedGraph import DirectedGraph
import unittest

class TestDirectedGraph(unittest.TestCase):
    def setUp(self):
        self.test_graph = DirectedGraph()

    def test_create_node(self):
        self.test_graph.create_node("A")
        self.assertTrue("A" in self.test_graph.graph)

    def test_add_edge(self):
        self.test_graph.add_edge("A", "B")
        self.assertEqual(self.test_graph.graph["A"], ["B"])

    def test_get_neighbours_for(self):
        self.test_graph.add_edge("A", "B")
        self.assertEqual(self.test_graph.get_neighbours_for("A"), ["B"])

    def test_path_between(self):
        self.test_graph.add_edge("A", "B")
        self.test_graph.add_edge("B", "C")
        self.test_graph.add_edge("C", "D")
        self.assertTrue(self.test_graph.path_between("A", "D"))

if __name__ == '__main__':
    unittest.main()
