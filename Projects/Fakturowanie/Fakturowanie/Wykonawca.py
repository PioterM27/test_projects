from Projects.Fakturowanie.Fakturowanie import Klient


class Wykonawca(Klient.Klient):
    def __init__(self,imie, nazwisko, nazwa_firmy, adres, dni_zaplaty):
        super().__init__(imie, nazwisko, nazwa_firmy, adres, dni_zaplaty)
