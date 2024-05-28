
class Utilisateur():
    def __init__(self, name):
        self.prenom= name
        self.status = 'iscrit'
        self.age=10
        print("Création d'un utilisateur")
        print("Nom: {}\nAge: {}\nStatus: {}".format(name,self.age, self.status))

    statut = 'inscrit'

    def setNom(self,name):
        self.nom = name

Pierre= Utilisateur("Pierre")

class Utilisateur:
    anciennete=0
    def __init__(self,name,age):
        self.user_name = name
        self.user_age = age
    def getNom(self):
        print("Salut!, je suis, self.user_name")
class Client(Utilisateur):
    is_client = True
eric = Utilisateur("Eric", 30)
pierre = Client("Pierre", 15)
pierre.user_name 
print(pierre.is_client)

class Utilisateur:
    status='inscrit'
    age=10

    def setNom(self, name):
        self.nom = name
Pierre= Utilisateur()
print(Pierre.setNom('Pierre'))
print(Pierre.status)
print(Pierre.age)

"""
class Client(Utilisateur):
    is_client = True
    anciennete = 10
    def __init__(self,nom,age,mail):
        self.user_name = nom
        self.user_age = age
        self.user_mail = mail
    def getNom(self):
        print("Je suis",self.user_name".Mon mail est",self.user_mail)
Pierre = Client("Nedh",19,pierre.L@issea-ce)
(‘Pierre’,25,

with open('code.txt','w') as cours:
    cours.write("je suis un goat et pas Sessi\nla question un est une question pertinante")
"""