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
            self.graph[node1]=[node2,power_min,dist]
        if (node2 not in self.nodes):
            n2=True
            self.nodes.append(node2)
            self.nb_nodes +=1
            self.graph[node2]=[node1,power_min,dist]
           

        if n1==False:self.graph[node1].append([node2,power_min,dist])
        #si le noeud avait déja été creér, on rajoute juste le voisin là en plus, sinon il existait deja via la fonction en haut
        if n2==False:self.graph[node2].append([node1,power_min,dist])
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
<<<<<<< HEAD
        return components

=======
        return components 
    
        
>>>>>>> a9fbd7854ec60b445bc348dafe8c5cb838c1b654
    
    def connected_components_set(self):
        """
        The result should be a set of frozensets (one per component), 
        For instance, for network01.in: {frozenset({1, 2, 3}), frozenset({4, 5, 6, 7})}
        """
        #map : prend une fonction et l'appliques à tous les éléments de la liste 
        #ici la fonction c'est frozenset qui fige les éléments de la liste components
        #on prend la liste de liste, chaque éléments devient une frozenset et il fait du tout un set via map
        return set(map(frozenset, self.connected_components()))
    
    def get_path_with_power(self, src, dest, power):
        
        raise NotImplementedError   
        
    


#on veut une fonction qui nous donne tous les chemins possibles pour l'utiliser plus tard
    def reachable(self, start ,end, visited) :
        res = []
        res_all_paths = []
        if start not in visited:
            visited.append(start)
            for neighbor in self.graph[start]: 
                if neighbor[0] == end:
                    res.append(end)
                else :
                    sub_paths = self.reachable(neighbor[0],end,visited)
                    res.append(sub_paths)
            for item in res :
                t=[start]
                t.extend(item)
                res_all_paths.append(t)
                #on créer un chemin qui commence par strat, on ajoute tous les chemins et on met le tout dans la var res_all_paths
                #on a ajoutéstart à tous les sous chemins
                #extend permet d'ajouter un element à chaque liste au lieu d'ajouter une liste à la liste de listes
                #ici on ajoute start à toutes les listes
        return res_all_paths
            

    def get_path_with_power(self, start, end, power):
        pass

                #la il va falloir parcourir pour trouver (les) chemins qui les lie
                #on part de starts et on essaie de regarder les voisins de ce start puis on applique une fonction recusrive 
                #qui cherche les autres voisins comme la question precedente
                #condition d'arrêt et de trouver end parmi les voisins
                #on créer une liste et on met start dedans et apres il faudrait ajouter chaque
            
    #il va falloir sommer la distance des arretes entre deux noeuds et la comparer à p 
    #trajet = couple (v,v') auquel il va falloir associer une distance (et une utilité/profit)
    #on donne un départ, une arrivée et un puissance max, s'il existe un trajet qui respecte on retourne un chemin, sinon on retourne none
    


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
        
        G=Graph(range(1,Lines[0][0]+1))
        for i in range(1,Lines[0][1]+1):
            if len(Lines[i])==4:
              G.add_edge(Lines[i][0],Lines[i][1],Lines[i][2],Lines[i][3])   
            else:
                G.add_edge(Lines[i][0],Lines[i][1],Lines[i][2])     
     
        return G