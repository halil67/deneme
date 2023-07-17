import os
import random
#import kategori


class Urun:
    urunler=[]
    def __init__(self,ktg_id,urun_id,adi,fiyat,puan):
        self.ktg_id=ktg_id
        self.urun_id=urun_id
        self.adi=adi
        self.fiyat=fiyat
        self.puan=puan
class Urun_islemleri:
    def kod_olustur(self):
        return random.randint(10000,99999)
    def urun_kaydet(self):
        strg=[]
        dosya_adi="urun.csv"
        if Urun.urunler:
            for urn in Urun.urunler:
                strg.append(f"{urn.ktg_id};{urn.urun_id};{urn.adi};{urn.fiyat};{urn.puan}\n")
            with open(dosya_adi,"w",encoding="utf-8") as fl:
                fl.writelines(strg)
        self.urun_oku()
    
    def Urun_ekle(self):
        if not self.kategoriler:self.kategori_oku()
        urun_id=self.kod_olustur()
        ktg_id=input("Kategori Kodu:")
        adi=input("Ürün Adi")
        fiyat=input("Ürün Fiyatı Giriniz")
        urn_rnd=random.randint(1,100)
        urun=Urun(ktg_id,urun_id,adi,fiyat,urn_rnd)
        Urun.urunler.append(urun)
        self.urun_kaydet()
        
    def urun_sil(self,ktg_id,urun_id):
        if not Urun.urunler:self.urun_oku()
        if Urun.urunler:
            for urn in Urun.urunler:
                if ktg_id==urn.ktg_id and urn.urun_id==urun_id:
                    Urun.urunler.remove(urn)
                    self.urun_kaydet()
    
    def urun_listele(self):
        if not Urun.urunler:self.urun_oku()
        print(f"Kategori kodu Urun Kodu  Urun Adı Fiyatı Ağırlığı")
        if Urun.urunler:
            for urn in Urun.urunler:
                print (f"  {urn.ktg_id}-{urn.urun_id}   {urn.adi}  {urn.fiyat}  {urn.puan}\n")
    
    def urun_oku(self):
        dosya_adi="urun.csv"
        Urun.urunler.clear
        if os.path.exists(dosya_adi):
            with open(dosya_adi,"r",encoding="utf-8") as fl:
                for satır in fl:
                    satır=satır.strip()
                    k_id,u_id,adi,fiyat,puan=satır.split(";")
                    urun=Urun(k_id,u_id,adi,fiyat,puan)
                    Urun.urunler.append(urun)
    kategriler=[]
    def kategori_oku(self):
        dosya_adi="kategori.csv"
        if os.path.exists(dosya_adi):
            with open(dosya_adi,"r",encoding="utf-8") as fl:
                for satır in fl:
                    satır=satır.strip()
                    k_id,adi,puan=satır.split(";")
                    self.kategriler.append([k_id,adi,puan])
                    
    def auto_urun(self):
        if not self.kategriler:self.kategori_oku()
        for ktg in self.kategriler:
            ktg_kod=ktg[0]
            for i in range(1,10):
                urn_kod=self.kod_olustur()
                urn_adi=f"{i}. Urun"
                urn_rnd=random.randint(1,100)
                urn_fiyat=random.randint(1,50)
                urun=Urun(ktg_kod,urn_kod,urn_adi,urn_fiyat,urn_rnd)
                Urun.urunler.append(urun)
        self.urun_kaydet()
        
    def urun_menu(self):
            while True:
                print("*******************************************************")
                print("** 1 - Ürün Ekle_____________________________________**")
                print("** 2 - Ürün Sil______________________________________**")
                print("** 3 - Ürün Listele__________________________________**")
                print("** 4 - Auto Ürün Ekle________________________________**")
                print("** 5 - Çıkış_________________________________________**")
                print("*******************************************************")
                secim=input("Seçimizniz:")
                if secim=="1":
                    self.urun_ekle()
                elif secim=="2":
                    mst_id=input("Urun Kodunu Giriniz:")
                    self.urun_sil(mst_id)
                elif secim=="3":
                    self.urun_listele()
                elif secim=="4":
                    self.auto_urun()
                elif secim=="5":
                    break
