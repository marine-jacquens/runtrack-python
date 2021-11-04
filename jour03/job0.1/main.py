def program():
    txt = str(input('Entrez votre texte '))
    doc = open('output.txt','w')
    doc.write(txt)
    doc.close()
    doc =open('output.txt','r')
    print(doc.read())

program()