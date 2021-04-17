from tkinter import *
import tkinter as tk
# import thermopy.iapws
import pyXSteam.XSteam
import program.Classes.Dane.DaneObliczenia as dt
from program.Classes.HelperClass.EntryField import EntryField
from program.Classes.HelperClass.FrameCreate import FrameCreate
import program.Classes.Funkcje.Funkcje as ff
import program.Classes.Tabs.Iteracje  as itN
import program.Classes.Dane.DaneIteracje as dta


class Obliczenia():
    def __init__(self, tab):
        self.tab = tab
        self.newData = dt.DaneObliczenia(self.tab)

    def getListOfEntryFieldAll(self, framex, daneLista, newData):
        print("Obliczenia")

        for var in newData:
            if (daneLista == newData[var]['ramka']):
                entry = EntryField(framex, newData[var]['zmiennaPola'], newData[var]["opis"],
                                   newData[var]["row"], newData[var]["columne"],
                                   newData[var]["flag"])
                entry.entryField()
                if (newData[var]["ramka"] == "ramka1"):
                    varTopic = Label(framex, width=40, bd=2, relief="sunken", text="Warunki początkowe", font=("Helvetica", 8))
                    varTopic.grid(row=7, column=0, columnspan=10, pady=4)
                    B = tk.Button(framex, text='Oblicz', command=lambda: [self.buttonCommand()])  # bardzo ważne
                    B.grid(row=10, column=2)

    def getFrameCreateAll(self):

        # newData = dt.DaneObliczenia(self.tab)
        newObj2 = self.newData.listOfElements1()
        newObj = self.newData.listaRamek1()
        for var in newObj:
            frame1 = FrameCreate(self.tab, newObj[var]['opis'], newObj[var]["row"],
                                 newObj[var]["columne"])
            frame2 = frame1.frameCreate()
            self.getListOfEntryFieldAll(frame2, var, newObj2)

        return frame2

    def buttonCommand(self):

        ff.deltaPz()
        ff.deltaIpz()
        ff.cieploNiskopreznej()
        ff.cieploSredniporeznej()
        ff.cieploWysokopreznej()
        ff.sumaCiepla()
        a1 = dta.DaneIteracje()
        asa = itN.Iteracje(self.tab, a1,self.newData)
        asa.poczatekIteracji()
