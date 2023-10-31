# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 15:40:48 2023

@author: C-117
"""

import tkinter as tk
import math

def sayi_tikla(sayi):
    btn_1.insert(tk.END, sayi)

def islem_tikla(islem):
    btn_1.insert(tk.END, " " + islem + " ")

def hesapla():
    girilen_ifade = btn_1.get()
    try:
        sonuc = eval(girilen_ifade)
        btn_1.delete(0, tk.END)
        btn_1.insert(0, sonuc)
    except:
        btn_1.delete(0, tk.END)
        btn_1.insert(0, "Hata")

def mutlak_deger():
    try:
        girilen_ifade = btn_1.get()
        sonuc = eval(girilen_ifade)
        mutlak_sonuc = abs(sonuc)
        btn_1.delete(0, tk.END)
        btn_1.insert(0, mutlak_sonuc)
    except:
        btn_1.delete(0, tk.END)
        btn_1.insert(0, "Hata")

def faktoriyel():
    try:
        girilen_ifade = btn_1.get()
        n = int(girilen_ifade)
        if n < 0:
            sonuc = "Negatif sayıların faktöriyeli tanımsızdır."
        else:
            sonuc = math.factorial(n)
        btn_1.delete(0, tk.END)
        btn_1.insert(0, sonuc)
    except:
        btn_1.delete(0, tk.END)
        btn_1.insert(0, "Hata: Lütfen bir pozitif tam sayı girin.")

def bellek_kaydet():
    global bellek
    bellek = btn_1.get()

def bellek_artir():
    global bellek
    try:
        bellek = str(float(bellek) + float(btn_1.get()))
    except:
        bellek = "Hata"

def bellek_azalt():
    global bellek
    try:
        bellek = str(float(bellek) - float(btn_1.get()))
    except:
        bellek = "Hata"

def bellek_oku():
    btn_1.delete(0, tk.END)
    btn_1.insert(0, bellek)

def temizle():
    btn_1.delete(0, tk.END)

pencere = tk.Tk()
pencere.title("Hesap Makinesi")

btn_1 = tk.Entry(pencere, width=30)
btn_1.grid(row=0, column=0, columnspan=4)

sayilar = "1234567890"
row, col = 1, 0
for sayi in sayilar:
    tk.Button(pencere, text=sayi, width=5, command=lambda sayi=sayi: sayi_tikla(sayi)).grid(row=row, column=col)
    col += 1
    if col > 2:
        col = 0
        row += 1

tk.Button(pencere, text=".", width=5, command=lambda: sayi_tikla(".")).grid(row=4, column=1)
tk.Button(pencere, text="=", width=5, command=hesapla).grid(row=4, column=2)
tk.Button(pencere, text="+", width=5, command=lambda: islem_tikla("+")).grid(row=1, column=3)
tk.Button(pencere, text="-", width=5, command=lambda: islem_tikla("-")).grid(row=2, column=3)
tk.Button(pencere, text="", width=5, command=lambda: islem_tikla("")).grid(row=3, column=3)
tk.Button(pencere, text="/", width=5, command=lambda: islem_tikla("/")).grid(row=4, column=3)
tk.Button(pencere, text="|x|", width=5, command=mutlak_deger).grid(row=5, column=3)
tk.Button(pencere, text="!", width=5, command=lambda: islem_tikla("!")).grid(row=6, column=3)

bellek = ""  
tk.Button(pencere, text="MC", width=5, command=temizle).grid(row=6, column=0)
tk.Button(pencere, text="M+", width=5, command=bellek_artir).grid(row=6, column=1)
tk.Button(pencere, text="M-", width=5, command=bellek_azalt).grid(row=6, column=2)
tk.Button(pencere, text="MR", width=5, command=bellek_oku).grid(row=6, column=3)
tk.Button(pencere, text="C", width=5, command=temizle).grid(row=6, column=4)

pencere.mainloop()