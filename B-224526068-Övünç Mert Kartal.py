class HesapMakinesi:
    def __init__(self):
        self.sonuc = 0

    def topla(self, sayi):
        self.sonuc += sayi

    def cikar(self, sayi):
        self.sonuc -= sayi

    def carp(self, sayi):
        self.sonuc *= sayi

    def bol(self, sayi):
        if sayi != 0:
            self.sonuc /= sayi
        else:
            print("Hata! Sıfıra bölme hatası.")

    def faktoriyel(self, sayi):
        faktoriyel = 1
        for i in range(1, sayi + 1):
            faktoriyel *= i
        self.sonuc = faktoriyel

    def mutlak_deger(self, sayi):
        self.sonuc = abs(sayi)

    def mc(self):
        self.sonuc = 0

    def m_plus(self, sayi):
        self.sonuc += sayi

    def m_minus(self, sayi):
        self.sonuc -= sayi

    def mr(self):
        return self.sonuc

    def temizle(self):
        self.sonuc = 0


hesap_makinesi = HesapMakinesi()

while True:
    print("1: Topla")
    print("2: Çıkar")
    print("3: Çarp")
    print("4: Böl")
    print("5: Faktoriyel")
    print("6: Mutlak Değer")
    print("7: MC (Memory Clear)")
    print("8: M+ (Memory Plus)")
    print("9: M- (Memory Minus)")
    print("10: MR (Memory Recall)")
    print("11: Temizle")
    print("0: Çıkış")

    secim = input("Yapmak istediğiniz işlemi seçin: ")

    if secim == "0":
        print("Hesap makinesi kapatılıyor...")
        break
    elif secim == "1":
        sayi = float(input("Toplama işlemi için sayı girin: "))
        hesap_makinesi.topla(sayi)
        print("Sonuç:", hesap_makinesi.sonuc)
    elif secim == "2":
        sayi = float(input("Çıkarma işlemi için sayı girin: "))
        hesap_makinesi.cikar(sayi)
        print("Sonuç:", hesap_makinesi.sonuc)
    elif secim == "3":
        sayi = float(input("Çarpma işlemi için sayı girin: "))
        hesap_makinesi.carp(sayi)
        print("Sonuç:", hesap_makinesi.sonuc)
    elif secim == "4":
        sayi = float(input("Bölme işlemi için sayı girin: "))
        hesap_makinesi.bol(sayi)
        print("Sonuç:", hesap_makinesi.sonuc)
    elif secim == "5":
        sayi = int(input("Faktoriyel hesaplama için sayı girin: "))
        hesap_makinesi.faktoriyel(sayi)
        print("Sonuç:", hesap_makinesi.sonuc)
    elif secim == "6":
        sayi = float(input("Mutlak değer hesaplama için sayı girin: "))
        hesap_makinesi.mutlak_deger(sayi)
        print("Sonuç:", hesap_makinesi.sonuc)
    elif secim == "7":
        hesap_makinesi.mc()
        print("Memory Cleared.")
    elif secim == "8":
        sayi = float(input("Memory'e eklemek istediğiniz sayıyı girin: "))
        hesap_makinesi.m_plus(sayi)
        print("Memory Updated.")
    elif secim == "9":
        sayi = float(input("Memory'den çıkarmak istediğiniz sayıyı girin: "))
        hesap_makinesi.m_minus(sayi)
        print("Memory Updated.")
    elif secim == "10":
        print("Memory Recall: ", hesap_makinesi.mr())
    elif secim == "11":
        hesap_makinesi.temizle()
        print("Hesap makinesi temizlendi. Sonuç: 0")
    else:
        print("Geçersiz bir seçim yaptınız. Lütfen tekrar deneyin.")
