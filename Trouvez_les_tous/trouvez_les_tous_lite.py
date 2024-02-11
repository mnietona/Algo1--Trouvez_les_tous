"""

Projet : Trouvez les tous : Lite
Nom Prenom : Nieto Navarrete Matias

Remarque : dans la fonction diviser_phrase, le set de mot est appelé "dico".

"""

def diviser_phrase(string, n, resultat):
    """
    Permet de diviser une phrase sans espace avec espace d'apres un set de mot donné.
    :param string: la phrase sans espace
    :param n: la taille de la phrase sasn espace
    :param resultat: la phrase avec espace
    """

    if (n == 0): # condition d'arret pour la recurssion

        chaine = resultat.split() # cree une liste des mots qui sont dans resultat
        for i in range(len(chaine) - 1):

            if (i + 1 >= len(chaine)):
                break

            # evite de verifier tout les mots, seulement ceux qui commencent par la meme lettre
            if (chaine[i][0] == chaine[i + 1][0]):
                lettre_dans_mot = True

                for j in range(len(chaine[i])-1):
                    if (chaine[i][j] == chaine[i+1][j]):
                        lettre_dans_mot = True
                    else:
                        lettre_dans_mot = False

                if (lettre_dans_mot):
                    del chaine[i]

        resultat = ""

        for mot in chaine:
            resultat += mot + " "

        print(resultat)

    for i in range(n + 1): # parcour la phrase

        if (string[:i] in dico): # dico correpsond au set de mot
            mot = string[:i]
            resultat += mot + " "
            # rappelle la fonction avec la phrase sans le premier mot et la nouvelle taille de la phrase
            diviser_phrase(string[i:], len(string[i:]), resultat)


def toutes_les_phrases(phrase):
    """
    Appelle la fonction diviser_phrase.
    :param phrase: la phrase sans espace
    """
    diviser_phrase(phrase, len(phrase), "")


if  __name__ =='__main__':
    # Exemple 1
    phrase = "magrandmerepossedeuncoffrefortdanssabassecours"
    dico = {"grand", "mere", "grandmere", "possede", "un", "coffre", "fort", "coffrefort", "dans", "sa", "bassecours",
            "basse", "cours", "ma"}
    toutes_les_phrases(phrase)
    print("\n")

    # Exemple 2
    phrase = "pineapplepenapple"
    dico = {"apple", "pen", "applepen", "pine", "pineapple"}
    toutes_les_phrases(phrase)
    print("\n")

    # Exemple 3
    phrase = "unbonhommeestforcementungentilhomme"
    dico = {"Un","bonhomme","force","ment","forcement","est","homme","bon","gentil","un","homme","gentilhomme"}
    toutes_les_phrases(phrase)