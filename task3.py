class Nikola:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        if self.name == "Никола":
            return f'меня зовут не {self.name}, а Никола, Лет {self.age}'
        else:
            return f'Имя = {self.name}, а лет {self.age} '

f = Nikola('Макс', 12)
print(f)