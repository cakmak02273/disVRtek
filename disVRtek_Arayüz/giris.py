import tkinter as tk
from hastakayıt import hastakayıtscreen


giris = tk.Tk()
giris.title("disVRtek Giriş Ekranı")
giris.geometry("250x250+700+300")

tc = tk.Label(giris, text="TC : ", font="Arial 16 bold").place(x=10, y=10)

TC_entry = tk.Entry(giris).place(x=70, y=16)

verigetirbutton = tk.Button(giris, text="Verigetir",
                            font="Arial 13").place(x=10, y=60)


hastakayıtbutton = tk.Button(giris, text="Hasta Kayıt", font="Arial 13",
                             command=hastakayıtscreen.haskay).place(x=100, y=60)


giris.mainloop()
