import tkinter as tk
from disleksitest import disleksitest


class hastakayıtscreen:
    def haskay():
        hastakayıt = tk.Tk()

        hastakayıt.title("disVRtek Hasta Ekranı")
        hastakayıt.geometry("500x300+700+300")

        ad = tk.Label(hastakayıt, text="adınız : ",
                      font="Arial 12 bold").place(x=10, y=10)

        ad_entry = tk.Entry(hastakayıt).place(x=80, y=13)

        soyad = tk.Label(hastakayıt, text="soyadınız : ",
                         font="Arial 12 bold").place(x=215, y=10)

        soyad_entry = tk.Entry(hastakayıt).place(x=315, y=13)

        tc = tk.Label(hastakayıt, text="TC No : ",
                      font="Arial 12 bold").place(x=10, y=50)

        tc_entry = tk.Entry(hastakayıt).place(x=80, y=53)

        email = tk.Label(hastakayıt, text="Email : ",
                         font="Arial 12 bold").place(x=247, y=50)

        email_entry = tk.Entry(hastakayıt).place(x=313, y=53)

        cinsiyet = tk.Label(hastakayıt, text="Cinsiyet",
                            font="Arial 12 bold").place(x=100, y=90)

        e = tk.IntVar()

        e.set(0)

        k = tk.IntVar()

        k.set(0)

        def checkboxtık():
            if e.get() == 1:
                k.set(0)
                print("Erkek")
            elif k.get() == 1:
                e.set(0)
                print("Kız")

        erkek_check = tk.Checkbutton(
            hastakayıt, text="E", font="bold", variable=e, command=checkboxtık).place(x=180, y=90)

        kız_check = tk.Checkbutton(
            hastakayıt, text="K", font="bold", variable=k, command=checkboxtık).place(x=230, y=90)
        
        kaydı_tamamla=tk.Button(hastakayıt,text="Kaydı Tamamla ve Teste Git",font="12",command=disleksitest.test).place(x=136, y=150)

        hastakayıt.mainloop()


# hastakayıtscreen.haskay()
