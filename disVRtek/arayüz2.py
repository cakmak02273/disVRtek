import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Combobox

form = tk.Tk()

form.title("disVRtek 2")
form.geometry("500x500+700+300")




entry = tk.Entry(form)
entry.pack()

# şifre girmek için
entry2 = tk.Entry(form, show="*").pack()


def veri():
    # etiket labelinin text ine entry ye girilenleri gönderiyo
    etiket["text"] = entry.get()


def sil():
    # 0. indexkten sonuncu indexs e kadar
    entry.delete(0, "end")


button = tk.Button(form, text="verileri al", command=veri)
button.pack()


button2 = tk.Button(form, text="DELETE", fg="red",
                    command=sil, activebackground="green")
button2.pack()


etiket = tk.Label(form, text="verilerin buraya gelmesi lazım")
etiket.pack()

x = tk.IntVar()
y = tk.StringVar()

x.set(0)
y.set(0)


def checkb():
    if x.get() == 0:
        print("onaylanmadı")
    else:
        print("onaylandı")


check = tk.Checkbutton(form, text="chechbox", fg="pink",
                       variable=x, command=checkb)
check.pack()


radio = tk.Radiobutton(form, text="radiobutton",
                       activebackground="red", value="1", variable=y)

radio.pack()


def mesaj():
    messagebox.showinfo(title=" showinfo", message="showinfo ")
    messagebox.askretrycancel(title="askretrycancel", message="askretrycancel")
    messagebox.askyesno(title="askyesno", message="askyesno")
   
    


button3 = tk.Button(form, text="Tıkla mesaj gelsin", fg="red",
                    command=mesaj, activebackground="green")
button3.pack()
a=tk.StringVar()
a.set(0)
dizi=["python", "C++","Java", "C#"]
# height methodu combobox da kaç değer görüneceğini söylüyor
kutu=Combobox(form, values=("1","2","3","4","5","6","7"),height=3).pack()
kutu2=Combobox(form, values=(dizi),textvariable=a).pack()
def getdeger():
    print(a.get())
    print(b.get())
buton=tk.Button(form, text="kutu get değer", command=getdeger).pack()
b=tk.StringVar()
b.set(0)
spin=tk.Spinbox(form,from_=1, to=25,textvariable=b).pack()


form.mainloop()
