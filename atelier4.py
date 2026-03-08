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

    def retirervoiture(self):

        if self.voitureservice is None:
            print("Cet employe n'a pas de voiture de service.")
        else:
            self.voitureservice.chauffeur = None
            self.voitureservice = None
            print("Voiture retiree avec succes.")

class Voiture:
   def __init__(self, matricule, annee, marque, kilometrage):
      self.matricule=matricule
      self.annee=annee
      self.marque=marque
      self.kilometrage=kilometrage
      self.chauffeur=None

   def afficherInformations(self):
       print(f" matricule : {self.matricule}")
       print(f" annee : {self.annee}")
       print(f" Marque : {self.marque}")
       print(f" kilometrage : {self.kilometrage}")
       if self.chauffeur is None:
           print("La voiture n'appartient a aucun chauffeur ")
       else:
           print(" La voiture appartient a : ", self.chauffeur.nom)

e1=Employee("A0","Malika","Hdd")
e2=Employee("A1","Nada","Bch")
e3=Employee("A2","Adem", "Haddad")

v1=Voiture("AO1",2020,"Mercedes", 150000)
v2=Voiture("AO2",2022,"Jeep", 100000)
v3=Voiture("AO3",2025,"TOYOTA",30000)
e1.afficherInformations()
e2.afficherInformations()
e3.afficherInformations()
v1.afficherInformations()
v2.afficherInformations()
v3.afficherInformations()