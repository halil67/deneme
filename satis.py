import os
import random
import firma
import kategori
import urun
import uuid
import datetime as dt
class Satis:
    satislar=[]
    def __init__(self,musteri_kodu,firma_kodu,kategori_kodu,urun_kodu,urun_adedi,urun_fiyati,satis_tutar,satis_tarihi,satis_saati):
        self.musteri_kodu=musteri_kodu
        self.firma_kodu=firma_kodu
        self.kategori_kodu=kategori_kodu
        self.urun_kodu=urun_kodu
        self.urun_adedi=urun_adedi
        self.urun_fiyati=urun_fiyati
        self.satis_tutar=satis_tutar
        self.satis_tarihi=satis_tarihi
        self.satis_saati=satis_saati

class ShoppingCart:
    def __init__(self):
        self.id=self.kod_olustur()
        self.items = []
    def kod_olustur(self):
        simdi=dt.datetime.now()
        
        return f"{simdi.year}_{simdi.month}_{simdi.day}_{random.randint(100000,999999)}"
    
    def add_item(self, product):
        self.items.append(product)
        
    def remove_item(self, product):
        self.items.remove(product)

    def get_total_price(self):
        total_price = 0.0
        for item in self.items:
            total_price += item[0]["fiyat"]
        return total_price

    def print_items(self):
        for item in self.items:
            print(item[0]["adi"], "-", item[0]["fiyat"])
    def save_to_file(self):
        
        filename = f"{self.id}.txt"  # Dosya adı
        with open(filename, "w") as file:
            for item in self.items:
                file.write(f"{item[0]['k_id']};{item[0]['u_id']};{item[0]['adi']};{item[0]['fiyat']}\n")
class Random_satis:
    urunler=[]
    def urun_oku(self):
        with open("urun.csv","r",encoding="utf-8") as fl:
            for satir in fl:
                satir=satir.strip()
                if satir:
                    k_id,u_id,adi,fiyat,puan=satir.split(";")
                    self.urunler.append({"k_id":k_id,"u_id":u_id,"adi":adi,"fiyat":float(fiyat),"puan":puan})
    
    firmalar=[]
    firma_agirlik=[]
    def firma_oku(self):
        with open("firmalar.csv","r",encoding="utf-8") as fl:
            for satir in fl:
                satir=satir.strip()
                if satir:
                    f_id,f_adi,puan=satir.split(";")
                    self.firmalar.append({"f_id":f_id,"f_adi":f_adi,"puan":puan})
        self.firma_agirlik=[int(p["puan"]) for p in self.firmalar]
    
    kategoriler=[]
    kat_agirlik=[]
    def kategori_oku(self):
        with open("kategori.csv","r",encoding="utf-8") as fl:
            for satir in fl:
                satir=satir.strip()
                if satir:
                    k_id,k_adi,puan=satir.split(";")
                    self.kategoriler.append({"k_id":k_id,"f_adi":k_adi,"puan":puan})
        self.kat_agirlik=[int(p["puan"]) for p in self.kategoriler]
    
    musteriler=[]
    mus_agirlik=[]
    def musteri_oku(self):
        with open("musteri.csv","r",encoding="utf-8") as fl:
            for satir in fl:
                satir=satir.strip()
                if satir:
                    m_id,m_adi,m_soyadi,m_cns,m_yas,puan,tarih=satir.split(";")
                    self.musteriler.append({"m_id":m_id,"m_adi":m_adi,"m_soyadi":m_soyadi,"m_cns":m_cns,"m_yas":m_yas ,"puan":puan,"k_tarih":tarih})
        self.mus_agirlik=[int(p["puan"]) for p in self.musteriler]
    def satis_yap(self):
        if not self.firmalar:self.firma_oku()
        if not self.kategoriler:self.kategori_oku()
        if not self.urunler:self.urun_oku()
        if not self.musteriler:self.musteri_oku()
        
        r_musteri_id=random.choices(self.musteriler,weights=self.mus_agirlik)[0]["m_id"]
        r_firma_id=random.choices(self.firmalar,weights=self.firma_agirlik)[0]["f_id"]
        urn_say=random.randint(1,10)
        cart = ShoppingCart()
        for i in range(1,urn_say):
            r_kategori_id=random.choices(self.kategoriler,weights=self.kat_agirlik)[0]["k_id"]
            s_urnler=[u for u in self.urunler if u["k_id"]==r_kategori_id]
            s_urun_agirlik=[int(p["puan"]) for p in s_urnler]
            s_urun=random.choices(s_urnler,weights=s_urun_agirlik)
            # Alışveriş sepeti oluşturma
            selected_product = s_urun
            cart.add_item(selected_product)
            print(f"{selected_product[0]['adi']} sepete eklendi.")
        # Sepetin içeriğini ve toplam fiyatı yazdırın
        print("\nSepetin İçeriği:")
        cart.print_items()
        cart.save_to_file()
        top_fiyat=cart.get_total_price()
        tarih=dt.datetime.now().date
        with open("satis.csv","a",encoding="utf-8") as fl:
            strg=f"{r_firma_id};{r_musteri_id};{cart.id};{tarih}"
        

class Satis_islemleri:
    pass
s=Random_satis()
for i in range(0,10000):
    s.satis_yap()
