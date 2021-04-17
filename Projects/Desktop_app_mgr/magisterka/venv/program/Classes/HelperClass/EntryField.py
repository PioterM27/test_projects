import tkinter as tk
from tkinter import ttk
from tkinter import *
import tkinter.ttk as ttka
import tkinter.messagebox as msb


class EntryField():
    def __init__(self, frame, name, labelText, row, column):
        self.frame = frame
        self.name = name
        self.labelText = labelText
        self.row = row
        self.column = column

    def __init__(self, frame, name, labelText, row, column, flag):
        self.frame = frame
        self.name = name
        self.labelText = labelText
        self.row = row
        self.column = column
        self.flag = flag

    def entryFieldColur(self):
        colourList = ['yellow', 'white', 'orange']
        if (self.flag == 1):
            return colourList[1]
        if (self.flag == 0):
            return colourList[0]
        else:
            return colourList[2]

    def entryField(val):
        # val.frame.pack(side=LEFT,fill='both')
        var1 = Entry(val.frame, font=('arial', 8), bd=3, bg=val.entryFieldColur(), width=10,
                     justify='left', textvariable=val.name)

        var1.grid(row=val.row, column=val.column)
        var1Label = Label((val.frame), font=('arial', 8, 'bold'), text=val.labelText, bd=2, anchor=W)
        var1Label.grid(row=(val.row), column=(val.column) - 1, ipady=10, sticky=S)
        return (var1)

    def entryUnitsField(val, units,zmienna):
        # val.frame.pack(side=LEFT,fill='both')
        # var1 = Entry(val.frame, font=('arial', 8), bd=3, bg=val.entryFieldColur(), width=5,
        #              justify='left', textvariable=val.name)
        # var1.grid(row=val.row, column=val.column)
        # return (var1)

        var1 = ttk.Combobox(val.frame, font=('arial', 8), width=5,
                            justify='left')

        var1.grid(row=val.row, column=val.column)
        if (units == 's'):
            var1['values'] = ('s', 'h', 'min')
            var1.current(1)
        elif (units == 'kg/s'):
            var1['values'] = ('kg/s', 't/h')
            var1.current(1)
        elif (units == 'm3'):
            var1['values'] = ('m3')
            var1.current(0)
        elif (units == 'm'):
            var1['values'] = ('m')
            var1.current(0)
        elif (units == 'J/kg'):
            var1['values'] = ('J/kg','kJ/kg')
            var1.current(0)
        elif (units == 'kg/m3'):
            var1['values'] = ('kg/m3')
            var1.current(0)

        else:
            var1['values'] = ('')
            # var1.current(0)


        # var1.bind("<<ComboboxSelected>>", val.callback(val.name,zmienna))
        return (var1)
    def callback(val,zm,zmienna):
        print("dziala czy nie")
        print(zmienna)