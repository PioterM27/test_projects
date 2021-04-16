import unittest
from Fakturowanie import *
import datetime


class TestKlient(unittest.TestCase):
    def setUp(self):
        data = {'imie': "Jan",
                'nazwisko': 'Kowalski',
                'nazwa_firmy': 'Kowal',
                'adres': "Sloneczna",
                'dnie_zaplaty': 9}
        self.klient = Klient.Klient(data['imie'],
                                    data['nazwisko'],
                                    data['nazwa_firmy'],
                                    data['adres'],
                                    data['dnie_zaplaty'])

    def test_static_nip_generator_method(self):
        self.assertEquals(len(Klient.Klient.nip_generator()), len(self.klient.nip), 'Długość numeru nip')

    def test_object_class(self):
        self.assertEquals(Klient.Klient, type(self.klient))


class TestProdukt(unittest.TestCase):
    def setUp(self):
        data = {'nazwa': "Czajnik",
                'cena_netto': 1000,
                'vat': 23,
                'kwota_vat': 230,
                'cena_brutto': 1230}
        self.produkt = Produkt.Produkt(data['nazwa'],
                                       data['cena_netto'],
                                       data['vat'])

    def test_oblicz_vat(self):
        result = 230
        self.assertEquals(result, self.produkt.oblicz_vat())

    def test_oblicz_brutto(self):
        result = 1230
        self.assertEquals(result, self.produkt.oblicz_brutto())

    def test_str_value(self):
        result = "Nazwa produktu to: Czajnik, cena netto to : 1000, kwota vat: 230.0, brutto 1230.0"
        self.assertEquals(result, str(self.produkt))


class TestFaktura(unittest.TestCase):
    def setUp(self):
        data = {'klient': Klient.Klient('Jan', 'Kowalski', 'Kowal', 'Sloneczna', 9),
                'product_list': Produkt.Produkt('Czajnik', 1000, 23),
                'date': datetime.date.today(),
                'payment_day': datetime.date.today() + datetime.timedelta(9)}
        self.fakturowanie = Fakturowanie(data['klient'])

    def test_check_created_file(self):
        self.fakturowanie.create_invoice()
        expected_file = 'Jan_Kowalski.txt'
        abs_path = 'D:\Szkolenie Python 2021\siipythonluty2021\kodzik\dla_chętnych\ksiegowosc\Fakturowanie\Fakturowanie_testy'
        file_list = os.listdir(abs_path)
        print(expected_file in file_list)
        self.assertTrue(expected_file in file_list)

    def test_remove_file(self):
        path = 'D:\Szkolenie Python 2021\siipythonluty2021\kodzik\dla_chętnych\ksiegowosc\Fakturowanie\Fakturowanie_testy'
        try:
            with open(path + '\Jan_Kowalski.txt', 'r')as f:
                f.read()
        except:
            print("Plik nie istenije")
        else:
            os.remove(path + '\Jan_Kowalski.txt')

            file_list = os.listdir(path)
            print("Jan_Kowalski.txt" in file_list)
            self.assertFalse("Jan_Kowalski.txt" in file_list)


if __name__ == "__main__":
    unittest.main()
