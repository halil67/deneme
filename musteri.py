import random
import datetime
import os
class Musteri:
    musteriler=[]   
    def __init__(self,musteri_kodu,musteri_adi,musteri_soyadi,musteri_cinsiyet,musteri_yas,musteri_Puan,kayit_tarihi):
        self.musteri_kodu=musteri_kodu
        self.musteri_adi=musteri_adi
        self.musteri_soyadi=musteri_soyadi
        self.musteri_cinsiyet=musteri_cinsiyet
        self.musteri_yas=musteri_yas
        self.musteri_Puan=musteri_Puan
        self.kayit_tarihi=kayit_tarihi

class Musteri_islemleri:

    def musteri_oku(self):
        Musteri.musteriler.clear
        dosya_adi="musteri.csv"
        if os.path.exists(dosya_adi):
            with open(dosya_adi,"r",encoding="utf-8") as fl:
                for satir in fl:
                    satir=satir.strip()
                    if satir:
                        musteri_kodu, musteri_Adi,musteri_soyadi,musteri_cinsiyet,musteri_yas, musteri_Puan,kayit_tarihi  =satir.split(";")
                        musteri=Musteri(musteri_kodu, musteri_Adi,musteri_soyadi,musteri_cinsiyet,musteri_yas, musteri_Puan,kayit_tarihi)
                        Musteri.musteriler.append(musteri)
                    
    def musteri_kaydet(self):
        dosya_adi="musteri.csv"
        strg=[]
        if Musteri.musteriler:
            for mst in Musteri.musteriler:
                strg.append(f"{mst.musteri_kodu};{mst.musteri_adi};{mst.musteri_soyadi};{mst.musteri_cinsiyet};{mst.musteri_yas};{mst.musteri_Puan};{mst.kayit_tarihi}\n")
            
            with open(dosya_adi,"w",encoding="utf-8") as fl:
                fl.writelines(strg)
        #self.musteri_oku()

    def kod_olustur(self):
        return random.randint(10000,99999)
    
    def musteri_giris(self):
        musteri_kodu=self.kod_olustur()
        musteri_adi=input("Adınızı Giriniz:")
        musteri_soyadı=input("Soyadınızı Giriniz:")
        musteri_cinsiyet=input("Cinsiyetinizi Giriniz")
        musteri_yas=input("Yaşınızı Giriniz")
        musteri_puan=random.randint(1,100)
        kayit_tarihi=datetime.datetime().date()
        musteri=Musteri(musteri_kodu,musteri_adi,musteri_soyadı,musteri_cinsiyet,musteri_yas,musteri_puan,kayit_tarihi)
        self.musteri_ekle(musteri)
        
    def auto_musteri(self):
        isimler=['Ahmet', 'Mehmet', 'Ali', 'Mustafa', 'Emre', 'İbrahim', 'Hasan', 'Yusuf', 'Ömer', 'Serkan',
            'Ayşe', 'Fatma', 'Zeynep', 'Emine', 'Hatice', 'Esra', 'İrem', 'Aylin', 'Elif', 'Sedef','Deniz', 'Yağmur', 'Cem', 'Ege', 'Can', 'İpek', 'Ceren', 'Aslı', 'Doruk', 'Derin']
        soyadlari = ['Yılmaz', 'Demir', 'Kaya', 'Çelik', 'Aydın', 'Şahin', 'Aksoy', 'Koç', 'Öztürk', 'Can']
        
        for i in range(0,random.randint(1,10)):
            kod=self.kod_olustur()
            ad=random.choice(isimler)
            soyad=random.choice(soyadlari)
            cns=random.choice("EK")
            yas=random.randint(20,50)
            puan=random.randint(1,100)
            tarih=datetime.datetime.now().date()
            while any(musteri.musteri_kodu == kod for musteri in Musteri.musteriler):
                kod = self.kod_olustur()
            musteri=Musteri(kod,ad,soyad,cns,yas,puan,tarih)
            
        self.musteri_ekle(musteri)
            
    def musteri_ekle(self,musteri):
        Musteri.musteriler.append(musteri)
        self.musteri_kaydet()
    
    def musteri_sil(self,mst_id):
        if Musteri.musteriler:
            for mst in Musteri.musteriler:
                if mst_id==mst.musteri_kodu:
                    Musteri.musteriler.remove(mst)
                    break
            self.musteri_kaydet()
            
    def musteri_listele(self):
        if Musteri.musteriler:
            print("Müşteri Listesi")
            print("Kodu     Adı Soyadı     Cns  Yaş     Puan    K.Tarihi")
            print("******************************************************")
            for mst in Musteri.musteriler:
                print(f"* | {mst.musteri_kodu}| {mst.musteri_adi} {mst.musteri_soyadi} | {mst.musteri_cinsiyet} | {mst.musteri_yas} | {mst.musteri_Puan} | {mst.kayit_tarihi} |")
            print("*******************************************************")
            print(f"{len(Musteri.musteriler)} Adet Müşteri Listelendi")
    def musteri_menu(self):
        while True:
            print("*******************************************************")
            print("** 1 - Müşteri Ekle__________________________________**")
            print("** 2 - Müşteri Sil___________________________________**")
            print("** 3 - Müşteri Listele_______________________________**")
            print("** 4 - Auto Müşteri Ekle_____________________________**")
            print("** 5 - Çıkış_________________________________________**")
            print("*******************************************************")
            secim=input("Seçimizniz:")
            if secim=="1":
                self.musteri_ekle()
            elif secim=="2":
                mst_id=input("Müşteri Kodunu Giriniz:")
                self.musteri_sil(mst_id)
            elif secim=="3":
                self.musteri_listele()
            elif secim=="4":
                self.auto_musteri()
            elif secim=="5":
                break
            
            