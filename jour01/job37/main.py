import re 

word = str(input('Entrez un mot '))

def swap(string):
    
    combo1 = word[0] + word[1] + word[3] + word[2] 
    combo2 = word[0] + word[2] + word[1] + word[3] 
    combo3 = word[1] + word[0] + word[2] + word[3] 

    list = [combo3, combo1, combo2]
    print(list)
    list.sort()
    return list[0]

def checkWord():
    newWord = ''
    check = re.findall(r"^[a-z]$",word)
    if(re.findall(r"^[a-z]{4}$",word)):
        print(swap(word))
    else:
        print('erreur')

checkWord()
