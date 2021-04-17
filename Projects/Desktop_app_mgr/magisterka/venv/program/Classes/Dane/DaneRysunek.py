import tkinter as tk
from tkinter import ttk, Canvas
from tkinter import *
import cmath
# import Tkinter
# import tkMessageBox
import tkinter.filedialog
from PIL import ImageTk, Image
import os
from program.Classes.HelperClass.EntryField import EntryField
from program.Classes.HelperClass.FrameCreate import FrameCreate
import program.Classes.ExcelOpenFile.ReadDataExcel as rE
from program.Classes.Bulider.Builder import Builder
from functools import partial
import program.Classes.Dane.DaneWejsciowe as dw
import program.Classes.Dane.DaneEntalpia as dt
import program.Classes.ExcelOpenFile.FileDialog as flD
# import matplotlib.pyplot as plt
# import numpy as np
import PIL.Image
import PIL.ImageTk
import program.Classes.ExcelOpenFile.OknaSchematu as nW
import program.Classes.Dane.DaneEntalpia as dElp
import program.Classes.Dane.DaneStrumienieMasy as dStr
import program.Classes.Dane.DaneEntalpia2 as dElp2
import program.Classes.Dane.DaneIteracje as itD

iwz = DoubleVar()


class DaneRysunek:
    def __init__(self, tab, parent):
        self.tab = tab
        self.parent = parent

    path = "C:\\Users\OEM\Desktop\praca magisterska\zdjecia\elementy\\"

    def getFrameCreate(self):
        # var2 = Frame(self.tab, width=500, height=310, bd=8, relief="sunken")
        var2 = Frame(self.tab, width=500, height=310, bd=8, relief="sunken")
        # canvas=tk.Canvas(var2)
        # scrollbar=ttk.Scrollbar(var2,orient=VERTICAL,command=canvas.yview())
        # scrollable_frame=ttk.Frame(canvas)
        # canvas.pack()
        # var3=var2.pack(expand=YES,fill=X,side=TOP)

        var3 = var2.pack(expand=YES, fill=X, side=TOP)
        var4 = Frame(self.tab, width=20, height=30, bd=8, relief="sunken")
        var5 = var4.pack(expand=YES, fill=X, side=BOTTOM)


        # varTopic = Label(var2, width=45, bd=2, relief="sunken", text="Rysuneg", font=("Helvetica", 8))
        # varTopic.pack(side=TOP)
        self.insertPicture(var2)
        self.listOfButtons(var4)
        # B = tk.Button(var3, text='Oblicz', command=lambda: [self.insertPicture(var2)])  # bardzo ważne
        # B.pack()
        # self.insertPicture(var3)


    # def insertPicture(self,frame):
    def callback(self, event):
        print(event.x)
        print(event.y)

    def insertPicture(self, frame):
        # E1 = Entry(self.tab, bd=5, show='*')  # tried this line of code but it didn't worked

        # img = ImageTk.PhotoImage(Image.open("png2.JPG"))
        # panel = Label(frame, image=img)
        # panel.pack(side="bottom", fill="both", expand="yes")
        # img = plt.imread(r'C://Users//OEM//Desktop//praca magisterska//png.JPG')
        # ax=plt.subplot()
        # ax.imshow(img)

        # canvas = Canvas(frame, width=200, height=200)
        # canvas.pack()
        # #mym=Image.open("C://Users//OEM//Desktop//praca magisterska//png2.PNG")
        # img = ImageTk.PhotoImage(Image.open("C:\\Users\OEM\Desktop\praca magisterska\png.JPG"))
        # print("asdasds")
        # canvas.create_image(200, 200, anchor=N, image=img)
        # path = "1.jpg"
        #
        # image = PhotoImage(Image.open(r'C://Users//OEM//Desktop//praca magisterska//png.JPG'))
        #
        # panel = Label(frame, image=image)
        #
        # panel.pack()
        ###############################################################################################Nie ruszac
        # im = PIL.Image.open(r"C:\Users\OEM\Desktop\praca magisterska\zdjecia\elementy\main.PNG")
        # photo = PIL.ImageTk.PhotoImage(im)
        #
        # label = Label(frame, image=photo)
        # label.image = photo  # keep a reference!
        #
        # label.pack()
        # dir_path = os.path.dirname(os.path.realpath(__file__))
        # filename=dir_path.replace("Dane","ExcelOpenFile\images\main.PNG")

        #
        # if '_MEIPASS2' in os.environ:
        #     filename = (os.path.join(os.environ['_MEIPASS2'], filename))
        #     fd = PIL.Image.open(filename, 'rb')
        #     photo = PIL.ImageTk.PhotoImage(fd)
        #     label = Label(frame, image=photo)
        #     label.image = photo  # keep a reference!
        #
        #     label.pack()
        # else:
            # dir_path = os.path.dirname(os.path.realpath(__file__))
            # pictureMainPath=dir_path.replace("Dane","ExcelOpenFile\images\main.PNG")
            # print("Przeroboinoa sciezka glownego rysunku "+pictureMainPath)
            path="C:\Program Files\imagesMgr\\"
            pictureMainPath=path+"main.PNG"
            im = PIL.Image.open(pictureMainPath)
            photo = PIL.ImageTk.PhotoImage(im)
            label = Label(frame, image=photo)
            label.image = photo  # keep a reference!

            label.pack()

        ##Przerobiona funkcja###
        # dir_path = os.path.dirname(os.path.realpath(__file__))
        # pictureMainPath=dir_path.replace("Dane","ExcelOpenFile\images\main.PNG")
        # print("Przeroboinoa sciezka glownego rysunku "+pictureMainPath)
        # im = PIL.Image.open(pictureMainPath)
        # photo = PIL.ImageTk.PhotoImage(im)
        #
        # label = Label(frame, image=photo)
        # label.image = photo  # keep a reference!
        #
        # label.pack()

        # self.callback()
        # frame.bind("<Button-1>",self.callback)
        # label.bind_all("<Button-1>",self.callback)
        ########################################################################################################################



    # def insertPicture(self, frame):
    #     fig, ax = plt.subplots()
    #     im = ax.imshow(image)
    #     patch = patches.Circle((260, 200), radius=200, transform=ax.transData)
    #     im.set_clip_path(patch)
    #
    #     ax.axis('off')
    #     plt.show()

    def listOfButtons(self, frame):
        B1 = tk.Button(frame, text='1', height=2, width=6, command=lambda: [
            self.newWindow("1", dElp._iSH5wyl, dStr._mps, 0, 0, 1)])  # bardzo ważne
        B1.pack(side=LEFT)
        B2 = tk.Button(frame, text='2', height=2, width=6,
                       command=lambda: [self.newWindow("Element", dElp._iRH2wyl, dStr._msp, dElp._TRH2wyl, dElp._pRH2wyl,
                                                       2)])  # bardzo ważne
        B2.pack(side=LEFT)
        B3 = tk.Button(frame, text='3', height=2, width=6,
                       command=lambda: [self.newWindow("Element", dElp2._inp, dStr._mnp, 0, 0, 3)])  # sprawdzic temp i p
        B3.pack(side=LEFT)
        B4 = tk.Button(frame, text='4', height=2, width=6,
                       command=lambda: [
                           self.newWindow("Element", dElp2._iznp, dStr._mznp, 0, 0, 4)])  # sprawdzic temp i p
        B4.pack(side=LEFT)
        B5 = tk.Button(frame, text='5', height=2, width=6,
                       command=lambda: [
                           self.newWindow("Element", dElp2._iI, dStr._mI, dElp2._TI, dElp2._pI, 5)])  # bardzo ważne
        B5.pack(side=LEFT)
        B6 = tk.Button(frame, text='6', height=2, width=6,
                       command=lambda: [
                           self.newWindow("Element", dElp2._iII, dStr._mII, dElp2._TII, dElp2._pII, 6)])  # bardzo ważne
        B6.pack(side=LEFT)
        B7 = tk.Button(frame, text='7', height=2, width=6,
                       command=lambda: [self.newWindow("Element", dElp2._iIII, dStr._mIII, dElp2._TIII, dElp2._pIII,
                                                       7)])  # bardzo ważne
        B7.pack(side=LEFT)
        B8 = tk.Button(frame, text='8', height=2, width=6,
                       command=lambda: [
                           self.newWindow("Element", dElp2._iIV, dStr._mIV, dElp2._TIV, dElp2._pIV, 8)])  # bardzo ważne
        B8.pack(side=LEFT)
        B9 = tk.Button(frame, text='9', height=2, width=6,
                       command=lambda: [
                           self.newWindow("Element", dElp2._iV, dStr._mV, dElp2._TV, dElp2._pV, 9)])  # bardzo ważne
        B9.pack(side=LEFT)
        B10 = tk.Button(frame, text='10', height=2, width=6,
                        command=lambda: [
                            self.newWindow("Element", dElp2._iVI, dStr._mVI, dElp2._TVI, dElp2._pVI, 10)])  # bardzo ważne
        B10.pack(side=LEFT)
        B11 = tk.Button(frame, text='11', height=2, width=6,
                        command=lambda: [self.newWindow("trse1", dElp2._iVII, dStr._mVII, dElp2._TVII, dElp2._pVII,
                                                        11)])  # bardzo ważne
        B11.pack(side=LEFT)
        B12 = tk.Button(frame, text='12', height=2, width=6,
                        command=lambda: [
                            self.newWindow("Element", dElp._iwz, dStr._mwz, dElp._Twz, dElp._pwz, 12)])  # bardzo ważne
        B12.pack(side=LEFT)
        B13 = tk.Button(frame, text='13', height=2, width=6,
                        command=lambda: [self.newWindow("Element", dElp._iods, dStr._mods, 0, 0, 13)])  # bardzo ważne
        B13.pack(side=LEFT)
        B14 = tk.Button(frame, text='14', height=2, width=6,
                        command=lambda: [self.newWindow("Element", 0, 0, 0, 0, 14)])  # bardzo ważne
        B14.pack(side=LEFT)
        # B15 = tk.Button(frame, text='test', height=2, width=6,
        #                 command=lambda:[self.test()])  # bardzo ważne
        # B15.pack(side=LEFT)
    def test(self):
        print("funkcja testujaca")
        print(itD.DaneIteracje.tabMsp[4].get())

    def newWindow(self, nazwa, et, sm, p, t, number):
        n1 = nW.OknaSchematu(nazwa, self.parent)
        window = n1.newWindow1()
        secondWindow = self.getFrameCreateElements(window)
        self.entryFieldNewWindow(secondWindow[1], et, 2,"Entalpia [J/kg]")
        self.entryFieldNewWindow(secondWindow[1], sm, 4,"Strumień masy [kg/s]")
        self.entryFieldNewWindow(secondWindow[1], p, 6,"Ciśnienie [MPa]")
        self.entryFieldNewWindow(secondWindow[1], t, 8,"Temperatura [K]")
        self.creteElementPicture(secondWindow[0], number - 1)
        # self.setEntryValues(tys,dElp._iwz)

    def getFrameCreateElements(self, window):
        tab = []
        newVar1a = Frame(window, width=180, height=186, bd=8, relief="sunken")
        # var3=var2.pack(expand=YES,fill=X,side=TOP)
        #  newVar3 = newVar2.pack(side=LEFT)
        newVar1b = newVar1a.grid(row=0, column=0)
        newVar2a = Frame(window, width=150, height=150, bd=8, relief="sunken")
        newVar2b = newVar2a.grid(row=0, column=1)
        # self.listOfButtons(var4)
        tab.append(newVar1a)
        tab.append(newVar2a)

        return tab

    def entryFieldNewWindow(self, frame, value, row,name):
        # val.frame.pack(side=LEFT,fill='both')
        var66 = Entry((frame), font=('arial', 8), bd=1, bg="red", width=10,
                      justify='left', textvariable=value)
        var66.grid(row=row, column=1)
        var1Label = Label((frame), font=('arial', 8, 'bold'), text=name, bd=2, anchor=W)
        var1Label.grid(row=row - 1, column=1, ipady=10, sticky=S)
        return value

    def entryUnitsFieldNewWindow(val):
        # val.frame.pack(side=LEFT,fill='both')
        # var1 = Entry(val.frame, font=('arial', 8), bd=3, bg=val.entryFieldColur(), width=5,
        #              justify='left', textvariable=val.name)
        # var1.grid(row=val.row, column=val.column)
        # return (var1)
        var1 = ttk.Combobox(val.frame, font=('arial', 8), width=5,
                            justify='left', textvariable=val.name)
        var1.grid(row=val.row, column=val.column)
        var1['values'] = ('Kj', 'Kg')
        var1.current(1)
        # var1.bind("<<ComboboxSelected>>", self.on_select_changed)
        return (var1)

    def setEntryValues(self, val1, val2):
        val1.set(val2.get())
        print(val1.get())
        print(val2.get())
        print(val1.get())

    def creteElementPicture(self, frame, nbr):

        # dir_path = os.path.dirname(os.path.realpath(__file__))
        # pictureElementPath = dir_path.replace("Dane", "ExcelOpenFile\images\\")
        pictureElementPath = "C:\Program Files\imagesMgr\\"
        elementPath = pictureElementPath + self.pictureList(nbr)
        im = PIL.Image.open(elementPath)
        # print("Tu tworze rysunek")
        # dir_path = os.path.dirname(os.path.realpath(__file__))
        # print(elementPath)
        # im = PIL.Image.open(r"C:\Users\OEM\Desktop\praca magisterska\zdjecia\test1.PNG")
        photo = PIL.ImageTk.PhotoImage(im)
        # print(frame)
        label = Label(frame, image=photo)
        label.image = photo  # keep a reference!
        label.grid()
        # print(self.pictureList(1))

    def pictureList(self, nbr):
        list = [
            "1.PNG",
            "2.PNG",
            "3.PNG",
            "4.PNG",
            "5.PNG",
            "6.PNG",
            "7.PNG",
            "8.PNG",
            "9.PNG",
            "10.PNG",
            "11.PNG",
            "12.PNG",
            "13.PNG",
            "14.PNG"

        ]
        return list[nbr]
