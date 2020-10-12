from tkinter import *


numbers = Tk()
numbers.title("addition")
numbers.geometry("300x200")

num1 = IntVar()
num2 = IntVar()
num3 = IntVar()


firstlabel= Label(numbers, text= "FirstNumber")
firstlabel.grid(row=0, column=0)

firstentry= Entry(numbers, textvariable=num1)
firstentry.grid(row=0, column=1)

secondlabel= Label(numbers, text="SecondNumber")
secondlabel.grid(row=1, column=0)

secondentry= Entry(numbers, textvariable=num2)
secondentry.grid(row=1, column=1)

resultlabel= Label(numbers,text="Result")
resultlabel.grid(row=2, column=0)

resultentry= Entry(numbers)
resultentry.grid(row=2, column=1)

def addition():
    resultentry.insert(0, num1.get() + num2.get())

addbtn= Button(numbers, text="Add", command=addition)
addbtn.grid(row=3, column=0)


def clear():
    firstentry.delete(0, END)
    secondentry.delete(0, END)
    resultentry.delete(0, END)

clearbtn= Button(numbers, text="Clear", command=clear)
clearbtn.grid(row=3, column=1)


numbers.mainloop()