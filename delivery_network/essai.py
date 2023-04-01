""" class UF : 
    def __init__(self,x):
        self.poids=0
        self.element=x 
        self.parent=self 
    def Find(self) : 
        if self.EstRacine() :
            return self 
        else : 
            self. parent=(self. parent ).find
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
        r1=s1.find()
        r2=s2.find() 
        UF.Link(r1, r2) 

    @staticmethod 
    def Test(sl, s2) : 
        return sl.Find()==s2.Find() 
    def EstRacine(self) : 
        return (self. parent == self)

def ACM_kruskal(G):
    Pred,Res, Part, Larete= {},[],{},[]
    for x in G[0]:
        Pred[x]=None
        Part[x]=UF.UF(x)
    for (y,d) in G[1][x] : 
        if (((x,d,y) not in Larete) and ((y,d,x) not in Larete)):
            Larete.append((x,d,y)) 
    Laretes= sorted(Larete, key=lambda x:x[2])
    #TriRapide() 
    print (Laretes)
    for (x,d,y) in Laretes:
        if not UF.UF.Test(Part[x],Part[y]):
            print ('choix de '+str((x,d,y))) 
            UF.UF.Union(Part[x],Part[y])
            Res.append((x,d,y)) 
    return Res  """



########################################################################
# from typing import List, Tuple

class UnionFind:
    def __init__(self, n: int):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, x: int) :
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
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


def kruskal(G):
    edge = []
    for source, neighbors in G.items():
        for dest, power_min, _ in neighbors:
            edge.append((source, dest, power_min))
    edges=quicksort(edge)
    uf = UnionFind(G.nb_nodes)
    mst = []
    for (source, dest, power_min) in edges:
        if uf.find(source) != uf.find(dest):
            uf.union(source, dest)
            mst.append((source, dest))
    return mst
