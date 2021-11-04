import re

def program():
    nbr = int(input('Entrez un nombre entier '))
    doc = open('../job02/data.txt','r')
    a = doc.readline()
    x = re.findall(r"([a-zA-Z]{1,})", a)

    compteur = 0

    n = 0
    while n < len(x):

        if(len(x[n]) == nbr):
            compteur+=1
        n+=1
    
    print(compteur)


program()