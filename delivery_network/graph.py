import heapq
import copy
import graphviz
import math

class Graph:
    def __init__(self, nodes=[]):
        self.nodes = nodes
        self.graph = dict([(n, []) for n in nodes])
        self.nb_nodes = len(nodes)
        self.nb_edges = 0
        #nécessaire à pour le calcul de la puissance min question16
        self.ancestors = {}

    def __str__(self):
        """Prints the graph as a list of neighbors for each node (one per line)"""
        if not self.graph:
            output = "The graph is empty"            
        else:
            output = f"The graph has {self.nb_nodes} nodes and {self.nb_edges} edges.\n"
            for source, destination in self.graph.items():
                output += f"{source}-->{destination}\n"
        return output
    
    #pour chaque noeud, on aura une sous liste de noeud composés de triplets, qui donneront ses voisins(une sous liste par voisins), 
    #un power min et la distance (en général 1). Voir test pour vérifier/comprendre
    def add_edge(self, node1, node2, power_min, dist=1):
        #on peut parametrer une distance, mais par défaut elle vaudra 1
        n1,n2=False,False
        if (node1 not in self.nodes):
            n1=True
            self.nodes.append(node1)
            self.nb_nodes +=1
            self.graph[node1]=[(node2,power_min,dist)]
        if (node2 not in self.nodes):
            n2=True
            self.nodes.append(node2)
            self.nb_nodes +=1
            self.graph[node2]=[(node1,power_min,dist)]
           

        if n1==False:self.graph[node1].append((node2,power_min,dist))
        #si le noeud avait déja été creér, on rajoute juste le voisin là en plus, sinon il existait deja via la fonction en haut
        if n2==False:self.graph[node2].append((node1,power_min,dist))
        self.nb_edges +=1

        #Donc par exemple, si Node1 existe mais pas node 2, alors n2 sera True et n1 false, et donc on ajouetera node 2 comme voisin de node 1
        
        #n1 n2 compliqué voir si on peut l'enlever (voir code prof)
        """"
        Adds an edge to the graph. Graphs are not oriented, hence an edge is added to the adjacency list of both end nodes. 

        Parameters: 
        -----------
        node1: NodeType
            First end (node) of the edge
        node2: NodeType
            Second end (node) of the edge
        power_min: numeric (int or float)
            Minimum power on this edge
        dist: numeric (int or float), optional
            Distance between node1 and node2 on the edge. Default is 1.
        """

    def dfs(self, node, visited, components):
        visited.append(node)
        components.add(node)
        print(f"on vient d'ajouter {node}")
        for neighbor in self.graph[node]:
        #node c'etst la clef donc on accède aux sous listes associés 
        #pour chacun des noeuds associés, on les parcourt 
            if neighbor[0] not in visited :
            #si le voisin n'est pas visité, on lui applique lui-même la fonction etc. et 
            #une fois que tous ses voisins auront été visités ca va remonter au noeud antérieur etc.
            #jusqu'à ce que tous les noeuds aient été visités
                self.dfs(neighbor[0], visited, components)



    def connected_components(self):
        visited = []
        #on créer une liste vide
        components = []
        for node in self.nodes:
            if node not in visited :
            #si le noeud n'est pas visité, on créer un set et on applique la fonction au noeud  
                composantes = set()
                #la diff avec une liste c'est que un set n'est pas ordonné
                self.dfs(node, visited, composantes)
                #on va vaoir le composantes rempli de toutes les villes connexes et ensuite on l'ajoute comme sous liste à component 
                #et on reprend avec les noeud pas encore explorés
                components.append(list(composantes))
                                  
        return components
 

    def connected_components_set(self):
        """
        The result should be a set of frozensets (one per component), 
        For instance, for network01.in: {frozenset({1, 2, 3}), frozenset({4, 5, 6, 7})}
        """
        #map : prend une fonction et l'appliques à tous les éléments de la liste 
        #ici la fonction c'est frozenset qui fige les éléments de la liste components
        #on prend la liste de liste, chaque éléments devient une frozenset et il fait du tout un set via map
        return set(map(frozenset, self.connected_components()))
    

        
    def get_path_with_power(self, start, end, power):
        visited = []
        res = []
        # On stocke la puissance  pour chaque arrête  visitée
        power_edge = {start: 0}

        def dfs(node, current_power, path):
            nonlocal res
            path.append(node)
            if node == end:
                # Si on atteint le nœud de destination, on vérifie si la power_edge parcourue est inférieure ou égale à la puissance maximale
                if current_power <= power:
                   res = path[:]
                
                # On ne retourne rien pour continuer la recherche de chemins possibles
            
            elif current_power <= power:
                for neighbor in self.graph[node]:
                     # On calcule la power_edge de l'arrête en cours 
                     current_power = neighbor[1]
                    # Si la power_edge n'a pas déjà été enregistrée pour ce voisin ou si elle est plus petite que la précédente,
                    # on l'enregistre dans power_edge
                     if neighbor[0] not in power_edge or current_power < power_edge[neighbor[0]]:
                        power_edge[neighbor[0]] = current_power
                        # On continue la recherche à partir de ce voisin
                        dfs(neighbor[0], current_power, path)
            
            # On enlève le nœud visité de la liste de chemins parcourus pour continuer la recherche de chemins possibles
            path.pop()
        
        dfs(start, 0, [])
        if res!=[]:
            return res
        else :
            return None
        
    ### la complexité de cette fonction est O(E + V) car la boucle for qui parcourt ts les arrêtes donne O(E) 
    ### et 

   
    def get_path_with_power_2(self, start, end, power):
        # Initialisation des distances
        distances = {node: float('inf') for node in self.nodes}
        distances[start] = 0

        # Initialisation du dictionnaire des prédecesseurs
        predecessors = {node: None for node in self.nodes}
        # Initialisation de la liste des nœuds à visiter
        to_visit = [(0, start)]

        while to_visit:
            # On récupère le nœud avec la distance minimale
            current_distance, current_node = heapq.heappop(to_visit)

            # Si on a atteint le nœud de destination et que la puissance utilisée sur le chemin est inférieure ou égale à power,
            # on reconstruit le chemin et on le retourne
            if current_node == end and current_distance <= power:
                path = []
                while current_node:
                    path.append(current_node)
                    current_node = predecessors[current_node]
                return list(reversed(path))

            # On parcourt tous les voisins du nœud courant
            for neighbor, power_min, dist in self.graph[current_node]:
                # On calcule la distance et la puissance utilisée pour atteindre le voisin
                distance = current_distance + dist
                power_used = max(power_min, distances[current_node])

                # Si la puissance utilisée pour atteindre le voisin est inférieure ou égale à power et que la distance est plus petite que la distance actuelle,
                # on met à jour les distances et les prédecesseurs
                if power_used <= power and distance < distances[neighbor]:
                    distances[neighbor] = distance
                    predecessors[neighbor] = current_node
                    heapq.heappush(to_visit, (distance, neighbor))

        # Si aucun chemin admissible n'a été trouvé, on retourne None
        return None
    
    def min_power_arbre(self, start, end):
        # On utilise un heap (tas) pour stocker les chemins possibles 
        heap = [(start, [])]
        visited = set()
        while heap:
            (current_node, path) = heapq.heappop(heap)
            # On ajoute le nœud en cours de traitement à la liste de chemins parcourus
            visited.add(current_node)
            # On ajoute le nœud en cours de traitement à la fin du chemin actuel
            path = path + [current_node]
            # Si on atteint le nœud de destination, on retourne le chemin et la longueur totale
            if current_node == end:
                # On calcule la puissance minimale nécessaire pour couvrir le chemin
                power_min = float(0)
                for i in range(len(path) - 1):
                    for neighbor in self.graph[path[i]]:
                        if neighbor[0] == path[i+1]:
                            print("path,minpower======",path,power_min,neighbor[1])
                            if neighbor[1] >= power_min:
                                power_min = neighbor[1]
                return path, power_min
            # On explore les voisins du nœud en cours de traitement
            for neighbor in self.graph[current_node]:
                if neighbor[0] not in visited:
                    # On ajoute le chemin possible dans le heap
                    heapq.heappush(heap, ( neighbor[0], path))
                    print("path======",heapq.heappush(heap, ( neighbor[0], path)))
        # Si on ne trouve pas de chemin, on retourne None
        return None, None



    def min_power(self, start, end):
        p=0
        for node in self.nodes:
            for neighbor in self.graph[node]:
                if p<neighbor[1]:
                   p=neighbor[1]
                
                
        max_power =p
        low, high = 0, max_power
        res = None

        while high > low :
            mid = (low + high) // 2
            path = self.get_path_with_power(start, end, mid)
            if path is not None:
                res = (path, mid)
                high = mid
            else:
                low = mid+1

        return res     

    def preprocess(self):
        # On initialise les ancêtres de chaque nœud avec lui-même et une puissance minimale de 0
        self.ancestors = {node: [(node, 0)] for node in self.nodes}
        # On calcule la puissance maximale à utiliser dans l'algorithme de doubling
        max_distance = int(math.log(self.nb_nodes, 2)) + 1

        # On parcourt chaque puissance de 2 jusqu'à la puissance maximale
        for i in range(max_distance):
            # On parcourt chaque nœud du graphe
            for node in self.nodes:
                # Si le nœud a déjà au moins i ancêtres, on peut ajouter son i-ème ancêtre
                if len(self.ancestors[node]) > i:
                    # On remonte l'arbre en prenant l'ancêtre de puissance 2^i
                    ancestor = self.ancestors[node][i][0]
                    # On calcule la puissance minimale maximale entre le nœud et son ancêtre de puissance 2^i
                    max_power = max(self.ancestors[node][i][1], self.ancestors[ancestor][i][1])
                    # On ajoute l'i-ème ancêtre du nœud avec la puissance minimale maximale
                    self.ancestors[node].append((self.ancestors[ancestor][i][0], max_power))



    def min_power_arbre_2(self, start, end):
        # Vérifie si les noeuds start et end existent dans le graphe
        if start not in self.nodes or end not in self.nodes:
            return None

        # Cas où start et end sont identiques, donc la puissance nécessaire est de 0
        if start == end:
            return 0

        # Calcul de la distance maximale entre les noeuds du graphe
        max_distance = int(math.log(self.nb_nodes, 2)) + 1

        # Initialisation du chemin entre start et end
        path = [start, end]
        # Initialisation des ancêtres du chemin
        path_ancestors = []

        # Parcours des ancêtres de end, depuis le plus lointain jusqu'au plus proche
        for i in range(max_distance, -1, -1):
            # Récupération de l'ancêtre de end à la distance i
            if path[-1] not in self.ancestors or i >= len(self.ancestors[path[-1]]):
                continue
            ancestor = self.ancestors[path[-1]][i][0]

            # Si l'ancêtre est start, on ajoute ses informations aux path_ancestors et on sort de la boucle
            if ancestor == start:
                path_ancestors.append(self.ancestors[path[-1]][i])
                break

            # Si l'ancêtre est un noeud du chemin, on l'ajoute au chemin et on ajoute ses informations aux path_ancestors
            if ancestor == path[-2]:
                path.append(self.ancestors[path[-1]][i][0])
                path_ancestors.append(self.ancestors[path[-2]][i])
            # Si l'ancêtre est un noeud différent du chemin, on l'ajoute au chemin et on ajoute ses informations aux path_ancestors
            else:
                path.append(ancestor)
                path_ancestors.append(self.ancestors[path[-2]][i])
                path_ancestors.append(self.ancestors[path[-1]][i])

        # Initialisation de la puissance minimale nécessaire à l'infini
        min_power = float('inf')

        # Parcours des informations des ancêtres du chemin, depuis les plus proches jusqu'aux plus lointains
        for i in range(len(path_ancestors) - 1, -1, -1):
            power = path_ancestors[i][1]

            # Si la puissance de l'ancêtre est inférieure à la puissance minimale actuelle, on la remplace
            if power < min_power:
                min_power = power

        # Renvoie la puissance minimale nécessaire pour parcourir le chemin entre start et end
        return min_power
   
    



def graph_from_file(filename):
    # import graph from a file
    fichier = open(filename)
    lignes = fichier.readlines()
    fichier.close()
    Lignes = []
    for ligne in lignes:
        Lignes.append(ligne.split())
    Lines = []
    for ligne in Lignes:
        mots = []
        for mot in ligne:
            mots.append(int(mot))
        Lines.append(mots)

    G = Graph(range(1, Lines[0][0] + 1))
    for i in range(1, Lines[0][1] + 1):
        if len(Lines[i]) == 4:
            G.add_edge(Lines[i][0], Lines[i][1], Lines[i][2], Lines[i][3])
        else:
            G.add_edge(Lines[i][0], Lines[i][1], Lines[i][2])

    return G

def list_from_route(filename):
    fichier=open(filename)
    lignes=fichier.readlines()
    fichier.close()
    Lignes=[]
    for ligne in lignes:
        Lignes.append(ligne.split())
    Lines=[]
    for ligne in Lignes:
        mots=[]
        for mot in ligne:
            mots.append(int(mot))
        Lines.append(mots)

    l=[]
    for i in range(1,Lines[0][0]+1):
        l.append((Lines[i][0],Lines[i][1]))
    return l


#graph 
def plot_graph(graph, start_node, end_node, path, route):
    dot = graphviz.Digraph()
    for node in graph:
        dot.node(node)
        for neighbor in graph[node]:
            dot.edge(node, neighbor, label=str(graph[node][neighbor]))
    dot.node(start_node, style='filled', fillcolor='lightblue')
    dot.node(end_node, style='filled', fillcolor='lightblue')
    dot.node(path[0], style='filled', fillcolor='orange')
    dot.node(path[-1], style='filled', fillcolor='orange')
    for i in range(len(path) - 1):
        dot.edge(path[i], path[i+1], color='orange', penwidth='3')
    for i in range(len(route) - 1):
        dot.edge(route[i], route[i+1], color='green', penwidth='3')
    dot.render('graph', format='png', view=True)

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
    


""" def kruskal(G):
    Res, Part, Larete= Graph(),{},[]
    for x in G.nodes:
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
 """