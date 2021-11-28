import networkx as nx
import matplotlib.pyplot as plt
import time

temps_debut = time.time()

#Création des listes vides Matrice et Ligne
matrice =[]
ligne =[]


#@Prédoncition : matrice et ligne sont des listes vides déjà déclarées, un fichier data.gr, se trouvant dans le répertoire courrant, correctement formaté comme montré à la page 152 du syllabus du cours de théorie des graphes édition 2009-2010
#@Postcondition: la liste matrice est remplie comme le fichier data.gr

def lecture_fichier(matrice, ligne):
    fichier = open("data.gr", "r")
    caracteres = fichier.read()


    for caractere in caracteres:
        if caractere == '\n': #Lorsqu'on arrive en fin de ligne, on ajoute la liste ligne à la matrice, et on vide la liste ligne pour qu'elle puisse en acceuillir une nouvelle
            matrice.append(ligne)
            ligne=[]
        if (caractere != ',') and (caractere != '\n') and (caractere != ' '): #rempli la liste ligne sans les caractéres de formatages ( , et \n ), et sans les éventuels espaces qui se seraient glissé
            ligne.append(caractere)

    if ligne != []:  #Ajout de la dernière ligne à la matrice si elle ne termine pas avec '\n'
        matrice.append(ligne)

    return matrice

#@Préconditions: matrice est un liste contenant une matrice représentant un graphe
#@Postcondition: G est un graphe créé avec NetworkX
def convert_networkX(matrice):

    #Création du graphe avec NetworkX et des sommets
    G = nx.Graph()
    longueur = len(matrice)

    i=0
    while i < longueur:
        i += 1
        G.add_node(i)

    #############

    #Création des arrêtes en parcourant la liste matrice, et ses "sous-listes"
    l = 0
    for ligne in matrice:
        l +=1
        c = 0
        for caract in ligne:
            c +=1
            if (caract != 'x'):
                G.add_edge(c,l)

    return G

#@Préconditions : G est un graphe correctement créé avec NetworkX
#@Postcondition: Affiche une représentation du graphe à l'écran
def draw_graph(G):
    nx.draw(G)
    plt.show()

#@Préconditions: G est un graphe correctement créé avec NetworkX
#                couleur est une liste vide déjà initialisée

#@Postconditions: couleur contient une "couleur" (ici un nombre) à chaque index correspondant au sommet

def coloriage(G, couleur):
    i = 0
    while i < len(matrice): #La boucle tourne tant que i est plus petit que la taille de la matrice
        compteur = 0
        couleur_voisin = []
        voisins = list(G.adj[i+1]) #voisins contient tous les sommets reliés au sommets i+1

        for voisin in voisins:
            compteur += couleur[voisin-1] #permet de vérifié si des coulerus ont déjà été attribué aux sommets voisins, si ce n'est pas le cas compteur sera égal à 0

            if couleur[voisin-1] != 0: # si une couleur est déjà attribuée à un sommet adjacent, alors on la met dans la liste couleur_voisin
                couleur_voisin.append(couleur[voisin-1])

        if compteur == 0: #Si aucun sommet adjacent n'a de couleur, alors on attribue la couleur 1 au sommet correspondant à l'index i
            couleur[i] = 1

        else: #Sinon on doit vérifier quelle couleur on peut attribuer
            c = 1
            tourne = True
            while tourne:  #On attribue la plus petite couleur possible qui ne se trouve pas dans la liste couleur_voisin
                if c not in couleur_voisin:
                    couleur[i] = c
                    tourne = False
                c+=1
        i +=1


    return couleur #voir @Postcondition





#Chargement de la matrice depuis le fichier
lecture_fichier(matrice,ligne)
ligne.clear()
G = convert_networkX(matrice)#Création de la matrice avec NetworkX


#Création de la liste couleur remplie de 0
couleur =[]
a = 0
while a < len(matrice):
    couleur.append(0)
    a+=1
############


couleur = coloriage(G, couleur)
print(couleur)

#draw_graph(G)

print("L'exécution complète a pris {} secondes".format(round(time.time() - temps_debut, 3)))
