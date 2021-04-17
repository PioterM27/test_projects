import tkinter as tk
from tkinter import ttk, Canvas
from tkinter import *

_dZas = DoubleVar()  # 'Średnica zasobnika: '
_hZas = DoubleVar()  # 'Wysokość zasobnika: '
_ilZas = DoubleVar()  # 'Ilość zasobników: '
_gestWody = DoubleVar()  # 'Gęstość wody w zasobnikach: '
_czasNap = DoubleVar()  # 'Czas napełniania zasobników: '
_Vzas = DoubleVar()  # Pojemnośc jednego zasobnika
_VzasMax = DoubleVar()  # Wymagana pojemność zasobnika dla pracy szczytowej
_strWody = DoubleVar()  # Strumien masy wody zasialajecj zasobnnik
# Dane wejściowe do obliczeń
_wd = DoubleVar()  # Wartość opałowa paliwa
_nk = DoubleVar()  # Sprawność kotła
_nwp = DoubleVar()  # Sprawnośc wysokoprężnej części turbiny
_nsp = DoubleVar()  # Sprawnośc średniopręznej części turbiny
_nnp = DoubleVar()  # Sprawnośc niskopreżnej części turbiny
_mzas = DoubleVar()  # Strumień masy wody zasilającej zasobnik
kj = DoubleVar()

canvas = Canvas()
_dZas.set('')
_hZas.set('')
_ilZas.set('')
_gestWody.set('')
_czasNap.set('')
_Vzas.set('')
_VzasMax.set('')
_strWody.set('')
_nk.set('')
_wd.set('')
_mzas.set('')
# =============================Ramki=========================#

ramka1 = {
    # "tab": ,
    "opis": "Obliczenie strumienia masy wody zasilającej zasobnik :",
    "row": 2,
    "columne": 0
}
ramka2 = {
    # "tab": ,
    "opis": "Dane wejściowe do obliczeń:",
    "row": 20,
    "columne": 1
}
ramka3 = {
    # "tab": ,
    "opis": "Rysunek",
    "row": 2,
    "columne": 1
}

listOfElements = {
    'zasobnikSr': {
        "ramka": 'ramka1',
        "zmiennaPola": _dZas,
        "opis": "Średnica zasobnika:",
        "row": 4,
        "columne": 2,
        "flag": 1,
        "units": 'm',

    },
    'zasobnikH': {
        "ramka": "ramka1",
        "zmiennaPola": _hZas,
        "opis": "Wysokość zasobnika:",
        "row": 6,
        "columne": 2,
        "flag": 1,
        "units": 'm',
    },
    'iloscZas': {
        "ramka": "ramka1",
        "zmiennaPola": _ilZas,
        "opis": "Ilośc zasobników:",
        "row": 8,
        "columne": 2,
        "flag": 1,
        "units": '',
    },
    'czasNap': {
        "ramka": "ramka1",
        "zmiennaPola": _czasNap,
        "opis": "Czas napełniania [s] :",
        "row": 10,
        "columne": 2,
        "flag": 1,
        "units": 's',

    },
    'pojZasob': {
        "ramka": "ramka1",
        "zmiennaPola": _Vzas,
        "opis": "Wymagana pojemność jednego zasobnika:",
        "row": 20,
        "columne": 2,
        "flag": 2,
        "units": 'm3',
    },
    'pojZasobMax': {
        "ramka": "ramka1",
        "zmiennaPola": _VzasMax,
        "opis": "Wymagana pojemność zasobnika \n dla pracy szytowej :",
        "row": 22,
        "columne": 2,
        "flag": 2,
        "units": 'm3',
    },
    'gestWody': {
        "ramka": "ramka1",
        "zmiennaPola": _gestWody,
        "opis": "Gęstość wody w zasobnikach :",
        "row": 14,
        "columne": 2,
        "flag": 1,
        "units": 'kg/m3',
    },
    'strMasyWody': {
        "ramka": "ramka1",
        "zmiennaPola": _mzas,
        "opis": "Strumień masy wody zasilającej zasobnik :",
        "row": 18,
        "columne": 2,
        "flag": 2,
        "units": 'kg/s',
    },
    'wartOpalowaPal': {
        "ramka": "ramka1",
        "zmiennaPola": _wd,
        "opis": "Wartość opałowa paliwa: ",
        "row": 12,
        "columne": 2,
        "flag": 1,
        "units": 'J/kg',
    },
    'sprawnoscKotla': {
        "ramka": "ramka1",
        "zmiennaPola": _nk,
        "opis": "Sprawność kotła: ",
        "row": 16,
        "columne": 2,
        "flag": 1,
        "units": '',
    },
}
