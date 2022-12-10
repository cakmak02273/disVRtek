import tkinter as tk
import random as rnd
from sesyazma import sesisle


r_sayı = rnd.randint(0, 2)


class disleksitest:

    def test():
        
        test = tk.Tk()
        test.title("disleksi tanı arayüzü")
        test.geometry("600x750+700+100")
        

        metin_dizi = ["Destan: Önemli tarihsel olayların efsaneleşmiş hikayeleridir.Milletlerin tarih öncesi  \ndönemlerdeki kuraklık göç deprem gibi büyük felaketlerini dile getiren destanlar\n bu bakımdan ulusal ve anonim ürünlerdir.",
                      "Masal: Yazarı belli olmayan olayları bilinmeyen bir ülkede ve zamanda geçen \niçinde olağanüstü olayların geçtiği kendine özgü anlatım biçimi olan edebi metinlerdir. \nBaşlangıçları ve sonuçları kalıplaşmıştır.", "Mesnevi: Uzun aşk maceralarının öğütlerinve çeşitli konuların anlatıldığı \nher beyti kendi içinde uyaklı olan Türk edebiyatı nazım biçimidir."]
        
        metin_label=tk.Label(test,text=metin_dizi[r_sayı],padx=10,pady=10,font="bold").place(x=1)
        
        # toplevel = tk.Toplevel()
        # toplevel.title("toplevel")
        # toplevel.geometry("500x500+700+300")
        
        
        metin_label=tk.Label(test,text=sesisle.sesyaz(),padx=10,pady=10,font="bold").place(x=1,y=200)

        test.mainloop()


disleksitest.test()
