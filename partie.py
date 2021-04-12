#--------------------------------------jeu puissance 4------------------------------------#
#--------------------------------------realisé par Neili Mariem FIA-01 groupe 1----------#
#--------------------------------------date de reception : 15/02/2021--------------------#

from Grille import Grille
from joueur import Joueur

#classe partie
class partie:
    def __init__(self,Grille):
        self.joueurs =[] #liste des deux joueurs du jeu
        self.joueur_actuel=None #attribut joueur actuel est le joueur qui joue dans chaque partie(joueur 1 ou 2)
        self.nb_parties_nulles=0 #nombre de parties nulles (personne n'a pas gagné)

    def start(self,Grille):
        #départ du jeu
        print("----Bienvenue au jeu Puissance 4----")
        #le menu du jeu
        print("----------------Menu-----------------")
        print("1- Commencer.")
        print("0- Quitter.")
        print("-----------------------------------")
        r= int(input("Veuillez choisir une option du menu du jeu: "))
        while r not in [0,1]:
            r= int (input("Veuillez respecter le chiffre des options données! "))
        if (r==0):
            print("----Merci et au revoir----")
            exit()
        else:
            #le premier joueur:
            print("-----Le permier joueur------")
            #demander le nom du permier joueur
            n1=input("Entrez votre nom: ")
            pion1= Joueur.demander_pion()
            j1= Joueur(n1,pion1)

            # le deuxieme joueur:
            print("-----Le deuxieme joueur------")
            # demander le nom du deuxieme joueur
            n2 = input("Entrez votre nom: ")
            #le pion du deuxieme joueur depend du 1 er joueur
            if pion1 =='N':
                pion2 = 'B'
            else:
                pion2 ='N'
            j2 = Joueur(n2, pion2)

        #l'ajout des joueurs à la liste des joueurs:
        self.joueurs.append(j1)
        self.joueurs.append(j2)

        recommence="" #variable qui contient le choix du joueur après la fin du jeu

        #la boucle du jeu
        while (True):
            #initilaliser la grille pour chaque nouvelle partie
            G.initialiser()
            self.tour(G)
            print(G)
            print("Partie terminée")
            if Grille.est_gagant(j1.pion):
                j1.nb_parties_gagnees +=1
                print("Partie gagnée par:", j1.nom)
            elif Grille.est_gagant(j2.pion):
                j2.nb_parties_gagnees += 1
                print("Partie gagnée par:", j2.nom)
            elif (not Grille.non_plein()):
                self.nb_parties_nulles +=1
                print("Partie nulle!")

            #les statistiques du jeu:
            print("---------------------------------------")
            print("les statistiques du jeu:")
            print("---------------------------------------")
            print ("Parties gagnées par ",j1.nom,":",j1.nb_parties_gagnees)
            print ("Parties gagnées par ",j2.nom,":",j2.nb_parties_gagnees)
            print ("Parties nulles",self.nb_parties_nulles)
            recommence= input("Voulez vous recommencer (Y/N): ")
            while recommence not in['Y','N']:
                recommence = input("Veuillez choisir une lettre parmi (Y/N)!: ")
            if (recommence == 'Y'):
                #une séparation entre les tours du jeu
                print('\n')
                print("------------Nouveau Tour-------------")
                print('\n')
            #sinon on sort du boucle du jeu
            else:
                break

        #fin du jeu
        print("----Merci bien et au revoir----")

    #methode de tour
    def tour(self,Grille):
        #variable qui va parcourir la liste des joueurs (joueur 1 ou joueur 2)
        p=0
        while(self.joueurs[0].nombre_total_pions !=0 and self.joueurs[1].nombre_total_pions !=0 and Grille.non_plein() and not Grille.est_gagant(self.joueurs[0].pion) and not Grille.est_gagant(self.joueurs[1].pion)):
            self.joueur_actuel=self.joueurs[p]
            print("c'est le tour de :",self.joueur_actuel.nom)
            print(Grille)
            c=Grille.demander_colonne()
            Grille.inserer_case(c,p)
            self.joueur_actuel.nombre_total_pions -=1
            print("---------------------------------------\n")
            p=p+1
            p=p%2


#le main du jeu
if __name__ == "__main__":
    G=Grille()
    p= partie(G)
    p.start(G)
    exit()
