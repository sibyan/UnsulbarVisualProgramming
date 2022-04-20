from tkinter import *
import tkinter.font as font
import math
root = Tk()
root.tittle("CALCULATOR")
root.geometry("310x400")
root["bg"] = "#d1d1d1"

myfont = font.Font(size=15)

e = Entry(root)
e["font"] = myfont
e["bg"] = "#d1d1d1"
e.grid(row=0,column=0,columnspan=4,padx=20,pady=20)


def angka(nilai):
    sebelum = e.get()



btn1 = Button(root,text="1",padx=30,pady=30,command=lambda:angka(1))
btn2 = Button(root,text="2",padx=30,pady=30,command=lambda:angka(2))
btn3 = Button(root,text="3",padx=30,pady=30,command=lambda:angka(3))
btn4 = Button(root,text="4",padx=30,pady=30,command=lambda:angka(4))
btn5 = Button(root,text="5",padx=30,pady=30,command=lambda:angka(5))
btn6 = Button(root,text="6",padx=30,pady=30,command=lambda:angka(6))
btn7 = Button(root,text="7",padx=30,pady=30,command=lambda:angka(7))
btn8 = Button(root,text="8",padx=30,pady=30,command=lambda:angka(8))
btn9 = Button(root,text="9",padx=30,pady=30,command=lambda:angka(9))
btn0 = Button(root,text="0",padx=30,pady=30,command=lambda:angka(0))

btn1.grid(row=3,column=0,pady=2)
btn2.grid(row=3,column=1,pady=2)
btn3.grid(row=3,column=2,pady=2)
btn4.grid(row=2,column=0,pady=2)
btn5.grid(row=2,column=1,pady=2)
btn6.grid(row=2,column=2,pady=2)
btn7.grid(row=1,column=0,pady=2)
btn8.grid(row=1,column=1,pady=2)
btn9.grid(row=1,column=2,pady=2)
btn0.grid(row=4,column=1,pady=2)

