import time
from graph import Graph,graph_from_file


data_path = "input/"
file_name = "network.01.in"

#g=graph_from_file("network.00.in")
#print(g)
""" g1 = graph_from_file("input/routes.1.in")
t0 = time.perf_counter()
g.min_power(4,12)
g.min_power(3,15)
g.min_power(15,9)
t1=time.perf_counter()
tmps_moy=(t1-t0)/3 
print("temps moy",tmps_moy)"""
####test_route_10
g1 = graph_from_file("input/routes.10.in")
t0 = time.perf_counter()
g1.min_power(60518,17231)
t1=time.perf_counter()
tmps_moy=(t1-t0)/3
print("temps moy",tmps_moy)


"""g=Graph([])
g.add_edge("Paris", "Palaiseau", 4, 20)
print(g)
"""