import json
import tkinter as tk
from tkinter import Entry, Button, END, Label
from datetime import date
import matplotlib.pyplot as plt



def save():
    sleep_time=entry_box.get()#get kullanıcıda metin almak için kullanılıyor ve her zaman string döndürür
    try:
        sleep_time=float(sleep_time)#sayıya çevirdik
        day=date.today().isoformat()#date.today bugünün tarihini verir,iso format ise bunu gün ay yıla çevirir,yani stringe çevirir.

        new_record={"date":day,"sleep_time":sleep_time}#verileri bir sözlükte kaydettik
        try:
          with open("datas.json","r") as data:#datas sı data diye okuma modunda açtım
             datas=json.load(data)#bu data içindeki verileri bir python sözlüğü olarak kaydeder.(dict yani),dosya asıl kod verileridir load ile bu kodlar json formatına çevrilmiştir
        except FileNotFoundError:#eğer veriler diye bir dosya yoksa hatayı bulur
             datas=[]#veriler yeni boş bir sözlüğe atanır

        datas.append(new_record)#üstteki kayıtlar bu listeye eklenir.

        with open("datas.json","w") as data:
             json.dump(datas,data,indent=2)#indent daha güzel bir metin sağlar bize alt alta yazar

        print("Veri kaydedildi",new_record)
        entry_box.delete(0,END)#girilen değer kullanıldıktan sonra kutucuktaki değeri sıfırlar ki yeni bir değer girilisin

    except ValueError:
           print("please enter a valid number")

def show_graphic():
    try:
        with open("datas.json","r") as data:
           datas=json.load(data)#python formatında açtık
        if not datas:
            print("there is not datas yet")
            return

        tarihler=[k["date"] for k in datas]
        süreler=[k["sleep_time"] for k in datas]


        plt.plot(tarihler,süreler,marker="o")#tarih verilerini süreler ile eşleştirdik,marker da bu noktalara işaret koydu
        plt.title("Sleep Tracker")
        plt.xlabel("date")
        plt.ylabel("Sleep time(hour)")
        plt.xticks(rotation=45)#tarih yazıları birbirine karışmasın  diye
        plt.tight_layout()#Kenar boşluklarını ayarlar taşmayı önler
        plt.show()#grafiği ekranda gösterir

    except FileNotFoundError:
        print("File of save not found")



root=tk.Tk() #kök pencere,root istediğimiz gibi atadığımız bir değişken.
root.title("Günlük uyku Takip Uygulaması")#başlık
root.geometry("400x300")#pencerenin boyutları

sticker=tk.Label(root,text="Kaç saat uyudun bugün")#Label istenilen pencereye metin ekler

entry_box=Entry(root) #pencereye bir giriş kutusu ekler

save_button=Button(root,text="Kaydet",command=save)#Buton oluşturduk,üzerine kaydet yazıp,buton çalıştığında hangi fonksiyon çalışacak belirledik
#ara yüze yerleştirme
sticker.grid(row=0,column=0,padx=10,pady=10)
entry_box.grid(row=1,column=0,padx=10)
save_button.grid(row=2,column=0,pady=10)
grafik_buton = Button(root, text="Grafiği Göster", command=show_graphic)#grafik butonunu ekledik
grafik_buton.grid(row=3, column=0, pady=10)#4. satır 1. sutün ve yukarı kısmı ile aşağı kısmı arasında 10 piksel olacak kadar
root.mainloop()#pencerenin hemen kapanmasını engeller




