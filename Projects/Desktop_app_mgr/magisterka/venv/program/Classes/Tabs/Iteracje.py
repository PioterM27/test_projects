import tkinter as tk
from tkinter import ttk, Canvas
from tkinter import *
# import thermopy.iapws
import pyXSteam.XSteam
import program.Classes.Dane.DaneIteracje as dt
from program.Classes.HelperClass.EntryField import EntryField
from program.Classes.HelperClass.FrameCreate import FrameCreate
from program.Classes.Tabs.IteracjeNN import InteracjeNN
# from program.Classes.Dane.DaneIteracjeNN import
import program.Classes.Tabs.IteracjeNN as itNN
import program.Classes.Funkcje.FunkcjeIteracje as it
import program.Classes.HelperClass.DodawanieIteracji as dod
import program.Classes.Dane.DaneIteracjeNN as dtNN
import program.Classes.Tabs.IteracjeNN as dtNN
import program.Classes.Funkcje.FunkcjeIteracjeNN as fNN
import program.Classes.Dane.DaneObliczeniaPoIteracji as dtPo
import program.Classes.Tabs.ObliczeniaPoIteracji as oblIT


class Iteracje():

    def __init__(self, tab, obj,dObl):
        self.tab = tab
        self.obj = obj #dane iteracje
        self.dObl=dObl #obliczenia przed iteracja obiekty

    def getListOfEntryFieldAll(self, framex, daneLista, n):
        # print(self.obj)
        # newObj = dt.DaneIteracje(1)
        newObj = self.obj

        listA = newObj.listOfElements1(n)

        for var in listA:
            if (daneLista == listA[var]['ramka']):
                entry = EntryField(framex, listA[var]['zmiennaPola'], listA[var]["opis"],
                                   listA[var]["row"], listA[var]["columne"],
                                   listA[var]["flag"])
                entry.entryField()

    def getFrameCreateAll(self, n):
        # newData=dt.DaneIteracje(1)
        newData = self.obj
        newObj = newData.listaRamek1()
        for var in newObj:
            frame1 = FrameCreate(self.tab, newObj[var]['opis'], newObj[var]["row"],
                                 newObj[var]["columne"])
            frame2 = frame1.frameCreate()
            self.getListOfEntryFieldAll(frame2, var, n)

        return frame2

    def button(self):
        B = tk.Button(self.tab, text='Start', command=self.poczatekIteracji)
        B.grid(row=2, column=2)

    def button2(self, f2, itera, f1):
        funkcja = self.pobierz(f2, itera, f1)
        # B = tk.Button(self.tab, text='Start', command=lambda: funkcja)
        # B.grid(row=8, column=3)

    def dodawanieZakladki(self, n, ite):
        tabs = dod.DodawanieIteracji()
        name = "tab" + str(n)
        nazwa = "It " + str(ite)
        zakladka = tabs.buttonCommand(name, nazwa)
        return zakladka
    def dodawanieOstatniejZakladki(self, n, ite):
        tabs = dod.DodawanieIteracji()
        name = "tab" + str(n)
        nazwa = "Obliczenia końcowe"
        zakladka = tabs.buttonCommand(name, nazwa)
        return zakladka


    def poczatekIteracji(self):
        iteracja = 0
        wartosc = 0
        currentTab = 7
        ite = 1
        print("las")
        # f1=fNN.FunkcjeIteracjeNN(self.obj,1)
        f1 = fNN.FunkcjeIteracjeNN()

        # a1 = dt.DaneIteracje()

        # while ((iteracja < it._ilosc.get()) | (wartosc < it._expectValue.get())):
        # tab="tab"+ currentTab
        # print (tab)
        # a1 = dt.DaneIteracje(it._ilosc.get())
        while ((iteracja < it._ilosc.get()) | (wartosc < it._expectValue.get())):
            tab = self.dodawanieZakladki(currentTab, ite)
            iteracjaNN = Iteracje(tab, self.obj,self.dObl)
            iteracjaNN.getFrameCreateAll(iteracja)
            iteracjaNN.button2(self.obj, iteracja, f1)
            print("to jest iteracja" + str(iteracja))
            print("Drukuje dane")

            print(self.obj.tabIskXW3[ite].get())
            print(ite)
            # self.Iteruj(f1)
            f1.test223(self.obj, iteracja)
            currentTab += 1
            iteracja += 1
            wartosc += 1
            ite += 1

        if (iteracja == it._ilosc.get()):
            tab = self.dodawanieOstatniejZakladki(currentTab, ite)
            newDataIt = oblIT.ObliczeniaPoIteracji(tab, self.obj, iteracja, f1,self.dObl)
            newDataIt.getFrameCreateAll()
            print("jest tu czy nie")
            ## tu wywolac funkcje strumienia cipla

    def pobierz(self, obj, n, f1):
        # print((ty.tabIwz[3]).get())
        print(n)
        f1.mPs(self.obj, n)
        f1.obliczenieM_I_II_III(self.obj, n)
        f1.mieszanieZaKondenstorem(self.obj, n)
        f1.xn1_xn2(self.obj, n)
        f1.xn3(self.obj, n)
        f1.xn3zaPktMieszania(self.obj, n)
        f1.xn4(self.obj, n)
        f1.xn5(self.obj, n)
        f1.odgzowywacz(self.obj, n)
        f1.Ipz(self.obj, n)
        f1.iskXW1(self.obj, n)
        f1.mWz(self.obj, n)
        f1.xw2(self.obj, n)
        f1.xw3(self.obj, n)
