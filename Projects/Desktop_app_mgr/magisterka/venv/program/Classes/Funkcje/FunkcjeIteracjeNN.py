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
import program.Classes.Funkcje.FunkcjeIteracje as fi
import program.Classes.Dane.DaneObliczeniaPoIteracji as poIt
# import numpy as np
import program.Classes.Dane.DaneIteracje as dtIt
import program.Classes.Funkcje.Funkcje as ff


class FunkcjeIteracjeNN:

    def __init__(self):
        pass
        # self.obj=obj
        # self.n=n

    def test223(self, obj, n):
        # obj.tabIwz[n]
        # obj.tabMps[n]
        # obj.tabMVII[n]

        print("wyswietl")
        print(en1._mpz.get())

        print("dziala albo nie")
        print(n)

        # obj.tabMps[n].set(200)
        # obj.tabIwz[n].set(400)

    def mPs(self, obj, n):
        print("losykosy")
        print(n)
        if (n == 0):
            tabMps = ((en1._iwz.get() * st._mwz.get()) - (en1._iods.get() * st._mods.get()) - (
                    st._mwt.get() * en1._iRH2wyl.get()) + (
                              st._mwt.get() * en1._iRH1wlot.get()) + (en1._ipz.get() * (
                    st._mwtrI.get() + st._mwtrIV.get() + st._mwtrV.get() + st._mwtrII.get() + st._mwtrIII.get())) + (
                              dt._wd.get() * dt._nk.get() * st._mpal.get())) / en1._iSH5wyl.get()
            print("asdasda")
            print(st._mwt.get())
            print(en1._iSH5wyl.get())
            print(tabMps)
            # obj.tabIwz[n].set(en1._iwz.get())
            print(en1._iwz.get())
            print(obj.tabIwz[0].get())
            obj.tabMps[n].set("{:.2f}".format(float(tabMps)))
            obj.tabMsp[n].set(st._msp.get())
            obj.tabMnp[n].set(st._mnp.get())
            obj.tabMznp[n].set(st._mznp.get())
            obj.tabMwt[n].set(st._mwt.get())
            obj.tabMI[n].set("{:.2f}".format(float(st._mI.get())))
            obj.tabMII[n].set("{:.2f}".format(float(st._mII.get())))
            obj.tabMIII[n].set("{:.2f}".format(float(st._mIII.get())))
            obj.tabMIV[n].set("{:.2f}".format(float(st._mIV.get())))
            obj.tabMV[n].set("{:.2f}".format(float(st._mV.get())))
            obj.tabMVI[n].set("{:.2f}".format(float(st._mVI.get())))
            obj.tabMVII[n].set("{:.2f}".format(float(st._mVII.get())))



        else:
            tabMps = ((obj.tabIwz[n - 1].get() * st._mwz.get()) - (en1._iods.get() * st._mods.get()) - (
                    st._mwt.get() * en1._iRH2wyl.get()) + (
                              st._mwt.get() * en1._iRH1wlot.get()) + (en1._ipz.get() * (
                    st._mwtrI.get() + st._mwtrIV.get() + st._mwtrV.get() + st._mwtrII.get() + st._mwtrIII.get())) + (
                              dt._wd.get() * dt._nk.get() * st._mpal.get())) / en1._iSH5wyl.get()
            obj.tabMps[n].set("{:.2f}".format(float(tabMps)))
            print("Tyyuitirtre " + str(obj.tabIwz[n - 1].get()))

        # Mieszanie za konde2snatorem

    def obliczenieM_I_II_III(self, obj, n):
        if (n == 0):
            pass
        #     obj.tabMI[n].set("{:.2f}".format(float(st._mI.get())))
        #     obj.tabMII[n].set("{:.2f}".format(float(st._mII.get())))
        #     obj.tabMIII[n].set("{:.2f}".format(float(st._mIII.get())))
        #     obj.tabMIV[n].set("{:.2f}".format(float(st._mIV.get())))
        #     obj.tabMV[n].set("{:.2f}".format(float(st._mV.get())))
        #     obj.tabMVI[n].set("{:.2f}".format(float(st._mVI.get())))
        #     obj.tabMVII[n].set("{:.2f}".format(float(st._mVII.get())))
        # obj.tabMsp[n].set(st._msp.get())
        # obj.tabMnp[n].set(st._mnp.get())
        # obj.tabMznp[n].set(st._mznp.get())

        else:
            mI = 0.047 * obj.tabMps[n].get()
            mII = 0.074 * obj.tabMps[n].get()
            mIII = 0.044 * obj.tabMps[n].get()
            mIV = 0.011 * obj.tabMps[n].get()
            mV = 0.025 * obj.tabMps[n].get()
            mVI = 0.057 * obj.tabMps[n].get()
            mVII = 0.011 * obj.tabMps[n].get()

            obj.tabMI[n].set("{:.2f}".format(float(mI)))
            obj.tabMII[n].set("{:.2f}".format(float(mII)))
            obj.tabMIII[n].set("{:.2f}".format(float(mIII)))
            obj.tabMIV[n].set("{:.2f}".format(float(mIV)))
            obj.tabMV[n].set("{:.2f}".format(float(mV)))
            obj.tabMVI[n].set("{:.2f}".format(float(mVI)))
            obj.tabMVII[n].set("{:.2f}".format(float(mVII)))

            mwt = obj.tabMps[n].get() - obj.tabMI[n].get() - obj.tabMII[n].get()
            msp = obj.tabMps[n].get() - obj.tabMI[n].get() - obj.tabMII[n].get() + (st._mwtrIV.get() + st._mwtrV.get())
            mnp = msp - obj.tabMIII[n].get() - obj.tabMIV[n].get() - obj.tabMV[n].get() - obj.tabMVI[n].get()
            mznp = mnp - obj.tabMVII[n].get()

            obj.tabMwt[n].set("{:.2f}".format(float(mwt)))
            obj.tabMsp[n].set("{:.2f}".format(float(msp)))
            obj.tabMnp[n].set("{:.2f}".format(float(mnp)))
            obj.tabMznp[n].set("{:.2f}".format(float(mznp)))

    def mieszanieZaKondenstorem(self, obj, n):

        tabIskzm = ((obj.tabMVII[n].get() * en2._ipVII.get()) + (obj.tabMznp[n].get() * en1._ipkond.get())) / (
                obj.tabMVII[n].get() + obj.tabMznp[n].get())

        obj.tabIskzm[n].set("{:.2f}".format(float(tabIskzm)))

        # XN1/XN2

    def xn1_xn2(self, obj, n):
        print("Wypisz n")
        print(obj.tabIskzm[n].get())
        tabIskXN2 = (obj.tabIskzm[n].get() * (obj.tabMVII[n].get() + obj.tabMznp[n].get() + dt._mzas.get()) + \
                     obj.tabMVII[n].get() * (en2._iVII.get() - en2._ipVII.get())) / (
                            obj.tabMVII[n].get() + obj.tabMznp[n].get() + dt._mzas.get())

        obj.tabIskXN2[n].set("{:.2f}".format(float(tabIskXN2)))
        # print("Nasze Wartosci")
        # print(obj.tabIskzm[n].get())
        # print(obj.tabMVII[n].get())
        # print(obj.tabMznp[n].get())
        # print(dt._mzas.get())

        # !!!!!!!!!! sprawdzic czy to ip5 to jest to samo co ipV

    def xn3(self, obj, n):  # !!!!tu może być błąd z ipVII bo może być ipVI

        tabIskXN3 = (obj.tabIskXN2[n].get() * (
                obj.tabMVII[n].get() + obj.tabMznp[n].get() + dt._mzas.get()) + en1._ip5.get() * (
                             obj.tabMV[n].get() + obj.tabMIV[n].get() + obj.tabMIII[n].get() - st._modg.get()) + (
                             obj.tabMVI[n].get() * en2._iVI.get()) - (en2._ip6.get() * (
                obj.tabMVI[n].get() + obj.tabMV[n].get() + obj.tabMIV[n].get() + obj.tabMIII[
            n].get() - st._modg.get()))) / \
                    (obj.tabMVII[n].get() + dt._mzas.get() + obj.tabMznp[n].get())
        obj.tabIskXN3[n].set("{:.2f}".format(float(tabIskXN3)))
        # !!!!!!!!!!!!!!!!!!!!!11 sprawdzić czy ip6 to ipVI

    def xn3zaPktMieszania(self, obj, n):

        tabIskXN3A = (obj.tabIskXN3[n].get() * (
                obj.tabMVII[n].get() + obj.tabMznp[n].get() + dt._mzas.get()) + en2._ip6.get() * (
                              obj.tabMVI[n].get() + obj.tabMV[n].get() + obj.tabMIV[n].get() + obj.tabMIII[
                          n].get() - st._modg.get())) / \
                     (obj.tabMVII[n].get() + dt._mzas.get() + obj.tabMznp[n].get() + obj.tabMVI[n].get() + \
                      obj.tabMV[n].get() + obj.tabMIV[n].get() + obj.tabMIII[n].get() - st._modg.get())

        obj.tabIskXN3A[n].set("{:.2f}".format(float(tabIskXN3A)))

        # !!!!!!!!!!!!!!!!!!!!!11 sprawdzić czy ip4 to ipIV

    def xn4(self, obj, n):
        tabIskXN4 = (en1._ip4.get() * (obj.tabMIV[n].get() + obj.tabMIII[n].get() - st._modg.get()) + (
                en2._iV.get() * obj.tabMV[n].get()) - en1._ip5.get() * (
                             obj.tabMV[n].get() + obj.tabMIV[n].get() + obj.tabMIII[n].get() - st._modg.get())
                     + obj.tabIskXN3A[n].get() * (
                             obj.tabMV[n].get() + obj.tabMIV[n].get() + obj.tabMVI[n].get() + obj.tabMVII[n].get() +
                             obj.tabMIII[n].get() - st._modg.get() + obj.tabMznp[n].get() + dt._mzas.get())) / (
                            obj.tabMV[n].get() + obj.tabMIV[n].get() + obj.tabMVI[n].get() + obj.tabMVII[n].get() +
                            obj.tabMIII[n].get() - st._modg.get() + obj.tabMznp[n].get() + dt._mzas.get())
        obj.tabIskXN4[n].set("{:.2f}".format(float(tabIskXN4)))

    def xn5(self, obj, n):
        tabIskXN5 = ((en2._iIV.get() * obj.tabMIV[n].get()) - en1._ip4.get() * (
                obj.tabMIV[n].get() + obj.tabMIII[n].get() - st._modg.get()) + obj.tabIskXN4[n].get() * (
                             obj.tabMV[n].get() + obj.tabMIV[n].get() + obj.tabMVI[n].get() + obj.tabMVII[n].get() +
                             obj.tabMIII[n].get() - st._modg.get() + obj.tabMznp[n].get() + dt._mzas.get())
                     + en1._ip3.get() * (obj.tabMIII[n].get() - st._modg.get())) / (
                            obj.tabMV[n].get() + obj.tabMIV[n].get() + obj.tabMVI[n].get() + obj.tabMVII[n].get() +
                            obj.tabMIII[n].get() - st._modg.get() + obj.tabMznp[n].get() + dt._mzas.get())
        obj.tabIskXN5[n].set("{:.2f}".format(float(tabIskXN5)))

    def odgzowywacz(self, obj, n):
        tabIwodODG = (en1._ip2.get() * (obj.tabMI[n].get() + obj.tabMII[n].get()) + en2._iIII.get() * st._modg.get() + \
                      obj.tabIskXN5[n].get() * (
                              obj.tabMV[n].get() + obj.tabMIV[n].get() + obj.tabMVI[n].get() + obj.tabMVII[n].get() +
                              obj.tabMIII[n].get() - st._modg.get() + obj.tabMznp[n].get() + dt._mzas.get())) / \
                     (obj.tabMV[n].get() + obj.tabMI[n].get() + obj.tabMIV[n].get() + obj.tabMVI[n].get() + obj.tabMII[
                         n].get() +
                      obj.tabMVII[n].get() + obj.tabMIII[n].get() +
                      obj.tabMznp[n].get() + dt._mzas.get())
        obj.tabIwodODG[n].set("{:.2f}".format(float(tabIwodODG)))

        # XW1
        # def

    def deltaPz():
        delpz = fi._pzp.get() - fi._ppp.get()

        fi._delpz.set(("{:.2f}".format(float(delpz))))

    def deltaIpz():
        delipz = fi._delpz / fi._qwododg
        fi._delipz.set("{:.2f}".format(float(delipz)))

    def Ipz(self, obj, n):
        tabIpz = obj.tabIwodODG[n].get() + fi._delipz.get()
        obj.tabIpz[n].set("{:.2f}".format(float(tabIpz)))

    def iskXW1(self, obj, n):
        tabIskXW1 = ((obj.tabIpz[n].get() * (
                obj.tabMV[n].get() + obj.tabMI[n].get() + obj.tabMIV[n].get() + obj.tabMVI[n].get() + obj.tabMII[
            n].get() + obj.tabMVII[
                    n].get() + obj.tabMIII[n].get() + obj.tabMznp[n].get())) + (
                             en2._iIII.get() * (obj.tabMIII[n].get() - st._modg.get())) - (
                             en1._ip3.get() * (obj.tabMIII[n].get() - st._modg.get()))) / (
                            obj.tabMV[n].get() + obj.tabMI[n].get() + obj.tabMIV[n].get() + obj.tabMVI[n].get() +
                            obj.tabMII[n].get() +
                            obj.tabMVII[n].get() + obj.tabMIII[n].get() +
                            obj.tabMznp[n].get())
        obj.tabIskXW1[n].set("{:.2f}".format(float(tabIskXW1)))

    def mWz(self, obj, n):
        tabMwz = (obj.tabMV[n].get() + obj.tabMI[n].get() + obj.tabMIV[n].get() + obj.tabMVI[n].get() + obj.tabMII[
            n].get() + obj.tabMVII[n].get() + obj.tabMIII[n].get() + obj.tabMznp[n].get())
        obj.tabMwz[n].set("{:.2f}".format(float(tabMwz)))

    def xw2(self, obj, n):
        tabIskXW2 = ((obj.tabMI[n].get() * en1._ip1.get()) - en1._ip2.get() * (
                obj.tabMI[n].get() + obj.tabMII[n].get()) + en2._iII.get() * obj.tabMII[n].get() + (
                             obj.tabIskXW1[n].get() * (
                             obj.tabMV[n].get() + obj.tabMI[n].get() + obj.tabMIV[n].get() + obj.tabMVI[n].get() +
                             obj.tabMII[n].get() +
                             obj.tabMVII[n].get() + obj.tabMIII[n].get() + obj.tabMznp[n].get()))) / (
                            obj.tabMV[n].get() + obj.tabMI[n].get() + obj.tabMIV[n].get() + obj.tabMVI[n].get() +
                            obj.tabMII[n].get() +
                            obj.tabMVII[n].get() + obj.tabMIII[n].get() +
                            obj.tabMznp[n].get())
        obj.tabIskXW2[n].set("{:.2f}".format(float(tabIskXW2)))

    def xw3(self, obj, n):
        tabIskXW3 = ((en2._iI.get() * obj.tabMI[n].get()) - (obj.tabMI[n].get() * en1._ip1.get()) + obj.tabIskXW2[
            n].get() * (
                             obj.tabMV[n].get() + obj.tabMI[n].get() + obj.tabMIV[n].get() + obj.tabMVI[n].get() +
                             obj.tabMII[n].get() + obj.tabMVII[
                                 n].get() + obj.tabMIII[n].get() + obj.tabMznp[n].get())) / (
                            obj.tabMV[n].get() + obj.tabMI[n].get() + obj.tabMIV[n].get() + obj.tabMVI[n].get() +
                            obj.tabMII[n].get() +
                            obj.tabMVII[n].get() + obj.tabMIII[n].get() +
                            obj.tabMznp[n].get())
        if (n == 0):
            obj.tabIwz[n].set("{:.2f}".format(float(tabIskXW3)))
            obj.tabIskXW3[n].set("{:.2f}".format(float(tabIskXW3)))
        else:
            obj.tabIwz[n].set("{:.2f}".format(float(tabIskXW3)))
            obj.tabIskXW3[n].set("{:.2f}".format(float(tabIskXW3)))

    ## Te wzory nie maja sprawności dlaczego ??
    def cieploWysokopreznejPoObl(self, obj, n):
        qwp = (obj.tabMps[n - 1].get() * (en1._iSH5wyl.get() - en2._iI.get()) + (
                obj.tabMps[n - 1].get() - obj.tabMI[n - 1].get()) * (
                       en2._iI.get() - en2._iII.get()))
        ff._qwp2.set(qwp)
        print("QWP" + str(qwp))
        print(n)
        print(obj.tabMps[n].get())
        print(en1._iSH5wyl.get())

    def cieploSredniporeznejPoObl(self, obj, n):
        qsp = ((
                obj.tabMsp[n - 1].get() * (en2._isp.get() - en2._iIII.get()) + (
                obj.tabMsp[n - 1].get() - obj.tabMIII[n - 1].get()) * (
                        en2._iIII.get() - en2._iIV.get()) + (
                        obj.tabMsp[n - 1].get() - obj.tabMIII[n - 1].get() - obj.tabMIV[n - 1].get()) *
                (en2._iIV.get() - en2._iV.get()) + (
                        obj.tabMsp[n - 1].get() - obj.tabMIII[n - 1].get() - obj.tabMIV[n - 1].get() - obj.tabMV[
                    n - 1].get()) * (
                        en2._iV.get() - en2._iVI.get())))
        ff._qsp2.set(qsp)

    def cieploNiskopreznejPoObl(self, obj, n):
        print("Jestem w tej funkcji")
        qnp = (obj.tabMnp[n - 1].get() * (en2._inp.get() - en2._iVII.get()) + (
                obj.tabMnp[n - 1].get() - obj.tabMVII[n - 1].get()) * (
                       en2._iVII.get() - en2._iznp.get()))
        ff._qnp2.set("{:.2f}".format(float(qnp)))

    def sumaCieplaPoObl(self, obj, n):
        qsum = ff._qwp2.get() + ff._qsp2.get() + ff._qnp2.get()
        ff._qsum2.set("{:.2f}".format(float(qsum)))

    def qProcentowe(self, obj, n):
        qproc = (100*ff._qsum2.get())/obj._q.get()
        obj._qProc.set("{:.2f}".format(float(qproc)))

    def spadekMocy(self,obj,n):
        spadek=100-obj._qProc.get()
        obj._spadekMocy.set("{:.2f}".format(float(spadek)))
