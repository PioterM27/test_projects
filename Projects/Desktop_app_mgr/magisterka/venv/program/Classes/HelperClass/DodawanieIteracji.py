import tkinter as tk
from tkinter import ttk, Canvas
from tkinter import *
import cmath
# import Tkinter
# import tkMessageBox

from program.Classes.HelperClass.EntryField import EntryField
from program.Classes.HelperClass.FrameCreate import FrameCreate
from program.Classes.Bulider.Builder import Builder
#from program.Classes.MainLoop import WindowCreate
from program.Classes.Tabs.IteracjeNN import InteracjeNN
import program.Classes.Dane.DaneWejsciowe as dw
import program.Classes.MainLoop as mn
import program.Classes.Tabs.IteracjeNN as itNN


class DodawanieIteracji():

    # def __init__(self, tab):
    #     self.tab = tab

    def buttonCommand(self,tab,name):
        test = mn.WindowCreate()
        curTab=test.CreateTabs(tab, name)
        return  curTab

    # def test(self):
    #     InteracjeNN.poczatekIteracji(self.tab)
    #     print("kutas")

    def button(self):
       B = tk.Button(self.tab,text='Start', command=self.test())
       B.grid()

