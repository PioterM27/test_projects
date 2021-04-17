import tkinter as tk
from tkinter import ttk
from tkinter import *

# import matplotlib.pyplot as plt
# import matplotlib.patches as patches
# import matplotlib.cbook as cbook

import program.Classes.MainLoop as mn
# from program.Classes.Tabs.Dane import Dane
import program.Classes.Tabs.Dane as dt
import program.Classes.Tabs.Entalpia as et
import program.Classes.Tabs.Entalpia2 as et2
import program.Classes.HelperClass.CheckBoxEntalphy as ent
import program.Classes.HelperClass.DodawanieIteracji as dit
from program.Classes.Bulider.Director import Director
from program.Classes.Bulider.Section import Section
import program.Classes.ExcelOpenFile.FileDialog as das
import program.Classes.ExcelOpenFile.ReadDataExcel as rE
import program.Classes.Tabs.Strumienie as str
import program.Classes.Tabs.Iteracje as it
import program.Classes.Tabs.IteracjeNN as dNN
import program.Classes.Dane.ZmienneDoIteracji as zm
import program.Classes.Dane.DaneIteracje as itdan
import program.Classes.Tabs.Obliczenia as obl
# from program.Classes.Tabs.Entalpia import waterAndsteam
import program.Classes.Dane.DaneRysunek as rys

# import program.Classes.Dane.DaneTabele as tab


# das.FileDialog()
e1 = mn.WindowCreate()
tab1 = e1.CreateTabs('tab1', 'Dane')
e2 = e1.returnPArent()
# print(tab1)
# tab2=e1.CreateTabs('tab2','Obliczenia')
tab3 = e1.CreateTabs('tab3', 'Entalpie')
tab4 = e1.CreateTabs('tab4', 'Entalpie 2')
tab5 = e1.CreateTabs('tab5', 'Strumienie Masy')
tab2 = e1.CreateTabs('tab2', 'Obliczenia')
tab6 = e1.CreateTabs('tab6', 'Rysunek')

# tab7=e1.CreateTabs('tab7','Wykres')
# tab6=e1.CreateTabs('tab6','Iteracja1')
# tab7=e1.CreateTabs('tab7','DaneIteracja1')
# ase=rE.ReadDataExcel()
# ase.wypelnijDaneExclem()

dane = dt.Dane(tab1)
entalpia = et.Entalpia(tab3)
entalpia2 = et2.Entalpia2(tab4)
entFrame = entalpia.getFrameCreateAll()
entFrame2 = entalpia2.getFrameCreateAll()
entalpia.buttonEntalpia()
obliczenia = obl.Obliczenia(tab2)
obliczenia.getFrameCreateAll()
#########################################
# Rysunek
rysunke = rys.DaneRysunek(tab6, e2)
tt = rysunke.getFrameCreate()

# rysunke.insertPicture(tt)
# Wykresy
# wykres=tab.DaneTabele(tab7)
# wykres.getFrameCreate()


strumienie = str.Strumienie(tab5)
strFrame = strumienie.getFrameCreateAll()
# strumienie.getListOfEntryField(strFrame)

# entalpia=ent.CheckBoxEntalphy(tab3)
# tab5=entalpia.sectionCreate()
# entalpia.checkButtonEntalp(tab5)

las = dane.getFrameCreate()
# las2=dane.getFrameCreateSecond()
dane.getListOfEntryField(las)
# entalpia.getListOfEntryField(entFrame)
# entalpia.createListboxField()
dane.createListboxField()
# dane.getListOfEntryFieldSecond(las2)
# f2=dane.getFrameCreate()
# f3=dane.getListOfEntryField(f2)
# entalpia=waterAndsteam()
# entalpia.obliczEntalpie()

# daneSection=Section(f3)
# daneSection.getSectionEntry()
# a1=itdan.DaneIteracje()


# iteracja=it.Iteracje(tab6,a1)
# iteracja.getFrameCreateAll(0)
# iteracja.button()


# a=zm.ZmienneDoIteracji()
# a.stworzZmienne(5)
# iteracja2=dNN.InteracjeNN()
# iteracja.button()
# test=dit.DodawanieIteracji(tab7)
# test.button()
# lol=dNN.InteracjeNN(tab7)
# lol.poczatekIteracji()
# lol.tworzeniePolIteracji()


mn.mainloop()
