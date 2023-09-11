# def Questions():
#     First_Name = input("What's your First name(example: My first name is -Your first name-)? ")
#     Last_Name = input("What's your First name(example: My last name is -Your last name-)? ")
#     Favorite_animal = input("What's your favorite animal(example: It's -Your favorite animal-)? ")
#     Favorite_fruit = input("What's your favorite fruit(example: It's -Your favorite fruit-)? ")
#     Favorite_food = input("What's your favorite food(example: It's -Your favorite food-)? ")
#     return Favorite_animal + "-" + Favorite_fruit + "-" + First_Name + "-" + Last_Name + "-" + Favorite_food

class Questions:
    def __init__(self, First_Name, Last_Name, Favorite_animal, Favorite_fruit, Favorite_food):
        self.First_Name = First_Name
        self.Last_Name = Last_Name
        self.Favorite_animal = Favorite_animal
        self.Favorite_fruit = Favorite_fruit
        self.Favorite_food = Favorite_food