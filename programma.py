class Prece:
    def __init__(self, nosaukums, cena, daudzums="Nav informācijas"):
        self.nosaukums = nosaukums 
        self.cena = cena 
        self.daudzumms = daudzums 

    def cena_ar_pvn(self, pvn=21):
        return self.cena * (1 + pvn / 100)
prece1 = Prece("Dators", 1000)
prece2 = Prece("Televizors", 500, 10)
prece3 = Prece("Galds", 50)
print(prece1.cena_ar_pvn())
print("Preces nosaukums ir: " + prece3.nosaukums + " Preces cena ir: " + str(prece3.cena) +" ,Cena ar pvn ir " + str(prece3.cena_ar_pvn()))


class Persona:
    def __init__(self, vards, vecums):
        self.vards = vards
        self.__vecums = vecums

    def dabut_vecumu(self):
        return self.__vecums

    def iestatit_vecumu(self, vecums):
        if vecums > 0:
            self.__vceums = vecums
        else:
            print("Vecumam jābūt pozitīvam skaitlim.")

cilveks = Persona("Jānis", 25)
cilveks.iestatit_vecumu(10)
print(cilveks.vards)


class Dzivnieks:
    def __init__(self,vards):
        self.vards = vards

    def skan(self):
        pass

class Suns(Dzivnieks):
    def skan(self):
        return f"{self.vards} saka: vau-vau!"

class Kakis(Dzivnieks):
    def skan(self):
        return f"{self.vards} saka: Mjau!"
suns = Suns("Reksis")
kakis = Kakis("Minka")

print(suns.skan())
print(kakis.skan())
print(suns.vards)

