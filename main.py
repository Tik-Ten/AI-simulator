from Questions import Questions

def Create_account():
    USERNAME = input("WRITE YOUR USERNAME: ")
    PASSWORD = input("WRITE YOUR PASSWORD: ")
    First_Name = input("What's your First name(example: My first name is -Your first name-)? ")
    Last_Name = input("What's your First name(example: My last name is -Your last name-)? ")
    Favorite_animal = input("What's your favorite animal(example: It's -Your favorite animal-)? ")
    Favorite_fruit = input("What's your favorite fruit(example: It's -Your favorite fruit-)? ")
    Favorite_food = input("What's your favorite food(example: It's -Your favorite food-)? ")

    Information = Questions(
        USERNAME=USERNAME
        PASSWORD=PASSWORD
        First_Name=First_Name, 
        Last_Name=Last_Name, 
        Favorite_animal=Favorite_animal, 
        Favorite_fruit=Favorite_fruit,
        Favorite_food=Favorite_food
    )
def Login():
    pass