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
    def __init__(self,kategori_kodu,urun_kodu,urun_adi,urun_fiyati,urun_puan,toplam_satis=0):
        self.kategori_kodu=kategori_kodu
        self.urun_kodu=urun_kodu
        self.urun_adi=urun_adi
        self.urun_fiyati=urun_fiyati
        self.urun_puan=urun_puan
        self.toplam_satis=toplam_satis

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

class listeler:
    def firma_oku(self,dosya_adi):
        Firma.firmalar.clear
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
        
lst=listeler()
lst.firma_grafik_bar()
#lst.musteri_listele()
#lst.urun_listele()
#lst.satis_listele()
