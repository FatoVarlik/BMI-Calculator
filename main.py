from tkinter import *

window = Tk()
window.title("BMI Calculator")
window.config(padx=30,pady=30)

height_label = Label(text="Enter Height(cm)", font=("Arial", 12, "normal"))
height_label.pack()

height_entry = Entry(width=20)
height_entry.pack()

weight_label = Label(text="Enter Weight(kg)", font=("Arial",12,"normal"))
weight_label.pack()

weight_entry = Entry(width=20)
weight_entry.pack()

result_label = Label()
result_label.pack()

def calculate():
    Height = height_entry.get()
    Weight = weight_entry.get()

    if Height == "" or Weight == "":
        result_label.config(text="Please enter both Height and Weight!")
    else:
        try:
            BMI = float(Weight) / (float(Height) / 100) ** 2
            string = result(BMI)
            result_label.config(text=string)
        except:
            result_label.config(text="Please enter valid number!")

def result(BMI):
    string =f"Your BMI is: {BMI}. "
    if BMI < 18.5:
        string += "You are Underweight."
    elif BMI < 25:
        string += "You are Normal."
    elif BMI < 30:
        string += "You are Overweight."
    else:
        string += "You are Obese."
    return string


button = Button(text="Calculate",font=("Arial",12,"normal"),command=calculate)
button.pack()

window.mainloop()
