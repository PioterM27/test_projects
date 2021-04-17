from tkinter import *
import tkinter as tk
# import thermopy.iapws
import pyXSteam.XSteam
import program.Classes.Dane.DaneObliczeniaPoIteracji as dt
from program.Classes.HelperClass.EntryField import EntryField
from program.Classes.HelperClass.FrameCreate import FrameCreate
import program.Classes.Funkcje.Funkcje as ff
import program.Classes.Tabs.Iteracje  as itN
import program.Classes.Dane.DaneIteracje as dta
import program.Classes.ExcelOpenFile.WriteDataExcel as wEx


class ObliczeniaPoIteracji:

    def __init__(self, tab,obj,nrIt,f1,dObl):
        self.tab = tab
        self.obj=obj #objekt z danymi  iteracje
        self.nrIt=nrIt #ostatni element iteracji
        self.f1=f1 # obiekt z tablicami z danmyimi iteracjami
        self.newData=dt.DaneObliczeniaPoIteracji(tab,obj)
        self.dObl=dObl #dane obliczenia przed iteracja
        self.excelW=wEx.WriteDataExcel(self.obj,self.nrIt,self.f1,self.newData,self.dObl)


    # newData = dt.DaneObliczeniaPoIteracji()

    def getListOfEntryFieldAll(self, framex, daneLista, newData):
        print("Obliczenia")

        for var in newData:
            if (daneLista == newData[var]['ramka']):
                entry = EntryField(framex, newData[var]['zmiennaPola'], newData[var]["opis"],
                                   newData[var]["row"], newData[var]["columne"],
                                   newData[var]["flag"])
                entry.entryField()
                # if (newData[var]["ramka"] == "ramka5"):
                #     print("pelemele")
                #     B = tk.Button(framex, text='Oblicz', command=lambda: [self.buttonCommand()])  # bardzo ważne
                #     B.grid(row=7, column=2)

    def getFrameCreateAll(self):

        # newData = dt.DaneObliczeniaPoIteracji(self.tab,self.obj)
        newObj2 = self.newData.listOfElements1()
        newObj = self.newData.listaRamek1()
        for var in newObj:
            frame1 = FrameCreate(self.tab, newObj[var]['opis'], newObj[var]["row"],
                                 newObj[var]["columne"])
            frame2 = frame1.frameCreate()
            self.getListOfEntryFieldAll(frame2, var, newObj2)
            if (newObj[var]["opis"] == "Akcje  :"):
                B = tk.Button(frame2, text='Oblicz', command=lambda: [self.buttonCommand(),self.switchAkcjeButton(B1)])  # bardzo ważne
                B.grid(row=7, column=4)
                B1 = tk.Button(frame2, text='Generuj dokument',state=tk.DISABLED, command=lambda: [self.generujDokumentObl()])  # bardzo ważne
                B1.grid(row=10, column=4)

        return frame2

    def buttonCommand(self):

        ff.deltaPz()
        ff.deltaIpz()
        self.f1.cieploWysokopreznejPoObl(self.obj,self.nrIt)
        self.f1.cieploSredniporeznejPoObl(self.obj, self.nrIt)
        self.f1.cieploNiskopreznejPoObl(self.obj, self.nrIt)
        self.f1.sumaCieplaPoObl(self.obj, self.nrIt)
        self.f1.qProcentowe(self.newData,self.nrIt)
        self.f1.spadekMocy(self.newData,self.nrIt)
        # excel=wEx.WriteDataExcel(self.obj,self.nrIt,self.f1,self.newData)
        # excel.generujRaport()


    def switchAkcjeButton(self,button):
        button['state']=tk.ACTIVE

    def generujDokumentObl(self):
        print("ta funkcja")
        self.excelW.checkifCopyFileExist()
        self.excelW.generujRaport()






