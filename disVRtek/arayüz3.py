import tkinter as tk
from PIL import Image, ImageTk

form = tk.Tk()
form.title("disVRtek3")
form.geometry("500x500+700+300")

scrol = tk.Scrollbar().pack(side=tk.RIGHT, fill=tk.Y)

toplevel = tk.Toplevel(bg="green")
toplevel.title("toplevel  ")
toplevel.geometry("500x500+700+300")

lbl = tk.Label(toplevel, text="aaaaaaaaaaaaaaaaa",)

text = tk.Text(form, width=20, height=50, padx=20, pady=30,
               bd=10, selectbackground="red").pack()

resim = ImageTk.PhotoImage(Image.open("./göz.png"))
buton = tk.Button(form, image=resim).place(relwidth=500,relheight=350)

form.mainloop()
