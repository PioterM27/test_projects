class Produkt:
    def __init__(self,nazwa,cena_netto,vat):
        self.nazwa=nazwa
        self.cena_netto=cena_netto
        self.vat=vat
        self.kwota_vat=self.oblicz_vat()
        self.cena_brutto=self.oblicz_brutto()
    def oblicz_vat(self):
        return self.cena_netto*(self.vat/100)
    def oblicz_brutto(self):
        return self.cena_netto+self.kwota_vat
    def __str__(self):
        return f"Nazwa produktu to: {self.nazwa}, cena netto to : {self.cena_netto}, kwota vat: {self.kwota_vat}, brutto{self.cena_brutto}"
