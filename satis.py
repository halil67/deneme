import os
import random
import firma
import kategori
import urun

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
        
class Satis_islemleri:
    pass