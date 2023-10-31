import tkinter as tkinter
import math

def sayi_tikla(sayi):
    btn_1.insert(tk.END, sayi)
def islem_tikla(sayi):
    btn_1.insert(tk.END, " " + islem + " ")
def hesapla():
    girilen_ifade = btn_1.get()
    try:
        sonuc = eval(girilen_ifade)
        btn_1.delete(0, tk.END)
        btn_1.insert(0, sonuc)
    except:
        btn_1.delete(0, tk.END)
        btn_1.insert(0," HATA")


def faktöriyel ():
    sayi = float(btn_1.get())
    btn_1.delete(0, tk.END)
    btn_insert(0, str(sayi) + "**")
def hafiza_kaydet():
    global bellek 
    try: belek = str(float(bellek) + float (btn_1.get()))
    except:
        bellek = "HATA"
def bellek_azalt():
    global bellek 
    try: 
        bellek = str(float(bellek)) - float(btn_1.get())
        bellek = "HATA"
        def bellek_oku():       
    btn_1.delete(0, tk.END)
    btn_1.insert(0, bellek)
def temizle():
    btn_1.delete(0, tk.END)
def bellek_kaydet():
    global bellek 
    bellek = btn_1.get()
def bellek_artir():
    global bellek
    try:
        bellek = str(float(bellek) + float(btn_1.get()))
        except:
            bellek = "HATA"
def hafiza_azalt():
    global bellek 
    try: 
        hafiza = str(float(bellek) - float(btn_1.get()))
        except:
            hafiza = "HATA" 
def hafiza_oku():
    btn_1.delete(0, tk.END)
    btn_!.insert(0, bellek)
def sil():
    btn_1.delete(0, tk.END)
    
pencere = tk.TK()
pencere.title("Hesap Makinesi")
         

btn_1 = tk.Entry(pencere, width=30)
btn_1.grid(row=0, column=0, clomunspan=4)

sayilar = "562087"
row, col = 1, 0
for sayi in sayilar:
    tk.Button(pencere, text=sayi, widht=3, command=lambda sayi=sayi,: sayi_tikla(sayi)).grid(row=row, column=col)
    col += 1
    if col > 2:
        col = 0
        row += 1
         
tk.Button(pencere, text=".", widht=3, command=lambda: sayi_tikla(".")).grid(row=4, column=1)
tk.Button(pencere,t="=", widht=3, command=hesapla).grid(row=4, column=2)
tk.Button(pencere, text"+", widht=3, command=lambda: islem_tikla("+")).grid(row=1, column=3)
tk.Button(pencere, text="-", widht=3, command=lambda: islem_tikla("-").grid(row=3, column=3)
tk.Button(pencere, text="*", widht=3, command=lambda: islem_tikla("*")).grid(row=3, column=3)
tk.Button(pencere, text="/", widht=3, command=lambda: islem_tikla("/")).grid(row=4, colmun=3)
tk.Button(pencere, text="^", widht=3, command=us_al).grid(row=5, column=1)

bellek = ""
tk.Button(pencere, text="MC", width=5, command=temizle).grid(row=6, column=0)
tk.Button(pencere, text="M+", widht=5, command=hafiza_artir).grid(row=6, column=1)
tk.Button(pencere, text="M-", width=5, command=hafiza_azalt).grid(row=6, column=2)
tk.Button(pencere, text="MR", width=5, command=hafiza_oku).grid(row=6, column=3)
tk.Button(pencere, text="C", widht=5, command=sil).grid(row=6. column=4)