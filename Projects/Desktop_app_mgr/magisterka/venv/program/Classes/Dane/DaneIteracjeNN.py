import tkinter as tk
from tkinter import ttk, Canvas
from tkinter import *

import program.Classes.Dane.DaneEntalpia as d1
import program.Classes.Dane.DaneEntalpia2 as d2
import program.Classes.Dane.DaneStrumienieMasy as st
import program.Classes.Funkcje.FunkcjeIteracje as it
# import numpy as np

n1=DoubleVar()
n2=DoubleVar()
n3=DoubleVar()
n4=DoubleVar()
n5=DoubleVar()
n6=DoubleVar()
n7=DoubleVar()
n8=DoubleVar()
n9=DoubleVar()
n10=DoubleVar()
n11=DoubleVar()
n12=DoubleVar()
n13=DoubleVar()
n14=DoubleVar()
n15=DoubleVar()
n16=DoubleVar()
n17=DoubleVar()
n18=DoubleVar()
n19=DoubleVar()
n20=DoubleVar()
n21=DoubleVar()
n22=DoubleVar()

listaRamek = {
    # 'ramka0': {
    #     # "tab": ,
    #     "opis": "Warunki początkowe:",
    #     "row": 1,
    #     "columne": 0
    # },
    'ramka1': {
        # "tab": ,
        "opis": "Para świeża:",
        "row": 2,
        "columne": 0
    },
    'ramka2': {
        # "tab": ,
        "opis": "Mieszanie za kondensatorem :",
        "row": 1,
        "columne": 1
    },
    'ramka3': {
        # "tab": ,
        "opis": "XN1/XN2",
        "row": 2,
        "columne": 1
    },
    'ramka4': {
        # "tab": ,
        "opis": "XN3",
        "row": 3,
        "columne": 1
    },
    'ramka5': {
        # "tab": ,
        "opis": "XN3 za punktem mieszania",
        "row": 4,
        "columne": 1
    },
    'ramka6': {
        # "tab": ,
        "opis": "XN4",
        "row": 5,
        "columne": 1
    },
    'ramka7': {
        # "tab": ,
        "opis": "XN5",
        "row": 6,
        "columne": 1
    },
    'ramka8': {
        # "tab": ,
        "opis": "Odgazowywacz",
        "row": 7,
        "columne": 1
    },
    'ramka9': {
        # "tab": ,
        "opis": "XW1",
        "row": 1,
        "columne": 2
    },
    'ramka10': {
        # "tab": ,
        "opis": "XW2",
        "row": 1,
        "columne": 3
    },
    'ramka11': {
        # "tab": ,
        "opis": "XW3",
        "row": 2,
        "columne": 3
    }
}

listOfElements = {
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
    #     "zmiennaPola": it._expectValue,
    #     "opis": 'Oczekiwana wartość ',
    #     "row": 2,
    #     "columne": 2,
    #     "flag": 1
    # },


    'etalpIwz': {
        "ramka": 'ramka1',
        "zmiennaPola": DoubleVar(),
        "opis": 'Entalpia iwz ',
        "row": 18,
        "columne": 2,
        "flag": 1
    },
    'strMps': {
        "ramka": 'ramka1',
        "zmiennaPola": DoubleVar(),
        "opis": 'strumien mps ',
        "row": 20,
        "columne": 2,
        "flag": 1
    },
    'strMsp': {
        "ramka": 'ramka1',
        "zmiennaPola": DoubleVar(),
        "opis": 'Strumień msp ',
        "row": 22,
        "columne": 2,
        "flag": 1
    },
    'strMnp': {
        "ramka": 'ramka1',
        "zmiennaPola": DoubleVar(),
        "opis": 'Strumien Mnp ',
        "row": 24,
        "columne": 2,
        "flag": 1
    },
    'strMznp': {
        "ramka": 'ramka1',
        "zmiennaPola": DoubleVar(),
        "opis": 'Strumien Mznp ',
        "row": 26,
        "columne": 2,
        "flag": 1
    },
    'entIskzm': {
        "ramka": 'ramka2',
        "zmiennaPola": DoubleVar(),
        "opis": 'Entalpia Iskzm ',
        "row": 4,
        "columne": 2,
        "flag": 1
    },
    'entIskxn2': {
        "ramka": 'ramka3',
        "zmiennaPola": DoubleVar(),
        "opis": 'Entalpia Iskxn3 ',
        "row": 6,
        "columne": 2,
        "flag": 1
    },
    'entIskxn3': {
        "ramka": 'ramka4',
        "zmiennaPola":DoubleVar(),
        "opis": 'Entalpia Iskxn3 ',
        "row": 8,
        "columne": 2,
        "flag": 1
    },
    'entIskxn3a': {
        "ramka": 'ramka5',
        "zmiennaPola": DoubleVar(),
        "opis": 'Entalipa IskXN3A ',
        "row": 10,
        "columne": 2,
        "flag": 1
    },
    'entIskxn4': {
        "ramka": 'ramka6',
        "zmiennaPola": DoubleVar(),
        "opis": 'Entalpia IskXn4 ',
        "row": 12,
        "columne": 2,
        "flag": 1
    },
    'entIskxn5': {
        "ramka": 'ramka7',
        "zmiennaPola": DoubleVar(),
        "opis": 'Entalpia Iskxn5 ',
        "row": 14,
        "columne": 2,
        "flag": 1
    },
    'entOdgaz': {
        "ramka": 'ramka8',
        "zmiennaPola": DoubleVar(),
        "opis": 'Entalpia IwodOdg ',
        "row": 16,
        "columne": 2,
        "flag": 1
    },
    'roOdhaz': {
        "ramka": 'ramka9',
        "zmiennaPola": DoubleVar(),
        "opis": 'Gestosc wododg ',
        "row": 4,
        "columne": 3,
        "flag": 1
    },
    'cisnieniePpp': {
        "ramka": 'ramka9',
        "zmiennaPola": DoubleVar(),
        "opis": 'Cisnienie przed pompa wod. zas kocio ',
        "row": 6,
        "columne": 3,
        "flag": 1
    },
    'cisieniePzp': {
        "ramka": 'ramka9',
        "zmiennaPola": DoubleVar(),
        "opis": 'Ciśnienie za pompą wody zasilającej kocioł ',
        "row": 8,
        "columne": 3,
        "flag": 1
    },
    'delPzp': {
        "ramka": 'ramka9',
        "zmiennaPola": DoubleVar(),
        "opis": 'delta pz ',
        "row": 10,
        "columne": 3,
        "flag": 1
    },
    'delIpzp': {
        "ramka": 'ramka9',
        "zmiennaPola": DoubleVar(),
        "opis": 'delta ipz ',
        "row": 12,
        "columne": 3,
        "flag": 1
    },
    'entpIpz': {
        "ramka": 'ramka9',
        "zmiennaPola": DoubleVar(),
        "opis": 'Entalpia ipz ',
        "row": 14,
        "columne": 3,
        "flag": 1
    },
    'entIskxw1': {
        "ramka": 'ramka9',
        "zmiennaPola": DoubleVar(),
        "opis": 'Entalpia Iskxw1 ',
        "row": 16,
        "columne": 3,
        "flag": 1
    },
    'strMwz': {
        "ramka": 'ramka9',
        "zmiennaPola": DoubleVar(),
        "opis": 'Strumień masy pary wz, t/h ',
        "row": 18,
        "columne": 3,
        "flag": 1
    },
    'entIskXW2': {
        "ramka": 'ramka10',
        "zmiennaPola": DoubleVar(),
        "opis": 'entalpia iskxw2 ',
        "row": 4,
        "columne": 4,
        "flag": 1
    },
    'entIskXw3': {
        "ramka": 'ramka11',
        "zmiennaPola": DoubleVar(),
        "opis": 'Entalpia IskXW3 ',
        "row": 6,
        "columne": 4,
        "flag": 1
    },

}







