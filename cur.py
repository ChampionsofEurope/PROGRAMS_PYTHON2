from tkinter import *

root = Tk()
root.geometry("400x400")

def choices():
    rupees = 99.73
    a = int()
    pound = rupees/70
    print(pound)

l1 = Label(text = "Currency Converter", font=("calibri",28,"bold"))
l1.pack(side = TOP)

butty = Button(text = "FROM POUND TO RUPEES", command = choices)
butty.place(x = 120, y = 120)



root.mainloop()
