from AI_simulator import AI 
from tkinter import Tk, Label, Button
Data = AI("Farbod", "Parkhooi", "Cat", "Banana", "Pizza", "swimming", "12", "Female") # Write your information
root = Tk()
gender_lable = Label(root, text=f"announcer gender(now:{Data.announcer_gender})", width=25)
gender_lable.place(x=0, y=0)
root.title("Farbod AI")
root.geometry("800x100")
def Start():
    root.destroy()
def Change():
    gender_lable.destroy()
    try: genderlable.destroy()
    except: pass
    Data.Change_announcer_gender(True)
    genderlable = Label(root, text=f"announcer gender(now:{Data.announcer_gender})", width=25)
    genderlable.place(x=0, y=0)
# Data.Start()
Button(root, text="Change announcer gender", command=Change).place(x=0, y=25)
Button(root, text="Who Use Me", command=Data.Who_use_me, font=("", 11), width=15).place(x=250, y=0)
Button(root, text="Start", command=Start, font=("", 11), width=15).place(x=400, y=0)
Button(root, text="Test", command=Data.Test, font=("", 11), width=15).place(x=250, y=30)
Button(root, text="Exit", command=Data.Say_bye, font=("", 11), width=15).place(x=400, y=30)
root.mainloop()
