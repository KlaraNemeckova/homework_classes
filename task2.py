import random

planets = ["Abafar", "Ahch-To", "Anaxes", "Bespin", "Cantonica", "Castilon", "Cato Neimoidia", "Corellia", "Coruscant",
           "Daiyu", "D'Qar", "Dagobah", "Dagobah", "Endor", "Exegol", "Felucia", "Hoth", "Iego", "Iridonia", "Jakku",
           "Jedha", "Kamino", "Kashyyyk", "Kessel", "Malastare", "Mandalore", "Mapuzo", "Mon Cala", "Mustafar", "Naboo",
           "Nevarro", "Ossus", "Pasaana", "Polis Massa", "Ryloth", "Saleucami", "Serenno", "Tatooine", "Umbara",
           "Utapau", "Wobani", "Yavin", "Zygerria"]
start = random.choice(planets)
end = random.choice(planets)


class Ship:
    def __init__(self, name, type, length):
        self.name = name
        self.type = type
        self.length = length

    def takes_off(self):
        print("Starting from {}.".format(start))

    def landing(self):
        if start == end:
            print("Change of plans, returns to {}.".format(start))
        else:
            print("Landing on {}.".format(end))


class Frigate(Ship):
    def __init__(self, name, type, length, passengers, equipment):
        super().__init__(name, type, length)
        self.passengers = passengers
        self.equipment = equipment

    def info(self, name, type, length, passengers, equipment):
        print(f"Name: {name}, type: {type}, length: {length}, passengers: {passengers}, equipment: {equipment}")

class Destroyer(Ship):
    def __int__(self, name, type, length):
        super().__init__(name, type, length)
    pass


class Cruiser(Ship):
    def __int__(self, name, type, length):
        super().__init__(name, type, length)
    pass


f = Frigate("Nebulon-B", "escort frigate", "300 m", "700 (medical patients)",
            "bacta tanks, medical droids, hospital")
f.info("Nebulon-B", "escort frigate", "300 m", "700 (medical patients)",
       "bacta tanks, medical droids, hospital")
f.takes_off()
f.landing()


# random name- Cruiser, Destroyer, Frigate
# přidat další lodě