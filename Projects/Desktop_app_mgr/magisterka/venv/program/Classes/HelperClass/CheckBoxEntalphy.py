import tkinter as tk
from tkinter import ttk
from tkinter import *
#import tkMessageBox

class CheckBoxEntalphy():
    def __init__(self,tab):
         self.tab=tab

    checkVar1=StringVar()
    checkVar2=StringVar()
    checkVar3=StringVar()

    ramka1={
              "opis": "Średnica",
              "row": 1,
              "columne": 0
    }
    def getTab(self):
        return self.tab
    
    def checkButtonEntalp(self,tab3):
      Lb1=Listbox(tab3)
      C1=Checkbutton(tab3,text="Test",variable=self.checkVar1,onvalue = 1, offvalue = 0, height=2,width = 20)
      C2 = Checkbutton(tab3, text="Test", variable=self.checkVar2, onvalue=1, offvalue=0, height=2, width=20)
      Lb1.insert(1,C1.pack(side=LEFT,fill=X))
      Lb1.insert(2,C2.pack(side=LEFT,fill=X))


    def sectionCreate(self):
         var2 = Frame(self.tab, width=150, height=4, bd=5, relief="sunken")
         #var2.grid(row=self.ramka1['row'], column=self.ramka1['columne'])
         var2.pack(fill='both', side=TOP )
         varTopic = Label(var2, width=150,height=1, bd=3, relief="sunken", text=self.ramka1['opis'])
         #varTopic.grid(row=(self.ramka1['row'])-1, column=self.ramka1['columne'], columnspan=600, pady=5)
         varTopic.pack(side=TOP,fill='both')
         return (var2)