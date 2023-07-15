import pandas as pd
import matplotlib.pyplot as plt

class Firma:
    firmalar=[]
    def __init__(self,id,firmaAdi,puan,satis_sayisi=0,toplamSatis=0):
        self.id=id
        self.firmaAdi=firmaAdi
        self.puan=puan
        self.satis_sayisi=satis_sayisi
        self.toplamSatis=toplamSatis
        
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
            
class Urun:
    urunler=[]
    def __init__(self,ktg_id,urun_id,adi,fiyat,puan):
        self.ktg_id=ktg_id
        self.urun_id=urun_id
        self.adi=adi
        self.fiyat=fiyat
        self.puan=puan
        
class Kategori:
    kategoriler=[]
    def __init__(self,id,adi,puan):
        self.id=id
        self.adi=adi
        self.puan=puan        
class Musteri:
    musteriler=[]
    def __init__(self,musteri_kodu,musteri_Adi,musteri_cinsiyet,musteri_yas,musteri_Puan,musteri_islem_sayisi=0,musteri_alis=0):
        self.musteri_kodu=musteri_kodu
        self.musteri_Adi=musteri_Adi
        self.musteri_cinsiyet=musteri_cinsiyet
        self.musteri_yas=musteri_yas
        self.musteri_Puan=musteri_Puan
        self.musteri_islem_sayisi=musteri_islem_sayisi
        self.musteri_alis=musteri_alis
import os
import random
class Firma_İslemleri:
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
            veri=[[i.id,i.firmaAdi,i.puan] for i in Firma.firmalar]
            sutunlar=["FirmaKodu","FirmaAdi","puan"]
            self.dfFirma=pd.DataFrame(veri,columns=sutunlar)
class Karegori_islemleri:
    def kod_olustur(self):
        return random.randint(10000,99999)
    def Kategori_kaydet(self):
        strg=[]
        dosya_adi="kategori.csv"
        if Kategori.kategoriler:
            for ktg in Kategori.kategoriler:
                strg.append(f"{ktg.id};{ktg.firmaAdi};{ktg.puan}\n")
            with open(dosya_adi,"w",encoding="utf-8") as fl:
                fl.writelines(strg)
                
    def kategori_ekle(self):
        if not Kategori.kategoriler:self.kategori_oku()
        ktg_kod=self.kod_olustur()
        ktg_adi=input("Firma Adi")
        ktg_rnd=random.randint(1,100)
        kategori=Firma(ktg_kod,ktg_adi,ktg_rnd)
        Kategori.kategoriler.append(kategori)
        self.firma_kaydet()
        
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
        if Kategori.kategoriler:
            for ktg in Kategori.kategoriler:
                print (f"  {ktg.id} -    {ktg.adi}   {ktg.puan}\n")
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
            veri=[[i.id,i.adi,i.puan] for i in Kategori.kategoriler]
            sutunlar=["KtgKodu","KtgAdi","puan"]
            self.dfKategori=pd.DataFrame(veri,columns=sutunlar)
class Urun_islemleri:
    def kod_olustur(self):
        return random.randint(10000,99999)
    def urun_kaydet(self):
        strg=[]
        dosya_adi="urun.csv"
        if Urun.urunler:
            for urn in Urun.urunler:
                strg.append(f"{urn.ktg_id};{urn.urun_id};{urn.Adi};{urn.fiyat};{urn.puan}\n")
            with open(dosya_adi,"w",encoding="utf-8") as fl:
                fl.writelines(strg)
                
    def Urun_ekle(self):
        if not Kategori.kategoriler:self.kategori_oku()
        urun_id=self.kod_olustur()
        ktg_id=input("Kategori Kodu:")
        adi=input("Ürün Adi")
        fiyat=input("Ürün Fiyatı Giriniz")
        urn_rnd=random.randint(1,100)
        urun=Firma(ktg_id,urun_id,adi,fiyat,urn_rnd)
        Urun.urunler.append(urun)
        self.urun_kaydet()
        
    def urun_sil(self,ktg_id,urn_id):
        if not Urun.urunler:self.urun_oku()
        if Urun.urunler:
            for urn in Urun.urunler:
                if ktg_id==urn.ktg_id and urn.urun_id==urn_id:
                    Urun.urunler.remove(urn)
                    self.urun_kaydet()
    def urun_listele(self):
        if not Urun.urunler:self.urun_oku()
        print(f"Kategori kodu Urun Kodu  Urun Adı Fiyatı Ağırlığı")
        if Urun.urunler:
            for urn in Urun.urunler:
                print (f"  {urn.ktg_id}-{urn.urn_id}   {urn.adi}  {urn.fiyat}  {urn.puan}\n")
    
    def urun_oku(self):
        dosya_adi="urun.csv"
        Urun.urunler.clear
        if os.path.exists(dosya_adi):
            with open(dosya_adi,"r",encoding="utf-8") as fl:
                for satır in fl:
                    satır=satır.strip()
                    k_id,u_id,adi,fiyat,puan=satır.split(";")
                    #satis_sayisi,toplam_satis=self.satis_hesapla(int(id))
                    urun=Urun(k_id,u_id,adi,fiyat,puan)
                    Urun.urunler.append(urun)
                    
            veri=[[i.ktg_id,i.urun_id,i.adi,i.fiyat,i.puan] for i in Urun.urunler]
            sutunlar=["KtgKodu","UrunKodu","urunAdi","Fiyat","puan"]
            self.dfUrun=pd.DataFrame(veri,columns=sutunlar)
class listeler:
    
        
    def musteri_oku(self,dosya):
        Musteri.musteriler.clear
        with open(dosya,"r",encoding="utf-8") as fl:
            for satir in fl:
                satir=satir.strip()
                musteri_kodu, musteri_Adi,musteri_cinsiyet,musteri_yas, musteri_Puan  =satir.split(";")
                #mst_islem_sayisi,mst_satis=self.musteri_satis_topla(musteri_kodu)
                musteri=Musteri(musteri_kodu, musteri_Adi,musteri_cinsiyet,musteri_yas, musteri_Puan)
                Musteri.musteriler.append(musteri)
        
        veri=[[i.musteri_kodu,i.musteri_Adi,i.musteri_cinsiyet,i.musteri_yas, i.musteri_Puan] for i in Musteri.musteriler]
        sutunlar=["MusteriKodu","MusteriAdi","Cinsiyet","Yas","puan"]
        self.dfMusteri=pd.DataFrame(veri,columns=sutunlar)
    
    def urun_oku(self, dosya):
        Urun.urunler.clear
        with open(dosya, 'r', encoding="utf-8") as fl:
            for satir in fl:
                satir = satir.strip()
                if satir:
                    kategori_kodu, urun_kodu, urun_adi, urun_fiyat, urun_puan = satir.split(';')
                    urun = Urun(int(kategori_kodu), int(urun_kodu), urun_adi,float(urun_fiyat),float(urun_puan) )
                    Urun.urunler.append(urun)

        veri=[[i.kategori_kodu,i.urun_kodu,i.urun_adi,i.urun_fiyati, i.urun_puan] for i in Urun.urunler]
        sutunlar=["kategori_kodu","urun_kodu","urun_adi","urun_fiyati","urun_puan"]
        self.dfUrun=pd.DataFrame(veri,columns=sutunlar)
    
    def __satis_oku(self,dosya):
        Satis.satislar.clear
        with open(dosya,"r",encoding="utf-8") as fl:
            for satir in fl:
                if satir:
                    satir=satir.strip()
                    musteri_kodu,firma_kodu,kategori_kodu,urun_kodu,urun_adedi,urun_fiyati,satis_tutar,satis_tarihi,satis_saati=satir.split(";")
                    satis=Satis( int(musteri_kodu),int(firma_kodu),int(kategori_kodu),int(urun_kodu),int(urun_adedi),float(urun_fiyati),float(satis_tutar),satis_tarihi,satis_saati)            
                    Satis.satislar.append(satis)
                    
        veri=[[i.musteri_kodu,i.firma_kodu,i.kategori_kodu,i.urun_kodu, i.urun_adedi, i.urun_fiyati, i.satis_tutar, i.satis_tarihi,i.satis_saati] for i in Satis.satislar]
        sutunlar=["musteri_kodu","firma_kodu","kategori_kodu","urun_kodu","urun_adedi","urun_fiyati","satis_tutar","satis_tarihi","satis_saati"]
        self.dfSatis=pd.DataFrame(veri,columns=sutunlar)        
        
        
    def __satis_kontrol(self):
        dosya="satislar.txt"
        if not Satis.satislar: 
            self.__satis_oku(dosya)
            
    def __musteri_kontrol(self):
        if not Musteri.musteriler:
            self.musteri_oku("musteriler.txt")
            
    def __firma_kontrol(self):
        if not Firma.firmalar:
            self.firma_oku("firmalar.txt")
            
    def __urun_kontrol(self):
        if not Urun.urunler:
            self.urun_oku("urunler.txt")

    def __firma_satis_toplam(self,firmaKod):
        
        firma_kodu_df = self.dfSatis[self.dfSatis["firma_kodu"] == firmaKod]
        
        return (firma_kodu_df["satis_tutar"].count() ,firma_kodu_df["satis_tutar"].sum())
    
    """-------------------------------------------------------------------------"""           
    def firma_liste(self):
        self.__firma_kontrol()
        self.__satis_kontrol()
        genelTop=self.dfSatis["satis_tutar"].sum()
        genelSay=self.dfSatis["satis_tutar"].count()
        top_say,top_tutar=0,0
        m1=f"| Firma  |   Firma        |  işlem  | işlem |  Toplam     | Satış  |"
        m2=f"|  Kodu  |     Adı        |  Sayısı | Oranı |   Satış     |  Oranı |"
        print("-"*len(m1))
        print(m1)
        print(m2)
        print("-"*len(m2))
        
        for _,frm in self.dfFirma.iterrows():
            satis_say,satis_toplam=self.__firma_satis_toplam(frm["FirmaKodu"])
            print(f'|   {frm["FirmaKodu"]:<5}| {frm["FirmaAdi"]:<15}| {satis_say:<8}| {round(satis_say/genelSay*100,2):<6}| {"{:,}".format(satis_toplam):<12}| {round(satis_toplam/genelTop*100,2):<7}|')
            print("-"*len(m2))
            
    def firma_grafik_bar(self):
        self.__firma_kontrol()
        self.__satis_kontrol()
        genelTop=self.dfSatis["satis_tutar"].sum()
        genelSay=self.dfSatis["satis_tutar"].count()
        data = []
        for _, frm in self.dfFirma.iterrows():
            satis_say, satis_toplam = self.__firma_satis_toplam(frm["FirmaKodu"])
            satis_orani_say = round(satis_say / genelSay * 100, 2)
            satis_orani_toplam = round(satis_toplam / genelTop * 100, 2)
            data.append([frm["FirmaKodu"], frm["FirmaAdi"], satis_say, satis_orani_say, satis_toplam, satis_orani_toplam])

        df = pd.DataFrame(data, columns=["Firma Kodu", "Firma Adı", "İşlem Sayısı", "İşlem Oranı", "Toplam Satış", "Satış Oranı"])
        
        df = df.sort_values(by="Firma Kodu")

        # Tabloya Oran sütunlarını ekleme
        df["İşlem Oranı"] = df["İşlem Oranı"].map("{:.2f}%".format)
        df["Satış Oranı"] = df["Satış Oranı"].map("{:.2f}%".format)

        # Bar grafik oluşturma
        plt.figure(figsize=(10, 6))
        colors = plt.cm.tab20(np.arange(len(df)))
        plt.bar(df["Firma Adı"], df["Toplam Satış"], color=colors)
        plt.xlabel("Firma")
        plt.ylabel("Toplam Satış")
        plt.title("Firma Bazında Toplam Satış ve Oranları")
        plt.xticks(rotation=45)

        # Oran etiketlerini ekleme
        for i, value in enumerate(df["Toplam Satış"]):
            plt.text(i, value, df["Satış Oranı"][i], ha="center", va="bottom")

        plt.tight_layout()
        plt.show()
    def firma_grafik_pie(self):
    
            self.__firma_kontrol()
            self.__satis_kontrol()
            genelTop = self.dfSatis["satis_tutar"].sum()
            genelSay = self.dfSatis["satis_tutar"].count()
            data = []
            for _, frm in self.dfFirma.iterrows():
                satis_say, satis_toplam = self.__firma_satis_toplam(frm["FirmaKodu"])
                satis_orani_say = round(satis_say / genelSay * 100, 2)
                satis_orani_toplam = round(satis_toplam / genelTop * 100, 2)
                data.append([frm["FirmaKodu"], frm["FirmaAdi"], satis_say, satis_orani_say, satis_toplam, satis_orani_toplam])

            df = pd.DataFrame(data, columns=["Firma Kodu", "Firma Adı", "İşlem Sayısı", "İşlem Oranı", "Toplam Satış", "Satış Oranı"])

            df = df.sort_values(by="Firma Kodu")

            # Pasta grafiği oluşturma
            plt.figure(figsize=(10, 6))
            wedges, texts, autotexts = plt.pie(df["Toplam Satış"], labels=df["Firma Adı"], autopct="%1.1f%%", startangle=90, counterclock=False)

            # Oran etiketlerini ekleme
            for i, text in enumerate(autotexts):
                oran = df.loc[i, "Satış Oranı"]
                text.set_text(f"{text.get_text()}")

            plt.title("Firma Bazında Toplam Satış Dağılımı")
            plt.axis("equal")

            plt.show()

    def urun_listele(self):
        self.__urun_kontrol()
        print(self.dfUrun)
        
    def musteri_listele(self):
        self.__musteri_kontrol()
        print(self.dfMusteri)
    
    def satis_listele(self):
        self.__satis_kontrol()
        print(self.dfSatis)
        
def menu():
    while True:
        print(f"***************MENU******************************")
        cvp=input("1-Firma işlemleri\n2-Kategori İşlemleri\n3-Ürün İşlemleri\n4-Müşteri İşlemleri\n5-Çıkış\nSeçiminizi Yapınız:")
        if cvp=="1":
            firma_menu()
        elif cvp=="2":
            kategori_menu()
        elif cvp=="3":
            urun_menu()
        elif cvp=="4":
            musteri_menu()
        elif cvp=="5":
            break
def firma_menu():
    while True:
        print(f"******************Firma İşlemleri*******************")
        print(f"* 1- Firma Ekle___________________________________1 *")
        print(f"* 2- Firma Sil____________________________________2 *")
        print(f"* 3- Firma Satış Rapor____________________________3 *")
        print(f"* 4- Çıkış________________________________________4 *")
        print(f"*****************************************************")
        cvp=input("Seçiminiz:")
        frm=Firma_İslemleri()
        if cvp=="1":
            frm.firma_ekle()
        elif cvp=="2":
            frm.firma_sil()
        elif cvp=="3":
            frm.firma_listele()
        elif cvp=="4":
            break
def kategori_menu():
    pass
def urun_menu():
    pass
def musteri_menu():
    pass
if __name__=="__main__":
    menu()
    #lst=listeler()
    #lst.firma_grafik_bar()
    #lst.musteri_listele()
    #lst.urun_listele()
    #lst.satis_listele()
