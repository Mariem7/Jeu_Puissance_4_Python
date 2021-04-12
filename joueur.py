#classe du joueur
class Joueur:

    def __init__(self,nom,pion):
        self.nom = nom  #Nom du joueur:
        # Le pion choisi par le joueur:
        self.pion = pion
        #Le nombre de pions au début de chaque partie est 21:
        self.nombre_total_pions=21
        # Nombre de parties gagnées par le joueur:
        self.nb_parties_gagnees = 0

    #methode pour demander le type de pion
    def demander_pion():
        pion=input("Veuillez choisir le couleur de votre pion (N/B): ")
        while pion not in ['N','B']:
            pion=input("Veuillez respecter la contrainte du choix du pion (N/B)!\nRessayez S.V.P: ")
        return pion