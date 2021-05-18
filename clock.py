from tkinter import *
from time import *

fenster = Tk()
fenster.title("The Time.")


def clock():
            text = strftime('%H:%M:%S')
            label.config(text=text)
            label.after(1000, clock)

label = Label(fenster, font=("ds-digital", 100),background="black",foreground="white")

label.pack(anchor="center")

clock()

mainloop()
