import tkinter as tk
from tkinter import ttk
from tkinter import *

class WindowCreate():

        form =tk.Tk()
        form.title("Magisterka")
        form.geometry("1480x720+0+0")
        tab_parent = ttk.Notebook(form)
        # canvas=tk.Canvas(form)
        # scroll=Scrollbar(form,orient=VERTICAL,command=canvas.yview())
        # scroll.pack(side=RIGHT,fill=Y)
        def returnPArent(self):
            return self.form

        def CreateTabs(self,_valTab,name):
            _valTab=ttk.Frame(self.tab_parent)
            self.tab_parent.add(_valTab,text=name)
            self.tab_parent.pack(expand=1,fill='both')
            print("Stad dane biore")
            return(_valTab)


        def CreateTabsScroll(self,_valTab,name):
            _valTab=ttk.Scrollbar(self.scroll,orient=VERTICAL)
            self.tab_parent.add(_valTab,text=name)
            self.tab_parent.pack(expand=1,fill='both')
            return(_valTab)


#
#      #1080x720
#
#
#
