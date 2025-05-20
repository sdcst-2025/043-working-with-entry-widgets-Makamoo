#!python3

"""
Create the interface shown.  The program should be able to perform the math operation specified
by the buttons and display the entry in the 3rd entry widget;
"""

import tkinter as tk

def run(e):
    print("All your info has been put into one widget")
    data1 = e1.get()
    data2 = e2.get()
    data11 = int(data1) * int(data2)
    data22 = int(data1) + int(data2)
    data33 = int(data1) - int(data2)
    data44 = int(data1) / int(data2)
    data = (data11,data22,data33,data44)
    e3.delete(0,tk.END)
    e3.insert(0,data)

w = tk.Tk()
e1 = tk.Entry(w,width=20)
e2 = tk.Entry(w,width=20)
e3 = tk.Entry(w,width=20)

l = []
l.append( tk.Label(w,text="Number 1"))
l.append( tk.Label(w,text="Number 2"))
l.append( tk.Label(w,text="Number Calculator"))


e = []
e.append( tk.Entry(w,text=""))
e.append( tk.Entry(w,text=""))
e.append( tk.Entry(w,text="answer",state='disabled'))

b1 = tk.Button(w,text="x")
b2 = tk.Button(w,text="+")
b3 = tk.Button(w,text="-")
b4 = tk.Button(w,text="÷")

b2.bind("<Button-2>",run)
b1.bind("<Button-1>",run)
b3.bind("<Button-3>",run)
b4.bind("<Button-4>",run)

l[2].grid(row=1,column=1,columnspan=4)
l[0].grid(row=2,column=1,columnspan=2)
l[1].grid(row=2,column=3,columnspan=2)
e1.grid(row=3,column=1, columnspan=2)
e2.grid(row=3,column=3, columnspan=2)
b1.grid(row=4,column=1)
b2.grid(row=4,column=2)
b3.grid(row=4,column=3)
b4.grid(row=4,column=4)
e3.grid(row=5,column=1,columnspan=4)

w.mainloop()
