import tkinter as tk
from tkinter import ttk, Canvas
from tkinter import *
# import thermopy.iapws
import pyXSteam.XSteam
import program.Classes.Dane.DaneStrumienieMasy as dt
from program.Classes.HelperClass.EntryField import EntryField
from program.Classes.HelperClass.FrameCreate import FrameCreate
import program.Classes.Funkcje.Funkcje as ff
import program.Classes.Funkcje.FunkcjeIteracjeNN as ffN
import program.Classes.Tabs.Iteracje  as itN
import program.Classes.Dane.DaneIteracje as dta


# from thermopy.iapws import *
from pyXSteam.XSteam import XSteam


class Strumienie():
    def __init__(self, tab):
        self.tab = tab

    # def getFrameCreate(self):
    #     frame1 = FrameCreate(self.tab,dt.ramka1['opis'], dt.ramka1.get("row"), dt.ramka1.get("columne"))
    #     frame2 = frame1.frameCreate()
    #     return frame2
    #
    # def getListOfEntryField(self, framex):
    #     B = tk.Button(framex, text='Oblicz', command=lambda: [self.buttonCommand()])  # bardzo ważne
    #     B.grid(row=20, column=2)
    #     for var in dt.listOfElements:
    #         entry = EntryField(framex, dt.listOfElements[var]['zmiennaPola'], dt.listOfElements[var]["opis"],
    #                            dt.listOfElements[var]["row"], dt.listOfElements[var]["columne"])
    #         entry.entryField()

    ##############################################################################################################

    def getListOfEntryFieldAll(self, framex, daneLista):

        for var in dt.listOfElements:
            if (daneLista == dt.listOfElements[var]['ramka']):
                entry = EntryField(framex, dt.listOfElements[var]['zmiennaPola'], dt.listOfElements[var]["opis"],
                                   dt.listOfElements[var]["row"], dt.listOfElements[var]["columne"],
                                   dt.listOfElements[var]["flag"])
                entry.entryField()
                if (dt.listOfElements[var]["ramka"] == "ramka3"):
                    B = tk.Button(framex, text='Oblicz', command=lambda: [self.buttonCommand()])  # bardzo ważne
                    B.grid(row=26, column=3)

    def getFrameCreateAll(self):
        for var in dt.listaRamek:
            frame1 = FrameCreate(self.tab, dt.listaRamek[var]['opis'], dt.listaRamek[var]["row"],
                                 dt.listaRamek[var]["columne"])
            frame2 = frame1.frameCreate()
            self.getListOfEntryFieldAll(frame2, var)

        return frame2

    def buttonCommand(self):
        ff.strumienMasyPary()
        ff.strumienMasyParyWtPrzeg()
        ff.strumienMasyParyNaWlNisk()
        ff.strumienMasyParyNaWylNisk()
        ff.strumienMasyPaliwa()
        # ff.deltaPz()
        # ff.deltaIpz()
        #
        #
        # a1=dta.DaneIteracje()
        # asa=itN.Iteracje(self.tab,a1)
        # asa.poczatekIteracji()


