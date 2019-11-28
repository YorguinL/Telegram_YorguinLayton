
import random
import sys

class ProgramaBot:

    def __init__(self):
        self.idUsuari = ""
        self.numUsuari = 0
        self.count = 0
        self.nAleatori = random.randint(1,101)
        self.rangValid = False
        self.solucio = False


    def comprovar(self):
        numTrobat = False
        if self.numUsuari in range(101):
            self.count +=1
            self.rangValid = True
            if not numTrobat:
                if self.numUsuari != self.nAleatori:
                    numTrobat == False
                    print("Nmero incorrecte, torna-ho a intentar")
                    self.solucio = False
                else:
                    numTrobat == True
                    print("Nmero correcte")
                    self.solucio = True
                    print("L'has endevinat en " + str(self.count) + " intents.")
        else:
            self.rangValid = False
            print("Estas fora del rang")
