import random
import sys

class ProgramaBot:

    def __init__(self, numUsuari):
        self.numUsuari = int(input("En quin nsmero estic pensant?"))
        self.count = 0
        nums.comprovar()

    def comprovar(self, numUsuari):

        if (numUsuari >= 1 and numUsuari <= 100):
            self.nAleatori = random.randint(1,100)
            numTrobat = False
            self.comprovar()
            while not numTrobat:
                for i in range(15):
                    if numUsuari != numAleatori:
                        count = i
                        numTrobat == False
                        print("Nmero incorrecte")
                        self.numUsuari = int(input("En quin nmero estic pensant?"))
                    else:
                        numTrobat == True
                        print("Nmero correcte")
        else :
            print("Valor incorrecte")

if __name__ == '__main__':
    nums = ProgramaBot(sys.argv[1])
    print nums.comprovar()

    
import random
import sys

class ProgramaBot:

    def __init__(self, numUsuari):
        self.numUsuari = int(input("Introdueix un nmero entre 0 i 100: "))
        self.count = 0
        nums.comprovar()

    def comprovar(self, numUsuari):

        if (numUsuari >= 1 and numUsuari <= 100):
            self.nAleatori = random.randint(0,100)
            numTrobat = False
            self.comprovar()
            while not numTrobat:
                for i in range(15):
                    if numUsuari != numAleatori:
                        count = i
                        numTrobat == False
                        print("Nmero incorrecte")
                        self.numUsuari = int(input(""))
                    else:
                        numTrobat == True
                        print("Nmero correcte")
                        print("L'has endevinat en " + str(count) + " intents.")
        else :
            print("El valor es troba fora del rang.")

if __name__ == '__main__':
    nums = ProgramaBot(sys.argv[1])
    print nums.comprovar()

    
    
    
    
    
