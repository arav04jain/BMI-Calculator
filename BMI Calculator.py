import tkinter as t
window = t.Tk()

window.title("Body Mass Index Calculator")
window.geometry("600x800")
window.configure(background="black")


label = t.Label(window, font=('aria', 30, 'bold'),
                text="BMI Calculator", fg="white", bd=10, anchor='w')
label.grid(row=0, column=1)
label.configure(background="black")


entry1_label = t.Label(window, font=('aria', 16, 'bold'), text="Feet:", fg="white", bd=10, anchor='w',
                       background="black")
entry1_label.grid(row=1, column=0)
h1 = t.Entry(window, font=('ariel', 16, 'bold'), textvariable="", bd=6, insertwidth=4, bg="white",
             justify='right')
h1.grid(row=1, column=1)


entry2_label = t.Label(window, font=('aria', 16, 'bold'), text="Inches:", fg="white", bd=10, anchor='w',
                       background="black")
entry2_label.grid(row=2, column=0)
h2 = t.Entry(window, font=('ariel', 16, 'bold'), textvariable="", bd=6, insertwidth=4, bg="white",
             justify='right')
h2.grid(row=2, column=1)


entry3_label = t.Label(window, font=('aria', 16, 'bold'), text="Weight:", fg="white", bd=10, anchor='w',
                       background="black")
entry3_label.grid(row=3, column=0)
w = t.Entry(window, font=('ariel', 16, 'bold'), textvariable="", bd=6, insertwidth=4, bg="white",
            justify='right')
w.grid(row=3, column=1)


def c(h1, h2, w,):

    h1 = int(h1)
    h2 = float(h2)
    w = float(w)

    h = ((h1*12)+h2)/39.37
    ls = t.Label(window, font=('Times New Roman', 25, 'bold'),
                 fg="white", bd=10, anchor='w', text="BMI Categories", bg="black")
    ls.grid(column=1, row=5)
    lss = t.Label(window, font=('Times New Roman', 15, 'bold'), fg="white",
                  bd=10, anchor='w', text="Underweight = <18.5", bg="black")
    lss.grid(column=1, row=6)
    lsss = t.Label(window, font=('Times New Roman', 15, 'bold'), fg="white",
                   bd=10, anchor='w', text="Normal weight = 18.5–24.9", bg="black")
    lsss.grid(column=1, row=7)
    lssss = t.Label(window, font=('Times New Roman', 15, 'bold'), fg="white",
                    bd=10, anchor='w', text="Overweight = 25–29.9", bg="black")
    lssss.grid(column=1, row=8)
    lsssss = t.Label(window, font=('Times New Roman', 15, 'bold'), fg="white",
                     bd=10, anchor='w', text="Obesity = BMI of 30 or greater", bg="black")
    lsssss.grid(column=1, row=9)

    bmi = w/(h*h)
    l = t.Label(window, font=('Times New Roman', 25, 'bold'),
                text="Your BMI is "+str(bmi), fg="white", bd=10, anchor='w', bg="black")
    l.grid(column=1, row=10)


btn1 = t.Button(window, text="ENTER", width=15, command=lambda: c(
    h1.get(), h2.get(), w.get()), height=2, font=('aria', 16, 'bold'))

btn1.grid(row=4, column=1)

label_sum = t.Label(window, text="Made By Arav Jain", font=(
    "Georgia", 30), background="black", fg="white")
label_sum.grid(row=12, column=1)
window.mainloop()
