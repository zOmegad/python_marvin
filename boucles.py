legumes = ["Salade", "Carotte", "Choux", "Aubergine"]

##############
# boucle sur une variable
##############
for x in legumes:
    print(x)
##############
# boucle sur une range
##############
def pyra():
    counter = 1
    valeur = int(input("choisi un nombre d'etage: "))

    for etage in range(7):
        print("#" * counter)
        counter += 1
##############
# boucle sur une condition / tant que x <= y, j'execute
##############
etage = 1

while etage <= 7:
    print("#"*etages)
    etage += 1
