from tkinter import *

root = Tk()
root.geometry("500x500")

l1 = Label(text = "ENTER PASSWORD", font = ("calibri",12,"bold"))
l1.place(x = 70, y = 80)

e1 = Entry(width = 23)
e1.place(x = 70, y = 120)

Pass = 0

inty = 1,2,3,4,5,6,7,8,9,0

def password():
    if Pass == inty == 0:
        print("Correct")
    else:
        print("Incorrect")

b1 = Button(text = "Correct or Incorrect?", font =("calibri",12,"bold"), command = password)
b1.pack(side = BOTTOM)

root.mainloop()
