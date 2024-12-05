import turtle

#
t = turtle.Turtle()

def escalier(taille,nb_marche):
    for i in range(1,nb_marche):
        t.forward(taille)
        t.left(90)
        t.forward(taille)
        t.right(90)
    t.forward(taille)

def carre(taille):
    for i in range (1,5):
        t.forward(taille)
        t.left(90)
     

def carres(taille_initial,nb):
    for i in range(1,nb):
        carre(taille_initial*(i+1))



#escalier(30,10)

#carre(100)

carres(30,5)








turtle.done()