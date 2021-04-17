import tkinter as tk
from tkinter import ttk, Canvas
from tkinter import *
import cmath as math
# import thermopy.iapws
import pyXSteam.XSteam
import program.Classes.Dane.DaneEntalpia as en1
import program.Classes.Dane.DaneEntalpia2 as en2
import program.Classes.Dane.DaneStrumienieMasy as st
import program.Classes.Dane.DaneObliczenia as oblD
import program.Classes.Dane.DaneWejsciowe as dt
import program.Classes.Funkcje.Funkcje as ff
import program.Classes.Funkcje.FunkcjeIteracjeNN as ffN
import program.Classes.Funkcje.FunkcjeIteracje as fi

# Dane
# Strumień masy paliwa
_mpal = DoubleVar()  # 'Strumień masy pary, t/h '
_qwp = DoubleVar()  # Ciepło wysokoprężnej
_qsp = DoubleVar()  # Ciepło średnioprężnej
_qnp = DoubleVar()  # Ciepło niskoprężnej
_qsum = DoubleVar()
_qwp2 = DoubleVar()  # Ciepło wysokoprężnej obliczenia koncowe po iteracjach
_qsp2 = DoubleVar()  # Ciepło średnioprężnej obliczenia koncowe po iteracjach
_qnp2 = DoubleVar()  # Ciepło niskoprężnej obliczenia koncowe po iteracjach
_qsum2 = DoubleVar()  # obliczenia koncowe po iteracjach


# Obliczenie strumienia masy paliwa

# def wymPojZas(self, _Vz):
#     maxPoj = (_Vz) * dw._ilZas.get()
#     dw._VzasMax.set(maxPoj)
#     print(maxPoj)
#     return maxPoj


# Strumień masy pary na wylocie z wysokoprężnej części turbiny
def strumienMasyPary():
    mwt = st._mps.get() - st._mI.get() - st._mII.get()
    st._mwt.set("{:.2f}".format(float(mwt)))


# Strumień masy pary wtórnie przegrzanej
def strumienMasyParyWtPrzeg():
    msp = st._mps.get() - st._mI.get() - st._mII.get() + (st._mwtrIV.get() + st._mwtrV.get())
    st._msp.set("{:.2f}".format(float(msp)))


# Strumień masy pary na wlocie do niskoprężnej części turbiny
def strumienMasyParyNaWlNisk():
    mnp = st._msp.get() - st._mIII.get() - st._mIV.get() - st._mV.get() - st._mVI.get()
    st._mnp.set("{:.2f}".format(float(mnp)))


# Strumień masy pary na wylocie z niskoprężnej części turbiny
def strumienMasyParyNaWylNisk():
    mznp = st._mnp.get() - st._mVII.get()
    st._mznp.set("{:.2f}".format(float(mznp)))


def strumienMasyPaliwa():
    mpal = -(((en1._iwz.get() * st._mwz.get()) - (en1._iods.get() * st._mods.get()) - (
            st._mps.get() * en1._iSH5wyl.get()) - (st._mwt.get() * en1._iRH2wyl.get()) + (
                      st._mwt.get() * en1._iRH1wlot.get())) + \
             (en1._ipz.get()
              * (st._mwtrI.get() + st._mwtrIV.get() + st._mwtrV.get() + st._mwtrII.get() + st._mwtrIII.get()))) / (
                       dt._wd.get() * dt._nk.get())

    st._mpal.set("{:.2f}".format(float(mpal)))


def cieploWysokopreznej():
    qwp = dt._nwp.get() * (st._mps.get() * (en1._iSH5wyl.get() - en2._iI.get()) + (st._mps.get() - st._mI.get()) * (
                en2._iI.get() - en2._iII.get()))
    _qwp.set(qwp)


def cieploSredniporeznej():
    qsp = dt._nsp.get() * ((st._msp.get() * (en2._isp.get() - en2._iIII.get()) + (st._msp.get() - st._mIII.get()) * (
                en2._iIII.get() - en2._iIV.get()) + (
                                    st._msp.get() - st._mIII.get() - st._mIV.get()) *
                            (en2._iIV.get() - en2._iV.get()) + (
                                        st._msp.get() - st._mIII.get() - st._mIV.get() - st._mV.get()) * (
                                        en2._iV.get() - en2._iVI.get())))
    _qsp.set(qsp)


def cieploNiskopreznej():
    qnp = dt._nnp.get() * (st._mnp.get() * (en2._inp.get() - en2._iVII.get()) + (st._mnp.get() - st._mVII.get()) * (
                en2._iVII.get() - en2._iznp.get()))
    _qnp.set(qnp)


def sumaCiepla():
    qsum = _qwp.get() + _qsp.get() + _qnp.get()
    _qsum.set(qsum)


def deltaPz():
    delpz = fi._pzp.get() - fi._ppp.get()

    fi._delpz.set(delpz)


def deltaIpz():
    delipz = fi._delpz.get() / fi._qwododg.get()
    fi._delipz.set(delipz)
