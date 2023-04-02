from graph import Graph,graph_from_file,
class UF : 
    def __init__(self,x):
        self.poids=0
        self.element=x 
        self.parent=self 
    def Find(self) : 
        if self.EstRacine() :
            return self 
        else : 
            self. parent=(self. parent ).Find()
        return self.parent 
    
    @staticmethod

    def Link(s1, s2): 
        if s1.poids > s2.poids : 
            s2.parent = s1.parent
        else : 
            s1. parent=s2
            if s1. poids==s2.poids : 
                s2.poids +=1

    @staticmethod 
    def Union(s1, s2) :
        r1=s1.Find()
        r2=s2.Find() 
        UF.Link(r1, r2) 

    @staticmethod 
    def Test(sl, s2) : 
        return sl.Find()==s2.Find() 
    def EstRacine(self) : 
        return (self. parent == self)

def ACM_kruskal(G):
    Pred,Res, Part, Larete= {},Graph(),{},[]
    for x in G.nodes:
        Pred[x]=None
        Part[x]=UF(x)
        for neighbor in G.graph[x] : 
            y,d= neighbor[0],neighbor[1]
            if (((x,y,d) not in Larete) and ((y,x,d) not in Larete)):
                Larete.append((x,y,d)) 
    Laretes= quicksort(Larete)
    for (x,y,d) in Laretes:
        if not UF.Test(Part[x],Part[y]): 
            UF.Union(Part[x],Part[y])
            Res.add_edge(x,y,d) 
    Res.nodes.sort()
    r= Res.nodes
    gr = Graph(r)
    for item in r:
        gr.graph[item] = Res.graph[item]
        gr.nb_edges = Res.nb_edges
    return gr 

#### trier une liste selon le 3e élément des sous listes
def quicksort(lst):
    # Si la liste est vide ou ne contient qu'un élément, elle est considérée comme triée
    if len(lst) <= 1:
        return lst
    
    # Choix d'un pivot, ici le premier élément de la liste
    pivot = lst[0]
    
    # Initialisation de trois listes vides pour stocker les éléments qui sont inférieurs,
    # égaux ou supérieurs au pivot
    less = []
    greater = []
    equal = []
    
    # Parcours de la liste pour répartir les éléments par rapport au pivot
    for element in lst:
        if element[2] < pivot[2]:
            less.append(element) # Si l'élément est inférieur au pivot, il est stocké dans la liste less
        elif element[2] > pivot[2]:
            greater.append(element) # Si l'élément est supérieur au pivot, il est stocké dans la liste greater
        else:
            equal.append(element) # Si l'élément est égal au pivot, il est stocké dans la liste equal
    
    # Récursion de la fonction sur les listes less et greater, puis concaténation des trois listes (dans l'ordre : less, equal, greater)
    return quicksort(less) + equal + quicksort(greater)


def create_output_file(network_file_name,route_file_name):
    # On lit le fichier  network dcorrspondant et on crée l'arbre correspondant
    G =  graph_from_file(network_file_name)
    Arbre=ACM_kruskal(G)
    #on crée la liste des chemins
    l=list_from_route(route_file_name)
    # On ouvre le fichier de sortie en mode écriture
    output_file_name = route_file_name.replace('.in', '.out')
    with open(output_file_name, 'w') as output_file:
        # On écrit la puissance minimale nécessaire pour couvrir chaque trajet dans le fichier de sortie
        for way in l:
            start,end=way[0],way[1]
            power_min_final =Arbre.min_power_arbre(start,end)[1]
            output_file.write(str(power_min_final) +'\n') # pour afficher les poids seulemen

########################################################################
# from typing import List, Tuple

""" class UnionFind:
    def __init__(self, n: int):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, x: int) :
        if self.parent[x]!= x:
            self.parent[x]= self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int):
        px, py = self.find(x), self.find(y)
        if px != py:
            if self.rank[px] > self.rank[py]:
                self.parent[py] = px
            elif self.rank[px] < self.rank[py]:
                self.parent[px] = py
            else:
                self.parent[py] = px
                self.rank[px] += 1
                
def quicksort(lst):
    # Si la liste est vide ou ne contient qu'un élément, elle est considérée comme triée
    if len(lst) <= 1:
        return lst
    
    # Choix d'un pivot, ici le premier élément de la liste
    pivot = lst[0]
    
    # Initialisation de trois listes vides pour stocker les éléments qui sont inférieurs,
    # égaux ou supérieurs au pivot
    less = []
    greater = []
    equal = []
    
    # Parcours de la liste pour répartir les éléments par rapport au pivot
    for element in lst:
        if element[1] < pivot[1]:
            less.append(element) # Si l'élément est inférieur au pivot, il est stocké dans la liste less
        elif element[1] > pivot[1]:
            greater.append(element) # Si l'élément est supérieur au pivot, il est stocké dans la liste greater
        else:
            equal.append(element) # Si l'élément est égal au pivot, il est stocké dans la liste equal
    
    # Récursion de la fonction sur les listes less et greater, puis concaténation des trois listes (dans l'ordre : less, equal, greater)
    return quicksort(less) + equal + quicksort(greater)


def kruskal_bis(G):
    uf = UnionFind(G.nb_nodes)
    edge = []
    for source, neighbors in G.graph.items():
        for dest, power_min, _ in neighbors:
            edge.append((source, dest, power_min))
    edges=quicksort(edge)
    mst = []
    for (source, dest, power_min) in edges:
        if uf.find(source) != uf.find(dest):
            uf.union(source, dest)
            mst.append((source, dest))
    print("======================<<<<<<<<<<<<<<",mst)
    return mst """
