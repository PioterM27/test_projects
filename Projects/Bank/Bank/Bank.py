from SerwisPlatnosci import SerwisPlatnosci
from Klient import Klient
import random


class Bank(SerwisPlatnosci):
    '''Główna klasa Bank'''
    _bank_id = 1000
    _bank_klient_id=100

    def __init__(self, nazwa):
        self.nazwa = nazwa
        self.bank_id = Bank._bank_id
        Bank._bank_id += 1001
        self.customer_list = {}

    '''
    Klasa otrzymuje obiekt klienta, klienci albo beda zapisywanie do pliku albo do SQLLite bazy
    
    '''

    def add_klient(self, Klient:Klient):
        _new_Klient = Klient
        _new_Klient.nr_rachunku = self.create_individual_client_number(_new_Klient.customer_id)
        _new_Klient.id_banku_klienta=self._bank_klient_id
        _new_Klient.bank=self
        Bank._bank_klient_id+=1
        self.customer_list[_new_Klient.id_banku_klienta]=_new_Klient.__dict__

    def create_individual_client_number(self, cst_id):
        rnd_nbr=random.randint(100,999)
        _temp_cst_nbr=[str(self.bank_id),str(rnd_nbr),str(cst_id)]
        crt_cst_number = ''.join(_temp_cst_nbr)
        return crt_cst_number

    def __str__(self):
        return self.nazwa
    def dodaj_bank_do_serwisu(self):
        SerwisPlatnosci.available_bank_id[self.bank_id]=self.nazwa
    # def dodaj_bank(self):
    #     SerwisPlatnosci.available_bank_id[self.bank_id] = self.nazwa
