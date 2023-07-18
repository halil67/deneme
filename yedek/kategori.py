import os
import random

class Kategori:
    kategoriler=[]
    def __init__(self,id,adi,puan):
        self.id=id
        self.adi=adi
        self.puan=puan  

class Karegori_islemleri:
    def kod_olustur(self):
        return random.randint(10000,99999)
    
    def Kategori_kaydet(self):
        strg=[]
        dosya_adi="kategori.csv"
        if Kategori.kategoriler:
            for ktg in Kategori.kategoriler:
                strg.append(f"{ktg.id};{ktg.adi};{ktg.puan}\n")
            with open(dosya_adi,"w",encoding="utf-8") as fl:
                fl.writelines(strg)
                
    def kategori_ekle(self):
        if not Kategori.kategoriler:self.kategori_oku()
        ktg_kod=self.kod_olustur()
        ktg_adi=input("Kategori Adi")
        ktg_rnd=random.randint(1,100)
        kategori=Kategori(ktg_kod,ktg_adi,ktg_rnd)
        Kategori.kategoriler.append(kategori)
        self.Kategori_kaydet()
        
    def kategori_sil(self,ktg_id):
        if not Kategori.kategoriler:self.kategori_oku()
        if Kategori.kategoriler:
            for ktg in Kategori.kategoriler:
                if ktg_id==ktg.id:
                    Kategori.kategoriler.remove(ktg)
                    self.kategori_kaydet()
    
    def kategori_listele(self):
        if not Kategori.kategoriler:self.kategri_oku()
        print(f"Kategori kodu   Kategori Adı Ağırlık")
        print("**************************************")
        if Kategori.kategoriler:
            for ktg in Kategori.kategoriler:
                print (f" | {ktg.id} |-    |{ktg.adi}   | {ktg.puan}|\n")
                print("-------------------------------------------")
    
    def kategori_oku(self):
        dosya_adi="kategori.csv"
        Kategori.kategoriler.clear
        if os.path.exists(dosya_adi):
            with open(dosya_adi,"r",encoding="utf-8") as fl:
                for satır in fl:
                    satır=satır.strip()
                    id,adi,puan=satır.split(";")
                    #satis_sayisi,toplam_satis=self.satis_hesapla(int(id))
                    kategori=Kategori(int(id),adi,int(puan))
                    Kategori.kategoriler.append(kategori)
                    
    def auto_kategori(self):
        for i in range(1,10):
            ktg_kod=self.kod_olustur()
            ktg_adi=f"{i}. Kategori"
            ktg_rnd=random.randint(1,100)
            kategori=Kategori(ktg_kod,ktg_adi,ktg_rnd)
            Kategori.kategoriler.append(kategori)
        self.Kategori_kaydet()
        
    def kategori_menu(self):
            while True:
                print("*******************************************************")
                print("** 1 - Kategori Ekle_________________________________**")
                print("** 2 - Kategori Sil___________________________________**")
                print("** 3 - Kategori Listele_______________________________**")
                print("** 4 - Auto Kategori Ekle_____________________________**")
                print("** 5 - Çıkış_________________________________________**")
                print("*******************************************************")
                secim=input("Seçimizniz:")
                if secim=="1":
                    self.kategori_ekle()
                elif secim=="2":
                    mst_id=input("Firma Kodunu Giriniz:")
                    self.kategori_sil(mst_id)
                elif secim=="3":
                    self.kategori_listele()
                elif secim=="4":
                    self.auto_kategori()
                elif secim=="5":
                    break
