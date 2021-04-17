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
import program.Classes.Dane.DaneIteracje as itD


class DaneObliczeniaPoIteracji:

    def __init__(self, tab,obj):
        self.tab = tab
        self.obj=obj

    _qwp2 = DoubleVar()  # Ciepło wysokoprężnej
    _qsp2 = DoubleVar()  # Ciepło średnioprężnej
    _qnp2 = DoubleVar()  # Ciepło niskoprężnej
    _qT = DoubleVar()
    _qnom=DoubleVar()
    _q=DoubleVar()
    _mwz=DoubleVar()
    _qProc = DoubleVar()
    _spadekMocy = DoubleVar()
    _mzas = DoubleVar()
    _mps = DoubleVar()
    _iwodODG=DoubleVar()

    def listOfElements1(self):
        self.listOfElements = {

            'wartosc': {
                "ramka": 'ramka0',
                "zmiennaPola": dt._nwp,
                "opis": 'Sprawność wysokoprężnej części ',
                "row": 2,
                "columne": 1,
                "flag": 1
            },
            'etalpIwz': {
                "ramka": 'ramka0',
                "zmiennaPola": dt._nsp,
                "opis": 'Sprawność średnioprężnej części ',
                "row": 3,
                "columne": 1,
                "flag": 1
            },
            'strMps': {
                "ramka": 'ramka0',
                "zmiennaPola": dt._nnp,
                "opis": 'Sprawność niskoprężnej części  ',
                "row": 4,
                "columne": 1,
                "flag": 1
            },
            'strMsp': {
                "ramka": 'ramka1',
                "zmiennaPola": d2._isp,
                "opis": 'Entalpia średniprężnej części isp [J/kg]',
                "row": 2,
                "columne": 2,
                "flag": 1
            },
            'strMnp': {
                "ramka": 'ramka1',
                "zmiennaPola": d2._inp,
                "opis": 'Entalpia niskoprężnej części inp [J/kg]',
                "row": 3,
                "columne": 2,
                "flag": 1
            },
            'strMznp': {
                "ramka": 'ramka1',
                "zmiennaPola": d2._iznp,
                "opis": 'Entalpia iznp [J/kg]',
                "row":4,
                "columne": 2,
                "flag": 1
            },
            'entIskzm': {
                "ramka": 'ramka2',
                "zmiennaPola": funk._qwp2,
                "opis": 'Ciepło wysokoprężnej Qwp [J/s] ',
                "row": 2,
                "columne": 3,
                "flag": 1
            },
            'entIskxn2': {
                "ramka": 'ramka2',
                "zmiennaPola": funk._qsp2,
                "opis": 'Ciepło średnioprężnej Qsp[J/s]',
                "row": 3,
                "columne": 3,
                "flag": 1
            },
            'niskoprezna': {
                "ramka": 'ramka2',
                "zmiennaPola": funk._qnp2,
                "opis": 'Ciepło niskoprężnej Qnp[J/s] ',
                "row": 4,
                "columne": 3,
                "flag": 1
            },
            'entIskxn3': {
                "ramka": 'ramka2',
                "zmiennaPola": funk._qsum2,
                "opis": 'Ciepło suma  Qt [J/s]',
                "row": 5,
                "columne": 3,
                "flag": 1
            },
            'roOdhaz': {
                "ramka": 'ramka3',
                "zmiennaPola": self._q,
                "opis": 'Q  ',
                "row": 2,
                "columne": 4,
                "flag": 2
            },
            'cisnieniePpp': {
                "ramka": 'ramka3',
                "zmiennaPola": self._qnom,
                "opis": 'Wartość nominalna Qnom [J/s]',
                "row": 3,
                "columne": 4,
                "flag": 2
            },
            'cisieniePzp': {
                "ramka": 'ramka3',
                "zmiennaPola":self.obj.tabMwz[2],
                "opis": 'Strumień masowy za pompą wody zasilającej kocioł mwz[kg/s]',
                "row": 4,
                "columne": 4,
                "flag": 1
            },
            'delPzp': {
                "ramka": 'ramka3',
                "zmiennaPola": self._qProc,
                "opis": ' Qproc ',
                "row": 5,
                "columne": 4,
                "flag": 1
            },
            'spadekMoc': {
                "ramka": 'ramka4',
                "zmiennaPola": self._spadekMocy,
                "opis": 'Spadek mocy ',
                "row": 2,
                "columne": 6,
                "flag": 1
            },
            'iwodODG': {
                "ramka": 'ramka4',
                "zmiennaPola": self._iwodODG ,
                "opis": 'iWodODG ',
                "row": 3,
                "columne": 6,
                "flag": 1
            },
            'mzas': {
                "ramka": 'ramka4',
                "zmiennaPola": self._mzas,
                "opis": 'mzas ',
                "row": 4,
                "columne": 6,
                "flag": 1
            },
            'mps': {
                "ramka": 'ramka4',
                "zmiennaPola": self._mps,
                "opis": 'mps ',
                "row": 5,
                "columne": 6,
                "flag": 1
            }
            # 'akcje': {
            #     "ramka": 'ramka5',
            #     "zmiennaPola":"",
            #     "opis": 'Oblicz ',
            #     "row": 5,
            #     "columne": 6,
            #     "flag": 1
            # }

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
            'ramka2': {
                # "tab": ,
                "opis": "Parametry wody zasilającej  :",
                "row": 1,
                "columne": 2
            },
            'ramka3': {
                # "tab": ,
                "opis": "Parametry wody zasilającej  :",
                "row": 2,
                "columne": 0
            },
            'ramka4': {
                # "tab": ,
                "opis": "Parametry wody zasilającej  :",
                "row": 2,
                "columne": 1
            },
            'ramka5': {
                # "tab": ,
                "opis": "Akcje  :",
                "row": 2,
                "columne": 2
            },

        }
        return self.listaRamek
