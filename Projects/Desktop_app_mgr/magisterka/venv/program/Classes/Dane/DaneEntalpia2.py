import tkinter as tk
from tkinter import ttk, Canvas
from tkinter import *

# Entalpia skroplin w XN3
_mp6 = DoubleVar()  # 'Strumień masy pary, t/h '
_Tp6 = DoubleVar()  # 'Temperatura pary, st. C '
_pp6 = DoubleVar()  # 'Ciśnienie pary, Mpa '
_ip6 = DoubleVar()  # 'Entalpia pary, kJ/kg: '

# Entalpia skroplin w XN1/XN2
_mpVII = DoubleVar()  # 'Strumień masy pary, t/h '
_TpVII = DoubleVar()  # 'Temperatura pary, st. C '
_ppVII = DoubleVar()  # 'Ciśnienie pary, Mpa '
_ipVII = DoubleVar()  # 'Entalpia pary, kJ/kg: '

# Entalpia pary upust nr I
_mI = DoubleVar()  # 'Strumień masy pary, t/h '
_TI = DoubleVar()  # 'Temperatura pary, st. C '
_pI = DoubleVar()  # 'Ciśnienie pary, Mpa '
_iI = DoubleVar()  # 'Entalpia pary, kJ/kg: '

# Entalpia pary upust nr II
_mII = DoubleVar()  # 'Strumień masy pary, t/h '
_TII = DoubleVar()  # 'Temperatura pary, st. C '
_pII = DoubleVar()  # 'Ciśnienie pary, Mpa '
_iII = DoubleVar()  # 'Entalpia pary, kJ/kg: '

# Entalpia pary upust nr III
_mIII = DoubleVar()  # 'Strumień masy pary, t/h '
_TIII = DoubleVar()  # 'Temperatura pary, st. C '
_pIII = DoubleVar()  # 'Ciśnienie pary, Mpa '
_iIII = DoubleVar()  # 'Entalpia pary, kJ/kg: '

# Entalpia pary upust nr IV
_mIV = DoubleVar()  # 'Strumień masy pary, t/h '
_TIV = DoubleVar()  # 'Temperatura pary, st. C '
_pIV = DoubleVar()  # 'Ciśnienie pary, Mpa '
_iIV = DoubleVar()  # 'Entalpia pary, kJ/kg: '

# Entalpia pary upust nr V
_mV = DoubleVar()  # 'Strumień masy pary, t/h '
_TV = DoubleVar()  # 'Temperatura pary, st. C '
_pV = DoubleVar()  # 'Ciśnienie pary, Mpa '
_iV = DoubleVar()  # 'Entalpia pary, kJ/kg: '

# Entalpia pary upust nr VI
_mVI = DoubleVar()  # 'Strumień masy pary, t/h '
_TVI = DoubleVar() # 'Temperatura pary, st. C '
_pVI = DoubleVar()  # 'Ciśnienie pary, Mpa '
_iVI = DoubleVar()  # 'Entalpia pary, kJ/kg: '

# Entalpia pary upust nr VII
_mVII = DoubleVar()  # 'Strumień masy pary, t/h '
_TVII = DoubleVar()  # 'Temperatura pary, st. C '
_pVII = DoubleVar()  # 'Ciśnienie pary, Mpa '
_iVII = DoubleVar()  # 'Entalpia pary, kJ/kg: '

# Entalpie do obliczenia strumienia masy paliwa

_isp = DoubleVar()
_inp = DoubleVar()
_iznp = DoubleVar()

# Entalpia skroplin w XN3
listOfElements13 = {
    # 'strMasPary': {
    #     "ramka": 'ramka13',
    #     "zmiennaPola": _mp6,
    #     "opis": "Strumień masy pary, t/h: ",
    #     "row": 4,
    #     "columne": 2
    # },
    'tempPary': {
        "ramka": 'ramka13',
        "zmiennaPola": _Tp6,
        "opis": "Temperatura pary, st. K:",
        "row": 6,
        "columne": 2,
        "flag": 1
    },
    'cisnPary': {
        "ramka": 'ramka13',
        "zmiennaPola": _pp6,
        "opis": "Ciśnienie pary, MPa:",
        "row": 8,
        "columne": 2,
        "flag": 1
    },
    'entalpiaPary': {
        "ramka": 'ramka13',
        "zmiennaPola": _ip6,
        "opis": "Entalpia pary, J/kg:",
        "row": 10,
        "columne": 2,
        "flag": 1
    }

}

# Entalpia skroplin w XN1/XN2
listOfElements14 = {
    # 'strMasPary': {
    #     "ramka": 'ramka14',
    #     "zmiennaPola": _mpVII,
    #     "opis": "Strumień masy pary, t/h: ",
    #     "row": 4,
    #     "columne": 2
    # },
    'tempPary': {
        "ramka": 'ramka14',
        "zmiennaPola": _TpVII,
        "opis": "Temperatura pary, st. K:",
        "row": 18,
        "columne": 2,
        "flag": 1
    },
    'cisnPary': {
        "ramka": 'ramka14',
        "zmiennaPola": _ppVII,
        "opis": "Ciśnienie pary, MPa:",
        "row": 20,
        "columne": 2,
        "flag": 1
    },
    'entalpiaPary': {
        "ramka": 'ramka14',
        "zmiennaPola": _ipVII,
        "opis": "Entalpia pary, J/kg:",
        "row": 22,
        "columne": 2,
        "flag": 1
    }

}

# Entalpia pary upust nr I
listOfElements15 = {
    # 'strMasPary': {
    #     "ramka": 'ramka15',
    #     "zmiennaPola": _mI,
    #     "opis": "Strumień masy pary, t/h: ",
    #     "row": 4,
    #     "columne": 2
    # },
    'tempPary': {
        "ramka": 'ramka15',
        "zmiennaPola": _TI,
        "opis": "Temperatura pary, st. K:",
        "row": 28,
        "columne": 2,
        "flag": 1
    },
    'cisnPary': {
        "ramka": 'ramka15',
        "zmiennaPola": _pI,
        "opis": "Ciśnienie pary, MPa:",
        "row": 30,
        "columne": 2,
        "flag": 1
    },
    'entalpiaPary': {
        "ramka": 'ramka15',
        "zmiennaPola": _iI,
        "opis": "Entalpia pary, J/kg:",
        "row": 32,
        "columne": 2,
        "flag": 1
    }

}

# Entalpia pary upust nr II
listOfElements16 = {
    # 'strMasPary': {
    #     "ramka": 'ramka16',
    #     "zmiennaPola": _mII,
    #     "opis": "Strumień masy pary, t/h: ",
    #     "row": 4,
    #     "columne": 2
    # },
    'tempPary': {
        "ramka": 'ramka16',
        "zmiennaPola": _TII,
        "opis": "Temperatura pary, st. K:",
        "row": 6,
        "columne": 3,
        "flag": 1
    },
    'cisnPary': {
        "ramka": 'ramka16',
        "zmiennaPola": _pII,
        "opis": "Ciśnienie pary, MPa:",
        "row": 8,
        "columne": 3,
        "flag": 1
    },
    'entalpiaPary': {
        "ramka": 'ramka16',
        "zmiennaPola": _iII,
        "opis": "Entalpia pary, J/kg:",
        "row": 10,
        "columne": 3,
        "flag": 1
    }

}

# Entalpia pary upust nr III
listOfElements17 = {
    # 'strMasPary': {
    #     "ramka": 'ramka17',
    #     "zmiennaPola": _mIII,
    #     "opis": "Strumień masy pary, t/h: ",
    #     "row": 4,
    #     "columne": 2
    # },
    'tempPary': {
        "ramka": 'ramka17',
        "zmiennaPola": _TIII,
        "opis": "Temperatura pary, st. K:",
        "row": 18,
        "columne": 3,
        "flag": 1
    },
    'cisnPary': {
        "ramka": 'ramka17',
        "zmiennaPola": _pIII,
        "opis": "Ciśnienie pary, MPa:",
        "row": 20,
        "columne": 3,
        "flag": 1
    },
    'entalpiaPary': {
        "ramka": 'ramka17',
        "zmiennaPola": _iIII,
        "opis": "Entalpia pary, J/kg:",
        "row": 22,
        "columne": 3,
        "flag": 1
    }

}

# Entalpia pary upust nr IV
listOfElements18 = {
    # 'strMasPary': {
    #     "ramka": 'ramka18',
    #     "zmiennaPola": _mIV,
    #     "opis": "Strumień masy pary, t/h: ",
    #     "row": 4,
    #     "columne": 2
    # },
    'tempPary': {
        "ramka": 'ramka18',
        "zmiennaPola": _TIV,
        "opis": "Temperatura pary, st. K:",
        "row": 28,
        "columne": 3,
        "flag": 1
    },
    'cisnPary': {
        "ramka": 'ramka18',
        "zmiennaPola": _pIV,
        "opis": "Ciśnienie pary, MPa:",
        "row": 30,
        "columne": 3,
        "flag": 1
    },
    'entalpiaPary': {
        "ramka": 'ramka18',
        "zmiennaPola": _iIV,
        "opis": "Entalpia pary, J/kg:",
        "row": 32,
        "columne": 3,
        "flag": 1
    }

}

# Entalpia pary upust nr V
listOfElements19 = {
    # 'strMasPary': {
    #     "ramka": 'ramka19',
    #     "zmiennaPola": _mV,
    #     "opis": "Strumień masy pary, t/h: ",
    #     "row": 4,
    #     "columne": 2
    # },
    'tempPary': {
        "ramka": 'ramka19',
        "zmiennaPola": _TV,
        "opis": "Temperatura pary, st. K:",
        "row": 6,
        "columne": 4,
        "flag": 1
    },
    'cisnPary': {
        "ramka": 'ramka19',
        "zmiennaPola": _pV,
        "opis": "Ciśnienie pary, MPa:",
        "row": 8,
        "columne": 4,
        "flag": 1
    },
    'entalpiaPary': {
        "ramka": 'ramka19',
        "zmiennaPola": _iV,
        "opis": "Entalpia pary, J/kg:",
        "row": 10,
        "columne": 4,
        "flag": 1
    }

}

# Entalpia pary upust nr VI
listOfElements20 = {
    # 'strMasPary': {
    #     "ramka": 'ramka20',
    #     "zmiennaPola": _mVI,
    #     "opis": "Strumień masy pary, t/h: ",
    #     "row": 4,
    #     "columne": 2
    # },
    'tempPary': {
        "ramka": 'ramka20',
        "zmiennaPola": _TVI,
        "opis": "Temperatura pary, st. K:",
        "row": 18,
        "columne": 4,
        "flag": 1
    },
    'cisnPary': {
        "ramka": 'ramka20',
        "zmiennaPola": _pVI,
        "opis": "Ciśnienie pary, MPa:",
        "row": 20,
        "columne": 4,
        "flag": 1
    },
    'entalpiaPary': {
        "ramka": 'ramka20',
        "zmiennaPola": _iVI,
        "opis": "Entalpia pary, J/kg:",
        "row": 22,
        "columne": 4,
        "flag": 1
    }

}

# Entalpia pary upust nr VII
listOfElements21 = {
    # 'strMasPary': {
    #     "ramka": 'ramka21',
    #     "zmiennaPola": _mVII,
    #     "opis": "Strumień masy pary, t/h: ",
    #     "row": 4,
    #     "columne": 2
    # },
    'tempPary': {
        "ramka": 'ramka21',
        "zmiennaPola": _TVII,
        "opis": "Temperatura pary, st. K:",
        "row": 28,
        "columne": 4,
        "flag": 1
    },
    'cisnPary': {
        "ramka": 'ramka21',
        "zmiennaPola": _pVII,
        "opis": "Ciśnienie pary, MPa:",
        "row": 30,
        "columne": 4,
        "flag": 1
    },
    'entalpiaPary': {
        "ramka": 'ramka21',
        "zmiennaPola": _iVII,
        "opis": "Entalpia pary, J/kg:",
        "row": 32,
        "columne": 4,
        "flag": 1
    }
}
listaRamek = {
    # 'ramka12' : {
    #     # "tab": ,
    #     "opis": "Dane dla  wody zasilającej za pompą wody zasilającej:",
    #     "row": 37,
    #     "columne": 2,
    #     "dane": listOfElements12
    # },
    'ramka13': {
        # "tab": ,
        "opis": "Paramtery dla skroplin w XN3 [pVI]:",
        "row": 4,
        "columne": 0,
        "dane": listOfElements13

    },
    'ramka14': {
        # "tab": ,
        "opis": "Parametry dla  skroplin w XN1/XN2 [pVII]:",
        "row": 14,
        "columne": 0,
        "dane": listOfElements14
    },
    'ramka15': {
        # "tab": ,
        "opis": "Parametry pary upust nr I [I]:",
        "row": 24,
        "columne": 0,
        "dane": listOfElements15
    },
    'ramka16': {
        # "tab": ,
        "opis": "Parametry pary upust nr II [II]:",
        "row": 4,
        "columne": 1,
        "dane": listOfElements16
    },
    'ramka17': {
        # "tab": ,
        "opis": "Parametry pary upust nr III [III]:",
        "row": 14,
        "columne": 1,
        "dane": listOfElements17
    },
    'ramka18': {
        # "tab": ,
        "opis": "Parametry pary upust nr IV [IV]:",
        "row": 24,
        "columne": 1,
        "dane": listOfElements18
    },
    'ramka19': {
        # "tab": ,
        "opis": "Parametry pary upust nr V [V]:",
        "row": 4,
        "columne": 2,
        "dane": listOfElements19
    },
    'ramka20': {
        # "tab": ,
        "opis": "Parametry pary upust nr VI [VI]:",
        "row": 14,
        "columne": 2,
        "dane": listOfElements20
    },
    'ramka21': {
        # "tab": ,
        "opis": "Parametry pary upust nr VII [VII]:",
        "row": 24,
        "columne": 2,
        "dane": listOfElements21
    }
}
