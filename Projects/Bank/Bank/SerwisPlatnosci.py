from abc import ABC,abstractclassmethod
from Bank import Bank
from Klient import Klient
from Przelew import Przelew

class SerwisPlatnosci(ABC):
    available_bank_id={}
    @classmethod
    def przelew(cls,od:Klient,do_number,value):
        new_przelew=Przelew()
        new_przelew.from_customer_id=od.id_banku_klienta
        new_przelew.from_customer_individual_number=od.nr_rachunku
        new_przelew.from_customer_bank=od.bank
        new_przelew.from_customer_value_to_send=value
        new_przelew.to_customer_individual_number=do_number
        new_przelew.to_customer_value_to_send=value


    def zlecenie_do_banku(self):
        return True or False
    def sprawdz_poprawnosc_klienta_od(self):
        pass
    def sprawdz_poprawnosc_klienta_do(self):
        pass
    def sprawdz_poprawnosc_banku_od(self):
        pass
    def sprawdz_poprawnosc_banku_do(self):
        pass
    def czy_klient_od_moze_wyslac_pieniadze(self):

        pass

    # @classmethod
    # def dodaj_bank(cls):
    #     pass

