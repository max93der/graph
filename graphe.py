#Théorie des graphes: Projet 5



#Maxime Deravet S202214
#
#Abdelilah Khaliphi S204896



#Importation des modules nécessaires
import networkx as nx
import matplotlib.pyplot as plt
import time

temps_debut = time.time() #Sauvegarde du temps du début pour calculer le temps total à la fin

#Création des listes vides Matrice et Ligne
matrice =[]
ligne =[]




###### ////////// DECLARATION DES FONCTIONS \\\\\\\\\\ ######

#@Prédoncition : matrice et ligne sont des listes vides déjà déclarées, un fichier "file", se trouvant dans le répertoire courant, correctement formaté comme montré à la page 152 du syllabus du cours de théorie des graphes édition 2009-2010
#@Postcondition: la liste matrice est remplie comme le fichier "file"
def lecture_fichier(matrice, ligne, file):
    fichier = open(file, "r")
    caracteres = fichier.read()

    if len(caracteres) == 0: #Vérification que le fichier n'est pas vide
        return -1

    for caractere in caracteres: #Parcours de tous les caractères du fichier

        if caractere == '\n': #Lorsqu'on arrive en fin de ligne, on ajoute la liste ligne à la matrice, et on vide la liste ligne pour qu'elle puisse en acceuillir une nouvelle
            matrice.append(ligne)
            ligne=[]

        if (caractere != ',') and (caractere != '\n') and (caractere != ' '): #rempli la liste ligne sans les caractéres de formatages ( , et \n ), et sans les éventuels espaces qui se seraient glissé
            ligne.append(caractere)

    if ligne != []:  #Ajout de la dernière ligne à la matrice si elle ne termine pas avec '\n'
        matrice.append(ligne)

    fichier.close()


    ####Programmation défensive###
    #Si jamais les dernières lignes sont vides, on les enlèves de la matrice
    tourne =1
    while tourne:
        if len(matrice[-1]) == 0:
            matrice.pop(-1)
        else:
            tourne =0


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
#Source : NetworkX documentation : "Drawing Graphs"
def draw_graph(G):
    nx.draw(G,with_labels=True, font_weight='bold')
    plt.show()





#@Préconditions: - G est un graphe correctement créé avec NetworkX
#                - couleur est une liste vide déjà initialisée
#
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
            G.add_node(i + 1, couleur=1)#Ajout de la couleur à NetworkX

        else: #Sinon on doit vérifier quelle couleur on peut attribuer
            c = 1
            tourne = True

            while tourne:  #On attribue la plus petite couleur possible qui ne se trouve pas dans la liste couleur_voisin
                if c not in couleur_voisin:
                    couleur[i] = c
                    G.add_node(i+1, couleur = c)  #Ajout de la couleur à NetworkX
                    tourne = False #Une fois qu'on a trouvé une couleur, on arrête la boucle
                c+=1

        i +=1

    # voir @Postcondition pour plus de détail
    return couleur



###### ////////// FIN FONCTIONS \\\\\\\\\\ ######




#Chargement de la matrice depuis le fichier
matrice = lecture_fichier(matrice,ligne, "data.gr")
ligne.clear() # On efface les résiduts de la liste ligne

G = convert_networkX(matrice)#Création du graphe G avec NetworkX


#Création de la liste couleur remplie de 0
couleur =[]
a = 0
while a < len(matrice):
    couleur.append(0)
    a+=1
############


couleur = coloriage(G, couleur) #attribution des couleurs aux sommets

print("Les sommets sont coloriés dans l'ordre comme suit : " , couleur )

draw_graph(G) #Affichage graphique

print(G)

#print(G.nodes.data())

print("L'exécution complète a pris {} secondes".format(round(time.time() - temps_debut, 3)))


#Fin programme