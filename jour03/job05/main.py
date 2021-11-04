import re
import matplotlib.pyplot as plt
import matplotlib as mlp 



def program():

    doc = open('../job02/data.txt','r')

    alphabetMaj = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    alphabetMin = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    alphabetDict = {'A':0,'B':0,'C':0,'D':0,'E':0,'F':0,'G':0,'H':0,'I':0,'J':0,'K':0,'L':0,'M':0,'N':0,'O':0,'P':0,'Q':0,'R':0,'S':0,'T':0,'U':0,'V':0,'W':0,'X':0,'Y':0,'Z':0}
    
    a = doc.read()
    x = re.findall(r"[a-z]",a,re.IGNORECASE)
    n = 0 

    while n < len(x):

        b = 0

        while b < 26:

            if(x[n] == alphabetMaj[b] or x[n] == alphabetMin[b]):
                letter = alphabetMaj[b]
                alphabetDict[letter] = alphabetDict.get(letter)+1

            b+=1
                
        n+=1
    
    print('dictionnaire : ', alphabetDict)
    
    c = 0
    while c < 26:
        
        plt.style.use('dark_background')
        plt.bar(alphabetMaj[c],alphabetDict.get(alphabetMaj[c]), color = 'yellow')
        plt.title('Pourcentage d\'apparition des lettres', fontsize = 15, fontweight = 'bold', color = 'yellow')
        plt.xlabel('Les lettres', color = 'yellow')
        plt.ylabel('Nombres d\'occurences par lettre', color = 'yellow')

        c +=1

    plt.show()

program()

