# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 14:41:13 2023

@author: C-117
"""

from tkinter import *
def yaz(x):
    global yazi
    yazi = yazi + x
    ekran.config(text=yazi)


def hesapla():
    global yazi
    a = eval(yazi)
    ekran.config(text=a)
    yazi = ""


def temizle():
    global yazi
    ekran.config(text="")
    yazi = ""


def sil():
    global yazi
    yazi = yazi[0:-1]
    ekran.config(text=yazi)

ftastemur = Tk()
ftastemur.geometry("340x280")
ftastemur.resizable(width=FALSE, height=FALSE)
ftastemur.title("Hesapnesi")

cerceveana1 = Frame()
cerceveana1.pack(expand=YES, fill=X)

cerceveana11 = Frame(cerceveana1)
cerceveana11.pack(side=TOP, expand=YES, fill=X)

cerceveana2 = Frame()
cerceveana2.pack()

cerceveana21 = Frame(cerceveana2)
cerceveana21.grid(row=0, column=0)

cerceveana22 = Frame(cerceveana2)
cerceveana22.grid(row=0, column=1)

cerceveana23 = Frame(cerceveana2)
cerceveana23.grid(row=1, column=0)

cerceveana24 = Frame(cerceveana2)
cerceveana24.grid(row=1, column=1)

cerceve4 = Frame(cerceveana21)
cerceve4.pack(padx=12)

cerceve2 = Frame(cerceveana22)
cerceve2.pack(padx=12)

yazi = ""
ekran = Label(cerceveana11)
ekran.config(textvariable=yazi, relief=SUNKEN, bg="white", height=2, anchor=E)
ekran.pack(expand=YES, fill=X, padx=12, pady=10)

c = 0
d = 0
e = 0
for i in (1, 2, 3, 4, 5, 6, 7, 8, 9):
    k = i % 3
    if k == 1:
        Button(cerceve4, text=i, fg="white", bg="black", font=("Arial", 10, "bold"), height=2, width=6,
               command=(lambda i=i: yaz(str(i)))).grid(row=c, column=1)
        c = c + 1
    if k == 2:
        Button(cerceve4, text=i, fg="white", bg="black", font=("Arial", 10, "bold"), height=2, width=6,
               command=(lambda i=i: yaz(str(i)))).grid(row=d, column=2)
        d = d + 1
    if k == 0:
        Button(cerceve4, text=i, fg="white", bg="black", font=("Arial", 10, "bold"), height=2, width=6,
               command=(lambda i=i: yaz(str(i)))).grid(row=e, column=3)
        e = e + 1

Button(cerceve2, text="X", fg="yellow", bg="Green", font=("Arial", 10, "bold"), height=2, width=6,
       command=(lambda i=i: yaz("*"))).grid(row=0, column=4)
Button(cerceve2, text="/", fg="yellow", bg="Green", font=("Arial", 10, "bold"), height=2, width=6,
       command=(lambda i=i: yaz("/"))).grid(row=1, column=4)
Button(cerceve2, text="=", fg="yellow", bg="Green", font=("Arial", 10, "bold"), height=2, width=6, command=hesapla).grid(
    row=2, column=4)
Button(cerceve4, text="(", fg="white", bg="black", font=("Arial", 10, "bold"), height=2, width=6,
       command=(lambda i=i: yaz("("))).grid(row=3, column=1)
Button(cerceve4, text="0", fg="white", bg="black", font=("Arial", 10, "bold"), height=2, width=6,
       command=(lambda i=i: yaz("0"))).grid(row=3, column=2)
Button(cerceve4, text=")", fg="white", bg="black", font=("Arial", 10, "bold"), height=2, width=6,
       command=(lambda i=i: yaz(")"))).grid(row=3, column=3)
Button(cerceve2, text="AC", fg="yellow", bg="Green", font=("Arial", 10, "bold"), height=2, width=6, command=temizle).grid(
    row=3, column=4)
Button(cerceve2, text="+", fg="yellow", bg="Green", font=("Arial", 10, "bold"), height=2, width=6,
       command=(lambda i=i: yaz("+"))).grid(row=0, column=5)
Button(cerceve2, text="-", fg="yellow", bg="Green", font=("Arial", 10, "bold"), height=2, width=6,
       command=(lambda i=i: yaz("-"))).grid(row=1, column=5)
Button(cerceve2, text=".", fg="yellow", bg="Green", font=("Arial", 10, "bold"), height=2, width=6,
       command=(lambda i=i: yaz("."))).grid(row=2, column=5)
Button(cerceve2, text="C", fg="yellow", bg="Green", font=("Arial", 10, "bold"), height=2, width=6, command=sil).grid(
    row=3, column=5)

ftastemur.mainloop()


 