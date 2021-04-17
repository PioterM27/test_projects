import tkinter as tk
from tkinter import ttk, Canvas
from tkinter import *

import program.Classes.Dane.DaneEntalpia as d1
import program.Classes.Dane.DaneEntalpia2 as d2
import program.Classes.Dane.DaneStrumienieMasy as st
import program.Classes.Funkcje.FunkcjeIteracje as it
import program.Classes.Funkcje.FunkcjeIteracjeNN as ff


class DaneIteracje:

    def __init__(self):
        # self.n = n
        print("stworzono mnie")

    tabIwz = []
    tabMps = []
    tabMI = []
    tabMII = []
    tabMIII = []
    tabMIV = []
    tabMV = []
    tabMVI = []
    tabMVII = []
    tabMwt = []
    tabMsp = []
    tabMnp = []
    tabMznp = []
    tabIskzm = []
    tabIskXN2 = []
    tabIskXN3 = []
    tabIskXN3A = []
    tabIskXN4 = []
    tabIskXN5 = []
    tabIwodODG = []
    tabIpz = []
    tabIskXW1 = []
    tabMwz = []
    tabIskXW2 = []
    tabIskXW3 = []

    def testFunk(self, nr, nawze):
        nazwa = (nawze) + str(nr)
        # print(nazwa)
        nazwa = DoubleVar()
        #i = DoubleVar()
        # print(nazwa.get())
        return nazwa

    # def tabliceZmiennych(self, n, nazwa):
    #     tabIwz = []
    #     tabMps = []
    #     tabMI = []
    #     tabMII = []
    #     tabMIII = []
    #     tabMIV = []
    #     tabMV = []
    #     tabMVI = []
    #     tabMVII = []
    #     tabMwt = []
    #     tabMsp = []
    #     tabMnp = []
    #     tabMznp = []
    #     tabIskzm = []
    #     tabIskXN2 = []
    #     tabIskXN3 = []
    #     tabIskXN3A = []
    #     tabIskXN4 = []
    #     tabIskXN5 = []
    #     tabIwodODG = []
    #     tabIpz = []
    #     tabIskXW1 = []
    #     tabMwz = []
    #     tabIskXW2 = []
    #     tabIskXW3 = []

    def dodajDoTablicy(self, n, nazwa):
        zmiennaObiektu = self.testFunk(n, str(nazwa))
        nazwa.append(zmiennaObiektu)



        return nazwa[n]

    def listOfElements1(self,n):
        self.listOfElements = {
            # 'ilIter': {
            #     "ramka": 'ramka0',
            #     "zmiennaPola": it._ilosc,
            #     "opis": 'Ilość iteracji ',
            #     "row": 1,
            #     "columne": 2,
            #     "flag": 1
            # },
            # 'wartosc': {
            #     "ramka": 'ramka0',
            #     "zmiennaPola": "",
            #     "opis": 'Oczekiwana wartość ',
            #     "row": 2,
            #     "columne": 2,
            #     "flag": 1
            # },
            'etalpIwz': {
                "ramka": 'ramka1',
                "zmiennaPola": self.dodajDoTablicy(n, self.tabIwz),
                "opis": 'Entalpia iwz [J/kg] ',
                "row": 4,
                "columne": 2,
                "flag": 2
            },
            'strMps': {
                "ramka": 'ramka2',
                "zmiennaPola": self.dodajDoTablicy(n, self.tabMps),
                "opis": 'Strumień mps [kg/s] ',
                "row": 20,
                "columne": 2,
                "flag": 1
            },
            'strMsp': {
                "ramka": 'ramka3',
                "zmiennaPola": self.dodajDoTablicy(n, self.tabMsp),
                "opis": 'Strumień msp [kg/s] ',
                "row": 22,
                "columne": 2,
                "flag": 1
            },
            'strMnp': {
                "ramka": 'ramka4',
                "zmiennaPola": self.dodajDoTablicy(n, self.tabMnp),
                "opis": 'Strumien Mnp [kg/s] ',
                "row": 24,
                "columne": 2,
                "flag": 1
            },
            'strMznp': {
                "ramka": 'ramka5',
                "zmiennaPola": self.dodajDoTablicy(n, self.tabMznp),
                "opis": 'Strumien Mznp [kg/s] ',
                "row": 26,
                "columne": 2,
                "flag": 1
            },
            'entIskzm': {
                "ramka": 'ramka6',
                "zmiennaPola": self.dodajDoTablicy(n, self.tabIskzm),
                "opis": 'Entalpia Iskzm [J/kg]',
                "row": 28,
                "columne": 2,
                "flag": 1
            },
            'entIskxn2': {
                "ramka": 'ramka7',
                "zmiennaPola": self.dodajDoTablicy(n, self.tabIskXN2),
                "opis": 'Entalpia Iskxn2 [J/kg]',
                "row": 6,
                "columne": 2,
                "flag": 1
            },
            'entIskxn3': {
                "ramka": 'ramka8',
                "zmiennaPola": self.dodajDoTablicy(n, self.tabIskXN3),
                "opis": 'Entalpia Iskxn3 [J/kg]',
                "row": 8,
                "columne": 2,
                "flag": 1
            },
            'entIskxn3a': {
                "ramka": 'ramka9',
                "zmiennaPola": self.dodajDoTablicy(n, self.tabIskXN3A),
                "opis": 'Entalipa IskXN3A [J/kg]',
                "row": 10,
                "columne": 2,
                "flag": 1
            },
            'entIskxn4': {
                "ramka": 'ramka10',
                "zmiennaPola": self.dodajDoTablicy(n, self.tabIskXN4),
                "opis": 'Entalpia IskXn4 [J/kg]',
                "row": 12,
                "columne": 2,
                "flag": 1
            },
            'entIskxn5': {
                "ramka": 'ramka11',
                "zmiennaPola": self.dodajDoTablicy(n, self.tabIskXN5),
                "opis": 'Entalpia Iskxn5 [J/kg]',
                "row": 14,
                "columne": 2,
                "flag": 1
            },
            'entOdgaz': {
                "ramka": 'ramka12',
                "zmiennaPola": self.dodajDoTablicy(n, self.tabIwodODG),
                "opis": 'Entalpia IwodOdg [J/kg]',
                "row": 16,
                "columne": 2,
                "flag": 1
            },
            # 'roOdhaz': {
            #     "ramka": 'ramka9',
            #     "zmiennaPola": it._qwododg,
            #     "opis": 'Gestosc wododg ',
            #     "row": 4,
            #     "columne": 3,
            #     "flag": 1
            # },
            # 'cisnieniePpp': {
            #     "ramka": 'ramka9',
            #     "zmiennaPola": it._ppp,
            #     "opis": 'Cisnienie przed pompa wod. zas kocio ',
            #     "row": 6,
            #     "columne": 3,
            #     "flag": 1
            # },
            # 'cisieniePzp': {
            #     "ramka": 'ramka9',
            #     "zmiennaPola": it._pzp,
            #     "opis": 'Ciśnienie za pompą wody zasilającej kocioł ',
            #     "row": 8,
            #     "columne": 3,
            #     "flag": 1
            # },
            # 'delPzp': {
            #     "ramka": 'ramka9',
            #     "zmiennaPola": it._delpz,
            #     "opis": 'delta pz ',
            #     "row": 10,
            #     "columne": 3,
            #     "flag": 1
            # },
            # 'delIpzp': {
            #     "ramka": 'ramka9',
            #     "zmiennaPola": it._delipz,
            #     "opis": 'delta ipz ',
            #     "row": 12,
            #     "columne": 3,
            #     "flag": 1
            # },
            'entpIpz': {
                "ramka": 'ramka13',
                "zmiennaPola": self.dodajDoTablicy(n, self.tabIpz),
                "opis": 'Entalpia Ipz [J/kg]',
                "row": 14,
                "columne": 3,
                "flag": 1
            },
            'entIskxw1': {
                "ramka": 'ramka14',
                "zmiennaPola": self.dodajDoTablicy(n, self.tabIskXW1),
                "opis": 'Entalpia Iskxw1 [J/kg]',
                "row": 16,
                "columne": 3,
                "flag": 1
            },
            'strMwz': {
                "ramka": 'ramka15',
                "zmiennaPola": self.dodajDoTablicy(n, self.tabMwz),
                "opis": 'Strumień masy pary wz, [kg/s] ',
                "row": 18,
                "columne": 3,
                "flag": 1
            },
            'entIskXW2': {
                "ramka": 'ramka16',
                "zmiennaPola": self.dodajDoTablicy(n, self.tabIskXW2),
                "opis": 'entalpia Iskxw2 [J/kg]',
                "row": 4,
                "columne": 4,
                "flag": 1
            },
            'entIskXw3': {
                "ramka": 'ramka17',
                "zmiennaPola": self.dodajDoTablicy(n, self.tabIskXW3),
                "opis": 'Entalpia IskXW3 [J/kg]',
                "row": 6,
                "columne": 4,
                "flag": 1
            },
            'masaMI': {
                "ramka": 'ramka18',
                "zmiennaPola": self.dodajDoTablicy(n, self.tabMI),
                "opis": 'Masa MI [kg/s]',
                "row": 8,
                "columne": 4,
                "flag": 1
            },
            'masaMII': {
                "ramka": 'ramka19',
                "zmiennaPola": self.dodajDoTablicy(n, self.tabMII),
                "opis": 'Masa MII [kg/s]',
                "row": 6,
                "columne": 4,
                "flag": 1
            },
            'masaMIII': {
                "ramka": 'ramka20',
                "zmiennaPola": self.dodajDoTablicy(n, self.tabMIII),
                "opis": 'Masa MIII [kg/s]',
                "row": 8,
                "columne": 4,
                "flag": 1
            },
            'masaMIV': {
                "ramka": 'ramka21',
                "zmiennaPola": self.dodajDoTablicy(n, self.tabMIV),
                "opis": 'Masa MIV [kg/s]',
                "row": 10,
                "columne": 4,
                "flag": 1
            },
            'masaMV': {
                "ramka": 'ramka22',
                "zmiennaPola": self.dodajDoTablicy(n, self.tabMV),
                "opis": 'Masa MV [kg/s]',
                "row": 12,
                "columne": 4,
                "flag": 1
            },
            'masaMVI': {
                "ramka": 'ramka23',
                "zmiennaPola": self.dodajDoTablicy(n, self.tabMVI),
                "opis": 'Masa MVI [kg/s]',
                "row": 14,
                "columne": 4,
                "flag": 1
            },
            'masaMVII': {
                "ramka": 'ramka24',
                "zmiennaPola": self.dodajDoTablicy(n, self.tabMVII),
                "opis": 'Masa MVII [kg/s]',
                "row": 16,
                "columne": 4,
                "flag": 1
            },
            'Mwt': {
                "ramka": 'ramka25',
                "zmiennaPola": self.dodajDoTablicy(n, self.tabMwt),
                "opis": 'Mwt [kg/s]',
                "row": 18,
                "columne": 4,
                "flag": 1
            },


        }
        return self.listOfElements

    def listaRamek1(self):
        self.listaRamek = {
            # 'ramka0': {
            #     # "tab": ,
            #     "opis": "Warunki początkowe:",
            #     "row": 1,
            #     "columne": 0
            # },
            'ramka1': {
                # "tab": ,
                "opis": "Para świeża:",
                "row": 1,
                "columne": 0
            },
            'ramka2': {
                # "tab": ,
                "opis": "Para świeża :",
                "row": 2,
                "columne": 0
            },
            'ramka3': {
                # "tab": ,
                "opis": "Para świeża:",
                "row": 3,
                "columne": 0
            },
            'ramka4': {
                # "tab": ,
                "opis": "Para świeża:",
                "row": 4,
                "columne": 0
            },
            'ramka5': {
                # "tab": ,
                "opis": "Para świeża:",
                "row": 5,
                "columne": 0
            },
            'ramka6': {
                # "tab": ,
                "opis": "Mieszanie za kondensatorem",
                "row": 6,
                "columne": 0
            },
            'ramka7': {
                # "tab": ,
                "opis": "XN1/XN2",
                "row": 1,
                "columne": 1
            },
            'ramka8': {
                # "tab": ,
                "opis": "XN3",
                "row": 2,
                "columne": 1
            },
            'ramka9': {
                # "tab": ,
                "opis": "XN3 za punktem mieszania",
                "row": 3,
                "columne": 1
            },
            'ramka10': {
                # "tab": ,
                "opis": "XN4",
                "row": 4,
                "columne": 1
            },
            'ramka11': {
                # "tab": ,
                "opis": "XN5",
                "row": 5,
                "columne": 1
            },
            'ramka12': {
                # "tab": ,
                "opis": "Odgazowywacz",
                "row":6,
                "columne": 1
            },
            'ramka13': {
                # "tab": ,
                "opis": "XW1",
                "row": 1,
                "columne": 2
            },
            'ramka14': {
                # "tab": ,
                "opis": "XW1",
                "row": 2,
                "columne": 2
            },
            'ramka15': {
                # "tab": ,
                "opis": "XW1",
                "row": 3,
                "columne": 2
            },
            'ramka16': {
                # "tab": ,
                "opis": "XW2",
                "row": 4,
                "columne": 2
            },
            'ramka17': {
                # "tab": ,
                "opis": "XW3",
                "row": 5,
                "columne": 2
            },
            'ramka18': {
                # "tab": ,
                "opis": "Strumienie masy",
                "row": 6,
                "columne": 2
            },
            'ramka19': {
                # "tab": ,
                "opis": "Strumienie masy",
                "row": 1,
                "columne": 3
            },
            'ramka20': {
                # "tab": ,
                "opis": "Strumienie masy",
                "row": 2,
                "columne": 3
            },
            'ramka21': {
                # "tab": ,
                "opis": "Strumienie masy",
                "row": 3,
                "columne": 3
            },
            'ramka22': {
                # "tab": ,
                "opis": "Strumienie masy",
                "row": 4,
                "columne": 3
            },
            'ramka23': {
                # "tab": ,
                "opis": "Strumienie masy",
                "row": 5,
                "columne": 3
            },
            'ramka24': {
                # "tab": ,
                "opis": "Strumienie masy",
                "row": 6,
                "columne": 3
            },
            'ramka25': {
                # "tab": ,
                "opis": "Mwt",
                "row": 7,
                "columne": 0
            },

        }
        return self.listaRamek
