import re 

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
        return(self.oeuvre)
    
    def ecrireUnLivre(self,titre):
        return (titre)

    def set_oeuvre(self,titre):
        self.oeuvre.append(titre)

class Client(Personne):

    nom = ""
    prenom = ""
    collection = []

    def __init__(self,nom,prenom):
        Personne.__init__(self,nom,prenom)

    def set_collection(self,livre):
        self.collection.append(livre) 
    
    def get_collection(self):
        return self.collection
    
    def inventaire(self):
        print(collection)


class Bibliotheque(Auteur):
    nom = ""
    catalogue = {} 

    def __init__(self,nom):
        self.nom = nom
        
    def set_catalogue(self,livre,quantite):
        self.catalogue[livre] = quantite

    def acheterLivre(self,auteur,livre,quantite):
        
        n = 0
        listeAuteurLivres = auteur.listerOeuvre()
        while n < len(listeAuteurLivres):
            if(listeAuteurLivres[n] == livre):
                self.catalogue[livre] = quantite
            n+=1
    
    def inventaire(self):
        print(self.catalogue)
    
    def louer(self,client,livre):

        n = 0
        while n < len(self.catalogue):
            if(self.catalogue.get(livre) > 0):
                client.set_collection(livre)
                self.catalogue[livre] = self.catalogue.get(livre) - 1
                break
            else:
                print('Y\'en a pas')  
            n+=1
    
    def rendreLivres(self,client):
        
        n = 0
        while n < len(client.collection):

            livreClient = client.collection[n]
            if(self.catalogue[livreClient]):
                client.collection.remove(livreClient)
                self.catalogue[livreClient] = self.catalogue.get(livreClient)+1
                continue
            n+=1



biblio = Bibliotheque("Fantastique")
auteur = Auteur("Rowling","J.K")
auteur.set_oeuvre('Harry Potter et la chambre des secrets')
auteur.set_oeuvre('Harry Potter à l\'école des sorciers')
auteur.set_oeuvre('Harry Potter et le prisonnier d\'Azkaban')
auteur.printname()
print(auteur.listerOeuvre())
biblio.acheterLivre(auteur,'Harry Potter et la chambre des secrets',5) 
biblio.set_catalogue('Harry Potter à l\'école des sorciers',25) 
biblio.set_catalogue('Harry Potter et le prisonnier d\'Azkaban',15) 
print(biblio.inventaire())
client = Client("Jacquens","Marine")
client.printname()
biblio.louer(client,'Harry Potter et la chambre des secrets')
biblio.louer(client,'Harry Potter et le prisonnier d\'Azkaban')
print(client.get_collection())
print(biblio.inventaire())
biblio.rendreLivres(client)
print(client.get_collection())
print(biblio.inventaire())

