from Klient import Klient
from Bank import Bank
from SerwisPlatnosci import SerwisPlatnosci

# a=Bank('mbank')
# b=Bank('PEKAO')
# # print(a.nazwa)
# print(a.bank_id)
# print(b.bank_id)
# a=Klient("Jan","Nowak")
# a.wyslij_przelew()
a=Bank('mbank')
b=Bank('PEKAO')
a.dodaj_bank_do_serwisu()
b.dodaj_bank_do_serwisu()
k1=Klient("Jan","Kowalski",'27-04-2000')
a.add_klient(k1)
# a.add_klient("Marian","Nowak",'31-03-1980')
print(a.customer_list[k1.id_banku_klienta]['name'])
# k1.saldo=120
print(k1.bank)
print(k1.wplac(10000))
k1.wplac(250)
print(k1.saldo)
print(k1.wyplac(800))
print(SerwisPlatnosci.available_bank_id)