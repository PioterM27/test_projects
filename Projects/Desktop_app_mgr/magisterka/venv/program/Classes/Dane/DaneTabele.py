import cmath
import os
import tkinter as tk
# import Tkinter
# import tkMessageBox
import tkinter.filedialog
from functools import partial
from tkinter import *
from tkinter import ttk, Canvas

import PIL.Image
import PIL.ImageTk
import matplotlib
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import numpy as np
import program.Classes.Dane.DaneEntalpia as dElp
import program.Classes.Dane.DaneEntalpia as dt
import program.Classes.Dane.DaneStrumienieMasy as dStr
import program.Classes.Dane.DaneWejsciowe as dw
import program.Classes.ExcelOpenFile.FileDialog as flD
import program.Classes.ExcelOpenFile.OknaSchematu as nW
import program.Classes.ExcelOpenFile.ReadDataExcel as rE
from PIL import ImageTk, Image
from program.Classes.Bulider.Builder import Builder
from program.Classes.HelperClass.EntryField import EntryField
from program.Classes.HelperClass.FrameCreate import FrameCreate

matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

class DaneTabele:

    def __init__(self,tab):
        self.tab=tab
        print("stworzono mnie")

    def tabelaZwykresem(self,tk):
        print("asd")

    def getFrameCreate(self):
        var2 = Frame(self.tab, width=500, height=310, bd=8, relief="sunken")
       # var3=var2.pack(expand=YES,fill=X,side=TOP)
        var3 = var2.pack(expand=YES, fill=X, side=LEFT)
        var4 = Frame(self.tab, width=500, height=310, bd=8, relief="sunken")
        var5 = var4.pack(expand=YES, fill=X,side=LEFT)
        self.tabelaZwykresem(var2)