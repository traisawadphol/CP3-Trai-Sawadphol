from tkinter import *

def calBMI(event):
    height = float(textBoxHeight.get())
    weight = float(textBoxWeight.get())
    bmi = weight/(height*height*0.01*0.01)
    bmi = round(bmi, 2)
    labelCalculate.configure(text=bmi)
    if bmi >= 30:
        labelShape.configure(text="อ้วนมาก")
    elif bmi >= 25:
        labelShape.configure(text="อ้วน")
    elif bmi >= 23:
        labelShape.configure(text="น้ำหนักเกิน")
    elif bmi >= 18.6:
        labelShape.configure(text="น้ำหนักปกติ เหมาะสม")
    else:
        labelShape.configure(text="ผอมเกินไป")

Mainwindow = Tk()
labelHeight = Label(Mainwindow, text="ส่วนสูง (cm)")
labelHeight.grid(row=0, column=0)

textBoxHeight = Entry(Mainwindow)
textBoxHeight.grid(row=0, column=1)

labelWeight = Label(Mainwindow, text="น้ำหนัก (kg)")
labelWeight.grid(row=1, column=0)

textBoxWeight = Entry(Mainwindow)
textBoxWeight.grid(row=1, column=1)

calculateButton = Button(Mainwindow, text= "คำนวน")
calculateButton.grid(row=2)
calculateButton.bind('<Button-1>', calBMI)

labelCalculate = Label(Mainwindow, text="BMI")
labelCalculate.grid(row=2, column=1)

labelShape = Label(Mainwindow, text="")
labelShape.grid(row=3, column=1)

Mainwindow.mainloop()
