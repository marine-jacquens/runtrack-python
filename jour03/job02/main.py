import re 

def program():

    doc =open('data.txt','r')
    a = doc.read()
    x = re.findall(r"([a-zA-Z]{1,})", a)

    print(len(x))

program()