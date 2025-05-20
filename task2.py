#!python3

"""
Create a window with 3 entry widgets and 1 button.
The first 2 entry widgets allow the user to enter in the 2 short sides of a right triangle.
When the button is clicked, calculate the length of the hypotenuse and display it in the 3rd entry widget.
Any labels you need for instruction are optional.
"""

import tkinter as tk 
import math

def run(e):
    print("Your hypotenuse has been revealed")
    data1 = e1.get()
    data1 = int(data1)
    data2 = e2.get()
    data2 = int(data2)
    data = math.sqrt(data1**2 + data2**2)
    e3.delete(0,tk.END)
    e3.insert(0,data)

win = tk.Tk()
e1 = tk.Entry(win,width=20)
e2 = tk.Entry(win,width=20)
b1 = tk.Button(win, text="Click to find hypotenuse")
e3 = tk.Entry(win,width=20)


b1.bind("<Button-1>",run)

e1.pack()
e2.pack()
b1.pack()
e3.pack()
    
win.mainloop()