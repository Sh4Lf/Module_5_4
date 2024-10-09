class House:

    houses_history = []

    def __new__(cls, *args):

        obj = super().__new__(cls)
        house_name = args[0]
        cls.houses_history.append(house_name)
        return obj

    def __init__(self, name):
        self.name = name

    def __del__(self):

        print(f"Дом '{self.name}' снесён, но он останется в истории.")


h1 = House('ЖК Немчиновка')
print(House.houses_history)
h2 = House('ЖК Минаевка')
print(House.houses_history)
h3 = House('ЖК Бордо')
print(House.houses_history)

del h2
del h3
del h1
print(House.houses_history)