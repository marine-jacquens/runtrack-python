class Personne:
    nom = ""
    prenom = ""

    def __init__(self,nom,prenom):
        self.nom = nom
        self.prenom = prenom

    def SePresenter(self):
        print(self.nom)
        print(self.prenom)

    def get_nom(self):
        return self.nom
    
    def get_prenom(self):
        return self.prenom
    
    def set_nom(self,nom):
        self.nom = nom
    
    def set_prenom(self,prenom):
        self.prenom = prenom

personne1 = Personne("Jacquens", "Marine")
personne2 = Personne("Giannotti", "Louis")
personne3 = Personne("Jacquens", "Elodie")

personne1.SePresenter()
personne1.set_nom("Roset")
print(personne1.get_nom())

personne2.SePresenter()
personne2.set_prenom("John")
print(personne2.get_prenom())
