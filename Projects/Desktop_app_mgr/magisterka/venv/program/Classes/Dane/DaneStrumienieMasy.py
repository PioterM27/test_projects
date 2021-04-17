import tkinter as tk
from tkinter import *
from tkinter import ttk, Canvas

# Strumień masy wody zasilającej kocioł
_mwz = DoubleVar()  # 'Strumień masy pary, t/h '
# Strumień masy odsolin
_mods = DoubleVar()  # 'Strumień masy pary, t/h '
# Strumień masy wody do wtryskiwacza pary świeżej nr I
_mwtrI = DoubleVar()  # 'Strumień masy pary, t/h '
# Strumień masy wody do wtryskiwacza pary świeżej nr II
_mwtrII = DoubleVar()  # 'Strumień masy pary, t/h '
# Strumień masy wody do wtryskiwacza pary świeżej nr III
_mwtrIII = DoubleVar()  # 'Strumień masy pary, t/h '
# Strumień masy wody do wtryskiwacza pary wtórnej nr IV
_mwtrIV = DoubleVar()  # 'Strumień masy pary, t/h '
# Strumień masy wody do wtryskiwacza pary wtórnej nr V
_mwtrV = DoubleVar()  # 'Strumień masy pary, t/h '
# Strumień masy pary - upust nr I
_mI = DoubleVar()  # 'Strumień masy pary, t/h '
# Strumień masy pary - upust nr II
_mII = DoubleVar()  # 'Strumień masy pary, t/h '
# Strumień masy pary - upust nr III
_mIII = DoubleVar()  # 'Strumień masy pary, t/h '
# Strumień masy pary - upust nr IV
_mIV = DoubleVar()  # 'Strumień masy pary, t/h '
# Strumień masy pary - upust nr V
_mV = DoubleVar()  # 'Strumień masy pary, t/h '
# Strumień masy pary - upust nr VI
_mVI = DoubleVar()  # 'Strumień masy pary, t/h '
# Strumień masy pary - upust nr VII
_mVII = DoubleVar()  # 'Strumień masy pary, t/h '
# Strumień masy pary świeżej
_mps = DoubleVar()  # 'Strumień masy pary, t/h '
# Strumień masy pary na wylocie z wysokoprężnej części turbiny   obliczenia
_mwt = DoubleVar()  # 'Strumień masy pary, t/h '
# Strumień masy pary wtórnie przegrzanej
_msp = DoubleVar()  # 'Strumień masy pary, t/h '
# Strumień masy pary na wlocie do niskoprężnej części turbiny
_mnp = DoubleVar()  # 'Strumień masy pary, t/h '
# Strumień masy pary na wylocie z niskoprężnej części turbiny
_mznp = DoubleVar()  # 'Strumień masy pary, t/h '
# Strumień masy pary do odgazowywacza
_modg = DoubleVar()  # 'Strumień masy pary, t/h '
# Strumien masy paliwa
_mpal = DoubleVar()

listaRamek = {
    'ramka1': {
        # "tab": ,
        "opis": "Obliczenie strumienii masy w :",
        "row": 4,
        "columne": 0
    },
    'ramka2': {
        # "tab": ,
        "opis": "Obliczenie strumienii masy w :",
        "row": 4,
        "columne": 1
    },
    'ramka3': {
        # "tab": ,
        "opis": "Obliczenie strumienii masy w :",
        "row": 4,
        "columne": 2
    }
    # 'ramka4': {
    #     # "tab": ,
    #     "opis": "Obliczenie strumienii masy w :",
    #     "row": 2,
    #     "columne": 1
    # },
    # 'ramka5': {
    #     # "tab": ,
    #     "opis": "Obliczenie strumienii masy w :",
    #     "row": 3,
    #     "columne": 0
    # }
    # 'ramka6': {
    #     # "tab": ,
    #     "opis": "Obliczenie strumienii masy w :",
    #     "row": 3,
    #     "columne": 1
    # }
}

listOfElements = {
    'wodZasKociol': {
        "ramka": 'ramka1',
        "zmiennaPola": _mwz,
        "opis": 'Strumień masy wody zasilającej kocioł [kg/s] ',
        "row": 4,
        "columne": 2,
        "flag": 1
    },
    'strMasOds': {
        "ramka": "ramka1",
        "zmiennaPola": _mods,
        "opis": "Strumień masy odsolin [kg/s]",
        "row": 6,
        "columne": 2,
        "flag": 1
    },
    'strWtrysParSwI': {
        "ramka": "ramka1",
        "zmiennaPola": _mwtrI,
        "opis": "Strumień masy wody do wtryskiwacza pary świeżej nr I [kg/s]",
        "row": 8,
        "columne": 2,
        "flag": 1
    },
    'strWtrysParSwII': {
        "ramka": "ramka1",
        "zmiennaPola": _mwtrII,
        "opis": "Strumień masy wody do wtryskiwacza pary świeżej nr II [kg/s]",
        "row": 10,
        "columne": 2,
        "flag": 1
    },
    'strWtrysParSwIII': {
        "ramka": "ramka1",
        "zmiennaPola": _mwtrIII,
        "opis": "Strumień masy wody do wtryskiwacza pary świeżej nr III [kg/s]",
        "row": 12,
        "columne": 2,
        "flag": 1
    },
    'strWtrysParWtrIV': {
        "ramka": "ramka1",
        "zmiennaPola": _mwtrIV,
        "opis": "Strumień masy wody do wtryskiwacza pary wtórnej nr IV [kg/s]",
        "row": 14,
        "columne": 2,
        "flag": 1
    },
    'strWtrysParWtrV': {
        "ramka": "ramka1",
        "zmiennaPola": _mwtrV,
        "opis": "Strumień masy wody do wtryskiwacza pary wtórnej nr V [kg/s]",
        "row": 16,
        "columne": 2,
        "flag": 1
    },
    'strMasyParyI': {
        "ramka": "ramka2",
        "zmiennaPola": _mI,
        "opis": "Strumień masy pary - upust nr I [kg/s]",
        "row": 4,
        "columne": 2,
        "flag": 1
    },
    'strMasyParyII': {
        "ramka": "ramka2",
        "zmiennaPola": _mII,
        "opis": "Strumień masy pary - upust nr II [kg/s]",
        "row": 6,
        "columne": 2,
        "flag": 1
    },
    'strMasyParyIII': {
        "ramka": "ramka2",
        "zmiennaPola": _mIII,
        "opis": "Strumień masy pary - upust nr III [kg/s]",
        "row": 8,
        "columne": 2,
        "flag": 1
    },
    'strMasyParyIV': {
        "ramka": "ramka2",
        "zmiennaPola": _mIV,
        "opis": "Strumień masy pary - upust nr IV [kg/s]",
        "row": 10,
        "columne": 2,
        "flag": 1
    },
    'strMasyParyV': {
        "ramka": "ramka2",
        "zmiennaPola": _mV,
        "opis": "Strumień masy pary - upust nr V [kg/s]",
        "row": 12,
        "columne": 2,
        "flag": 1
    },
    'strMasyParyVI': {
        "ramka": "ramka2",
        "zmiennaPola": _mVI,
        "opis": "Strumień masy pary - upust nr VI [kg/s]",
        "row": 14,
        "columne": 2,
        "flag": 1
    },
    'strMasyParyVII': {
        "ramka": "ramka2",
        "zmiennaPola": _mVII,
        "opis": "Strumień masy pary - upust nr VII [kg/s]",
        "row": 16,
        "columne": 2,
        "flag": 1
    },
    'strMasyParySw': {
        "ramka": "ramka3",
        "zmiennaPola": _mps,
        "opis": "Strumień masy pary świeżej [kg/s]",
        "row": 4,
        "columne": 3,
        "flag": 1
    },
    'strMasyParyWysCzTurb': {
        "ramka": "ramka3",
        "zmiennaPola": _mwt,
        "opis": "Strumień masy pary na \n wylocie z wysokoprężnej części turbiny [kg/s]",
        "row": 14,
        "columne": 3,
        "flag": 0
    },
    'strMasyParyWtPrzeg': {
        "ramka": "ramka3",
        "zmiennaPola": _msp,
        "opis": "Strumień masy pary wtórnie przegrzanej [kg/s]",
        "row": 8,
        "columne": 3,
        "flag": 0
    },
    'strMasyParyNiskCzesTrbWl': {
        "ramka": "ramka3",
        "zmiennaPola": _mnp,
        "opis": "Strumień masy pary na wlocie do niskoprężnej części turbiny [kg/s]",
        "row": 10,
        "columne": 3,
        "flag": 0
    },
    'strMasyParyNiskCzesTrbWyl': {
        "ramka": "ramka3",
        "zmiennaPola": _mznp,
        "opis": "Strumień masy pary na wylocie z niskoprężnej części turbiny [kg/s]",
        "row": 12,
        "columne": 3,
        "flag": 0
    },
    'strMasyParyOdg': {
        "ramka": "ramka3",
        "zmiennaPola": _modg,
        "opis": "Strumień masy pary do odgazowywacza [kg/s]",
        "row": 6,
        "columne": 3,
        "flag": 1
    },
    'strMasyPaliwa': {
        "ramka": "ramka3",
        "zmiennaPola": _mpal,
        "opis": "Strumień masy paliway [kg/s]",
        "row": 16,
        "columne": 3,
        "flag": 0
    }
}
