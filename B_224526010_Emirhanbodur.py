# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 13:55:59 2023

@author: C-117
"""

import tkinter as tk
import math

def sayi_bas(sayi):
    btn_1.insert(tk.END, sayi)

def islem_bas(islem):
    btn_1.insert(tk.END, " " + islem + " ")

def hesap():
    girilen_ifade = btn_1.get()
    try:
        sonuc = eval(girilen_ifade)
        btn_1.delete(0, tk.END)
        btn_1.insert(0, sonuc)
    except:
        btn_1.delete(0, tk.END)
        btn_1.insert(0, "Hata")



def hafz_kaydet():
    global bellek
    bellek = btn_1.get()

def hafz_artir():
    global bellek
    try:
        bellek = str(float(bellek) + float(btn_1.get()))
    except:
        bellek = "Hata"

def hafz_azalt():
    global bellek
    try:
        bellek = str(float(bellek) - float(btn_1.get()))
    except:
        bellek = "Hata"

def hafz_oku():
    btn_1.delete(0, tk.END)
    btn_1.insert(0, bellek)
def sil():
    btn_1.delete(0, tk.END)

pencere = tk.Tk()
pencere.title("Hesap Makinesi")
pencere=tk.Label(bg="red")

btn_1 = tk.Entry(pencere, width=30)
btn_1.grid(row=0, column=0, columnspan=4)

sayilar = "7894561230"
row, col = 1, 0
for sayi in sayilar:
    tk.Button(pencere, text=sayi, width=5, command=lambda sayi=sayi: sayi_bas(sayi)).grid(row=row, column=col)
    col += 1
    if col > 2:
        col = 0
        row += 1
#Python'da lambda, tek satırlık fonksiyonlardır. Bir ya da daha fazla parametre kabul ederler, ancak tek bir işlem yapabilirler.
tk.Button(pencere, text=".", width=5, command=lambda: sayi_bas(".")).grid(row=4, column=1)

tk.Button(pencere, text="=", width=5, command=hesap).grid(row=4, column=2)

tk.Button(pencere, text="+", width=5, command=lambda: islem_bas("+")).grid(row=1, column=3)

tk.Button(pencere, text="-", width=5, command=lambda: islem_bas("-")).grid(row=2, column=3)

tk.Button(pencere, text="*", width=5, command=lambda: islem_bas("*")).grid(row=3, column=3)

tk.Button(pencere, text="/", width=5, command=lambda: islem_bas("/")).grid(row=4, column=3)


bellek = ""  

tk.Button(pencere, text="MC", width=5, command=sil).grid(row=7, column=0)

tk.Button(pencere, text="M+", width=5, command=hafz_artir).grid(row=7, column=1)

tk.Button(pencere, text="M-", width=5, command=hafz_azalt).grid(row=7, column=2)

tk.Button(pencere, text="MR", width=5, command=hafz_oku).grid(row=7, column=3)

tk.Button(pencere, text="C", width=5, command=sil).grid(row=7, column=4)


pencere.pack()
pencere.mainloop()