import time
from graph import Graph,graph_from_file,create_output_file,kruskal


data_path = "input/"
file_name = "network.01.in"

""" g=graph_from_file("input/network.5.in")
print(g) """
####test_route_7
""" t0 = time.perf_counter()
g.min_power(4,12)
g.min_power(3,15)
g.min_power(15,9)
t1=time.perf_counter()
tmps_moy=(t1-t0)/3 
print("temps moy",tmps_moy)  
####test_route_7
g1 = graph_from_file("input/routes.7.in")
t0 = time.perf_counter()
g1.min_power(194708,87133)
t1=time.perf_counter()
tmps_moy2=(t1-t0)
print("temps moy2",tmps_moy2)
 """

 
""" g=Graph([])
    g.add_edge("Paris", "Palaiseau", 4, 20)
    print(g) """
# temps_total=0
# for i in range(2,3):
#     to=time.perf_counter()
#     create_output_file("input/network."+str(i)+".in","input/routes."+str(i)+".in")
#     t1=time.perf_counter()
#     temps_total=temps_total+(t1-to)
# print("temps final",temps_total)
#temps_total=0

to=time.perf_counter()
r=kruskal("input/network.1.in")
t1=time.perf_counter()
print("temps",t1-to)


