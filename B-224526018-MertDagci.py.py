# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 15:10:15 2023

@author: C-117
"""

import tkinter as tk

def sayi_tikla(sayi):
    ifade = giris_alani.get()
    giris_alani.delete(0, tk.END)
    giris_alani.insert(0, ifade + str(sayi))

def islem_tikla(islem):
    ifade = giris_alani.get()
    giris_alani.delete(0, tk.END)
    giris_alani.insert(0, ifade + " " + islem + " ")

def hesapla():
    ifade = giris_alani.get()
    try:
        sonuc = eval(ifade)
        giris_alani.delete(0, tk.END)
        giris_alani.insert(0, sonuc)
    except:
        giris_alani.delete(0, tk.END)
        giris_alani.insert(0, "Hata")

def hesapla_faktoriyel(number):
    factorial = 1
    if number >= 0:
        for i in range(1, number + 1):
            factorial *= i
        return factorial
    else:
        return None
 
def bellek_kaydet():
    global bellek
    bellek = giris_alani.get()

def bellek_ekle():
    global bellek
    try:
        bellek = str(float(bellek) + float(giris_alani.get()))
    except:
        bellek = "Hata"

def bellek_cikar():
    global bellek
    try:
        bellek = str(float(bellek) - float(giris_alani.get()))
    except:
        bellek = "Hata"

def bellek_oku():
    giris_alani.delete(0, tk.END)
    giris_alani.insert(0, bellek)

def temizle():
    giris_alani.delete(0, tk.END)
    
    

pencere = tk.Tk()
pencere.title("Hesap Makinesi")

giris_alani = tk.Entry(pencere, width=30)
giris_alani.grid(row=0, column=0, columnspan=4)

sayilar = "7894561230"
satir, sutun = 1, 0
for sayi in sayilar:
    tk.Button(pencere, text=sayi, width=8, command=lambda num=sayi: sayi_tikla(num)).grid(row=satir, column=sutun)
    sutun += 1
    if sutun > 2:
        sutun = 0
        satir += 1

tk.Button(pencere, text=",", width=8, command=lambda: sayi_tikla(".")).grid(row=4, column=1)
tk.Button(pencere, text="=", width=8, command=hesapla).grid(row=4, column=2)
tk.Button(pencere, text="+", width=8, command=lambda: islem_tikla("+")).grid(row=1, column=3)
tk.Button(pencere, text="-", width=8, command=lambda: islem_tikla("-")).grid(row=2, column=3)
tk.Button(pencere, text="!", width=8, command= lambda: hesapla_faktoriyel("!")).grid(row=3, column=3)
tk.Button(pencere, text="/", width=8, command=lambda: islem_tikla("/")).grid(row=4, column=3)

bellek = ""

tk.Button(pencere, text="MC", width=8, command=temizle).grid(row=6, column=0)
tk.Button(pencere, text="M+", width=8, command=bellek_ekle).grid(row=6, column=1)
tk.Button(pencere, text="M-", width=8, command=bellek_cikar).grid(row=6, column=2)
tk.Button(pencere, text="MR", width=8, command=bellek_oku).grid(row=6, column=3)
tk.Button(pencere, text="C", width=8, command=temizle).grid(row=1, column=4)

pencere.mainloop()
