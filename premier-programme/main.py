def demander_nom():
    reponse_nom=""
    while(reponse_nom==""):
        try:
            reponse_nom=input("Quel est votre nom ?:")
        except:
            print("Entrez un nom valid")
    return reponse_nom


def demander_age():
    age_int=0
    while age_int == 0:
        age_str=input("Quel est votre age ?")
        try:
            age_int=int(age_str)
        except:
            print("ERREUR: vous devez rentrer un nombre pour l'age")
    return age_int


nom=demander_nom()
age=demander_age()
while (nom==""):
    nom=input("Quel est votre nom ?")
print("votre nom est " + nom)
print("votre age est " + str(age))

if(age<10):
    print('Vous etes enfant')
elif(age==17):
    print('Vous etes presque majeur')
elif (age ==18):
    print('Tout juste majeur: Felicitations')
elif (age>60):
    print('Vous etes senior')
elif (age>=18):
    print('Vous etes majeur')
else:
    print("Vous etes mineur")
