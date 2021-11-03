class Livre:

    titre =""

    def __init__(self,titre):
        self.titre = titre
    
    def print(self):
        print(self.titre)

class Personne:

    def __init__(self,nom,prenom):
        self.nom = nom
        self.prenom = prenom
    
    def printname(self):
        print(self.nom, self.prenom)

class Auteur(Personne):

    oeuvre =[]

    def __init__(self,nom,prenom):
        Personne.__init__(self,nom,prenom)

    def listerOeuvre(self):
        print(self.oeuvre)
    
    def ecrireUnLivre(self,titre):
        return (titre)

    def set_oeuvre(self,titre):
        self.oeuvre.append(titre)

jk = ['Harry Potter à l\'école des sorciers','Harry Potter et la chambre des secrets']


p1 = Auteur("Rowling","J.K")

# à revoir
titre = p1.ecrireUnLivre("Harry Potter et le prisonnier d'Azkaban")
p2 = Livre(titre)
p1.set_oeuvre(titre)
p1.listerOeuvre()


# p2.p1 = p1
# p1.display()
# p2.print()
# p1.p2 = p2
# p2.display()
# p1.display()














# def get_oeuvre(self,oeuvre):
# return self.oeuvre 
    
# def get_titre(self,titre):
# return self.titre 


    
# def set_titre(self,titre):
# self.titre = titre