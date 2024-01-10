class Dog:
    def __init__(self, name, breed="Mutt"):
        self.name = name
        self.breed = breed

    def bark(self):
        print("Woof!")

    def get_adopted(self, owner_name):
        self.owner = owner_name

fido = Dog("Fido")
fido.name
# Fido

fido.get_adopted("Sophie")

snoopy = Dog("Snoopy")
snoopy.name
# Snoopy