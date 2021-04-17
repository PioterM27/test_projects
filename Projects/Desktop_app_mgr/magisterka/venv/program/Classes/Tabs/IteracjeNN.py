import tkinter as tk
from tkinter import ttk, Canvas
from tkinter import *
# import thermopy.iapws
import pyXSteam.XSteam
# import program.Classes.Dane.DaneIteracje as dt
from program.Classes.HelperClass.EntryField import EntryField
from program.Classes.HelperClass.FrameCreate import FrameCreate
import program.Classes.Dane.DaneEntalpia as en1
import program.Classes.Dane.DaneEntalpia2 as en2
import program.Classes.Dane.DaneStrumienieMasy as st
import program.Classes.Dane.DaneWejsciowe as dt
import program.Classes.Dane.DaneEntalpia as d1
import program.Classes.Dane.DaneEntalpia2 as d2
import program.Classes.Dane.DaneStrumienieMasy as st
import program.Classes.Funkcje.FunkcjeIteracje as it
import program.Classes.Funkcje.FunkcjeIteracjeNN as itNN
import program.Classes.HelperClass.DodawanieIteracji as dod
import program.Classes.Dane.DaneIteracjeNN as dt
# import numpy as np


# Klasa do obliczeń
class InteracjeNN():

    def __init__(self, tab, itNbr):
        self.tab = tab
        self.itNbr = itNbr

    def getListOfEntryFieldAll(self, framex, daneLista):

        for var in dt.listOfElements:
            if (daneLista == dt.listOfElements[var]['ramka']):
                entry = EntryField(framex, dt.listOfElements[var]['zmiennaPola'],
                                   dt.listOfElements[var]["opis"],
                                   dt.listOfElements[var]["row"], dt.listOfElements[var]["columne"],
                                   dt.listOfElements[var]["flag"])
                entry.entryField()

    def getFrameCreateAll(self):

        for var in dt.listaRamek:
            frame1 = FrameCreate(self.tab, dt.listaRamek[var]['opis'], dt.listaRamek[var]["row"],
                                 dt.listaRamek[var]["columne"])
            frame2 = frame1.frameCreate()
            self.getListOfEntryFieldAll(frame2, var)

        return frame2
