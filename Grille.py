#la classe Grille

class Grille:
    def __init__(self):
        #une matrice avec un nombre de colonnes =7 et nombre de lignes =6
        self.grille = [[], [], [], [], [], []]
        #initalisation de la grille à 0
        self.initialiser()

    #methode pour initialiser la grille
    def initialiser(self):
        #vider la Grille pour recommencer la partie
        self.grille.clear()
        #initialiser la grille à 0
        self.grille=[[0]* 7 for i in range(6)]

    #methode pour afficher la grille
    def __str__(self):
        s = "  _0_|_1_|_2_|_3_|_4_|_5_|_6_\n"
        for i in range(0, 6):
            s += str(i) + "| "
            for j in range(0, 7):
                s += str(self.grille[i][j])+ " | " #on utilise la methode str pour transformer le case de la grille de entier vers chaine et la concatainer dans l'affichage
            if i <= 4:
                s += "\n |---|---|---|---|---|---|---|\n"
            else:
                s += "\n |---|---|---|---|---|---|---|"
        return s

    #methode qui demande la colonne choisie avec les conditions necessaires:
    def demander_colonne(self):
        c=int(input("Veuillez choisir une colonne: "))
        #il faut que la colonne saisie soit dans l'intervalle de [0,6]
        while c not in range(0,7):
            c=int(input("Donner une colonne entre 0 et 6 S.V.P: "))
        #lorsque la colonne est pleine on demande de resaisir la colonne
        while self.grille[0][c]!= 0:
            c=int(input("Cette colonne est pleine! Donner une autre colonne S.V.P: "))
        return c

    #methode d'insertion de case dans la grille
    def inserer_case(self,colonne,p):
        ligne=5
        while self.grille[ligne][colonne] != 0:
            ligne-=1
        if p == 0:
            self.grille[ligne][colonne]=1
        else:
            self.grille[ligne][colonne]=2

    #methode qui renvoi si une grille est non pleine ou pas
    def non_plein(self):
        for j in range (0,7):
            if (self.grille[0][j]== 0):
                return True
        return False

    #methode pour savoir qui est le gagant horizontalement ( 4 cases alignées horizontalement)
    def est_gagant_h(self,pion):
        for line in range(6):
            for colonne in range(4):
                if pion == 'N':
                    if (self.grille[line][colonne]==1) and (self.grille[line][colonne+1]==1) and (self.grille[line][colonne+2]==1) and (self.grille[line][colonne+3] == 1):
                        return True
                elif pion =='B':
                    if (self.grille[line][colonne]==2) and (self.grille[line][colonne+1]==2) and (self.grille[line][colonne+2]==2) and (self.grille[line][colonne+3] == 2):
                        return True
                else:
                    return False

    #methode pour savoir qui est le gagant verticalement ( 4 cases alignées verticalement)
    def est_gagant_v(self,pion):
        for colonne in range(7):
            for line in range(6):
                if pion =='N':
                    if (self.grille[line][colonne]==1) and (self.grille[line -1][colonne]==1) and (self.grille[line -2][colonne]==1) and (self.grille[line -3][colonne]== 1):
                        return True
                elif pion == 'B':
                    if (self.grille[line][colonne]==2) and (self.grille[line -1][colonne]==2) and ( self.grille[line -2][colonne]==2) and ( self.grille[line -3][colonne]==2):
                        return True
                else:
                    return False

    #methode pour savoir qui est le gagant ( 4 cases alignées diagonalement du haut à gauche vers le bas à droit)
    def est_gagant_d_des(self,pion):
        for line in range(3):
            for colonne in range(4):
                if pion== 'N':
                    if (self.grille[line][colonne] == 1) and (self.grille[line +1][colonne +1]==1)and (self.grille[line +2][colonne +2]==1) and (self.grille[line +3][colonne +3]==1):
                        return True
                elif pion == 'B':
                    if (self.grille[line][colonne] == 2) and (self.grille[line +1][colonne +1] == 2) and (self.grille[line +2][colonne +2] == 2) and (self.grille[line +3][colonne +3] == 2):
                        return True
                else:
                    return False

    #methode pour savoir qui est le gagant ( 4 cases alignées diagonalement du haut à droit vers le bas à gauche)
    def est_gagant_d_asc (self,pion):
        for line in range(3):
            for colonne in range (3,7):
                if pion == 'N':
                    if (self.grille[line][colonne]==1) and (self.grille[line +1][colonne -1]==1)and (self.grille[line +2][colonne -2]==1) and (self.grille[line +3][colonne -3]==1):
                        return True
                elif pion == 'B':
                    if (self.grille[line][colonne] == 2) and (self.grille[line +1][colonne -1] == 2) and (self.grille[line +2][colonne -2] == 2) and (self.grille[line +3][colonne - 3] == 2):
                        return True
                else:
                    return False

    #methode pour savoir qui est le gagant dans tous les positions
    def est_gagant(self, pion):
        if (self.est_gagant_d_des(pion)) or (self.est_gagant_d_asc(pion)) or (self.est_gagant_h(pion)) or (self.est_gagant_v(pion)):
            return True
        else:
            return False




