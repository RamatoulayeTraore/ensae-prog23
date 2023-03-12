# This will work if ran from the root folder.
import sys 
sys.path.append("delivery_network/")

from graph import Graph, graph_from_route

import unittest 

class Test_GraphLoading(unittest.TestCase):
    def test_route1(self):
        g = graph_from_route("input/routes.1.in")
        print("============>",g)
        self.assertEqual(g.nb_edges,10)


if __name__ == '__main__':
    unittest.main()