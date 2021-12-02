#Théorie des graphes: Projet 5



#Maxime Deravet S202214
#
#Abdelilah Khaliphi S204896



#Importation des modules nécessaires
import networkx as nx
import matplotlib.pyplot as plt
import time
import os, random

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
    chiffre = 0 #plus de détails sur 'chiffre' plus bas


    if len(caracteres) == 0: #Vérification que le fichier n'est pas vide
        return -1

    for caractere in caracteres: #Parcours de tous les caractères du fichier

        if caractere == '\n': #Lorsqu'on arrive en fin de ligne, on ajoute la liste ligne à la matrice, et on vide la liste ligne pour qu'elle puisse en acceuillir une nouvelle
            if ligne != []:#Vérification que la ligne contient quelque chose
                matrice.append(ligne)
            ligne=[]
            chiffre = 0

        if (caractere != ',') and (caractere != '\n') and (caractere != ' '): #rempli la liste ligne sans les caractéres de formatages ( , et \n ), et sans les éventuels espaces qui se seraient glissé
            if chiffre == 0:
                ligne.append(caractere)
            chiffre +=1

        if (caractere == ',') or (caractere=='\n'):
            chiffre = 0

    # Chiffre permet de n'ajouter qu'une seule fois un nombre qui serait composé de plusieurs chiffres.
    # On incrémente chiffre à chaque fois qu'on ajoute quelque chose à la liste ligne,
    # On réinitialise chiffre à 0 quand on rencontre une ',' ou un '\n'
    # On vérifie que chiffre est égal à 0, donc qu'on a bien un nouveau nombre, avant de l'ajouter à la matrice



    if ligne != []:  #Ajout de la dernière ligne à la matrice si elle ne termine pas avec '\n'
        matrice.append(ligne)
    fichier.close()

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





#@Préconditions: - G est un graphe correctement créé avec NetworkX
#                - couleur est une liste remplie de 0, dont la taille est égale au nombre de sommets
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




#@Préconditions : G est un graphe correctement créé avec NetworkX, couleur contient les couleurs associées à chaque sommet
#@Postcondition: Affiche une représentation du graphe à l'écran
#Source : NetworkX documentation : "Drawing Graphs"
def draw_graph(G):
    nx.draw(G,with_labels=True, node_color = couleur, font_weight='bold', font_color="whitesmoke")
    plt.show()

###### ////////// FIN FONCTIONS \\\\\\\\\\ ######




#Permet de choisir un fichier random
dir = 'tests'
filename = random.choice(os.listdir(dir))
path = os.path.join(dir,filename)
print("Le graphe affiché est le",filename)
####################################


matrice = lecture_fichier(matrice, ligne, path) #Si on veut choisir un fichier personalisé, remplasser path par le nom ou le chemin du fichier
                                                #Il faut aussi commenter la ligne supérieure qui print le numéro du graphe affiché

ligne.clear() # On efface les résiduts de la liste ligne


G = convert_networkX(matrice)#Création du graphe G avec NetworkX


#Création de la liste couleur remplie de 0
couleur =[]
a = 0
while a < len(matrice):
    couleur.append(0)
    a+=1
##########################################


couleur = coloriage(G, couleur) #attribution des couleurs aux sommets

print("Les sommets sont coloriés dans l'ordre comme suit : " , couleur )

draw_graph(G) #Affichage graphique



print("L'exécution complète a pris {} secondes".format(round(time.time() - temps_debut, 3)))
#Fin programme
