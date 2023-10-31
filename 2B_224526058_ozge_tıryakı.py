# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 14:42:39 2023

@author: C-117
"""

import tkinter as tk
import math

def sayı_tıkla(Sayi):
    btn_1.insert(tk.End,sayi)
def islem_tikla(islem):
    btn_1.insert(tk.END, " " + islem + " ")
def hesapla():
    girilen_ifade = btn_1.get()
    try:
        sonuc = eval(girilen_ifade)
        btn_1.delete(0,tk.END)
        btn_1.insert(0,sonuc)
    except:
        btn_1.delete(0,tk.END)
        btn_1.insert(0, "Hata")
def us_al
    sayi=float(btn_1.get())
    btn_1.delete(0. tk.END) 
    btn_1.insert(0, str(sayi) + "**")
def bellek_kaydet():
    global bellek
    bellek: btn_1.get()
def bellek_arttir():
    global bellek
    try: 
        bellek = str(float(bellek)+ float(btn_1.get()))
    except:
        bellek= "Hata"
def bellek_azalt():
    global bellek
    try:
        bellek= str(float(bellek) - float(btn_1.get()))
    except:
        bellek= "Hata"
def bellek_oku():
    btn_1.delete(0. tk.END)
    btn_1.insert(0, bellek) 
def temizle():
    btn_1.delete(0, tk.END)
pencere= tk.Tk()
pencere.title("Hesap Makinesi")
btn_1= tk.Entry(pencere, width=30)
btn_1.grid(row=0, column=0,columspan=4)
sayilar="7894561230"
row, col= 1, 0
for sayi in sayilar
    tk.Button(pencer4e, text=sayi, width=5, command=lambda sayi=sayi: sayi_tikla(sayi)).grid(row=row, column=col)
    col += 1 
    if col > 2:
        col = 0
        row += 1
tk.Button(pencere, text=".", width=5, command=lambda: sayi_tikla(".")).grid(row=4, column=1)
tk.Button(pencere, text="=", width=5, command=hesapla).grid(row=4, column=2)
tk.Button(pencere, text="+", width=5, command=lambda: islem=tikla("+").grid(row=1, column=3)
tk.Button(pencere, text="-", width=5, command=lambda: islem=tikla("-").grid(row=2, column=3)
tk.Button(pencere, text="*", width=5, command=lambda: islem=tikla("*").grid(row=3, column=3)
tk.Button(pencere, text="/", width=5, command=lambda: islem=tikla("/").grid(row=4, column=3)                   
tk.Button(pencere, text="^", width=5, command=us_al).grid(row=5, column=1)

bellek = ""
tk.Button(pencere, text="MC", width=5, command=temizle).grid(row=6, column=0)
 
    
    