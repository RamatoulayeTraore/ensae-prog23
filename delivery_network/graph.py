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
    
    def add_edge(self, node1, node2, power_min, dist=1):
        n1,n2=0,0
        if (node1 not in self.nodes):
            n1=1
            self.nodes.append(node1)
            self.nb_nodes +=1
            self.graph[node1]=[node2,power_min,dist]
        if (node2 not in self.nodes):
            n2=1
            self.nodes.append(node2)
            self.nb_nodes +=1
            self.graph[node2]=[node1,power_min,dist]
           

        if n1==0:self.graph[node1].append([node2,power_min,dist])
        if n2==0:self.graph[node2].append([node1,power_min,dist])
        self.nb_edges +=1
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
        visited[node] = True
        components.add(node)
        for neighbor in self.graph[node]:
            if not visited[neighbor[0]]:
                self.dfs(neighbor[0], visited, components)

    def connected_components(self):
        visited = [False] * self.nb_nodes
        components = []
        for node in range(self.nb_nodes):
            if not visited[node]:
                composantes = set()
                self.dfs(node, visited, composantes)
                components.append(list(composantes))
        return components

    
    def connected_components_set(self):
        """
        The result should be a set of frozensets (one per component), 
        For instance, for network01.in: {frozenset({1, 2, 3}), frozenset({4, 5, 6, 7})}
        """
        return set(map(frozenset, self.connected_components()))
    
    def get_path_with_power(self, src, dest, power):
        
        raise NotImplementedError   
        
    def get_path_with_power(self, start, end, power):
        visited = []
        res = []
        # On stocke la distance parcourue depuis le début pour chaque nœud visité
        distance = {start: 0}

        def dfs(node, current_power, path):
            nonlocal res
            visited.append(node)
            path.append(node)
            
            if node == end:
                # Si on atteint le nœud de destination, on vérifie si la power parcourue est inférieure ou égale à la puissance du camion
                if current_power <= power:
                    res = path[:]
                # On ne retourne rien pour continuer la recherche de chemins possibles
            
            elif current_power <= power:
                for neighbor in self.graph[node]:
                    # On calcule la power parcourue depuis le début jusqu'à ce voisin
                    neighbor_power = current_power + neighbor[1]
                    # Si la power n'a pas déjà été enregistrée pour ce voisin ou si elle est plus petite que la précédente,
                      # on l'enregistre dans power
                    if neighbor[0] not in power or neighbor_power < power[neighbor[0]]:
                        power[neighbor[0]] = neighbor_power
                        # On continue la recherche à partir de ce voisin
                        dfs(neighbor[0], neighbor_power, path)
            
            # On enlève le nœud visité de la liste de chemins parcourus pour continuer la recherche de chemins possibles
            path.pop()
        
        dfs(start, 0, [])
        return res


                #la il va falloir parcourir pour trouver (les) chemins qui les lie
                #on part de starts et on essaie de regarder les voisins de ce start puis on applique une fonction recusrive 
                #qui cherche les autres voisins comme la question precedente
                #condition d'arrêt et de trouver end parmi les voisins
                #on créer une liste et on met start dedans et apres il faudrait ajouter chaque
            
    #il va falloir sommer la distance des arretes entre deux noeuds et la comparer à p 
    #trajet = couple (v,v') auquel il va falloir associer une distance (et une utilité/profit)
    #on donne un départ, une arrivée et un puissance max, s'il existe un trajet qui respecte on retourne un chemin, sinon on retourne none

def graph_from_file(filename):
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
        
        G=Graph(range(1,Lines[0][0]+1))
        for i in range(1,Lines[0][1]+1):
            if len(Lines[i])==4:
              G.add_edge(Lines[i][0],Lines[i][1],Lines[i][2],Lines[i][3])   
            else:
                G.add_edge(Lines[i][0],Lines[i][1],Lines[i][2])     
     
        return G