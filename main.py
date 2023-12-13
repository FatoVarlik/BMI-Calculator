from tkinter import *

window = Tk()
window.title("BMI Calculator")
window.minsize(width=450, height=300)

label_1 = Label(text="Height", font=("Arial",12,"bold"))
label_1.place(x=225-56/2, y=20)
# label_1.update()
# print(label_1.winfo_height())
# print(label_1.winfo_width())

entry_1 = Entry(width=20)
entry_1.place(x=225-124/2, y=50)
#entry_1.update()
# print(entry_1.winfo_height())
# print(entry_1.winfo_width())

label_2 = Label(text="Weight", font=("Arial",12,"bold"))
label_2.place(x=225-59/2, y=80)
# label_2.update()
# print(label_2.winfo_height())
# print(label_2.winfo_width())

entry_2 = Entry(width=20)
entry_2.place(x=225-124/2, y=110)
# entry_2.update()
# print(entry_2.winfo_height())
# print(entry_2.winfo_width())


def calculate():
    Height = entry_1.get()
    Height = float(Height) / 100
    Weight = entry_2.get()
    BMI = float(Weight) / Height ** 2
    print(BMI)

    if BMI < 18.5:
        print("Düşük Kilolusunuz.")
    elif BMI < 25:
        print("Normalsiniz.")
    elif BMI < 30:
        print("Fazla Kilolusunuz.")
    else:
        print("Obezsiniz.")


button = Button(text="Calculate",font=("Arial",12,"normal"),command=calculate)
button.place(x=225-79/2, y=150)
# button.update()
# print(button.winfo_height())
# print(button.winfo_width())

window.mainloop()
