import random

planets = ["Abafar", "Ahch-To", "Anaxes", "Bespin", "Cantonica", "Castilon", "Cato Neimoidia", "Corellia", "Coruscant",
           "Daiyu", "D'Qar", "Dagobah", "Dagobah", "Endor", "Exegol", "Felucia", "Hoth", "Iego", "Iridonia", "Jakku",
           "Jedha", "Kamino", "Kashyyyk", "Kessel", "Malastare", "Mandalore", "Mapuzo", "Mon Cala", "Mustafar", "Naboo",
           "Nevarro", "Ossus", "Pasaana", "Polis Massa", "Ryloth", "Saleucami", "Serenno", "Tatooine", "Umbara",
           "Utapau", "Wobani", "Yavin", "Zygerria"]

class Ship:
    def __init__(self, type, length):
        self.type = type
        self.length = length

    def starting(self):
        pass

    def landing(self):
        pass
        # pokud stejné --> "change of plans, returns to ___"


class Frigate(Ship):
    pass


class Destroyer(Ship):
    pass


class Cruiser(Ship):
    pass


# random name- Cruiser, Destroyer, Frigate
# přidat další lodě