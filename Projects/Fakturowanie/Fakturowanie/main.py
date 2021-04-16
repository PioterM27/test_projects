from Projects.Fakturowanie.Fakturowanie import Klient
from Projects.Fakturowanie.Fakturowanie import Produkt
from Projects.Fakturowanie.Fakturowanie import Fakturowanie
from Projects.Fakturowanie.Fakturowanie import Wykonawca
import datetime

a = Klient.Klient("Jan", "Kowalski", "Kowal", "Sloneczna", 9)
b = Klient.Klient("Piotr", "Nowak", "NowakStal", "Krakowska", 14)
c = Klient.Klient("Piotr", "Nowak", "NowakStal", "Krakowska", 14)
c = Klient.Klient("Piotr", "Nowak", "NowakStal", "Krakowska", 14)
d = Wykonawca.Wykonawca("Piotr", "Nowak", "NowakStal", "Krakowska", 14)

print("Wykonawaca" +d.nip)

print("Nip a " + a.nip)
print("Nip b " + b.nip)
print("Nip c " + c.nip)  # f=Fakturowanie.Fakturowanie(a)
# f2=Fakturowanie.Fakturowanie(b)
# p1=f.add_product()
# p1=f.add_product()
# p2=f2.add_product()
# p2=f2.add_product()
# f.create_invoice()
# f2.create_invoice()
