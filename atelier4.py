class Employee:
    def __init__(self, numpermis, nom, prenom):
        self.numpermis=numpermis
        self.nom=nom
        self.prenom=prenom
        self.voitureservice=None

    def afficherInformations(self):
        print("Numero de permis :", self.numpermis)
        print("Nom :", self.nom)
        print("Prenom :", self.prenom)

        if self.voitureservice is None:
            print("Voiture de service : aucune")
        else:
            print("Voiture de service :", self.voitureservice.matricule)