n = int(input("indiquer un nombre d'étages: "))
pyramide = '#'
print(" " *(n+1) + pyramide)

for x in range(n):
    pyramide += '##'

    print(' ' * (n-x) + pyramide)
