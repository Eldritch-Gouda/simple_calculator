import tkinter as tk
from tkinter import *

#---GUI---

#---Window---

window = tk.Tk()
window.title = "Taschenrechner"
window.geometry("500x300")

#---Ein- Ausgabefeld---

ausgabefeld = tk.Entry(window, width=25, font=("Arial", 20))
ausgabefeld.place(x=20, y=20)

#---Buttons---

eins = tk.Button(window, width=5, font=("Arial", 15), text="1")
eins.place(x=20, y=60)
zwei = tk.Button(window, width=5, font=("Arial", 15), text="2")
zwei.place(x=85, y=60)
drei = tk.Button(window, width=5, font=("Arial", 15), text="3")
drei.place(x=150, y=60)
vier = tk.Button(window, width=5, font=("Arial", 15), text="4")
vier.place(x=20, y=100)
fünf = tk.Button(window, width=5, font=("Arial", 15), text="5")
fünf.place(x=85, y=100)
sechs = tk.Button(window, width=5, font=("Arial", 15), text="6")
sechs.place(x=150, y=100)
sieben = tk.Button(window, width=5, font=("Arial", 15), text="7")
sieben.place(x=20, y=140)
acht = tk.Button(window, width=5, font=("Arial", 15), text="8")
acht.place(x=85, y=140)
neun = tk.Button(window, width=5, font=("Arial", 15), text="9")
neun.place(x=150, y=140)
null = tk.Button(window, width=5, font=("Arial", 15), text="0")
null.place(x=20, y=180)
positiv_negativ = tk.Button(window, width=5, font=("Arial", 15), text="+/-")
positiv_negativ.place(x=85, y=180)
komma = tk.Button(window, width=5, font=("Arial", 15), text=",")
komma.place(x=150, y=180)
plus = tk.Button(window, width=5, font=("Arial", 15), text="+")
plus.place(x=215, y=60)
minus = tk.Button(window, width=5, font=("Arial", 15), text="-")
minus.place(x=215, y=100)
mal = tk.Button(window, width=5, font=("Arial", 15), text="*")
mal.place(x=215, y=140)
geteilt = tk.Button(window, width=5, font=("Arial", 15), text="/")
geteilt.place(x=215, y=180)
loeschen = tk.Button(window, width=5, font=("Arial", 15), text="<-")
loeschen.place(x=280, y=60)
ergebnis = tk.Button(window, width=5, font=("Arial", 15), text="=")
ergebnis.place(x=280, y=180)


#---Button Funktionen---



window.mainloop()