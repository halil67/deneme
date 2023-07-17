import pandas as pd
import matplotlib.pyplot as plt
import firma
import kategori


        




import os
import random



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
