import tkinter as tk
from tkinter import ttk, Canvas
from tkinter import *
import cmath as math
# import thermopy.iapws
import pyXSteam.XSteam
import program.Classes.Dane.DaneEntalpia as en1
import program.Classes.Dane.DaneEntalpia2 as en2
import program.Classes.Dane.DaneStrumienieMasy as st
import program.Classes.Dane.DaneWejsciowe as dt

#Warunki początkowe
_ilosc=IntVar()
_expectValue=DoubleVar()

_iskzm = DoubleVar()  # mieszanie za kondensatorem
_iskxn2 = DoubleVar()  # xn1/xn2
_iskxn3 = DoubleVar()  # xn3
_iskxn3A = DoubleVar()  # xn3 za punktem mieszania
_iskxn4 = DoubleVar()  # xn4
_iskxn5 = DoubleVar()  # xn5
_iwododg = DoubleVar()  # odgazowywacz
_iskxw1 = DoubleVar()  # xw1
_qwododg = DoubleVar()
_ppp = DoubleVar()
_pzp = DoubleVar()
_delpz = DoubleVar()
_delipz = DoubleVar()
_ipz = DoubleVar()
_mwz = DoubleVar()
_iskxw2 = DoubleVar()
_iskxw3 = DoubleVar()
_mps = DoubleVar()


def mPs():
    mps = (en1._iwz.get() * st._mwz.get())
    _mps.set(round(mps), 2)


# Mieszanie za kondesnatorem
def mieszanieZaKondenstorem():
    iskzm = (st._mVII.get() * en2._ipVII.get())
    _iskzm.set(round(iskzm),2)


# XN1/XN2

def xn1_xn2():
    _iskxn2 = (st._mVII + st._mznp + dt._mzas)


# !!!!!!!!!! sprawdzic czy to ip5 to jest to samo co ipV
def xn3():
    _iskxn3 = (st._mVII + st._mznp + dt._mzas)


# !!!!!!!!!!!!!!!!!!!!!11 sprawdzić czy ip6 to ipVI
def xn3zaPktMieszania():
    _iskxn3A = (_iskxn3 * (st._mVII + st._mznp + dt._mzas) + en2._ip6 * (
            st._mVI + st._mV + st._mIV + st._mIII - st._modg)) / st._mVII + dt._mzas + st._mVI + st._mV + st._mIV + st._mIII - st._modg


# !!!!!!!!!!!!!!!!!!!!!11 sprawdzić czy ip4 to ipIV
def xn4():
    _iskxn4 = (en1._ip4 * (st._mIV + st._mIII - st._modg) + (en2._iV * st._mV) - en1._ip5 * (
            st._mV + st._mIV + st._mIII - st._modg)
               + _iskxn3A * (st._mV + st._mIV + st._mVI + st._mVII + st._mIII - st._modg + st._mznp + dt._mzas)) / (
                      st._mV + st._mIV + st._mVI + st._mVII + st._mIII - st._modg + st._mznp + dt._mzas)


def xn5():
    _iskxn5 = (en2._iIV * st._mIV)



def odgzowywacz():
    _iwododg = en1._ip2 * (st._mI + st._mII) + en2._iIII * st._modg + _iskxn5


# XW1

def deltaPz():
    _delpz = _pzp - _ppp


def deltaIpz():
    _delipz = _delpz / _qwododg


def Ipz():
    _ipz = _iwododg + _delipz


def iskXW1():
    _iskxw1 = (st._mV + st._mI + st._mIV + st._mVI + st._mII + st._mVII + st._mIII_ + st._mznp))


def mWz():
    _mwz = (st._mV + st._mI + st._mIV + st._mVI + st._mII + st._mVII + st._mIII_ + st._mznp)


def xw2():
    _iskxw2 = (st._mI * en1._ip1) - en1._ip2 * (st._mI + st._mII) + en2._iII * st._mII


def xw3():
    _iskxw3 = (en2._iI + st._mI) - st._mI * en1._ip1 + _iskxw2
