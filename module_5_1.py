class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if 1 <= new_floor <= self.number_of_floors:
            print(f'{new_floor} этаж')
        else:
            print(
                f'{new_floor} - в "{h2.name}" такого этажа не существует. Выше {self.number_of_floors}-го этажа '
                f'не подняться.')


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
