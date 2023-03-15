import heapq
import copy
import graphviz

class Graph:
    def __init__(self, nodes=[]):
        self.nodes = nodes
        self.graph = dict([(n, []) for n in nodes])
        self.nb_nodes = len(nodes)
        self.nb_edges = 0


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
        
    ### la complexité de cette fonction est O(E) car la boucle for qui parcourt ts les arrêtes donne O(E) 
    ### et la copie de path dans res donne O(V).

   
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
    #la complexité de cette fonction est O((E+V)logV). 
    #logV est le coût d'insertion et de suppression d'un élément dans un tas binaire
    #O(V) car dans la boucle whhile ts les noeuds sont visités au maximum une fois
    #O(E) car la boucle for parcourt tous les voisins
    
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


    ''' La complexité de get_path_with_power() est de O(log(V+E)), donc la complexité de la 
    fonction min_power() sera de O((V+E)*log(V+E)*log P), où P est la plage de puissance des chemins dans le graphe.

    La boucle for qui initialise la variable p est en O(V*E), car elle parcourt tous les nœuds et toutes les arêtes du graphe
    Le bloc while effectue une recherche dichotomiqe, qui nécessite O(log P) itérations, où P est la plage de puissance des chemins dans le graphe
    Dans chaque itération de la boucle while, nous appelons la fonction get_path_with_power() qui a une complexité de O(log(V+E)). 
    '''

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
            
    
def graph_from_file(filename):
    # import graph from a file
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

        if len(Lines[0])==2:
            G=Graph(range(1,Lines[0][0]+1))
            for i in range(1,Lines[0][1]+1):
                if len(Lines[i])==4:
                   G.add_edge(Lines[i][0],Lines[i][1],Lines[i][2],Lines[i][3])  
                else:
                    G.add_edge(Lines[i][0],Lines[i][1],Lines[i][2]) 
        else:
            G=Graph([])
            for i in range(1,Lines[0][0]+1):
               # if i==11:break
                if len(Lines[i])==4:
                    G.add_edge(Lines[i][0],Lines[i][1],Lines[i][2],Lines[i][3])  
                else:
                    G.add_edge(Lines[i][0],Lines[i][1],Lines[i][2])            
        return G

""" def graph_from_file(filename):
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

    return G """



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
    


def kruskal(graph):
    # Créer une structure de données ensemble-disjoint pour suivre les composantes connexes
    # du graphe. Chaque noeud commence dans son propre ensemble.
    disjoint_set = {node: {node} for node in graph.nodes}

    # Créer une liste d'arêtes triées par poids (distance) dans l'ordre non décroissant.
    edge = []
    for source, neighbors in graph.graph.items():
        for dest, power_min, _ in neighbors:
            edge.append((source, dest, power_min))
    edges = sorted(edge, key=lambda x:x[2])

    # Parcourir la liste triée d'arêtes et ajouter celles qui connectent différentes
    # composantes jusqu'à ce qu'il ne reste plus qu'une seule composante connexe.
    k = 0
    result = Graph()
    while k < graph.nb_nodes - 1 and edges:
        source, dest , weight = edges.pop(0)
        if disjoint_set[source] != disjoint_set[dest]:
            # Ajouter l'arête au graphe résultat et fusionner les ensembles contenant
            # les noeuds source et destination.
            result.add_edge(source, dest, weight)
            disjoint_set[source].update(disjoint_set[dest])
            for node in disjoint_set[dest]:
                disjoint_set[node] = disjoint_set[source]
            k += 1

    if k < graph.nb_nodes - 1:
        # Si le graphe n'est pas connexe, lever une exception.
        raise ValueError("Le graphe n'est pas connexe")
    else:
        result.nodes.sort()# permet de trier la list des noeux
        r= result.nodes
        gr = Graph(r)
        for item in r:
            gr.graph[item] = result.graph[item]
        gr.nb_edges = result.nb_edges
    return gr



""" Il semble que l'exécution de la fonction graph_from_file a été interrompue à cause d'une erreur.
L'erreur se produit lorsque la fonction essaie d'ajouter une arête au graphe en utilisant la méthode add_edge() de la classe Graph. 
Il est difficile de déterminer la cause exacte de cette erreur sans plus d'informations, mais il est possible que cela soit dû à une erreur 
de syntaxe dans le fichier d'entrée ou à une erreur de mémoire en raison d'un grand nombre de nœuds ou d'arêtes
. Il est recommandé de vérifier le format du fichier d'entrée et de s'assurer qu'il est correctement structuré.
Il peut également être utile de tester la fonction avec un fichier d'entrée plus petit pour déterminer si la
taille du graphe est un facteur contribuant à l'erreur. """

""" La complexité de la solution précédente est la suivante:

Construction de l'arbre couvrant minimum : O(E log V), où E est le nombre d'arêtes et V est le nombre de sommets dans le graphe.

Recherche du chemin entre les sommets de départ et d'arrivée dans l'arbre couvrant : O(E log V) (en utilisant une file de priorité).

Calcul de la puissance minimale : O(T), où T est le nombre de trajets.

Ainsi, la complexité totale est O((E+T) log V).

En pratique, le temps d'exécution dépendra des données spécifiques, mais il est probable que la solution sera plus rapide que la première version du code car elle ne nécessite pas de calculer la liste des trajets à l'avance. De plus, l'utilisation d'un dictionnaire pour stocker les puissances minimales pour chaque trajet permettra une recherche efficace des valeurs nécessaires pour chaque chemin.

Cependant, le temps d'exécution sera toujours proportionnel au nombre d'arêtes et de trajets dans le graphe, donc la complexité totale reste la même en termes de pire cas."""