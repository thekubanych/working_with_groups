
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