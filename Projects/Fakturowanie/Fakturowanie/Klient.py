# Klient powinien zawierac nazwe firmy, NIP i adres oraz liczbe dni do zaplaty faktury.
# Jak w init odpalalem program tworzyle sie dwa razy konstruktor
import random


class Klient:
    klient_id = 0

    def __init__(self, imie, nazwisko, nazwa_firmy, adres, dni_zaplaty):
        print("Jestem konstruktorem klienta")
        self.imie = imie
        self.nazwisko = nazwisko
        self.nazwa_firmy = nazwa_firmy
        self.adres = adres
        self.dni_zaplaty = dni_zaplaty
        self.klient_id = Klient.klient_id
        self.nip = self._nip_generator()
        Klient.klient_id+=1

    def _nip_generator(self):
        random_value = random.randint(111111, 999999)
        _nipValue = (str(random_value)+str(self.klient_id))
        print(_nipValue)
        return _nipValue
