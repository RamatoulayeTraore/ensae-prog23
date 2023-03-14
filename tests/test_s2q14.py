# This will work if ran from the root folder.
import sys 
sys.path.append("delivery_network")

from graph import Graph,graph_from_file,kruskal
import unittest   # The test framework

class Test_min_power_arbre(unittest.TestCase):
    def test_network0(self):
        g = graph_from_file("input/network.00.in")
        g_mst = kruskal(g)
        self.assertEqual(g_mst.min_power_arbre(3, 7)[1], 14)
        self.assertEqual(g_mst.min_power_arbre(3, 7)[0], [3,2,5,7])

    def test_network2(self):
        g = graph_from_file("input/network.05.in")
        g_mst = kruskal(g)
        self.assertEqual(g_mst.min_power_arbre(2,4)[1], 6)
        self.assertEqual(g_mst.min_power_arbre(2, 4)[0], [2,1,4])

if __name__ == '__main__':
    unittest.main()
