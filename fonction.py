class Prenom():

    def __init__(self):
        self.prenom = " "

    def pseudo(self):
        self.prenom = input("comment vous appeler vous? ")
        self.affichage()

    def affichage(self):
        print(self.prenom)

objet = Prenom()
objet.pseudo()
