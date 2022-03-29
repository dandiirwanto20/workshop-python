class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []    # membuat daftar kosong baru untuk setiap anjing

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
d.tricks
# ['roll over'] (Output)
e.tricks
# ['play dead'] (Output)