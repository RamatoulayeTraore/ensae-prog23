import math
import math

# Méthode pour calculer l'arbre des ancêtres
def binary_lifting(self):
    # Calcul du nombre de bits nécessaires pour représenter num_nodes en binaire
    log_n = int(math.ceil(math.log2(self.nb_nodes)))
    # Initialisation de la matrice d'ancêtres et de la matrice de puissances
    self.ancestor = [[-1] * self.nb_nodes for i in range(log_n)]
    self.power = [[0] * self.nb_nodes for i in range(log_n)]

    # Remplissage des matrices d'ancêtres et de puissances pour chaque noeud
    for i in self.nodes:
        for j in self.graph[i]:
            # Pour chaque voisin du noeud i
            neighbor, power = j[0],j[1]
            # Stockage de l'ancêtre et de la puissance correspondante
            self.ancestor[0][neighbor] = i
            self.power[0][neighbor] = power

    # Boucle pour calculer les autres niveaux de la matrice d'ancêtres et de puissances
    for i in range(1, log_n):
        for j in self.nodes:
            # Si l'ancêtre au niveau précédent n'est pas inexistant (-1)
            if self.ancestor[i-1][j] != -1:
                ancestor = self.ancestor[i-1][j]
                # Stockage de l'ancêtre de niveau supérieur et de la puissance maximale des deux ancêtres
                self.ancestor[i][j] = self.ancestor[i-1][ancestor]
                self.power[i][j] = max(self.power[i-1][j], self.power[i-1][ancestor])



def min_power_binary_lifting(self, start, end):
    # Calcul du nombre de niveaux nécessaires pour le binary lifting
    log_n = int(math.ceil(math.log2(self.num_nodes)))

    # Si le point de départ est le même que le point d'arrivée, la puissance minimale est de 0
    if start == end:
        return 0

    # Si le trajet entre le point de départ et le point d'arrivée est infini, la puissance minimale est infinie
    if self.dist[start][end] == float('inf'):
        return float('inf')

    # Initialisation des variables pour stocker l'ancêtre et la puissance minimale
    ancestor = start
    power_min = 0

    # Parcours de l'arbre en utilisant le binary lifting pour trouver le plus grand ancêtre commun
    # entre le point de départ et le point d'arrivée
    for i in range(log_n-1, -1, -1):
        # Si l'ancêtre de l'extrémité à la distance 2^i est plus proche ou égale au point de départ,
        # on met à jour la puissance minimale et l'extrémité
        if self.ancestor[i][end] != -1 and self.dist[start][self.ancestor[i][end]] >= 2**i:
            power_min = max(power_min, self.power[i][end])
            end = self.ancestor[i][end]

    # Si le plus grand ancêtre commun est le point de départ, la puissance minimale est déjà trouvée
    if self.ancestor[0][end] == ancestor:
        return power_min

    # Parcours de l'arbre en utilisant le binary lifting pour trouver le plus grand ancêtre commun
    # entre l'ancêtre du point de départ et le plus grand ancêtre commun entre le point de départ et le point d'arrivée
    for i in range(log_n-1, -1, -1):
        # Si l'ancêtre à la distance 2^i du point de départ est différent de l'ancêtre à la distance 2^i
        # de l'extrémité, on met à jour la puissance minimale, l'ancêtre du point de départ et l'extrémité
        if self.ancestor[i][ancestor] != self.ancestor[i][end]:
            power_min = max(power_min, self.power[i][ancestor], self.power[i][end])
            ancestor = self.ancestor[i][ancestor]
            end = self.ancestor[i][end]

    # Retourne la puissance minimale entre le point de départ et le plus grand ancêtre commun,
    # la puissance minimale entre l'extrémité et le plus grand ancêtre commun et la puissance minimale trouvée
    # lors de la recherche de l'ancêtre entre le point de départ et l'extrémité
    return max(power_min, self.power[0][ancestor], self.power[0][end])



""" def min_power_binary_lifting(self, start, end):
    log_n = int(math.ceil(math.log2(self.num_nodes)))

    if start == end:
        return 0

    if self.dist[start][end] == float('inf'):
        return float('inf')

    ancestor = start
    power_min = 0

    for i in range(log_n-1, -1, -1):
        if self.ancestor[i][end] != -1 and self.dist[start][self.ancestor[i][end]] >= 2**i:
            power_min = max(power_min, self.power[i][end])
            end = self.ancestor[i][end]

    if self.ancestor[0][end] == ancestor:
        return power_min

    for i in range(log_n-1, -1, -1):
        if self.ancestor[i][ancestor] != self.ancestor[i][end]:
            power_min = max(power_min, self.power[i][ancestor], self.power[i][end])
            ancestor = self.ancestor[i][ancestor]
            end = self.ancestor[i][end]

    return max(power_min, self.power[0][ancestor], self.power[0][end])
 """