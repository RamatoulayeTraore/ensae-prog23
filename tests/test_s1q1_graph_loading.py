# This will work if ran from the root folder.
import sys 
sys.path.append("delivery_network/")

import unittest 
from graph import Graph, graph_from_file

class Test_GraphLoading(unittest.TestCase):
    def test_network0(self):
        g = graph_from_file("input/network.00.in")
        print("fdjjldvd",g)
        self.assertEqual(g.nb_nodes, 10)
        self.assertEqual(g.nb_edges, 9)

    """    def test_network1(self):
        g = graph_from_file("input/network.01.in")
        self.assertEqual(g.nb_nodes, 7)
        self.assertEqual(g.nb_edges, 5)
    
    def test_route1(self):
        g = graph_from_file("input/routes.1.in")
        self.assertEqual(g.nb_nodes, 20)
        self.assertEqual(g.nb_edges, 140) """
    

if __name__ == '__main__':
    unittest.main()
