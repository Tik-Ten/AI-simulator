from pyttsx3 import init
engin = init()
engin.setProperty("rate", 120)
voice = engin.getProperty('voices') 
class AI:
    def __init__(self, First_Name, Last_Name, Favorite_animal, Favorite_fruit, Favorite_food, Favorite_sport, Age, announcer_gender):
        self.First_Name = First_Name
        self.Last_Name = Last_Name 
        self.Favorite_animal = Favorite_animal
        self.Favorite_fruit = Favorite_fruit
        self.Favorite_food = Favorite_food
        self.Favorite_sport = Favorite_sport
        self.Age = Age 
        self.announcer_gender = announcer_gender
    def Test(self):
        engin.say("Hello Hello! 1, 2, 3, 4... My name is Farbod AI.")
        engin.runAndWait()
    def Start(self):
        engin.setProperty("rate", 130)
        engin.say("Hey everyone this is Farbod AI.")
        engin.runAndWait()
    def Show_info(self):
        from tkinter import messagebox as msg
        msg.showinfo("Info", f"""First name : {self.First_Name}
Last name : {self.Last_Name}
Favorite animal : {self.Favorite_animal}
Favorite fruit : {self.Favorite_fruit}
Favorite food : {self.Favorite_food}
Favorite sport : {self.Favorite_sport}
Age : {self.Age}""")
    def Say_hi(self):
        engin.setProperty("rate", 173)
        engin.say(f"Oh, Hello! I think your name is {self.First_Name} {self.Last_Name}. What's up?")
        engin.runAndWait()
    def Say_bye(self): 
        engin.say("Ok")
        engin.setProperty("rate", 160)
        engin.say("Bye bye!")
        engin.runAndWait()
        exit()
    def Say_by(self):
        engin.say("This application created by Farbod Parkhooi. this is his Github link: https://www.github.com/tik-ten")
        engin.runAndWait()
        from tkinter import messagebox as msg
        msg.showinfo("Github link:", "https://www.github.com/tik-ten")
    def Say_name(self):
        engin.say("My name is AI Simulator!")
        engin.runAndWait()
    def Detect_with_camera(self):
        from cv2 import VideoCapture, waitKey
        from cvzone.HandTrackingModule import HandDetector
        Detector = HandDetector(maxHands=1)
        cap = VideoCapture(0)
        while True:
            rec, frame = cap.read()
            Hands, frame = Detector.findHands(frame)
            if Hands:
                Hand1 = Hands[0]
                lmList1 = Hand1["lmList"]
                length, _, _ = Detector.findDistance(lmList1[8][0:2], lmList1[4][0:2], frame)
                if length < 20:
                    pass # code
            waitKey(1)
    def Change_announcer_gender(self, direction):
        if direction == False: pass
        elif direction == True: 
            if self.announcer_gender == "Male": 
                self.announcer_gender = "Female"
                engin.setProperty('voice', voice[1].id)
                print("C fem")
            else: 
                self.announcer_gender = "Male"
                engin.setProperty('voice', voice[0].id)
                print("C mai")
        if self.announcer_gender == "Male": 
            return "Male"
        else: 
            return "Female"
    def Who_use_me(self):
        from faker import Faker
        Names = ""
        faker = Faker()
        for i in range(5):
            Names += faker.name() + ", "
        engin.say(f"Too many peoples use me. for example {Names}")
        engin.runAndWait()
