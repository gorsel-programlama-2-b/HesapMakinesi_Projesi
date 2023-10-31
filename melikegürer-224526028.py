import tkinter as tk

def hesap_makinesi():
    hesap = tk.Tk()
    hesap.title("Hesap Makinesi")

    pencere= tk.Entry(hesap, width=30, borderwidth=14)
    pencere.grid(row=0, column=0, columnspan=12)
    

    def button_click(sayi):
        mevcut = pencere.get()
        pencere.delete(0, tk.END)
        pencere.insert(0, mevcut + sayi)

    def hesapla():
        try:
            sonuc = print(pencere.get())
            pencere.delete(0, tk.END)
            pencere.insert(0, sonuc)
        except:
            pencere.delete(0, tk.END)
            pencere.insert(0, "Hata")
            


     
    buttonlar = [ 
                  '7','8','9','-',
                  '4','5','6','+',
                  '1','2','3','*',
                  '0','!','=','/',]
    row_val = 1
    col_val = 0

    for button in buttonlar:
        tk.Button(hesap, text=button, padx=30, pady=30, command=lambda b=button: button_click(b) if b != "=" else hesapla()).grid(row=row_val, column=col_val)
        col_val += 1
        if col_val > 3:
            col_val = 0
            row_val += 1

    hesap.mainloop()

hesap_makinesi()