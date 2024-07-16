class Device:
    def __init__(self, category):
        self.category = category


    def description(self):
        print("It is a type of {}".format(self.category))

    def turn_on(self):
        print("The device is switched on.")

    def turn_off(self):
        print("The device is switched off.")

    def broken(self):
        print("The device is broken.")


class CoffeeMachine(Device):
    def __init__(self, category, brand, year, color):
        super().__init__(category)
        self.brand = brand
        self.year = year
        self.color = color

    def informations(self, brand, year, color):
        print(f"Coffee machine - brand: {brand}, year of production: {year}, color: {color}")


class Blender(Device):
    def __init__(self, category, brand, year, wattage, volume):
        super().__init__(category)
        self.brand = brand
        self.year = year
        self.wattage = wattage
        self.volume = volume


    def informations(self, brand, year, wattage, volume):
        print(f"Blender - brand: {brand}, year of production: {year}, wattage: {wattage}, volume: {volume}")


class MeatGrinder(Device):
    def __init__(self, category, brand, year, wattage):
        super().__init__(category)
        self.brand = brand
        self.year = year
        self.wattage = wattage

    def informations(self, brand, year, wattage):
        print(f"Meat Grinder - brand: {brand}, year of production: {year}, wattage: {wattage}")


d = Device("Kitchen Appliances")
print(d.category)
print()

c = CoffeeMachine("Kitchen Appliances", "Bosch", "2015", "black & grey")
c.informations("Bosch", "2015", "black & grey")
c.turn_on()

print()

b = Blender("Kitchen Appliances", "Philips", "2019", "1000 W", "2 l")
b.informations("Philips", "2019", "1000 W", "2 l")
b.broken()


print()

g = MeatGrinder("Kitchen Appliances", "Tefal", "2012", "2200 W")
g.informations("Tefal", "2012", "2200 W")
g.turn_off()

g.description()
