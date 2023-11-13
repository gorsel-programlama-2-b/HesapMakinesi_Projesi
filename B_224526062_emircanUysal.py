# proje : hesapmakinesi emircanuysal programlama 2 sınıf b gurubu
import tkinter as tk
field_text=""
def add_to_field(sth):
    global field_text
    field_text=field_text+str(sth)
    field.delete("1.0","end")
    field.insert("1.0",field_text)
def calculate():
    global field_text
    result=str(eval(field_text))
    field.delete("1.0", "end")
    field.insert("1.0", result)
def clear():
    global field_text
    field_text=""
    field.delete("1.0", "end")

def faktoriyel(n):
    if n == 0:
        return 1
    else:
        return n * faktoriyel(n - 1)



def faktoriel():
    global field_text
    try:
        number = int(field_text)
        result = faktoriyel(number)
        field.delete("1.0", "end")
        field.insert("1.0", result)
    except ValueError:
        field.delete("1.0", "end")
        field.insert("1.0", "Geçersiz Giriş")



def mutlak_deger(n):
    return abs(n)

def mutlakdeger():
    global field_text
    try:
        sayi = float(field_text)
        result = mutlak_deger(sayi)
        field.delete("1.0", "end")
        field.insert("1.0", result)
    except ValueError:
        field.delete("1.0", "end")
        field.insert("1.0", "Geçersiz Giriş")


pencere=tk.Tk()
pencere.geometry("300x300")
field=tk.Text(pencere,height=2,width=21,font=("Times New Roman",20))
field.grid(row=1,column=1,columnspan=4)

#####################################################
# numara butonları
#####################################################
btn1=tk.Button(pencere,text="1",command=lambda: add_to_field(1),width=5,font=("Times New Roman",14))
btn1.grid(row=4,column=1)

btn2=tk.Button(pencere,text="2",command=lambda: add_to_field(2),width=5,font=("Times New Roman",14))
btn2.grid(row=4,column=2)

btn3=tk.Button(pencere,text="3",command=lambda: add_to_field(3),width=5,font=("Times New Roman",14))
btn3.grid(row=4,column=3)

btn4=tk.Button(pencere,text="4",command=lambda: add_to_field(4),width=5,font=("Times New Roman",14))
btn4.grid(row=3,column=1)

btn5=tk.Button(pencere,text="5",command=lambda: add_to_field(5),width=5,font=("Times New Roman",14))
btn5.grid(row=3,column=2)

btn6=tk.Button(pencere,text="6",command=lambda: add_to_field(6),width=5,font=("Times New Roman",14))
btn6.grid(row=3,column=3)

btn7=tk.Button(pencere,text="7",command=lambda: add_to_field(7),width=5,font=("Times New Roman",14))
btn7.grid(row=2,column=1)

btn8=tk.Button(pencere,text="8",command=lambda: add_to_field(8),width=5,font=("Times New Roman",14))
btn8.grid(row=2,column=2)

btn9=tk.Button(pencere,text="9",command=lambda: add_to_field(9),width=5,font=("Times New Roman",14))
btn9.grid(row=2,column=3)

btn0=tk.Button(pencere,text="0",command=lambda: add_to_field(0),width=5,font=("Times New Roman",14))
btn0.grid(row=5,column=1)



#####################################################
# operator
#####################################################
btn_plus=tk.Button(pencere,text="+",command=lambda: add_to_field("+"),width=5,font=("Times New Roman",14))
btn_plus.grid(row=4,column=4)

btnEksi=tk.Button(pencere,text="-",command=lambda: add_to_field("-"),width=5,font=("Times New Roman",14))
btnEksi.grid(row=5,column=4)

btn_times=tk.Button(pencere,text="*",command=lambda: add_to_field("*"),width=5,font=("Times New Roman",14))
btn_times.grid(row=3,column=4)

btnBöl=tk.Button(pencere,text="/",command=lambda: add_to_field("/"),width=5,font=("Times New Roman",14))
btnBöl.grid(row=2,column=4)

btnSil=tk.Button(pencere,text="clear",command=lambda: clear(),width=5,font=("Times New Roman",14))
btnSil.grid(row=5,column=3)

btnNokta=tk.Button(pencere,text=".",command=lambda: add_to_field("."),width=5,font=("Times New Roman",14))
btnNokta.grid(row=5,column=2)

btn_open_parenthesis=tk.Button(pencere,text="(",command=lambda: add_to_field("("),width=5,font=("Times New Roman",14))
btn_open_parenthesis.grid(row=6,column=1)

btn_close_parenthesis=tk.Button(pencere,text=")",command=lambda: add_to_field(")"),width=5,font=("Times New Roman",14))
btn_close_parenthesis.grid(row=6,column=2)

btn_equal=tk.Button(pencere,text="=",command=lambda: calculate(),width=13,font=("Times New Roman",14))
btn_equal.grid(row=6,column=3,columnspan=2)


btn_faktöriel = tk.Button(pencere, text="!", command=lambda: faktoriel(), width=5, font=("Times New Roman", 14))
btn_faktöriel.grid(row=6, column=5)


btn_mutlak_deger = tk.Button(pencere, text="|x|", command=lambda: mutlakdeger(), width=5, font=("Times New Roman", 14))
btn_mutlak_deger.grid(row=5, column=5)



pencere.mainloop()

