pyramide = ["#", "##", "###", "####"]
##########
# boucle sur une variable
##########
for x in pyramide:
    print(x)

##########
# boucle sur une range
##########
counter = 1
valeur = int(input("Choisis un nombre d'étages: "))

for x in range(valeur):
    print("#" * counter)
    counter += 1

#########
# boucle sur une condition | tant que x <= y, j'execute
#########
etages = 1

while etages <= 7:
    print("#"*etages)
    etages += 1
