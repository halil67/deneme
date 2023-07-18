import firma as fr
import kategori as kt
import musteri as mst
import urun as urn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class Satis_Rapor:
    def liste_yukle(self):
        if not fr.Firma.firmalar:fr.Firma_islemleri().firma_oku()
        if not kt.Kategori.kategoriler:kt.Karegori_islemleri().kategori_oku()
        if not urn.Urun.urunler:urn.Urun_islemleri().urun_oku()
        if not mst.Musteri.musteriler:mst.Musteri_islemleri().musteri_oku()
        
    satislar=[]
    def satis_oku(self):
        self.liste_yukle()
        with open("satis.csv","r",encoding="utf-8") as fl:
            for satir in fl:
                satir=satir.strip()
                if satir:
                    r_firma_id,r_musteri_id,cart_id,urn_say,top_fiyat,tarih=satir.split(";")
                    firmaAdi = next((frm.firmaAdi for frm in fr.Firma.firmalar if int(frm.id) == int(r_firma_id)), None)
                    mstAdi,mstCns,mstYasi=next(((ms.musteri_adi+ " "+ ms.musteri_soyadi,ms.musteri_cinsiyet,ms.musteri_yas) for ms in mst.Musteri.musteriler if ms.musteri_kodu == r_musteri_id), None)
                    self.satislar.append([int(r_firma_id), firmaAdi,int(r_musteri_id), mstAdi, mstCns, mstYasi, cart_id, int(urn_say), float(top_fiyat), tarih])
            sutunlar = ["firma_kodu", "FirmaAdi", "MusteriKodu", "MusteriAdiSoyadi", "MusteriCns", "MusretiYas", "Satis_id", "UrunAdet", "tutar", "tarih"]
            self.dfSatis = pd.DataFrame(self.satislar, columns=sutunlar)
    
        
    def firma_satis_toplam(self,firma_id):
        firma_kodu_df = self.dfSatis[self.dfSatis["firma_kodu"] == int(firma_id)]
        return (firma_kodu_df["UrunAdet"].sum() ,firma_kodu_df["tutar"].sum())
    
    def firma_listesi(self):
        if  not self.satislar:self.satis_oku()
        print(f"Firma Kodu | Firma Adi  | TopAdet | TopSatis |")
        print("***********************************************")
        for e,frm in enumerate(fr.Firma.firmalar):
            urunsay,topsatis=self.firma_satis_toplam(frm.id)
            strg=f"{e+1} | {frm.id} | {frm.firmaAdi} | {'{:,}'.format(urunsay) } | {'{:,}'.format(topsatis):<10} |" 
            print( strg+"\n"+f"{'*'*len(strg)}")
    
    def musteri_listesi(self):
        if  not self.satislar:self.satis_oku()
        print(f"Musteri Kodu  |  Adi Soyadi        |Cns|Yaş |T.Adet | TopSatis    |")
        print("*******************************************************************")
        for e,ms in enumerate(mst.Musteri.musteriler):
            urunsay,topsatis=self.musteri_satis_toplam(ms.musteri_kodu)
            strg=f"{e+1} | {ms.musteri_kodu}     | {ms.musteri_adi +' '+ ms.musteri_soyadi:<18} | {ms.musteri_cinsiyet} | {ms.musteri_yas} | {'{:,}'.format(urunsay):<5} | {'{:,}'.format(topsatis):<11} |" 
            print( strg+"\n"+f"{'*'*len(strg)}")
            
    def musteri_satis_toplam(self,m_id):
        musteri_kodu_df = self.dfSatis[self.dfSatis["MusteriKodu"] == int(m_id)]
        return (musteri_kodu_df["UrunAdet"].sum(), musteri_kodu_df["tutar"].sum())
    
    def firma_grafik_pie(self):
        self.satis_oku()
        genelTop = self.dfSatis["tutar"].sum()
        genelSay = self.dfSatis["tutar"].count()
        data = []
        for _, frm in enumerate(fr.Firma.firmalar):
            satis_say, satis_toplam = self.firma_satis_toplam(frm.id)
            satis_orani_say = round(satis_say / genelSay * 100, 2)
            satis_orani_toplam = round(satis_toplam / genelTop * 100, 2)
            data.append([frm.id, frm.firmaAdi, satis_say, satis_orani_say, satis_toplam, satis_orani_toplam])

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
    def firma_grafik_bar(self):
        self.satis_oku()
        genelTop=self.dfSatis["tutar"].sum()
        genelSay=self.dfSatis["UrunAdet"].sum()
        data = []
        for _, frm in enumerate(fr.Firma.firmalar):
            satis_say, satis_toplam = self.firma_satis_toplam(frm.id)
            satis_orani_say = round(satis_say / genelSay * 100, 2)
            satis_orani_toplam = round(satis_toplam / genelTop * 100, 2)
            data.append([frm.id, frm.firmaAdi, satis_say, satis_orani_say, satis_toplam, satis_orani_toplam])

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
    def menu(self):
        while True:
            print("********************************")
            print("1- Firma Satış Rapor")
            print("2- Firma Satış Rapor Bar Grafiği")
            print("3- Firma Satış Rapor Pasta Grafiği")
            print("4- Müşreti satış Rapor")
            print("5- Çıkış")
            cvp=input("Seçiminizi Yapınız:")
            if cvp=="1":
                self.firma_listesi()
            elif cvp=="2":
                self.firma_grafik_bar()
            elif cvp=="3":
                self.firma_grafik_pie()
            elif cvp=="4":
                self.musteri_listesi()
            elif cvp=="5":
                break 
