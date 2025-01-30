class Birds:
    def fly(self):
        return "They can fly"

class Mammal:
    def walk(self):
        return "They can walk"

class Bat(Birds,Mammal):
    def detect(self):
        return "They use Echo Location"

bat=Bat()
print(bat.fly())
print(bat.walk())
find=Mammal()
find=bat
print(find.detect())