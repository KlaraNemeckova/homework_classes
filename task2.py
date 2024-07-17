import random

planets = ["Abafar", "Ahch-To", "Anaxes", "Bespin", "Cantonica", "Castilon", "Cato Neimoidia", "Corellia", "Coruscant",
           "Daiyu", "D'Qar", "Dagobah", "Dagobah", "Endor", "Exegol", "Felucia", "Hoth", "Iego", "Iridonia", "Jakku",
           "Jedha", "Kamino", "Kashyyyk", "Kessel", "Malastare", "Mandalore", "Mapuzo", "Mon Cala", "Mustafar", "Naboo",
           "Nevarro", "Ossus", "Pasaana", "Polis Massa", "Ryloth", "Saleucami", "Serenno", "Tatooine", "Umbara",
           "Utapau", "Wobani", "Yavin", "Zygerria"]


class Ship:
    def __init__(self, name, type, length):
        self.name = name
        self.type = type
        self.length = length

    def takes_off(self):
        global start
        start = random.choice(planets)
        print("Starting from {}.".format(start))

    def landing(self):
        end = random.choice(planets)
        if start == end:
            print("Change of plans, returns to {}.".format(end))
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
    def __int__(self, name, type, length, width, armament):
        super().__init__(name, type, length)
        self.width = width
        self.armament = armament

    def info(self, name, type, length, width, armament):
        print(f"Name: {name}, type: {type}, length: {length}, width: {width}, armament: {armament}")


class Cruiser(Ship):
    def __int__(self, name, type, length, roles, affiliation):
        super().__init__(name, type, length)
        self.roles = roles
        self.affiliation = affiliation

    def info(self, name, type, length, roles, affiliation):
        print(f"Name: {name}, type: {type}, length: {length},  roles: {roles}, affiliation: {affiliation}")


f = Frigate("Nebulon-B", "escort frigate", "300 m", "700 (medical patients)",
            "bacta tanks, medical droids, hospital")
f.info("Nebulon-B", "escort frigate", "300 m", "700 (medical patients)",
       "bacta tanks, medical droids, hospital")
f.takes_off()
f.landing()

print("-----")

d = Destroyer("Supremacy", "Star Destroyer - Star Dreadnought", "13 240 m")
d.info("Supremacy", "Star Destroyer - Star Dreadnought", "13 240 m", "60 543 m",
       "ion cannons, tractor beam projectors, 8 Resurgent-class Star Destroyers, TIE fighters")
d.takes_off()
d.landing()

print("-----")

c = Cruiser("Resurgent", "Star Destroyer - Battlecruiser", "2 916 m")
c.info("Resurgent", "Star Destroyer - Battlecruiser", "2 916 m",
       "Carrier, Destroyer, Military transport, Command ship", "First Order, Final Order")
c.takes_off()
c.landing()








