import tkinter as tk
from tkinter import ttk,Canvas
from tkinter import *
# import  thermopy.iapws
import pyXSteam.XSteam
import program.Classes.Dane.DaneEntalpia as dt
import program.Classes.ExcelOpenFile.ReadDataExcel as rE
from program.Classes.HelperClass.EntryField import EntryField
from program.Classes.HelperClass.FrameCreate import FrameCreate

from functools import partial

# from thermopy.iapws import *
from pyXSteam.XSteam import XSteam

class Entalpia():
    def __init__(self,tab):
      self.tab=tab


    def createListboxField(self):
        frameListBox=FrameCreate(self.tab,dt.ramka0['opis'],dt.ramka0.get("row"), dt.ramka0.get("columne"))
        ff=frameListBox.frameCreate()
        variable=StringVar(frameListBox)
        variable.set(dt.opcje[2])
        w=OptionMenu(ff,variable,*dt.opcje)
        w.grid(column=2)
        variable.trace('w',partial(self.stan,widget=variable))

        # w.bind('<Button-1>',self.stan(variable))


    #sprawdzic *args
    def stan(self,*args,widget=None):
        print(widget.get())
        print('asa')
        if(widget.get()=='Wczytaj dane z pliku'):
         ase = rE.ReadDataExcel()
         ase.wypelnijDaneExclem()


    def getFrameCreate(self):
        frame1 = FrameCreate(self.tab,dt.ramka1['opis'], dt.ramka1.get("row"), dt.ramka1.get("columne"))
        frame2 = frame1.frameCreate()
        return frame2
    #########################################################################################################
    #TEST#############

    def getListOfEntryFieldAll(self, framex,daneLista):
        #B = tk.Button(framex, text='Oblicz', command=lambda: [self.buttonCommand()])  # bardzo ważne
        #B.grid(row=20, column=2)
        #print(daneLista['strMasPary'].get('zmiennaPola'))

        for var in daneLista:
            entry = EntryField(framex, daneLista[var]['zmiennaPola'], daneLista[var]["opis"],
                               daneLista[var]["row"], daneLista[var]["columne"],daneLista[var]["flag"])
            entry.entryField()


    def getFrameCreateAll(self):
        for var in dt.listaRamek:
         frame1 = FrameCreate(self.tab,dt.listaRamek[var]['opis'], dt.listaRamek[var]["row"], dt.listaRamek[var]["columne"])
         frame2 = frame1.frameCreate()
         self.getListOfEntryFieldAll(frame2,dt.listaRamek[var]['dane'])


        return frame2
    #self.listOfElements[var]['zmiennaPola']


    #################################
    def createAllEntalphy(self):
        print()
    # def getFrameCreateSecond(self):
    #     frame3 = FrameCreate(self.tab, self.ramka2['opis'], self.ramka2.get("row"), self.ramka2.get("columne"))
    #     frame4 = frame3.frameCreate()
    #     return frame4
    #
    def getListOfEntryField(self, framex):
        #B = tk.Button(framex, text='Oblicz', command=lambda: [self.buttonCommand()])  # bardzo ważne
        #B.grid(row=20, column=2)
        for var in dt.listOfElements:
            entry = EntryField(framex, dt.listOfElements[var]['zmiennaPola'], dt.listOfElements[var]["opis"],
                               dt.listOfElements[var]["row"], dt.listOfElements[var]["columne"])
            entry.entryField()

    def buttonEntalpia(self):
        B = tk.Button(self.tab, text='Oblicz', command=lambda: [self.obliczEntalpie()])  # bardzo ważne
        B.grid(row=26, column=3)
    def msg(self,event):

        print ("Wciśnięto (jakiś) Button w pozycji (x,y):")
    # def getListOfEntryFieldSecond(self, framex):
    #     for var in self.listOfElements:
    #         entry = EntryField(framex, self.listOfElements[var]['zmiennaPola'], self.listOfElements[var]["opis"],
    #                            self.listOfElements[var]["row"], self.listOfElements[var]["columne"])
    #         entry.entryField()


    def obliczEntalpie(self):
        for var in dt.listaRamek:
            list=dt.listaRamek[var]['dane']
            T=list.get('tempPary').get('zmiennaPola').get()
            P=list.get('cisnPary').get('zmiennaPola').get()
            I=self.waterAndSteam(P,T)*1000
            list.get('entalpiaPary').get('zmiennaPola').set("{:.2f}".format(float(I)))





    def waterAndSteam(self,P,T):
        w = XSteam()
        # tp=w.enthalpy()
        tp=w.h_pt(P,T) # p=MPa, T=K
        print(tp)
        return tp
#
# class waterAndsteam():
#     w = XSteam()
#
#
#
#     def obliczEntalpie(self):
#
#         #tp=w.enthalpy()
#         print(self.w.h_pt(0.7,438.15)) # p=MPa, T=K
#         #return w


