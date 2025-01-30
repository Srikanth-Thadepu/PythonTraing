class Food:
    def taste(self):
        print("Food tastes good")

class Spicy(Food):
    def taste(self):
        print("It is spicy!!")

class Sweet(Food):
    def taste(self):
        print("It is sweet...")

def  food_taste(its_taste):
    its_taste.taste()

spicy=Spicy()
sweet=Sweet()

food_taste(Food())
food_taste(spicy)
food_taste(sweet)