import pandas as pd
import matplotlib.pyplot as plt
import firma as f
import kategori as k
import musteri as m
import urun as u
import satis as s
import satisRapor as sR
def menu():
    while True:
        print(f"***************MENU******************************")
        print("** 1-Firma işlemleri******************************")
        print("** 2-Kategori İşlemleri***************************")
        print("** 3-Ürün İşlemleri*******************************")
        print("** 3-Ürün İşlemleri*******************************")
        print("** 4-Müşteri İşlemleri****************************")
        print("** 5-Satış İşlemleri******************************")
        print("** 6-Raporlamalar*********************************")
        print("** 7-Çıkış****************************************")
        print("**************************************************")
        
        cvp=input("Seçiminizi Yapınız:")
        if cvp=="1":
            f.Firma_islemleri().firma_menu()
        elif cvp=="2":
            k.Karegori_islemleri().kategori_menu()
        elif cvp=="3":
            u.Urun_islemleri().urun_menu()
        elif cvp=="4":
            m.Musteri_islemleri().musteri_menu()
        elif cvp=="5":
            s.Random_satis().satis_yap()
        elif cvp=="6":
            sR.Satis_Rapor().menu()
        
        elif cvp=="7":
            break

if __name__=="__main__":
    menu()
    
