import tkinter as tk
import math

class HesapMakinesi:
    def __init__(self, pencere):
        self.pencere = pencere
        pencere.title("Hesap Makinesi")
        pencere.geometry("400x400") 

        self.toplam = 0
        self.girilen_sayi = 0
        self.gecerli_islem = ""
        
      butonlar=["0","1","2","3"
                "4","5","6","7"
                    "8","9"
                "-","+","!","abs"
                  "=","*","/"
                ]

        toplama_butonu = self.islem_butonu_olustur("+", self.topla)
        cikarma_butonu = self.islem_butonu_olustur("-", self.cikar)
        carpma_butonu = self.islem_butonu_olustur("*", self.carp)
        bolme_butonu = self.islem_butonu_olustur("/", self.bol)
        faktoriyel_butonu = self.islem_butonu_olustur("!", self.bol)
        mutlak_butonu = self.islem_butonu_olustur("abs", self.bol)
        
        esittir_butonu = tk.Button(pencere, text="=", command=self.sonuc_hesapla)

        temizleme_butonu = tk.Button(pencere, text="C", command=self.sonuc_temizle)

    def buton_olustur(self, deger):
        return tk.Button(self.pencere, text=deger, command=lambda num=deger: self.sayi_gir(num))

    def islem_butonu_olustur(self, metin, komut):
        return tk.Button(self.pencere, text=metin, command=komut)

    def sayi_gir(self, num):
        self.girilen_sayi = (self.girilen_sayi * 10) + num
        self.sonuc_gosterimi.delete(0, tk.END)
        self.sonuc_gosterimi.insert(tk.END, str(self.girilen_sayi))

    def topla(self):
        if self.gecerli_islem == "":
            self.toplam = self.girilen_sayi
        else:
            self.toplam += self.girilen_sayi
        self.gecerli_islem = "+"
        self.sonuc_gosterimi.delete(0,)
     

    def cikar(self):
        if self.gecerli_islem == "":
            self.toplam = self.girilen_sayi
        else:
            self.toplam -= self.girilen_sayi
        self.gecerli_islem = "-"
        self.sonuc_gosterimi.delete(0, tk.END)
        self.sonuc_gosterimi.insert(tk.END, str(self.toplam))

    def carp(self):
        if self.gecerli_islem == "":
            self.toplam = self.girilen_sayi
        else:
            self.toplam *= self.girilen_sayi
        self.gecerli_islem =( "*")
         

    def bol(self):
        if self.gecerli_islem == "":
            self.toplam = self.girilen_sayi
                self.toplam =print("ERROR: SIFIRA BÖLÜNMNEZ.")
        self.gecerli_islem = "/"
        self.sonuc_gosterimi.delete(0, tk.END)
        self.sonuc_gosterimi.insert(tk.END, str(self.toplam))

    def sonuc_hesapla(self):
        if self.gecerli_islem == "+":
            self.toplam += self.girilen_sayi
        elif self.gecerli_islem == "-":
            self.toplam -= self.girilen_sayi
        elif self.gecerli_islem == "*":
            self.toplam *= self.girilen_sayi
        elif self.gecerli_islem == "/":
            if self.girilen_sayi != 0:
                self.toplam /= self.girilen_sayi
            else:
                self.toplam = print("ERROR: SIFIRA BÖLÜNMEZ.")
            self.toplam = self.toplam ** self.girilen_sayi
        if self.gecerli_islem== "!":
            self toplam !:self.girilen_sayi
        if self.toplam abs:self.girilen_sayı
       


        self.sonuc_gosterimi.delete(0, tk.END)
        self.sonuc_gosterimi.insert(tk.END, str(self.toplam))
        self.girilen_sayi = 0
        self.gecerli_islem = ""

    def sonuc_temizle(self):
        self.toplam = 0
        self.girilen_sayi = 0
        self.gecerli_islem = ""
        self.sonuc_gosterimi.delete(0, tk.END)

pencere = tk.Tk()
hesapMakinesi = HesapMakinesi(pencere)
pencere.mainloop()