from graph import Graph,graph_from_file,list_from_route,kruskal


def create_output_file(network_file_name,route_file_name):
    # On lit le fichier  network dcorrspondant et on crée l'arbre correspondant
    G =  graph_from_file(network_file_name)
    Arbre=kruskal(G)
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

# classe pour représenter un sommet de l'arbre
class Node:
    def __init__(self, id):
        self.id = id
        self.parent = self
        self.rank = 0

# classe pour représenter une arête
class Edge:
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w

# algorithme de LCA
def LCA(u, v, parents):
    path = set()
    while u != parents[u]:
        path.add(u)
        u = parents[u]
    path.add(u)
    while v != parents[v]:
        if v in path:
            return v
        v = parents[v]
    return v

# algorithme de Kruskal avec l'algorithme de LCA
def kruskal(G):
    # trier les arêtes par poids croissant
    edge = []
    for x in G.nodes:
        for neighbor in G.graph[x] : 
            y,d= neighbor[0],neighbor[1]
            if (((x,y,d) not in edge) and ((y,x,d) not in edge)):
                e=Edge(x,y,d)
                edge.append(e) 
    edges= quicksort(edge)
    
    # initialiser les nœuds
    nodes = {}
    for e in edges:
        nodes[e.u] = Node(e.u)
        nodes[e.v] = Node(e.v)

    # initialiser la structure de données pour le LCA
    parents = {}
    max_weight = {}
    for node in nodes.values():
        parents[node.id] = node.id
        max_weight[node.id] = 0

    # construire l'arbre
    mst = []
    for e in edges:
        u = nodes[e.u]
        v = nodes[e.v]
        u_root = u
        v_root = v

        # trouver les racines des arbres contenant u et v
        while u_root.parent != u_root:
            u_root = u_root.parent
        while v_root.parent != v_root:
            v_root = v_root.parent

        # vérifier si u et v sont dans des arbres différents
        if u_root != v_root:
            mst.append(e)

            # unir les arbres en mettant la racine du plus petit sous l'arbre du plus grand
            if u_root.rank < v_root.rank:
                u_root.parent = v_root
            elif u_root.rank > v_root.rank:
                v_root.parent = u_root
            else:
                v_root.parent = u_root
                u_root.rank += 1

            # mettre à jour les poids maximaux sur le chemin entre u et v dans la structure de données pour le LCA
            lca = Node(LCA(u.id, v.id, parents))
            while u != lca:
                u_parent = u.parent
                max_weight[u.id] = e.w
                u.parent = lca
                u = u_parent
            while v != lca:
                v_parent = v.parent
                max_weight[v.id] = e.w
                v.parent = lca
                v = v_parent

            # mettre à jour les poids maximaux pour le LCA
            max_weight[lca.id] = e.w
            parents[lca.id] = lca.id

    return mst


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