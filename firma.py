import random
import os
class Firma:
    firmalar=[]
    def __init__(self,id,firmaAdi,puan,satis_sayisi=0,toplamSatis=0):
        self.id=id
        self.firmaAdi=firmaAdi
        self.puan=puan
        self.satis_sayisi=satis_sayisi
        self.toplamSatis=toplamSatis
class Firma_islemleri:
    def kod_olustur(self):
        return random.randint(10000,99999)
    def firma_kaydet(self):
        strg=[]
        dosya_adi="firmalar.csv"
        if Firma.firmalar:
            for frm in Firma.firmalar:
                strg.append(f"{frm.id};{frm.firmaAdi};{frm.puan}\n")
            with open(dosya_adi,"w",encoding="utf-8") as fl:
                fl.writelines(strg)
                
    def firma_ekle(self):
        if not Firma.firmalar:self.firma_oku()
        frm_kod=self.kod_olustur()
        frm_adi=input("Firma Adi")
        frm_rnd=random.randint(1,100)
        firma=Firma(frm_kod,frm_adi,frm_rnd)
        Firma.firmalar.append(firma)
        self.firma_kaydet("firmalar.csv")
        
    def firma_sil(self,frm_id):
        if not Firma.firmalar:self.firma_oku("firmalar.csv")
        if Firma.firmalar:
            for frm in Firma.firmalar:
                if frm_id==frm.id:
                    Firma.firmalar.remove(frm)
                    self.firma_kaydet()
    def firma_listele(self):
        if not Firma.firmalar:self.firma_oku()
        print(f"Firma kodu     Firma Adı Ağırlık")
        if Firma.firmalar:
            for frm in Firma.firmalar:
                print (f"{frm.id}- {frm.firmaAdi} {frm.puan}\n")
    
    def firma_oku(self):
        dosya_adi="firmalar.csv"
        Firma.firmalar.clear
        if os.path.exists(dosya_adi):
            with open(dosya_adi,"r",encoding="utf-8") as fl:
                for satır in fl:
                    satır=satır.strip()
                    id,adi,puan=satır.split(";")
                    #satis_sayisi,toplam_satis=self.satis_hesapla(int(id))
                    firma=Firma(int(id),adi,int(puan))
                    Firma.firmalar.append(firma)
            