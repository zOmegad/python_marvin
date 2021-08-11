fruits = ["Pomme", "Poire", "Banane", "Abricot"]
# la liste commence avec l'élément 0 .... +x

print(fruits[1])
print(fruits.index("Poire"))
fruits.append("Pomme")
print(fruits)

print(fruits.count("Poire"))

fruits.sort()
print(fruits)

def lol():
    personnage = {"Nom": "Simon", "Age": 22, "fruits": fruits}
    # Dictionnaire: comporte une clé et sa valeure
    print(personnage)
    print(personnage["Age"])

    date = (1998)
    # Tuple, valeur que je ne souhaite pas modifier
    print(date)
