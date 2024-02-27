class Rad:
    def __init__(self, hersteller, preis, gaenge):
        self.hersteller = hersteller
        self.preis = preis
        self.gaenge = gaenge

    def __str__(self):
        return (f"Rad info: Hersteller={self.hersteller}" +
                f"mit {self.gaenge} Gaengen kostet â‚¬{self.preis}")

    def fahren(self):
        print(f"Ich fahre ein {self.hersteller} bike!")


class Mountainbike(Rad):
    def __init__(self, hersteller, preis, gaenge, federweg):
        super().__init__(hersteller, preis, gaenge)
        self.federweg = federweg

    def __str__(self):
        return (f"Mountainbike! {super().__str__()} und" +
                f"hat {self.federweg} mm Federweg!")

    def shredern(self):
        if self.federweg < 100:
            print("langsam, langsam")
        elif self.federweg < 150:
            print("macht schon Freude :)")
        else:
            print("Juhu! Shredern like Fabio Wibmer")


if __name__ == "__main__":

    r1 = Rad("Puch", 350, 1)
    r2 = Rad("KTM", 1350, 12)
    m1 = Mountainbike("Cube", 5000, 12, 120)
    m2 = Mountainbike("Rotwild", 7000, 12, 170)
    bike_list = [r1, r2, m1, m2]
    for bike in bike_list:
        print(bike)
        bike.fahren()
        if isinstance(bike, Mountainbike):
            bike.shredern()