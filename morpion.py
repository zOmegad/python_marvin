class Joueur():
    def __init__(self):
        self.joueur_1 = "X"
        self.joueur_2 = "O"
        self.joueur_actuel = self.joueur_1

    def changer_joueur(self):
        if self.joueur_actuel == self.joueur_1:
            self.joueur_actuel= self.joueur_2
        elif self.joueur_actuel == self.joueur_2:
            self.joueur_actuel = self.joueur_1


class Jeu():
    def __init__(self):
        self.partie_fini = False
        self.coup = ""

    def jouer(self, carte, joueur):
        while self.partie_fini is False:
            carte.affichage()
            self.selection(joueur, carte)
            self.victoire(carte, joueur)
            joueur.changer_joueur()

        joueur.changer_joueur()
        carte.affichage()
        print("GG , "+ joueur.joueur_actuel+ " a gagner")

    def victoire(self, carte, joueur):
        print(joueur.joueur_actuel)
        if carte.grille["1"] == joueur.joueur_actuel:
            if carte.grille["2"] == joueur.joueur_actuel:
                if carte.grille["3"] == joueur.joueur_actuel:
                    self.partie_fini = True
            if carte.grille["5"] == joueur.joueur_actuel:
                if carte.grille["9"] == joueur.joueur_actuel:
                    self.partie_fini = True
            if carte.grille["4"] == joueur.joueur_actuel:
                if carte.grille["7"] == joueur.joueur_actuel:
                    self.partie_fini = True
        if carte.grille["3"] == joueur.joueur_actuel:
            if carte.grille["6"] == joueur.joueur_actuel:
                if carte.grille["9"] == joueur.joueur_actuel:
                    self.partie_fini = True
            if carte.grille["5"] == joueur.joueur_actuel:
                if carte.grille["7"] == joueur.joueur_actuel:
                    self.partie_fini = True
        if carte.grille["5"] == joueur.joueur_actuel:
            if carte.grille["4"] == joueur.joueur_actuel:
                if carte.grille["6"] == joueur.joueur_actuel:
                    self.partie_fini = True
            if carte.grille["2"] == joueur.joueur_actuel:
                if carte.grille["8"] == joueur.joueur_actuel:
                    self.partie_fini = True
        if carte.grille["7"] == joueur.joueur_actuel:
            if carte.grille["8"] == joueur.joueur_actuel:
                if carte.grille["9"] == joueur.joueur_actuel:
                    self.partie_fini = True


    def selection(self, joueur, carte):
        tour = False
        while tour is False:
            self.coup = int(input("joueur " + joueur.joueur_actuel + " choisi un coup!"))
            if self.coup in range(1,10):
                if carte.grille[str(self.coup)] == " ":
                    carte.grille[str(self.coup)] = joueur.joueur_actuel
                    return True
                else:
                    print("coup indisponible")
            else:
                print("votre coup n'est pas valide veuiller recommencer")


class Carte():
    def __init__(self):
        self.grille = {"1": " ", "2": " ", "3": " ", "4": " ", "5": " ", "6": " ", "7": " ", "8": " ", "9": " "}

    def affichage(self):
        print(self.grille["1"] + "|" + self.grille["2"] + "|" + self.grille["3"])
        print("—————")
        print(self.grille["4"] + "|" + self.grille["5"] + "|" + self.grille["6"])
        print("—————")
        print(self.grille["7"] + "|" + self.grille["8"] + "|" + self.grille["9"])

carte = Carte()
joueur = Joueur()
jeu = Jeu()
jeu.jouer(carte, joueur)

#placé un coup sur la grille
#vérifié que le coup existe et que la case et bien libre
#vérifié la victoire
