class House:
    def __init__(self, name, number_of_floor):
        self.name = name
        self.number_of_floor = number_of_floor

    def go_to(self, new_floor):
        if (new_floor > self.number_of_floor or new_floor < 1):
            return print("Такого этажа не существует")

        floor = 1
        while floor <= new_floor:
            print(floor)
            floor += 1


h1 = House("ЖК Эльбрус", 30)
h2 = House("ЖК Звездный", 7)

h1.go_to(7)
h2.go_to(9)

print(h1.name, h1.number_of_floor)
print(h2.name, h2.number_of_floor)

