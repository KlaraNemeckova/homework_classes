class Device:
    def __init__(self, category):
        self.category = category

    def turn_on(self, category):
        pass

    def turn_off(self, category):
        pass


class CoffeeMachine(Device):
    def __init__(self, category, brand, year, color):
        super().__init__(category)
        self.brand = brand
        self.year = year
        self.color = color


    def informations(self, brand, year, color):
        print(f"Coffee machine - brand: {brand}, year of production: {year}, color: {color}")


class Blender(Device):
    def __init__(self, category, brand, year, wattage):
        super().__init__(category)
        self.brand = brand
        self.year = year
        self.wattage = wattage

    def informations(self, brand, year, wattage):
        print(f"Blender - brand: {brand}, year of production: {year}, wattage: {wattage}")


class MeatGrinder:
    def __init__(self, brand, year, wattage):
        super().__init__(brand)
        self.year = year
        self.wattage = wattage

    def informations(self, brand, year, wattage):
        print(f"Meat Grinder - brand: {brand}, year of production: {year}, wattage: {wattage}")


d = Device("Kitchen Appliances")
print(d.category)
c = CoffeeMachine("Kitchen Appliances", "Bosch", "2015", "black & grey")
c.informations("Bosch", "2015", "black & grey")


# Blender - Philips, 1000 W, 2 l
#Grinder - Tefal, 2200 W








