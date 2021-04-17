import tkinter as tk
from tkinter import ttk, Canvas
from tkinter import *

import program.Classes.Dane.DaneEntalpia as d1
import program.Classes.Dane.DaneEntalpia2 as d2
import program.Classes.Dane.DaneStrumienieMasy as st
import program.Classes.Funkcje.FunkcjeIteracje as it
import program.Classes.Funkcje.FunkcjeIteracjeNN as ff
import program.Classes.Funkcje.Funkcje as funk
import program.Classes.Dane.DaneWejsciowe as dt

# _qwododg = DoubleVar()
# _ppp = DoubleVar()
# _pzp = DoubleVar()
# _delpz = DoubleVar()
# _delipz = DoubleVar()

class DaneObliczenia:

    def __init__(self,tab):
        self.tab=tab
        print("stworzono mnie")



    def listOfElements1(self):
        self.listOfElements = {
            'mpalStr': {
                "ramka": 'ramka0',
                "zmiennaPola": st._mpal,
                "opis": 'Strumien masy paliwa [kg/s]',
                "row": 1,
                "columne": 2,
                "flag": 1
            },
            'wysPrez': {
                "ramka": 'ramka0',
                "zmiennaPola":dt._nwp ,
                "opis": 'Sprawność wysokoprężnej części',
                "row": 2,
                "columne": 2,
                "flag": 1
            },
            'etalpIwz': {
                "ramka": 'ramka0',
                "zmiennaPola": dt._nsp,
                "opis": 'Sprawność średnioprężnej części',
                "row": 3,
                "columne": 2,
                "flag": 1
            },
            'strMps': {
                "ramka": 'ramka0',
                "zmiennaPola": dt._nnp,
                "opis": 'Sprawność niskoprężnej części',
                "row": 4,
                "columne": 2,
                "flag": 1
            },
            'strMsp': {
                "ramka": 'ramka0',
                "zmiennaPola": d2._isp,
                "opis": 'Entalpia pary wtórnie przegrzanej[J/kg]',
                "row": 5,
                "columne": 2,
                "flag": 1
            },
            'strMnp': {
                "ramka": 'ramka0',
                "zmiennaPola": d2._inp,
                "opis": 'Entalpia pary na wlocie z niskoprężnej części turbiny[J/kg]',
                "row": 6,
                "columne": 2,
                "flag": 1
            },
            'strMznp': {
                "ramka": 'ramka0',
                "zmiennaPola": d2._iznp,
                "opis": 'Entalpia pary na wylocie z niskoprężnej części turbiny[J/kg]',
                "row": 7,
                "columne": 2,
                "flag": 1
            },
            'entIskzm': {
                "ramka": 'ramka0',
                "zmiennaPola": funk._qwp,
                "opis": 'Ciepło wysokoprężnej części turbinyy[W] ',
                "row": 8,
                "columne": 2,
                "flag": 2
            },
            'entIskxn2': {
                "ramka": 'ramka0',
                "zmiennaPola": funk._qsp,
                "opis": 'Ciepło średnioprężnej części turbiny[W] ',
                "row": 9,
                "columne": 2,
                "flag": 2
            },
            'qnpTurb': {
                "ramka": 'ramka0',
                "zmiennaPola": funk._qnp,
                "opis": 'Ciepło niskoprężnej części turbiny [W] ',
                "row": 10,
                "columne": 2,
                "flag": 2
            },
            'entIskxn3': {
                "ramka": 'ramka0',
                "zmiennaPola": funk._qsum,
                "opis": 'Ciepło suma[W] ',
                "row": 11,
                "columne": 2,
                "flag": 2
            },
            'roOdhaz': {
                "ramka": 'ramka1',
                "zmiennaPola": it._qwododg,
                "opis": 'Gestosc wody w odgazowywaczu [kg/m^3]  ',
                "row": 1,
                "columne": 2,
                "flag": 1
            },
            'cisnieniePpp': {
                "ramka": 'ramka1',
                "zmiennaPola": it._ppp,
                "opis": 'Cisnienie przed pompa wod. zas kocioł [Pa] ',
                "row": 2,
                "columne": 2,
                "flag": 1
            },
            'cisieniePzp': {
                "ramka": 'ramka1',
                "zmiennaPola": it._pzp,
                "opis": 'Ciśnienie za pompą wody zasilającej kocioł [Pa] ',
                "row": 3,
                "columne": 2,
                "flag": 1
            },
            'delPzp': {
                "ramka": 'ramka1',
                "zmiennaPola": it._delpz,
                "opis": 'Różnica ciśnień w pompie wody zasilającej [in/out][Pa] ',
                "row": 4,
                "columne": 2,
                "flag": 2
            },
            'delIpzp': {
                "ramka": 'ramka1',
                "zmiennaPola": it._delipz,
                "opis": 'Entalpia wody zasilającej za pompą wody zasilającej podczas napełniania [J/kg] ',
                "row": 5,
                "columne": 2,
                "flag": 2
            },
            'ilIter': {
                "ramka": 'ramka1',
                "zmiennaPola": it._ilosc,
                "opis": 'Ilość iteracji ',
                "row": 8,
                "columne": 2,
                "flag": 1
            },
            'wartosc': {
                "ramka": 'ramka1',
                "zmiennaPola": it._expectValue,
                "opis": 'Oczekiwana wartość ',
                "row": 9,
                "columne": 2,
                "flag": 1
            },

        }
        return self.listOfElements

    def listaRamek1(self):
        self.listaRamek = {
            'ramka0': {
                # "tab": ,
                "opis": "Obliczenie strumienia masy paliwa:",
                "row": 1,
                "columne": 0
            },
            'ramka1': {
                # "tab": ,
                "opis": "Parametry wody zasilającej  :",
                "row": 1,
                "columne": 1
            },


        }
        return self.listaRamek