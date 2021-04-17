#from program.Classes.Bulider.Builder import Builder
import tkinter as tk
from tkinter import ttk
from tkinter import *
from program.Classes.HelperClass.EntryField import EntryField
from program.Classes.HelperClass.FrameCreate import FrameCreate

class Section():
    def __init__(self,listOfEntry):
        self.listOfEntry=listOfEntry
        
    # def getSectionFrame(self):
    #     f3=self.frame.frameCreate()
    #     return f3 
    def getSectionEntry(self):
        self.listOfEntry.entryField()
    # def __init__(self):
    #     self._frame=None
    #     #self._entry=None
    # def setFrame(self,frame):
    #     self._frame=frame
    # #def setEntry(self,entry):
    #   #  self._entry=entry