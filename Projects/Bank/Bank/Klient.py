import json
import datetime

class Klient:
    klient_id = 0

    def __init__(self, name, lastname,birthDate):
        self.name = name
        self.lastname = lastname
        self.customer_id=Klient.klient_id
        # self.birthDate=datetime.date.(birthDate) zrobic odpowiednie formatowanie
        self.nr_rachunku=None
        self.id_banku_klienta=None
        self.saldo = 0
        self.bank=None
        Klient.klient_id += 1
    @property
    def saldo(self):
        return self._saldo
    @saldo.setter
    def saldo(self,ile):
        self._saldo=ile

    def __str__(self):
        return self.name
    def wplac(self,ile):
       exist = True if self.id_banku_klienta in self.bank.customer_list.keys() else False
       if exist:
           self.saldo+=ile
       return self.saldo
    def wyplac(self,ile):
        exist = True if self.id_banku_klienta in self.bank.customer_list.keys() else False
        if exist:
            try:
                if ile > self.saldo:
                 raise ValueError("Niewystarczająca ilość pieniędzy na koncie")
            except ValueError as e:
                print(e)
            else:
                self.saldo-=ile
        return self.saldo







        # if self.bank.






