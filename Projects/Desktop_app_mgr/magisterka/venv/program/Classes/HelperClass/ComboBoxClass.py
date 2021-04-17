import tkinter as tk
from tkinter import ttk
from tkinter import *
import tkinter.ttk as ttka
import tkinter.messagebox as msb

class ComboBoxClass:

    def __init__(self, frame, name, labelText, row, column, flag):
        self.frame = frame
        self.name = name
        self.labelText = labelText
        self.row = row
        self.column = column
        self.flag = flag


    def entryCombobox(val,units,zm):
        # val.frame.pack(side=LEFT,fill='both')
        var1 = ttka.Combobox(val.frame, font=('arial', 8), width=5,
                            justify='left',postcommand=lambda:val.convert(var1,zm))
        var1.grid(row=val.row, column=val.column+1)
        # var1 = ttka.Combobox(val.frame, font=('arial', 8), width=5,
        #                      justify='left', validatecommand=lambda: val.loki(val.name, var1.current()),
        #                      postcommand=lambda:(val.loki(val.name,var1))
        # var1.grid(row=val.row, column=val.column + 1)

        if (units == 's'):
            var1['values'] = ('s', 'h', 'min')
            var1.current(0)
        elif (units == 'kg/s'):
            var1['values'] = ('kg/s', 't/h')
            var1.current(0)
        elif (units == 'm3'):
            var1['values'] = ('m3')
            var1.current(0)
        elif (units == 'm'):
            var1['values'] = ('m')
            var1.current(0)
        elif (units == 'J/kg'):
            var1['values'] = ('J/kg', 'kJ/kg')
            var1.current(0)
        elif (units == 'kg/m3'):
            var1['values'] = ('kg/m3')
            var1.current(0)

        else:
            var1['values'] = ('')
            # var1.current(0)

        return (var1)
    def loki(val):
        print("yu")

        # print("loki")
        # # print(name.get())
        # print((obj.current()))
        # print(obj['values'][0])
        # # val.koki(obj)
    def convert(val,obj,zm):
        choice=obj.current()
        name=obj['values'][choice]
        if(name=='kg/s'):
            test=val.t_h(zm.get())
            zm.set(test)
        elif(name=='t/h'):
            test=val.kg_s(zm.get())
            zm.set(test)
        elif (name == 's'):
            test = val.hours(zm.get())
            zm.set(test)
        elif (name == 'h'):
            test = val.sekundy(zm.get())
            zm.set(test)


    def kg_s(self,val):
        value=(val*1000)/3600
        return value
    def t_h(self,val):
        print(val)
        value=(val*3600)/1000
        return value
    def sekundy(self,val):
        value = val * 3600
        return value
    def hours(self,val):
        value = val / 3600
        return value
    def j_kg(self,val):
        pass
    def kJ_kg(self,val):
        pass

