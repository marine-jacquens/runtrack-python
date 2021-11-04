def program():
    txt = str(input('Entrez votre texte '))
    doc = open('output.txt','w')
    doc.write(txt)
    doc.close()

program()