import tkinter as tk
form = tk.Tk()

form.title("disVRtek")
# 1.500 genişlik 2. 500 yükseklik 700 soldan hizalıyo 300 yukardan hizalıyo
form.geometry("500x500+700+300")
# minimum küçültme
form.minsize(400, 400)
# maksimum büyültme
form.maxsize(700, 700)
# x veya y ekseninde boyutların büyütme veya küçültme yapılıp yapılmaması
form.resizable(True, True)
# uygulamanın hangi boyutda açılacağını belirliyo normal = normal boyutda açıyorken zoomed = full ekran şeklinde açıyo
form.state("normal")
# form.state("zoomed")
# form.state("iconic")


# saydamlık için
# form.wm_attributes("-alpha", 0.3)

textbox= tk.Entry(form,fg="red")
textbox.pack()

etiket = tk.Label(text="tkinter aaaaaaaaaaaa",
                  fg="blue", bg="yellow", font="Times")
# labeli ekranda görünür yapıyo
etiket.pack()

etiket2 = tk.Label(form, text="aaaaaaaaaaaa", font="Times 17 bold")

# labeli ekranda görünür yapıyo
etiket2.pack()


def yaz():
    label = tk.Label(
        form, text="Butona tıklayarak beni yazdırdın", fg="red", bg="black")
    # labelı ekranda görünür yapıyo
    label.pack()


def renkdegis():
    # config etiket labelının özelliklerini değiştirmemize yarıyo
    etiket.config(text="Rengim Değişti", fg="red", bg="black")


button2 = tk.Button(form, text="Tıkla", fg="green",
                    bg="gray", font="Italic 16", command=yaz)

button2.pack(side=tk.LEFT)

button = tk.Button(form, text="renk", fg="green",
                   bg="gray", font="Italic 16", command=renkdegis)

# butonu ekranda görünür yapıyo
button.pack(side=tk.BOTTOM,fill=tk.X)

# expand sayfanın ortasına yerleştiriyo 1 yerine tk.YES de yazılabilir

button3 = tk.Button(form, text="expand", fg="green",
                   bg="gray", font="Italic 16", command=renkdegis)

# butonu ekranda görünür yapıyo
button3.pack(side=tk.BOTTOM,expand=1)


#anchor "n " yukarı "s" aşağı "e" sağ  "w" sol "center" orta kısma konumlandırır
button4 = tk.Button(form, text="anchor")
button4.pack(anchor="ne")

#ipadx ve ipady boyutları ayarlamamıza yarıyor
button5 = tk.Button(form, text="ipad")
button5.pack(anchor="nw",ipadx=20,ipady=20)


button7 = tk.Button(form, text="place_width_hight")
button7.place(width=50,height=50)

# place etiketi istediğimiz yere konumlandırmamıza yarıyor
button6 = tk.Button(form, text="place")
button6.place(x=50,y=100)

# rel komutu ile konumlandırıyoruz ama penceremizi büyütüp küçütüğünde dinamik şekilde hareket ediyor
button6 = tk.Button(form, text="placerel")
button6.place(relx=0.7,rely=0.9)



form.mainloop()


# form2 = tk.Tk()

# form2.title("tkinter2 ")
# etiket = tk.Label(text="tkinter bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb")
# etiket.pack()
# etiket2 = tk.Label(form2, text="bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb")
# etiket2.pack()
# form2.mainloop()
