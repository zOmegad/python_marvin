# variable = input(phrase)

nom = input("ton nom de famille ")
prenom = input("tu t'appel ")
age = input("tu as ")

# nom de la liste (variable.) + methode(x)

info = []
info.append(nom)
info.append(prenom)
info.append(age)

print(info)

#Dictionnaire

personne = {}
personne['nom'] = nom
personne['prenom'] = prenom
personne['age'] = age
print(personne)
