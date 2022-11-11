#Modularité

from math import sqrt
from random import *
from Calculatrice.addition import addition
from Calculatrice.division import division
from Calculatrice.multiplication import multiplication
from Calculatrice.soustraction import soustraction

# Polymorphisme

class Animaux: 
    pattes=0

    def seDeplacer(self):
        pass


class Chien(Animaux):
    pattes=4

    def seDeplacer(self):
        print("Je cours !")


class Aigle(Animaux):
    pattes=2

    def seDeplacer(self):
        print("Je vole !")

class Requin(Animaux):
    pattes=0

    def seDeplacer(self):
        print("Je nage !")


# Généricité 

def add(a, b):
    return a + b



def main():

    # Polymorphisme
    print("Exemple Polymorphisme")
    animal = Requin()
    animal.seDeplacer()

    animal = Chien()
    animal.seDeplacer()

    animal = Aigle()
    animal.seDeplacer()

    # Généricité 
    print("\nExemple Généricité")
    print(add("Bon", "jour"))
    print(add(1, 2))

    #Modularité1
    print("\nExemple Modularité")
    print(sqrt(4))
    print(randint(1, 10))

    #Modularité2
    print("\nExemple Modularité")
    print(addition(1,2))
    print(soustraction(3.5,"2"))
    print(multiplication(1.2,2.5))
    print(division("20.8","2.5"))

if __name__ == "__main__":
    main()