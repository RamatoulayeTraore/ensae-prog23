import copy 

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








    tab=0
    def reachable(self, start ,end, current_path, all_paths) :
        tab_str = "===" * Graph.tab    
        Graph.tab += 1
        current_path.append(start)
        for neighbor in self.graph[start]: 
            if neighbor[0] == end:
                print(f"{tab_str}{current_path} destination trouvée")
                res = copy.copy(current_path)
                res.append(end)
                all_paths.append(res)
            elif  neighbor[0] in current_path :
                pass
                print(f"{tab_str}{current_path} skip : deja visité")
            else :
                print(f"{tab_str}{current_path} on descend dans les noeuds")
                self.reachable(neighbor[0],end,current_path, all_paths)
        current_path.remove(start)      
        Graph.tab-=1
            
        
    
    def get_all_max_powers(self,all_paths) :
        all_max_powers =[]
        for path in all_paths:
            max_edge_power = 0
            #on va utiliser un systeme de current node next node
            #on prend un node dans la liste et on regarde la trajet avec chacun des suivants
            current_node =path[0]
            for next_node in path[1:] :
                edge_list=self.graph[current_node]
                #donne tous les triplets du nodes étudiés (edge)
                for edge in edge_list :
                    if edge[0] == next_node :
                    #si le edge qu'on etudie est bien le next node alors on va prendre la puissance du trajet 
                        a = edge[1]
                        if a> max_edge_power :
                            max_edge_power = a
                current_node = next_node
            all_max_powers.append(max_edge_power)
        return all_max_powers 
        #si il est plu spuissant que le précédent il deveint le power max

    def get_path_with_power(self, start, end, power):
        all_paths =[]
        current_path=[]
        self.reachable(start, end, current_path, all_paths)
        #on récupère la liste des chemins
        print(all_paths)
        power_list = self.get_all_max_powers(all_paths)
        final_power = min(power_list)
        if final_power > power :
            return None
        else :
            return all_paths[power_list.index(final_power)]
        #index est la fonction réciproque de celle qui a t[i] donne li ieme élément de t 
        #donc t.index(i) me donne la position de i dans t (renvoie la premiere en cas de doublon)
        #ainsi on peut récupérer le chemin lié à final_power








                        
                    
                    


                


            



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