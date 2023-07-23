import firma as fr
import kategori as kt
import musteri as mst
import urun as urn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import locale
class Satis_Rapor:
    def liste_yukle(self):
        if not fr.Firma.firmalar:fr.Firma_islemleri().firma_oku()
        if not kt.Kategori.kategoriler:kt.Karegori_islemleri().kategori_oku()
        if not urn.Urun.urunler:urn.Urun_islemleri().urun_oku()
        if not mst.Musteri.musteriler:mst.Musteri_islemleri().musteri_oku()
        
    satislar=[]
    def satis_oku(self):
        self.liste_yukle()
        dosya="satis.csv"
        if os.path.exists(dosya):
            with open(dosya,"r",encoding="utf-8") as fl:
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
            print("5- Ürün Bazlı Rapor")
            print("6- Firma Bazlı Rapor")
            print("7- Müşreti Bazlı Rapor")
            print("8- Cinsiyet Rapor")
            print("9- Yaş Bazlı Rapor")
            print("q- Çıkış")
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
                self.satis_say_urun()  
            elif cvp=="6":
                self.firma_say_urun()  
            elif cvp=="7":
                self.musteri_say_urun() 
            elif cvp=="8":
                self.gender_say_urun()
            elif cvp=="9":
                self.old_say_urun()
                
            elif cvp=="q":
                break 

    def satis_detay(self):
        if not self.satislar:self.satis_oku()
        dosya="shopDetail.csv"
        if os.path.exists(dosya):
            veri=[]
            with open(dosya,"r",encoding="utf-8") as fl:
                for satir in fl:
                    satir=satir.strip()
                    if satir:
                        id,k_id,u_id,u_adi,u_fiyat=satir.split(";")
                        f_kodu,firmaAdi,m_kodu,mstAdi,mstCns,mstYasi=next(((s[0],s[1],s[2],s[3],s[4],s[5]) for s in self.satislar if id==s[6]),None)
                        veri.append([id,f_kodu,firmaAdi,m_kodu,mstAdi,mstCns,mstYasi,u_id,u_adi,float(u_fiyat)])
            
            sutunlar=["id","f_kodu","firmaAdi","m_kodu","mstAdi","mstCns","mstYasi","u_id","u_adi","u_fiyat"]
            self.df=pd.DataFrame(veri,columns=sutunlar)
            self.toplam_tutar=self.df["u_fiyat"].sum()
            self.toplam_sayi=self.df["u_fiyat"].count()
            
    def format_currency(self, amount):
        return f'{amount:.2f} ₺'
    def satis_say_urun(self):
        self.satis_detay()
        product_counts = self.df.groupby('u_adi')['u_id'].count().reset_index()
        product_counts["oranC"]=product_counts["u_id"]/self.toplam_sayi*100
        product_price =  self.df.groupby('u_adi')['u_fiyat'].sum().reset_index()
        product_price["oranP"]=product_price["u_fiyat"]/self.toplam_tutar*100
        product_info = pd.merge(product_counts, product_price, on='u_adi', suffixes=('_count', '_price'))
        product_info["oranC"] = product_info["oranC"].round(2)
        product_info["oranP"] = product_info["oranP"].round(2)
        product_info["u_fiyat"] = product_info["u_fiyat"].apply(self.format_currency)
        
        new_column_order = ['u_adi', 'u_id','oranC' ,'u_fiyat', 'oranP']
        product_info = product_info[new_column_order]
        new_column_names = {'u_adi': 'Ürün Adı','u_id': 'Ürün Adedi','oranC': 'Adet Oranı',
                            'u_fiyat': 'Toplam Satış','oranP': 'Satış Oranı'}
        product_info.rename(columns=new_column_names, inplace=True)

        print(product_info)
        
    def firma_say_urun(self):
        self.satis_detay()
        
        firma_counts=self.df.groupby("firmaAdi")["f_kodu"].count().reset_index()
        firma_counts["oranC"]=round(firma_counts["f_kodu"]/self.toplam_sayi*100,2)
        firma_price=self.df.groupby("firmaAdi")["u_fiyat"].sum().reset_index()
        firma_price["oranP"]=round(firma_price["u_fiyat"]/self.toplam_tutar*100,2)
        firma_info=pd.merge(firma_counts,firma_price, on="firmaAdi", suffixes=("_count","_price"))
        firma_info["u_fiyat"] = firma_info["u_fiyat"].apply(self.format_currency)
        names={"firmaAdi":"Firma Adı","f_kodu":"Satıs Adet","oranC":"Adet Oranı%","u_fiyat":"Toplam Satış","oranP":"Satış Oranı"}
        firma_info.rename(columns=names,inplace=True)
        print(firma_info)
        print(f"Toplam Adet:{self.toplam_sayi}")
        print(f"Toplam Satış:{self.toplam_tutar}")
    def musteri_say_urun(self):
        self.satis_detay()
        musteri_count=self.df.groupby("mstAdi")["m_kodu"].count().reset_index()
        musteri_count["oranC"]=round(musteri_count["m_kodu"]/self.toplam_sayi*100,2)
        musteri_price=self.df.groupby("mstAdi")["u_fiyat"].sum().reset_index()
        musteri_price["oranP"]=round(musteri_price["u_fiyat"]/self.toplam_tutar*100,2)
        musteri_info=pd.merge(musteri_count,musteri_price,on="mstAdi",suffixes=("c","p"))
        musteri_info["u_fiyat"]=musteri_info["u_fiyat"].apply(self.format_currency)
        names={"mstAdi":"Müşter Ad Soyad","m_kodu":"Ürün Adet","oranC":"Adet Oranı%","u_fiyat":"Toplam Satınalma","oranP":"Satınalma Oranı"}
        musteri_info.rename(columns=names,inplace=True)
        print(musteri_info)
        print(f"Toplam Adet:{self.toplam_sayi}")
        print(f"Toplam Satış:{self.toplam_tutar}")
        
    def gender_say_urun(self):
        
        self.satis_detay()
        gender_count=self.df.groupby("mstCns")["u_fiyat"].count().reset_index()
        gender_price=self.df.groupby("mstCns")["u_fiyat"].sum().reset_index()
        gender_info=pd.merge(gender_count,gender_price, on="mstCns",suffixes=("_c","_p"))
        print(gender_info)
        plt.figure(figsize=(20, 20))
        plt.subplot(2, 2, 1)  # 1 satırlık, 2 sütunlu grid içinde ilk alt grafik (bar grafiği)
        plt.bar(gender_info['mstCns'], gender_info['u_fiyat_c'])
        plt.xlabel('Ürün Adı')
        plt.ylabel('Ürün Adedi')
        plt.title('Ürün Adedi')
        plt.xticks(rotation=45)

        # Pie Grafiği
        plt.subplot(1, 2, 2)  # 1 satırlık, 2 sütunlu grid içinde ikinci alt grafik (pie grafiği)
        plt.bar(gender_info['mstCns'], gender_info['u_fiyat_p'])
        plt.xlabel('Ürün Adı')
        plt.ylabel('Toplam Satış')
        plt.title('Toplam Satış')
        plt.xticks(rotation=45)

        plt.tight_layout()  # Alt grafikler arasındaki boşlukları düzenlemek için
        plt.show()
        
    def old_say_urun(self):  
        self.satis_detay()
        old_count=self.df.groupby("mstYasi")["u_fiyat"].count().reset_index()
        old_price=self.df.groupby("mstYasi")["u_fiyat"].sum().reset_index()
        old_info=pd.merge(old_count,old_price, on="mstYasi",suffixes=("_c","_p"))
        print(old_info)
        

s=Satis_Rapor()
s.menu()