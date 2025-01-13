import tkinter as tk
from tkinter import *

#---GUI---

#---Window---

window = tk.Tk()
window.title = "Calculator"
window.geometry("500x300")

#---Ein- Ausgabefeld---

ausgabefeld = tk.Entry(window, width=25, font=("Arial", 20))
ausgabefeld.place(x=20, y=20)

#---Buttons---

one = tk.Button(window, width=5, font=("Arial", 15), text="1")
one.place(x=20, y=60)
two = tk.Button(window, width=5, font=("Arial", 15), text="2")
two.place(x=85, y=60)
three = tk.Button(window, width=5, font=("Arial", 15), text="3")
three.place(x=150, y=60)
four = tk.Button(window, width=5, font=("Arial", 15), text="4")
four.place(x=20, y=100)
five = tk.Button(window, width=5, font=("Arial", 15), text="5")
five.place(x=85, y=100)
six = tk.Button(window, width=5, font=("Arial", 15), text="6")
six.place(x=150, y=100)
seven = tk.Button(window, width=5, font=("Arial", 15), text="7")
seven.place(x=20, y=140)
eight = tk.Button(window, width=5, font=("Arial", 15), text="8")
eight.place(x=85, y=140)
nine = tk.Button(window, width=5, font=("Arial", 15), text="9")
nine.place(x=150, y=140)
zero = tk.Button(window, width=5, font=("Arial", 15), text="0")
zero.place(x=20, y=180)
positive_negative = tk.Button(window, width=5, font=("Arial", 15), text="+/-")
positive_negative.place(x=85, y=180)
comma = tk.Button(window, width=5, font=("Arial", 15), text=",")
comma.place(x=150, y=180)
plus = tk.Button(window, width=5, font=("Arial", 15), text="+")
plus.place(x=215, y=60)
minus = tk.Button(window, width=5, font=("Arial", 15), text="-")
minus.place(x=215, y=100)
multiplication = tk.Button(window, width=5, font=("Arial", 15), text="*")
multiplication.place(x=215, y=140)
divide = tk.Button(window, width=5, font=("Arial", 15), text="/")
divide.place(x=215, y=180)
erase = tk.Button(window, width=5, font=("Arial", 15), text="<-")
erase.place(x=280, y=60)
result = tk.Button(window, width=5, font=("Arial", 15), text="=")
result.place(x=280, y=180)


#---Button Functions---



window.mainloop()
