import re 

def program():

    doc =open('domains.xml','r')
    a = doc.read()
    x = re.findall(r"([.][a-z]{2,3})", a)

    print(len(x))

program()