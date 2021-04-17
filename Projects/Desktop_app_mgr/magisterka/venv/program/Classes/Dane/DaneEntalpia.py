import tkinter as tk
from tkinter import ttk, Canvas
from tkinter import *

# Entalpia wody zasilającej(przed kotłem)
_mwz = DoubleVar()  # 'Strumień masy pary, t/h '
_Twz = DoubleVar()  # 'Temperatura pary, st. C '
_pwz = DoubleVar()  # 'Ciśnienie pary, Mpa '
_iwz = DoubleVar()  # 'Entalpia pary, kJ/kg: '

# Entalpia wody zasilającej za pompą wody zasilającej
_mpz = DoubleVar()  # 'Strumień masy pary, t/h '
_Tpz = DoubleVar()  # 'Temperatura pary, st. C '
_ppz = DoubleVar()  # 'Ciśnienie pary, Mpa '
_ipz = DoubleVar()  # 'Entalpia pary, kJ/kg: '

# Entalpia skroplin w kondensatorze
_mpkond = DoubleVar()  # 'Strumień masy pary, t/h '
_Tpkond = DoubleVar()  # 'Temperatura pary, st. C '
_ppkond = DoubleVar()  # 'Ciśnienie pary, Mpa '
_ipkond = DoubleVar()  # 'Entalpia pary, kJ/kg: '

# Entalpia odsolin
_mods = DoubleVar()  # 'Strumień masy pary, t/h '
_Tods = DoubleVar()  # 'Temperatura pary, st. C '
_pods = DoubleVar()  # 'Ciśnienie pary, Mpa '
_iods = DoubleVar()  # 'Entalpia pary, kJ/kg: '

# Entalpia pary świeżej
_mSH5wyl = DoubleVar()  # 'Strumień masy pary, t/h '
_TSH5wyl = DoubleVar()  # 'Temperatura pary, st. C '
_pSH5wyl = DoubleVar()  # 'Ciśnienie pary, Mpa '
_iSH5wyl = DoubleVar()  # 'Entalpia pary, kJ/kg: '

# Entalpia pary na wylocie z wysokoprężnej części turbiny
_mRH1wlot = DoubleVar()  # 'Strumień masy pary, t/h '
_TRH1wlot = DoubleVar()  # 'Temperatura pary, st. C '
_pRH1wlot = DoubleVar()  # 'Ciśnienie pary, Mpa '
_iRH1wlot = DoubleVar()  # 'Entalpia pary, kJ/kg: '

# Entalpia pary wtórnie przegrzanej
_mRH2wyl = DoubleVar()  # 'Strumień masy pary, t/h '
_TRH2wyl = DoubleVar()  # 'Temperatura pary, st. C '
_pRH2wyl = DoubleVar()  # 'Ciśnienie pary, Mpa '
_iRH2wyl = DoubleVar()  # 'Entalpia pary, kJ/kg: '

# Entalpia skroplin w XW3
_mp1 = DoubleVar()  # 'Strumień masy pary, t/h '
_Tp1 = DoubleVar()  # 'Temperatura pary, st. C '
_pp1 = DoubleVar()  # 'Ciśnienie pary, Mpa '
_ip1 = DoubleVar()  # 'Entalpia pary, kJ/kg: '

# Entalpia skroplin w XW2
_mp2 = DoubleVar()  # 'Strumień masy pary, t/h '
_Tp2 = DoubleVar()  # 'Temperatura pary, st. C '
_pp2 = DoubleVar()  # 'Ciśnienie pary, Mpa '
_ip2 = DoubleVar()  # 'Entalpia pary, kJ/kg: '

# Entalpia skroplin w XW1
_mp3 = DoubleVar()  # 'Strumień masy pary, t/h '
_Tp3 = DoubleVar()  # 'Temperatura pary, st. C '
_pp3 = DoubleVar()  # 'Ciśnienie pary, Mpa '
_ip3 = DoubleVar()  # 'Entalpia pary, kJ/kg: '

# Entalpia skroplin w XN5
_mp4 = DoubleVar()  # 'Strumień masy pary, t/h '
_Tp4 = DoubleVar()  # 'Temperatura pary, st. C '
_pp4 = DoubleVar()  # 'Ciśnienie pary, Mpa '
_ip4 = DoubleVar()  # 'Entalpia pary, kJ/kg: '

# Entalpia skroplin w XN4
_mp5 = DoubleVar()  # 'Strumień masy pary, t/h '
_Tp5 = DoubleVar()  # 'Temperatura pary, st. C '
_pp5 = DoubleVar()  # 'Ciśnienie pary, Mpa '
_ip5 = DoubleVar()  # 'Entalpia pary, kJ/kg: '

#
# _czasNap = IntVar()  # 'Czas napełniania zasobników: '
# _Vzas = DoubleVar()  # Pojemnośc jednego zasobnika
# _VzasMax = DoubleVar()  # Wymagana pojemność zasobnika dla pracy szczytowej
# _strWody = DoubleVar()  # Strumien masy wody zasialajecj zasobnnik
# canvas = Canvas()
# _dZas.set('')
# _hZas.set('')
# _ilZas.set('')
# _gestWody.set('')
# _czasNap.set('')
# _Vzas.set('')
# _VzasMax.set('')
# _strWody.set('')
# =============================Ramki=========================#
ramka0 = {
    "opis": "Wczytaj Dane ",
    "row": 1,
    "columne": 0

}

opcje = [
    "Wybierz opcje wczytania Entalpii :",
    "Wczytaj dane z pliku",
    "Wprowadz dane ",
    "Pobierz formularz"
]

listOfElements = {
    # 'strMasPary': {
    #     "ramka": 'ramka1',
    #     "zmiennaPola": _mwz,
    #     "opis": "Strumień masy pary, t/h: ",
    #     "row": 4,
    #     "columne": 2
    # },
    'tempPary': {
        "ramka": 'ramka1',
        "zmiennaPola": _Twz,
        "opis": "Temperatura pary, st. K:",
        "row": 6,
        "columne": 2,
        "flag": 1
    },
    'cisnPary': {
        "ramka": 'ramka1',
        "zmiennaPola": _pwz,
        "opis": "Ciśnienie pary, MPa:",
        "row": 8,
        "columne": 2,
        "flag": 1
    },
    'entalpiaPary': {
        "ramka": 'ramka1',
        "zmiennaPola": _iwz,
        "opis": "Entalpia pary, J/kg:",
        "row": 10,
        "columne": 2,
        "flag": 1
    }

}

# Entalpia wody zasilającej za pompą wody zasilającej
listOfElements2 = {
    # 'strMasPary': {
    #     "ramka": 'ramka2',
    #     "zmiennaPola": _mpz,
    #     "opis": "Strumień masy pary, t/h: ",
    #     "row": 16,
    #     "columne": 2
    # },
    'tempPary': {
        "ramka": 'ramka2',
        "zmiennaPola": _Tpz,
        "opis": "Temperatura pary, st. K:",
        "row": 18,
        "columne": 2,
        "flag": 1
    },
    'cisnPary': {
        "ramka": 'ramka2',
        "zmiennaPola": _ppz,
        "opis": "Ciśnienie pary, MPa:",
        "row": 20,
        "columne": 2,
        "flag": 1
    },
    'entalpiaPary': {
        "ramka": 'ramka2',
        "zmiennaPola": _ipz,
        "opis": "Entalpia pary, J/kg:",
        "row": 22,
        "columne": 2,
        "flag": 1
    }

}

# Entalpia skroplin w kondensatorze
listOfElements3 = {
    # 'strMasPary': {
    #     "ramka": 'ramka3',
    #     "zmiennaPola": _mpkond,
    #     "opis": "Strumień masy pary, t/h: ",
    #     "row": 26,
    #     "columne": 2
    # },
    'tempPary': {
        "ramka": 'ramka3',
        "zmiennaPola": _Tpkond,
        "opis": "Temperatura pary, st. K:",
        "row": 28,
        "columne": 2,
        "flag": 1
    },
    'cisnPary': {
        "ramka": 'ramka3',
        "zmiennaPola": _ppkond,
        "opis": "Ciśnienie pary, MPa:",
        "row": 30,
        "columne": 2,
        "flag": 1
    },
    'entalpiaPary': {
        "ramka": 'ramka3',
        "zmiennaPola": _ipkond,
        "opis": "Entalpia pary, J/kg:",
        "row": 32,
        "columne": 2,
        "flag": 1
    }

}
# Entalpia odsolin
listOfElements4 = {
    # 'strMasPary': {
    #     "ramka": 'ramka4',
    #     "zmiennaPola": _mods,
    #     "opis": "Strumień masy pary, t/h: ",
    #     "row": 36,
    #     "columne": 2
    # },
    'tempPary': {
        "ramka": 'ramka4',
        "zmiennaPola": _Tods,
        "opis": "Temperatura pary, st. K:",
        "row": 6,
        "columne": 2,
        "flag": 1
    },
    'cisnPary': {
        "ramka": 'ramka4',
        "zmiennaPola": _pods,
        "opis": "Ciśnienie pary, MPa:",
        "row": 8,
        "columne": 2,
        "flag": 1
    },
    'entalpiaPary': {
        "ramka": 'ramka4',
        "zmiennaPola": _iods,
        "opis": "Entalpia pary, J/kg:",
        "row": 10,
        "columne": 2,
        "flag": 1
    }

}
# Entalpia pary świeżej
listOfElements5 = {
    # 'strMasPary': {
    #     "ramka": 'ramka5',
    #     "zmiennaPola": _mSH5wyl,
    #     "opis": "Strumień masy pary, t/h: ",
    #     "row": 4,
    #     "columne": 3
    # },
    'tempPary': {
        "ramka": 'ramka5',
        "zmiennaPola": _TSH5wyl,
        "opis": "Temperatura pary, st. K:",
        "row": 18,
        "columne": 2,
        "flag": 1
    },
    'cisnPary': {
        "ramka": 'ramka5',
        "zmiennaPola": _pSH5wyl,
        "opis": "Ciśnienie pary, MPa:",
        "row": 20,
        "columne": 2,
        "flag": 1
    },
    'entalpiaPary': {
        "ramka": 'ramka5',
        "zmiennaPola": _iSH5wyl,
        "opis": "Entalpia pary, J/kg:",
        "row": 22,
        "columne": 2,
        "flag": 1
    }

}
# Entalpia pary na wylocie z wysokoprężnej części turbiny
listOfElements6 = {
    # 'strMasPary': {
    #     "ramka": 'ramka6',
    #     "zmiennaPola": _mRH1wlot,
    #     "opis": "Strumień masy pary, t/h: ",
    #     "row": 4,
    #     "columne": 4
    # },
    'tempPary': {
        "ramka": 'ramka6',
        "zmiennaPola": _TRH1wlot,
        "opis": "Temperatura pary, st. K:",
        "row": 28,
        "columne": 2,
        "flag": 1
    },
    'cisnPary': {
        "ramka": 'ramka6',
        "zmiennaPola": _pRH1wlot,
        "opis": "Ciśnienie pary, MPa:",
        "row": 30,
        "columne": 2,
        "flag": 1
    },
    'entalpiaPary': {
        "ramka": 'ramka6',
        "zmiennaPola": _iRH1wlot,
        "opis": "Entalpia pary, J/kg:",
        "row": 32,
        "columne": 2,
        "flag": 1
    }

}

# Entalpia pary wtórnie przegrzanej
listOfElements7 = {
    # 'strMasPary': {
    #     "ramka": 'ramka7',
    #     "zmiennaPola": _mRH2wyl,
    #     "opis": "Strumień masy pary, t/h: ",
    #     "row": 4,
    #     "columne": 5
    # },
    'tempPary': {
        "ramka": 'ramka7',
        "zmiennaPola": _TRH2wyl,
        "opis": "Temperatura pary, st. K:",
        "row": 6,
        "columne": 3,
        "flag": 1

    },
    'cisnPary': {
        "ramka": 'ramka7',
        "zmiennaPola": _pRH2wyl,
        "opis": "Ciśnienie pary, MPa:",
        "row": 8,
        "columne": 3,
        "flag": 1
    },
    'entalpiaPary': {
        "ramka": 'ramka7',
        "zmiennaPola": _iRH2wyl,
        "opis": "Entalpia pary, J/kg:",
        "row": 10,
        "columne": 3,
        "flag": 1
    }

}
# Entalpia skroplin w XW3
listOfElements8 = {
    # 'strMasPary': {
    #     "ramka": 'ramka8',
    #     "zmiennaPola": _mp1,
    #     "opis": "Strumień masy pary, t/h: ",
    #     "row": 4,
    #     "columne": 6
    # },
    'tempPary': {
        "ramka": 'ramka8',
        "zmiennaPola": _Tp1,
        "opis": "Temperatura pary, st. K:",
        "row": 18,
        "columne": 3,
        "flag": 1
    },
    'cisnPary': {
        "ramka": 'ramka8',
        "zmiennaPola": _pp1,
        "opis": "Ciśnienie pary, MPa:",
        "row": 20,
        "columne": 3,
        "flag": 1
    },
    'entalpiaPary': {
        "ramka": 'ramka8',
        "zmiennaPola": _ip1,
        "opis": "Entalpia pary, J/kg:",
        "row": 22,
        "columne": 3,
        "flag": 1
    }

}

# Entalpia skroplin w XW2
listOfElements9 = {
    # 'strMasPary': {
    #     "ramka": 'ramka9',
    #     "zmiennaPola": _mp2,
    #     "opis": "Strumień masy pary, t/h: ",
    #     "row": 4,
    #     "columne": 2
    # },
    'tempPary': {
        "ramka": 'ramka9',
        "zmiennaPola": _Tp2,
        "opis": "Temperatura pary, st. K:",
        "row": 28,
        "columne": 3,
        "flag": 1
    },
    'cisnPary': {
        "ramka": 'ramka9',
        "zmiennaPola": _pp2,
        "opis": "Ciśnienie pary, MPa:",
        "row": 30,
        "columne": 3,
        "flag": 1
    },
    'entalpiaPary': {
        "ramka": 'ramka9',
        "zmiennaPola": _ip2,
        "opis": "Entalpia pary, J/kg:",
        "row": 32,
        "columne": 3,
        "flag": 1
    }

}

# Entalpia skroplin w XW1
listOfElements10 = {
    # 'strMasPary': {
    #     "ramka": 'ramka10',
    #     "zmiennaPola": _mp3,
    #     "opis": "Strumień masy pary, t/h: ",
    #     "row": 4,
    #     "columne": 2
    # },
    'tempPary': {
        "ramka": 'ramka10',
        "zmiennaPola": _Tp3,
        "opis": "Temperatura pary, st. K:",
        "row": 6,
        "columne": 4,
        "flag": 1
    },
    'cisnPary': {
        "ramka": 'ramka10',
        "zmiennaPola": _pp3,
        "opis": "Ciśnienie pary, MPa:",
        "row": 8,
        "columne": 4,
        "flag": 1

    },
    'entalpiaPary': {
        "ramka": 'ramka10',
        "zmiennaPola": _ip3,
        "opis": "Entalpia pary, J/kg:",
        "row": 10,
        "columne": 4,
        "flag": 1
    }

}

# Entalpia skroplin w XN5
listOfElements11 = {
    # 'strMasPary': {
    #     "ramka": 'ramka11',
    #     "zmiennaPola": _mp4,
    #     "opis": "Strumień masy pary, t/h: ",
    #     "row": 4,
    #     "columne": 2
    # },
    'tempPary': {
        "ramka": 'ramka11',
        "zmiennaPola": _Tp4,
        "opis": "Temperatura pary, st. K:",
        "row": 18,
        "columne": 4,
        "flag": 1
    },
    'cisnPary': {
        "ramka": 'ramka11',
        "zmiennaPola": _pp4,
        "opis": "Ciśnienie pary, MPa:",
        "row": 20,
        "columne": 4,
        "flag": 1
    },
    'entalpiaPary': {
        "ramka": 'ramka11',
        "zmiennaPola": _ip4,
        "opis": "Entalpia pary, J/kg:",
        "row": 22,
        "columne": 4,
        "flag": 1
    }

}

# Entalpia skroplin w XN4
listOfElements12 = {
    # 'strMasPary': {
    #     "ramka": 'ramka12',
    #     "zmiennaPola": _mp5,
    #     "opis": "Strumień masy pary, t/h: ",
    #     "row": 4,
    #     "columne": 2
    # },
    'tempPary': {
        "ramka": 'ramka12',
        "zmiennaPola": _Tp5,
        "opis": "Temperatura pary, st. K:",
        "row": 28,
        "columne": 4,
        "flag": 1
    },
    'cisnPary': {
        "ramka": 'ramka12',
        "zmiennaPola": _pp5,
        "opis": "Ciśnienie pary, MPa:",
        "row": 30,
        "columne": 4,
        "flag": 1
    },
    'entalpiaPary': {
        "ramka": 'ramka12',
        "zmiennaPola": _ip5,
        "opis": "Entalpia pary, J/kg:",
        "row": 32,
        "columne": 4,
        "flag": 1
    }

}

listaRamek = {
    'ramka1': {
        # "tab": ,
        "opis": "Parametry wody zasilającej(przed kotłem) [wz] : ",
        "row": 4,
        "columne": 0,
        "dane": listOfElements
    },
    'ramka2': {
        # "tab": ,
        "opis": "Parametry wody zasilającej za pompą wody zasilającej [pz]",
        "row": 14,
        "columne": 0,
        "dane": listOfElements2
    },
    'ramka3': {
        # "tab": ,
        "opis": "Parametry skroplin w kondensatorze [kond]",
        "row": 24,
        "columne": 0,
        "dane": listOfElements3
    },
    'ramka4': {
        # "tab": ,
        "opis": "Parametry odsolin [ods]",
        "row": 4,
        "columne": 1,
        "dane": listOfElements4

    },
    'ramka5': {
        # "tab": ,
        "opis": "Parametry pary świeżej [SH5wyl]",
        "row": 14,
        "columne": 1,
        "dane": listOfElements5
    },

    'ramka6': {
        # "tab": ,
        "opis": "Parametry pary na wylocie z wysokoprężnej części turbiny [RH1wlot]",
        "row": 24,
        "columne": 1,
        "dane": listOfElements6
    },

    'ramka7': {
        # "tab": ,
        "opis": "PArametry pary wtórnie przegrzanej[RH2wyl]",
        "row": 4,
        "columne": 2,
        "dane": listOfElements7
    },
    'ramka8': {
        # "tab": ,
        "opis": "Parametry skroplin w XW3 [pI]",
        "row": 14,
        "columne": 2,
        "dane": listOfElements8
    },
    'ramka9': {
        # "tab": ,
        "opis": "Parametry skroplin w XW2 [pII]",
        "row": 24,
        "columne": 2,
        "dane": listOfElements9
    },
    'ramka10': {
        # "tab": ,
        "opis": "Parametry skroplin w XW1 [pIII]",
        "row": 4,
        "columne": 3,
        "dane": listOfElements10
    },
    'ramka11': {
        # "tab": ,
        "opis": "Parametry skroplin w XN5 [pIV]",
        "row": 14,
        "columne": 3,
        "dane": listOfElements11
    },
    'ramka12': {
        # "tab": ,
        "opis": "Parametry skroplin w XN4 [pV]",
        "row": 24,
        "columne": 3,
        "dane": listOfElements12
    }
}
