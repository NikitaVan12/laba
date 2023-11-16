class Soda:
    def __init__(self, add):
        self.add = add

    def show_my_drink(self):
        if self.add:
            print(f"Газировка и {self.add}")
        else:
            print("Обычная газировка")

soda1 = Soda(1)
soda1.show_my_drink()

soda2 = Soda("Кола")