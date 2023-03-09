# This will work if ran from the root folder.
import sys 
sys.path.append("delivery_network/")

import unittest 
from graph import Graph,graph_from_file_2

class Test_GraphLoading2(unittest.TestCase):
    """ def test_network0(self):
        g = graph_from_file("input/network.00.in")
        self.assertEqual(g.nb_nodes, 10)
        self.assertEqual(g.nb_edges, 9)
    # quand on run, il nous confirme que les test fonctionnent
        print(g)

    def test_network1(self):
        g = graph_from_file("input/network.01.in")
        self.assertEqual(g.nb_nodes, 7)
        self.assertEqual(g.nb_edges, 5) """
    
    def test_network4(self):
        g = graph_from_file_2("input/network.04.in")
        self.assertEqual(len(g), 4)
        self.assertEqual(g,[(2,3,4,3),(3,4,4,2),(1,4,11,6),(2,1,4,89)])
        

if __name__ == '__main__':
    unittest.main()