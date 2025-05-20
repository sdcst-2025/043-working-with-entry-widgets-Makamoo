"""
##### Task 1
Create entry widets to allow user to enter their:
* name
* student number
* grade

Create a button so that when they click on the button, it states all of the information in a 4th entry widget
"""

import tkinter as tk 

def run(e):
    print("All your info has been put into one widget")
    data1 = e1.get()
    data2 = e2.get()
    data3 = e3.get()
    data = (data1,",",data2,",",data3)
    e4.delete(0,tk.END)
    e4.insert(0,data)

win = tk.Tk()
l1 = tk.Label(win, width=15, text="Name")
l2 = tk.Label(win, width=15, text="Student Number")
l3 = tk.Label(win, width=15, text="Grade")
l4 = tk.Label(win, width=15, text="Student Info")
e1 = tk.Entry(win,width=20)
e2 = tk.Entry(win,width=20)
e3 = tk.Entry(win,width=20)
b1 = tk.Button(win, text="Click To Combine Info")
e4 = tk.Entry(win,width=30)


b1.bind("<Button-1>",run)

l1.pack()
e1.pack()
l2.pack()
e2.pack()
l3.pack()
e3.pack()
b1.pack()
l4.pack()
e4.pack()
    
win.mainloop()