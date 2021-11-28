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

#@Préconditions: matrice est un liste contenant une matrice représentative d'un graphe
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

def draw_graph(G):
    nx.draw(G)
    plt.show()


lecture_fichier(matrice,ligne)
ligne = []

G = convert_networkX(matrice)
draw_graph(G)


print("L'exécution complète a pris {} secondes".format(round(time.time() - temps_debut, 2)))
