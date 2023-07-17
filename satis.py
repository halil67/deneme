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
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, product):
        self.items.append(product)

    def remove_item(self, product):
        self.items.remove(product)

    def get_total_price(self):
        total_price = 0.0
        for item in self.items:
            total_price += item["fiyat"]
        return total_price

    def print_items(self):
        for item in self.items:
            print(item["adi"], "-", item["fiyat"])
urunler=[]
def urun_oku():
    with open("urun.csv","r",encoding="utf-8") as fl:
        for satir in fl:
            satir=satir.strip()
            if satir:
                k_id,u_id,adi,fiyat,puan=satir.split(";")
                urunler.append({"k_id":k_id,"u_id":u_id,"adi":adi,"fiyat":float(fiyat),"puan":puan})

# Alışveriş sepeti oluşturma
cart = ShoppingCart()
urun_oku()
# Ürünleri listeleyin
print("Ürünler:")
for index, urun in enumerate(urunler):
    print(f"{index+1}. {urun['adi']} - {urun['fiyat']}")

# Kullanıcıdan ürün seçmesini isteyin
while True:
    choice = input("Eklemek istediğiniz ürünün numarasını girin (Çıkmak için 'q' tuşuna basın): ")
    if choice == "q":
        break
    elif not choice.isdigit() or int(choice) <= 0 or int(choice) > len(urunler):
        print("Geçersiz seçim. Tekrar deneyin.")
        continue

    selected_product = urunler[int(choice) - 1]
    cart.add_item(selected_product)
    print(f"{selected_product['adi']} sepete eklendi.")

# Sepetin içeriğini ve toplam fiyatı yazdırın
print("\nSepetin İçeriği:")
cart.print_items()
print("Toplam Fiyat:", cart.get_total_price())

class Satis_islemleri:
    pass