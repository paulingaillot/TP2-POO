#Modularité

from Calculatrice.addition import addition
from Calculatrice.division import division
from Calculatrice.multiplication import multiplication
from Calculatrice.soustraction import soustraction

# Polymorphisme

class Animaux: 
    pattes=0

    def seDeplacer(self):
        print("Je me deplace")


class Chien(Animaux):
    pattes=4

    def seDeplacer(self):
        print("Je cours !")


class Aigle(Animaux):
    pattes=2

    def seDeplacer(self):
        print("Je vole")

class Requin(Animaux):
    pattes=0

    def seDeplacer(self):
        print("Je nage")


# Généricité 

def calculator(a,b):
    return int(a)+int(b)



def main():

    # Polymorphisme

    r = Requin()
    r.seDeplacer()

    c = Chien()
    c.seDeplacer()

    a = Aigle()
    a.seDeplacer()

    # Généricité 

    print(calculator(1,2))
    print(calculator(1.0,2))
    print(calculator(1.0,2.0))
    print(calculator("1","2"))

    #Modularité

    print(addition(1,2))
    print(soustraction(3.5,"2"))
    print(multiplication(1.2,2.5))
    print(division("20.8","2.5"))


if __name__ == "__main__":
    main()