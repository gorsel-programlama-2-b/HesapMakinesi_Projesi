# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 15:36:00 2023

@author: C-117
"""

import math

class HesapMakinesi:
    def __init__(self):
        self.hafiza = 0
        self.suanki_deger = 0

    def topla(self, x):
        self.suanki_deger += x

    def cikar(self, x):
        self.suanki_deger -= x

    def carp(self, x):
        self.suanki_deger *= x

    def bol(self, x):
        if x != 0:
            self.suanki_deger /= x
        else:
            print("Hata: Sıfıra bölme")

    def faktoriyel(self):
        self.suanki_deger = math.factorial(int(self.suanki_deger))

    def mutlak_deger(self):
        self.suanki_deger = abs(self.suanki_deger)

    def hafiza_kaydet(self):
        self.hafiza = self.suanki_deger

    def hafiza_hatirla(self):
        self.suanki_deger = self.hafiza

    def temizle(self):
        self.suanki_deger = 0

    def goster(self):
        return self.suanki_deger

hesap_makinesi = HesapMakinesi()

while True:
    print("Şuanki Değer:", hesap_makinesi.goster())
    print("Seçenekler:")
    print("1. Topla")
    print("2. Çıkar")
    print("3. Çarp")
    print("4. Böl")
    print("5. Faktoriyel")
    print("6. Mutlak Değer")
    print("7. M (Hafızaya Kaydet)")
    print("8. MR (Hafıza Geri Çağırma)")
    print("9. Temizle")
    print("10. Çıkış")

    secim = input("Seçiminizi yapın: ")

    if secim == '1':
        num = float(input("Toplanacak sayıyı girin: "))
        hesap_makinesi.topla(num)
    elif secim == '2':
        num = float(input("Çıkarılacak sayıyı girin: "))
        hesap_makinesi.cikar(num)
    elif secim == '3':
        num = float(input("Çarpılacak sayıyı girin: "))
        hesap_makinesi.carp(num)
    elif secim == '4':
        num = float(input("Bölünecek sayıyı girin: "))
        hesap_makinesi.bol(num)
    elif secim == '5':
        hesap_makinesi.faktoriyel()
    elif secim == '6':
        hesap_makinesi.mutlak_deger()
    elif secim == '7':
        hesap_makinesi.hafiza_kaydet()
    elif secim == '8':
        hesap_makinesi.hafiza_hatirla()
    elif secim == '9':
        hesap_makinesi.temizle()
    elif secim == '10':
        break
    else:
        print("Hatalı işlem. Tekrar deneyin!")




