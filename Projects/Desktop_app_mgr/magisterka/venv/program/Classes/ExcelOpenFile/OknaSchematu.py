import tkinter as tk
from tkinter import ttk
from tkinter import *
import tkinter.ttk as ttka
import tkinter.messagebox as msb
from program.Classes.HelperClass.FrameCreate import FrameCreate


class OknaSchematu():
    def __init__(self,nazwa,parent):
        # self.frame = frame
        self.nazwa = nazwa
        self.parent=parent
        # self.labelText = labelText
        # self.row = row
        # self.column = column

    def newWindow1(self):
        form = tk.Toplevel(self.parent)
        form.title(self.nazwa)
        form.geometry("500x320+0+0")
        return  form




