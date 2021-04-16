from Projects.Fakturowanie.Fakturowanie import Klient
from Projects.Fakturowanie.Fakturowanie import Produkt
import datetime
import os



class Fakturowanie:
    def __init__(self,klient:Klient):
        self.klient=klient
        self.product_list=[]
        self.date=datetime.date.today()
        self.payment_day=self.when_pay()
    def add_product(self):
        product_name=input("Nazwa produktu")
        product_price=float(input("Cena produktu netto"))
        product_vat=int(input("Stawka VAT"))
        new_product=Produkt.Produkt(product_name,product_price,product_vat)
        self.product_list.append(new_product)
        return self.product_list
    def when_pay(self):
        current_day=self.date
        return current_day+datetime.timedelta(self.klient.dni_zaplaty)
    def create_invoice(self):
        file_name=str(self.klient.imie)+"_"+self.klient.nazwisko+".txt"
        with open(file_name,'x',encoding='utf-8') as f:
            f.write(f"Data wystawienia: {self.date} \n")
            f.write(f"Płatnośc do: {self.payment_day}\n")
            f.write("Dane klienta:\n")
            f.write(f"{self.klient.imie} {self.klient.nazwisko}\n")
            f.write(f"Adres {self.klient.adres}\n")
            f.write(f"Nazwa firmy: {self.klient.nazwa_firmy}\n")
            f.write(f"NIP: {self.klient.nip}\n\n")
            f.write("\n")
            for item,value in enumerate(self.product_list):
                f.write(f"{item}: {value.nazwa} {value.cena_netto} {value.vat} {value.cena_brutto}\n")





# self.nazwa=nazwa
#         self.cena_netto=cena_netto
#         self.vat=vat
#         self.kwota_vat=self.oblicz_vat()
#         self.cena_brutto=self.oblicz_brutto()

