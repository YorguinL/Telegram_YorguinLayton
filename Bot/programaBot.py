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
