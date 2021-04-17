import tkinter as tk
from tkinter import ttk, Canvas
from tkinter import *
import cmath
# import Tkinter
# import tkMessageBox
import tkinter.filedialog


from program.Classes.HelperClass.EntryField import EntryField
from program.Classes.HelperClass.FrameCreate import FrameCreate
import program.Classes.ExcelOpenFile.ReadDataExcel as rE
from program.Classes.Bulider.Builder import Builder
from functools import partial
import program.Classes.Dane.DaneWejsciowe as dw
import program.Classes.Dane.DaneEntalpia as dt
import program.Classes.ExcelOpenFile.FileDialog as flD


class Dane():

    def __init__(self, tab):
        self.tab = tab

    def getFrameCreate(self):
        frame1 = FrameCreate(self.tab, dw.ramka1['opis'], dw.ramka1.get("row"), dw.ramka1.get("columne"))
        frame2 = frame1.frameCreate()
        return frame2

    def getFrameCreateSecond(self):
        frame3 = FrameCreate(self.tab, dw.ramka2['opis'], dw.ramka2.get("row"), dw.ramka2.get("columne"))
        frame4 = frame3.frameCreate()

        return frame4

    def getListOfEntryField(self, framex):
        B = tk.Button(framex, text='Oblicz', command=lambda: [self.buttonCommand()])  # bardzo ważne
        B.grid(row=26, column=2)
        for var in dw.listOfElements:
            entry = EntryField(framex, dw.listOfElements[var]['zmiennaPola'], dw.listOfElements[var]["opis"],
                               dw.listOfElements[var]["row"], dw.listOfElements[var]["columne"],dw.listOfElements[var]["flag"])
            entryUnit = EntryField(framex, dw.listOfElements[var]['units'], dw.listOfElements[var]["opis"],
                               dw.listOfElements[var]["row"], dw.listOfElements[var]["columne"]+1,dw.listOfElements[var]["flag"])
            entry.entryField()
            entryUnit.entryUnitsField(dw.listOfElements[var]['units'],dw.listOfElements[var]['zmiennaPola'])

    def getListOfEntryFieldSecond(self, framex):
        for var in dw.listOfElements:
            entry = EntryField(framex, dw.listOfElements[var]['zmiennaPola'], dw.listOfElements[var]["opis"],
                               dw.listOfElements[var]["row"], dw.listOfElements[var]["columne"])
            entry.entryField()

    def pojemnoscZasobnika(self):
        poj_Vz = cmath.pi * ((dw._dZas.get() / 2) ** 2) * dw._hZas.get()
        print("dane podstawowe")
        print(cmath.pi)
        print(dw._dZas.get() / 2)
        print((dw._dZas.get() / 2) ** 2)
        print(dw._hZas.get())


        # poj_Vz = 3.14 * ((1.5) ** 2) * 25.5
        dw._Vzas.set("{:.2f}".format(float(poj_Vz)))
        print(poj_Vz)
        return poj_Vz

    def buttonCommand(self):
        zw = self.pojemnoscZasobnika()
        zw2 = self.wymPojZas(zw)
        self.strMasPar(zw2)

    def wymPojZas(self, _Vz):
        maxPoj = (_Vz) * dw._ilZas.get()
        dw._VzasMax.set("{:.2f}".format(float(maxPoj)))
        print(maxPoj)
        return maxPoj

    def strMasPar(self, _Vzas):
        _mzas = (_Vzas * dw._gestWody.get()) / (dw._czasNap.get())
        dw._strWody.set("{:.2f}".format(float(_mzas)))
        return _mzas

    def createListboxField(self):
        frameListBox = FrameCreate(self.tab, dt.ramka0['opis'], dt.ramka0.get("row"), dt.ramka0.get("columne"))
        ff = frameListBox.frameCreate()
        variable = StringVar(frameListBox)
        variable.set(dt.opcje[2])
        w = OptionMenu(ff, variable, *dt.opcje)
        w.grid(column=2)
        variable.trace('w', partial(self.stan, widget=variable))


    def stan(self,*args,widget=None):
        print(widget.get())
        print('asa')
        if(widget.get()=='Wczytaj dane z pliku'):
         file=flD.FileDialog()
         name=file.callback()
         ase = rE.ReadDataExcel(name)
         ase.wypelnijDaneExclem()
        elif(widget.get()=='Pobierz formularz'):
            file=flD.FileDialog()
            name=file.callback2()