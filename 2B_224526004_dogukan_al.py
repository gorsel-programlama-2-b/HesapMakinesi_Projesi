import tkinter as tk
from tkinter import messagebox

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.columnconfigure((0,1,2,3,4), weight = 1, uniform = "x")
        self.rowconfigure((0,1,2,3,4,5), weight = 1, uniform = "x")
        self.geometry("400x400")
        self.title("calculator")
        
        
        # widgets 
        self.value = tk.StringVar(value = "0")
        self.label = tk.Label(self,text = "0",textvariable=self.value).grid(column = 0, columnspan=3, row = 0, sticky="nwse")
        self.m_values = []
        
        self.MC = tk.Button(self,text = "MC",command = self.clear).grid(column = 4,row = 2,sticky="nwse")
        self.MP = tk.Button(self,text = "M+",command = lambda : self.m_values.append(self.value.get())).grid(column = 4,row = 3,sticky="nwse")
        self.MM = tk.Button(self,text = "M-",command = lambda : self.m_values.append("-" + self.value.get())).grid(column = 4,row = 4,sticky="nwse")
        self.MR = tk.Button(self,text = "MR",command = self.calculate_m).grid(column = 4,row = 5,sticky="nwse")
        
        self.equal = tk.Button(self,text = "=",command = self.calculate).grid(row = 1,column = 0,sticky="nwse")
        self.clear = tk.Button(self,text = "C",command = lambda : self.value.set(value = "0")).grid(row = 1,column = 1,sticky="nwse")
        self.faktoriyel = tk.Button(self,text = "!",command =lambda:self.append("!")).grid(row = 1,column = 2,sticky="nwse")
        self.mutlak_deger = tk.Button(self,text = "M",command =lambda: self.value.set(value=abs(int(self.value.get())))).grid(row = 1,column = 3,sticky="nwse")
        self.button0 = tk.Button(self,text = "0",command=lambda: self.append("0")).grid(row = 5 ,column = 0,sticky="nwse",columnspan=3)
        self.button1 = tk.Button(self,text = "1",command=lambda: self.append("1")).grid(row = 2 ,column = 0,sticky="nwse")
        self.button2 = tk.Button(self,text = "2",command=lambda: self.append("2")).grid(row = 2 ,column = 1,sticky="nwse")
        self.button3 = tk.Button(self,text = "3",command=lambda: self.append("3")).grid(row = 2 ,column = 2,sticky="nwse")
        self.button4 = tk.Button(self,text = "4",command=lambda: self.append("4")).grid(row = 3 ,column = 0,sticky="nwse")
        self.button5 = tk.Button(self,text = "5",command=lambda: self.append("5")).grid(row = 3 ,column = 1,sticky="nwse")
        self.button6 = tk.Button(self,text = "6",command=lambda: self.append("6")).grid(row = 3 ,column = 2,sticky="nwse")
        self.button7 = tk.Button(self,text = "7",command=lambda: self.append("7")).grid(row = 4 ,column = 0,sticky="nwse")
        self.button8 = tk.Button(self,text = "8",command=lambda: self.append("8")).grid(row = 4 ,column = 1,sticky="nwse")
        self.button9 = tk.Button(self,text = "9",command=lambda: self.append("9")).grid(row = 4 ,column = 2,sticky="nwse")
        self.collection = tk.Button(self,text = "+",command=lambda: self.append("+")).grid(row = 2, column = 3, sticky = "nwse")
        self.extraction = tk.Button(self,text = "-",command=lambda: self.append("-")).grid(row = 3, column = 3, sticky = "nwse")
        self.impact = tk.Button(self,text = "*",command=lambda: self.append("*")).grid(row = 4, column = 3, sticky = "nwse")
        self.divide = tk.Button(self,text = "/",command=lambda: self.append("/")).grid(row = 5, column = 3, sticky = "nwse")
        self.mainloop()
        
        
    def append(self,value):
        if self.value.get() == "0":
            self.value.set(value = value)
        else:
            new_value = self.value.get() + value
            self.value.set(value = new_value)
    
    def calculate(self):
        try:
            if "!" in self.value.get():
                result = 1
                for i in range(1,int(self.value.get()[:-1])+1):
                    result *= i
                self.value.set(value = str(result))
            
            else:   
                result = eval(self.value.get())
                self.value.set(value = result)
        except ZeroDivisionError:
            self.value.set(value = "0")
            messagebox.showinfo(title="Error",message="0 a bölünemez")

    def calculate_m(self):
        result = ""
        for i in self.m_values:
            result += i
        if result == "":
            self.value.set(value = "0")
        else:
            result = eval(result)
            self.value.set(value = result)
            self.m_values = []
        
    def clear(self):
        self.m_values = []
if __name__ == "__main__":
    app = App()