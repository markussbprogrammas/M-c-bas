from abc import ABC, abstractmethod

class Transportlidzeklis(ABC):
    @abstractmethod
    def kustiba(self):
        pass


class Auto (Transportlidzeklis):
    def kustiba(self):
        return "Auto brauc pa ielu."

class Laiva (Transportlidzeklis):
    def kustiba(self):
        return"Laiva peld pa ūdeni."

    
transporti = [Auto(), Laiva()]

for transportlidzeklis in transporti:
    print(transportlidzeklis.kustiba())