import re
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mlp 

def program():

    doc = open('../job02/data.txt','r')
    a = doc.read()
    x = re.findall(r"([a-zA-Z]{1,})", a)
    wordSizeDict = {}
    checkDict = {}
    allSizes = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]

    #print(x)

    n = 0
    while n < len(x):

        wordSizeDict[x[n]] = len(x[n])

        key = wordSizeDict.get(x[n])

        checkDict[key] = 0

        n+=1
    
    b = 0

    while b < len(x):

        if(len(x[b]) == wordSizeDict.get(x[b])):

            checkDict[len(x[b])] = checkDict.get(len(x[b])) + 1
       
        b+=1

    print(checkDict)

    plt.style.use('dark_background')
    plt.title('Pourcentage d\'apparition de chaque taille de mot', fontsize = 15, fontweight = 'bold', color = 'pink')
    plt.xlabel('Tailles des mots', color = 'pink')
    plt.ylabel('Nombres de mots de chaque taille', color = 'pink') 

    c = 0
    while c < len(allSizes):

        if(checkDict.get(c)):
            #plt.hist(x, linewidth=2, edgecolor='#E6E6E6');
            plt.bar(allSizes[c],checkDict.get(c), color = 'pink')

        c+=1


    plt.show()
    

program()

