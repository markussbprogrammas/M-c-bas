from math import pow, pi 
class Forma:
    def nosaukums(self):
        pass
    def laukums(self):
        pass

class Aplis(Forma):
    def __init__(self, radiuss):
        self.radiuss = radiuss
    def nosaukums(self):
        return "Aplis"

    def laukums(self):
        return pi * self.radiuss ** 2

class Kvadrats(Forma):
    def __init__(self, mala):
        self.mala= mala
    def nosaukums(self):
        return "Kvadrats"

    def laukums(self):
        return self.mala ** 2


class Taisnsturis:
    def __init__(self, mala1, mala2):
        self.mala1 = mala1
        self.mala2 = mala2
    def nosaukums(self):
        return "Taisnsturis"  
        

    def laukums(self):
        return self.mala1 * self.mala2

nosaukumi = [Aplis.nosaukums(""), Kvadrats.nosaukums(""),Taisnsturis.nosaukums("")]
formas= [Aplis(5), Kvadrats(4), Taisnsturis(5,8)]


for forma in formas:
    print(f"Nosaukums ir : {forma.nosaukums()} Laukums ir: {"{:.3f}".format (round(forma.laukums(), 3))}")
