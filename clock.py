from tkinter import *
import datetime

root = Tk()
root.config(bg='black')
label = Label(root, text="", font=('times', 24))


def data():
    time = datetime.datetime.now()
    label.config(text=time.strftime('%H:%M:%S %p'))
    root.after(1000, data)


label.pack()
data()
root.mainloop()
