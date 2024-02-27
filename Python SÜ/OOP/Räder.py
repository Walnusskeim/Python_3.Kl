"""
Class practice
Maximilian
❤
26.02.2024
"""

class Rad:
    def __init__(self, hersteller, preis, gaenge):
        self.hersteller = str(hersteller)
        self.preis = float(preis)
        self.gaenge = int(gaenge)


    def __str__(self):
        return f"Hersteller: {self.hersteller}, Preis: {self.preis}, Gaenge: {self.gaenge}"


    def fahren(self):
        return "Fahren"

class Mountainbike(Rad):
    def __init__(self, hersteller, preis, gaenge, federung):
        super().__init__(hersteller, preis, gaenge)
        self.federweg = int(federweg)


    def __str__(self):
        return super().__str__() + f", Federweg: {self.federweg}"


    def schreddern(self):
        if self.federweg > 100:
            return "Schreddern"
        else:
            return "Nicht schreddern"



if __name__ == "__main__":
    bike1 = Rad("Hersteller1", 1000, 21)
    bike2 = Rad("Hersteller2", 1500, 24)
    bike3 = Mountainbike("Hersteller3", 2000, 27, 160)
    bike4 = Mountainbike("Hersteller4", 2500, 30, 180)

    for bike in [bike1, bike2, bike3, bike4]:
        print(bike)
        print(bike.fahren())
        if isinstance(bike, Mountainbike):
            print(bike.schreddern())
        print("\n")
