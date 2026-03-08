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

    def affectervoiture(self, voiture):
        if self.voitureservice is not None:
            print(" On ne peut pas affecter la voiture car cet employee a deja une voiture de service ")

        elif voiture.chauffeur is not None:
            print("Cette voiture est deja affectee a un autre employe.")
        else:
            self.voitureservice = voiture
            voiture.chauffeur = self
            print("Voiture affectee avec succes.")