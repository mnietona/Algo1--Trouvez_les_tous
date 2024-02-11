"""

Projet : Trouvez les tous : Pro
Nom Prenom : Nieto Navarrete Matias

"""

class TLT:

    def __init__(self,nom_du_fichier):
        self.nom_du_fichier = nom_du_fichier
        self.grille = self.recuperer_grille(self.nom_du_fichier)
        self.liste_solution = self.recuperer_mot_possible(self.nom_du_fichier)
        self.prefixe = self.prefixes(self.liste_solution)
        self.direction = {'N': (-1, 0), 'NE': (-1, 1), 'E': (0, 1), 'SE': (1, 1), 'S': (1, 0), 'SW': (1, -1), 'W': (0, -1), 'NW': (-1, -1)}
        self.mot_trouver = []
        self.historique = []

    def cree_liste_fichier(self,nom_du_fichier):
        """
        Cree une liste a partir d'un fichier
        :param nom_du_fichier: nom du fichier.txt
        :return: la liste
        """
        liste = []

        with open(nom_du_fichier) as f:
            for ligne in f:
                liste.append(ligne.rstrip())

        return liste

    def nettoye_liste(self,liste):
        """
        Cree une seule liste et supprime tout ce qui n'est pas une lettre
        :param liste: liste a nettoyer
        :return: la liste prope
        """
        liste_propre=[]

        for i in range(len(liste)):
            for j in range(len(liste[i])):
                liste_propre.append(liste[i][j])

        while("," in liste_propre):
            liste_propre.remove(",")

        return liste_propre

    def cree_grille(self, liste_propre, n):
        """
        Cree la grille (matrice NxN) d'apres une liste
        :param liste_propre: liste des lettres
        :param n: taille de la matrice
        :return: la grille
        """
        grille = []

        for i in range(n):
            liste_lettre = []
            for j in range(n):
                liste_lettre.append(liste_propre[0])
                del liste_propre[0]
            grille.append(liste_lettre)

        return grille

    def recuperer_grille(self,nom_du_fichier):
        """
        Cree la grille (matrice NxN) a partir du fichier
        :param nom_du_fichier: nom du fichier.txt
        :return: la grille
        """
        liste = self.cree_liste_fichier(nom_du_fichier)
        lettre = []
        n = int(liste[0])

        for i in range(n):
            lettre.append(liste[i + 2])

        return self.cree_grille(self.nettoye_liste(lettre),n)

    def recuperer_mot_possible(self,nom_du_fichier):
        """
        Cree une liste des mot possible a partir d'un fichier
        :param nom_du_fichier: nom du fichier.txt
        :return: liste des mots
        """
        liste = self.cree_liste_fichier(nom_du_fichier)

        for i in range(int(liste[0]) + 3):
            del liste[0]

        return liste

    def prefixes(self,liste_de_mots):
        """
        Cree un set ou se trouve tout les prefixes des mot a trouver
        :param liste_de_mots: la liste des mot possible
        :return: un set des prefixes des mot possible
        """
        s = set()
        for mot in liste_de_mots:
            for i in range(2,len(mot)):
                s.add(mot[:i])

        return s

    def trouver_mot_rec(self,i, j, resultat):
        """
        Recois les coordonner de la lettre et trouve tout les mots possibles de la lettre a la position i j

        :param i: coordonne x de la lettre
        :param j: coordonne y de la lettre
        :param resultat : le mot a trouver
        :return: liste des mot de la lettre demande au debut
        """

        if (resultat in self.liste_solution and resultat not in self.mot_trouver):
            self.mot_trouver.append(resultat)

        dire = ['N', 'S', 'W', 'E', 'NE', 'NW', 'SW', 'SE']

        for cote in dire:

            # Permet de pas sortir de la grille
            if (i + self.direction.get(cote)[0] < 0 or j + self.direction.get(cote)[1] < 0
                    or i + self.direction.get(cote)[0] >= len(self.grille)
                    or j + self.direction.get(cote)[1] >= len(self.grille)):
                continue

            # Permet de pas prendre la lettre precedente
            elif ((i + self.direction.get(cote)[0], j + self.direction.get(cote)[1]) in self.historique):
                continue

            else:
                resultat += self.grille[i + self.direction.get(cote)[0]][j + self.direction.get(cote)[1]]
                # resultat est un prefix ou bien resultat est un mot qu'il faut trouver
                if (self.mot_dans_prefix(resultat,self.prefixe)
                        or resultat in self.liste_solution and resultat not in self.mot_trouver):

                    self.historique.append((i, j)) # ajoute la coordonne de la lettre dans l'historique pour l'utilser qu'une seul fois
                    # Fait la recursion avec le i et j de la lettre suivante et avec resultat qui a une lettre en plus
                    self.trouver_mot_rec(i + self.direction.get(cote)[0], j + self.direction.get(cote)[1], resultat)
                    resultat = resultat[:-1]
                    self.historique.pop() # supprime la coordonne de l'historique pour pouvoir l'utiliser une autre fois avec un autre mot

                else:
                    resultat = resultat[:-1]

        return self.mot_trouver

    def mot_dans_prefix(self,mot,prefixes):
        """
        Renvoi vrai si le mot existe comme prefix
        :param mot: le mot a cherche dans prefixes
        :param prefixes: la liste des prefixes
        :return: vrai ou faux
        """
        variable = False
        if (mot in prefixes):
            variable = True
        return variable

    def trouver_tout_les_mots(self):
        """
        Parcourt la grille et appel trouver_mot_rec
        :return: La liste de tout les mots trouver
        """
        for i in range(len(self.grille)):
            for j in range(len(self.grille)):
                self.trouver_mot_rec(i,j,self.grille[i][j])

        return self.mot_trouver

    def tester(self,liste_mot_trouver):
        """
        Verifie que 2 listes sont les memes
        :param liste_mot_trouver: liste des mot trouver dans la grille
        :return: vrai ou faux
        """
        print("Nbr de mot touver : ", len(liste_mot_trouver))
        print("Nbr de mot à touver : ", len(self.liste_solution))
        return (sorted(liste_mot_trouver) == sorted(self.liste_solution))

    def affichage_grille(self):
        """
        Affiche la grille sur le terminal
        :param grille: la matrice NxN des lettres
        :return:
        """
        for i in range(len(self.grille)):
            print(self.grille[i])


if  __name__ =='__main__':

    grilles = ["grille_1.txt", "grille_2.txt", "grille_3.txt"]
    
    for grille in grilles:
        tlt = TLT(grille)
        a = tlt.trouver_tous_les_mots()
        b = tlt.tester(a)
        print(b)
   




