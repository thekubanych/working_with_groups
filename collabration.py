
class MyYears:
    def __init__(self, age):
        self.age = age

    def get(self):
        return self.age

    def append(self, x):
        self.age = f'Бир жылдан кийн {x}'



a = MyYears(16)
a.append(15)
print(a.get())

class Doniko:
    def __init__(self, name):
        self.name = name


    def get_info(self):
        return self.name

D = Doniko('Daniel')
print(D.get_info())