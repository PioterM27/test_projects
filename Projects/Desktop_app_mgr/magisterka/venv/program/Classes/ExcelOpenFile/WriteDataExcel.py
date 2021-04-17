# import pandas as ppa
# from pandas import ExcelWriter
# from pandas import ExcelFile
import openpyxl as op
import time
import shutil,os



import program.Classes.Tabs.Dane as duj
import program.Classes.Dane.DaneWejsciowe as dw
import program.Classes.Dane.DaneEntalpia as de1
import program.Classes.Dane.DaneEntalpia2 as de2
import program.Classes.Dane.DaneStrumienieMasy as st
import program.Classes.Funkcje.FunkcjeIteracje as it
import program.Classes.Dane.DaneObliczenia as dOb
import program.Classes.Funkcje.Funkcje as ff
import program.Classes.Funkcje.FunkcjeIteracje as fI
import program.Classes.Funkcje.FunkcjeIteracjeNN as fIN
from tkinter import filedialog as fd
from tkinter.filedialog import asksaveasfile
import os as os
import sys,glob

class WriteDataExcel:
    # expectedDir = sys.argv[1]
    # fileName_relative=glob.glob(expectedDir+"**/*.xlsx",recursive=True)
    # fileName_absolut=os.path.basename(fileName_relative)
    # print(fileName_absolut)
    # def __init__(self):
    #     pass
    def __init__(self,obj,nrIt,f1,newData,dObl):
        self.obj=obj #objekt z danymi do iteracji
        self.nrIt=nrIt #ostatni element iteracji
        self.f1=f1 # obiekt z tablicami z danmyimi iteracjami
        self.newData=newData # dane obliczenia po iteracji
        self.dObl=dObl #obliczenia przed iteracja
        # self.excelW=wEx.WriteDataExcel(self.obj,self.nrIt,self.f1,self.newData)

    def generujRaport(self):
        #pobiera aktualny folder
        # print("jestem tutaj tez 12")
        # dir_path = os.path.dirname(os.path.realpath(__file__))
        #
        # print(dir_path)
        # path="D:\KursAI\pythonprojects\\venv\magisterka_version2\\venv\program\Classes\ExcelOpenFile\GotowyTest.xlsx"
        # wb=op.load_workbook(r"D:\KursAI\pythonprojects\venv\magisterka_version2\venv\program\Classes\ExcelOpenFile\GotowyTest.xlsx")
        # ws=wb["Arkusz1"]
        # test=wb.get_sheet_names()
        # print(test)
        # wcell=ws.cell(6,1)
        # wcell.value=5
        # os.startfile(path, 'open')
        # name = fd.asksaveasfile(filetypes = files, defaultextension = files)
        # wb.save("C:\\Users\OEM\Desktop\GotowyArkuszmgrWypełniony.xlsx")

        #1 Kopiowanie formularza do wypełnienia
        files=('D:\KursAI\pythonprojects\\venv\magisterka_version2\\venv\program\Classes/ExcelOpenFile\GotowyTest.xlsx')
        #zwraca folder w ktorym zapisano nowy plkik
        # files = "C:\Program Files\imagesMgr\GotowyTest.xlsx"
        temporaryFile=shutil.copy(files,'D:\KursAI\pythonprojects\\venv\magisterka_version2\\venv\program\Classes/ExcelOpenFile\\sample2.xlsx',follow_symlinks=True)
        print(temporaryFile)
        #otwieramy i zapisujemy dane do tymczzasowego pliku
        wb = op.load_workbook(temporaryFile)
        ws = wb["Arkusz1"]
        self.wypelnijRaportDanymi(ws)
        wb.save(temporaryFile)
        fd=os.startfile(temporaryFile, 'open')
    def wypelnijRaportDanymi(self,ws):
        print("jestem tutaj tez")
        #Dane Wejściowe Wej (wiersz,kolumna)
        wcellWej1 = ws.cell(3,2)
        wcellWej1.value = dw._dZas.get()
        wcellWej2 = ws.cell(4,2)
        wcellWej2.value = dw._hZas.get()
        wcellWej3 = ws.cell(5,2)
        wcellWej3.value = dw._ilZas.get()
        wcellWej4 = ws.cell(6,2)
        wcellWej4.value = dw._gestWody.get()
        wcellWej5 = ws.cell(7,2)
        wcellWej5.value = dw._czasNap.get()
        wcellWej6 = ws.cell(8,2)
        wcellWej6.value = dw._wd.get()
        wcellWej7 = ws.cell(9,2)
        wcellWej7.value = dw._nk.get()
        wcellWej8 = ws.cell(10,2)
        wcellWej8.value = dw._mzas.get()
        wcellWej9 = ws.cell(11,2)
        wcellWej9.value = dw._Vzas.get()
        wcellWej10 = ws.cell(12,2)
        wcellWej10.value = dw._VzasMax.get()
        #Strumienie masy
        wcellMas1=ws.cell(20,2)
        wcellMas1.value=st._mwz.get()
        wcellMas2 = ws.cell(21, 2)
        wcellMas2.value = st._mods.get()
        wcellMas3 = ws.cell(22, 2)
        wcellMas3.value = st._mwtrI.get()
        wcellMas4 = ws.cell(23, 2)
        wcellMas4.value = st._mwtrII.get()
        wcellMas5 = ws.cell(24, 2)
        wcellMas5.value = st._mwtrIII.get()
        wcellMas6 = ws.cell(25, 2)
        wcellMas6.value = st._mwtrIV.get()
        wcellMas7 = ws.cell(26, 2)
        wcellMas7.value = st._mwtrV.get()
        wcellMas8 = ws.cell(27, 2)
        wcellMas8.value = st._mI.get()
        wcellMas9 = ws.cell(28, 2)
        wcellMas9.value = st._mII.get()
        wcellMas10 = ws.cell(29, 2)
        wcellMas10.value = st._mIII.get()
        wcellMas11 = ws.cell(30, 2)
        wcellMas11.value = st._mIV.get()
        wcellMas12 = ws.cell(31, 2)
        wcellMas12.value = st._mV.get()
        wcellMas13 = ws.cell(32, 2)
        wcellMas13.value = st._mVI.get()
        wcellMas14 = ws.cell(33, 2)
        wcellMas14.value = st._mVII.get()
        wcellMas15 = ws.cell(34, 2)
        wcellMas15.value = st._mps.get()
        wcellMas16 = ws.cell(35, 2)
        wcellMas16.value = st._modg.get()
        #Strumienie masy paliwa
        wcellMasPal1 = ws.cell(37, 2)
        wcellMasPal1.value = dw._nwp.get()
        wcellMasPal2 = ws.cell(38, 2)
        wcellMasPal2.value = dw._nsp.get()
        wcellMasPal3 = ws.cell(39, 2)
        wcellMasPal3.value = dw._nnp.get()
        wcellMasPal4 = ws.cell(40, 2)
        wcellMasPal4.value = de2._isp.get()
        wcellMasPal5 = ws.cell(41, 2)
        wcellMasPal5.value = de2._inp.get()
        wcellMasPal6 = ws.cell(42, 2)
        wcellMasPal6.value = de2._iznp.get()
        wcellMasPal7 = ws.cell(43, 2)
        wcellMasPal7.value = ff._qwp.get()
        wcellMasPal8 = ws.cell(44, 2)
        wcellMasPal8.value = ff._qsp.get()
        wcellMasPal9 = ws.cell(45, 2)
        wcellMasPal9.value = ff._qnp.get()
        wcellMasPal10 = ws.cell(46, 2)
        wcellMasPal10.value = ff._qsum.get()


        #Parametry czynnika podczas napełniania
        wcellNap1 = ws.cell(48, 2)
        wcellNap1.value = self.obj.tabIwz[self.nrIt-1].get()
        wcellNap2 = ws.cell(49, 2)
        wcellNap2.value = self.obj.tabMps[self.nrIt-1].get()
        wcellNap3 = ws.cell(50, 2)
        wcellNap3.value = self.obj.tabMI[self.nrIt-1].get()
        wcellNap4 = ws.cell(51, 2)
        wcellNap4.value = self.obj.tabMII[self.nrIt-1].get()
        wcellNap5 = ws.cell(52, 2)
        wcellNap5.value = self.obj.tabMIII[self.nrIt-1].get()
        wcellNap6 = ws.cell(53, 2)
        wcellNap6.value = self.obj.tabMIV[self.nrIt-1].get()
        wcellNap7 = ws.cell(54, 2)
        wcellNap7.value = self.obj.tabMV[self.nrIt-1].get()
        wcellNap8 = ws.cell(55, 2)
        wcellNap8.value = self.obj.tabMVI[self.nrIt-1].get()
        wcellNap9 = ws.cell(56, 2)
        wcellNap9.value = self.obj.tabMVII[self.nrIt-1].get()
        # Dane z Iteracji

        wcellIt1 = ws.cell(62, 2)
        wcellIt1.value= self.obj.tabIskzm[self.nrIt-1].get()
        wcellIt2 = ws.cell(64, 2)
        wcellIt2.value = self.obj.tabIskXN2[self.nrIt-1].get()
        wcellIt3 = ws.cell(66, 2)
        wcellIt3.value = self.obj.tabIskXN3[self.nrIt-1].get()
        wcellIt4 = ws.cell(68, 2)
        wcellIt4.value = self.obj.tabIskXN4[self.nrIt-1].get()
        wcellIt5 = ws.cell(70, 2)
        wcellIt5.value = self.obj.tabIskXN5[self.nrIt-1].get()
        wcellIt6 = ws.cell(72, 2)
        wcellIt6.value = self.obj.tabIwodODG[self.nrIt-1].get()
        wcellIt7 = ws.cell(74, 2)
        wcellIt7.value = self.obj.tabIpz[self.nrIt-1].get()
        wcellIt8 = ws.cell(75, 2)
        wcellIt8.value = self.obj.tabIskXW1[self.nrIt-1].get()
        wcellIt9 = ws.cell(76, 2)
        wcellIt9.value = self.obj.tabMwz[self.nrIt-1].get()
        wcellIt10 = ws.cell(78, 2)
        wcellIt10.value = self.obj.tabIskXW2[self.nrIt-1].get()
        wcellIt11 = ws.cell(80, 2)
        wcellIt11.value = self.obj.tabIskXW3[self.nrIt-1].get()
        wcellIt12 = ws.cell(83, 2)
        wcellIt12.value = ff._qwp2.get()
        wcellIt13 = ws.cell(84, 2)
        wcellIt13.value = ff._qsp2.get()
        wcellIt14 = ws.cell(85, 2)
        wcellIt14.value = ff._qnp2.get()
        wcellIt15 = ws.cell(86, 2)
        wcellIt15.value = ff._qsum2.get()
        wcellIt16 = ws.cell(87, 2)
        wcellIt16.value = self.newData._q.get()
        wcellIt17 = ws.cell(88, 2)
        wcellIt17.value = self.newData._qnom.get()
        wcellIt18 = ws.cell(89, 2)
        wcellIt18.value = self.newData._qProc.get()
        wcellIt19 = ws.cell(90, 2)
        wcellIt19.value = self.newData._spadekMocy.get()
        wcellIt19 = ws.cell(95, 2)
        wcellIt19.value = fI._qwododg.get()
        wcellIt19 = ws.cell(96, 2)
        wcellIt19.value = fI._ppp.get()
        wcellIt19 = ws.cell(97, 2)
        wcellIt19.value = fI._pzp.get()
        wcellIt19 = ws.cell(98, 2)
        wcellIt19.value = fI._delpz.get()
        wcellIt19 = ws.cell(99, 2)
        wcellIt19.value = fI._delipz.get()

    def checkifCopyFileExist(self):
        arr=os.listdir("D:\KursAI\pythonprojects\\venv\magisterka_version2\\venv\program\Classes/ExcelOpenFile")
        print(arr)
        yy=arr.__contains__("sample2.xlsx")
        print(yy)
        if(yy==True):
            print("usuwam")
            os.remove(
                'D:\KursAI\pythonprojects\\venv\magisterka_version2\\venv\program\Classes\ExcelOpenFile\sample2.xlsx')
        else:
            pass



        # fd=os.open(temporaryFile,os.O_WRONLY)
        # tt=os.close(fd)
        # print(str(tt))

        #2

        # os.remove('D:\KursAI\pythonprojects\\venv\magisterka_version2\\venv\program\Classes\ExcelOpenFile\sample2.xlsx')

        # nazaw = os.getcwd()
        # # classPAth=ins.getfile(FileDialog.__class__)
        # # classPAth=os.path.abspath(sys.modules[FileDialog.__module__].__file__)
        # filePAth = ('Classes/ExcelOpenFile/pythonExcel2.xlsx')
        # print(nazaw)
        # # path = 'D:\\KursAI\\pythonprojects\\venv\\magisterka_version2\\venv\\program\\Classes\\ExcelOpenFile\\pythonExcel2.xlsx'
        # newPath = nazaw[:-4]
        # # lastPath=newPath+filePAth
        # lol = os.path.join(newPath, filePAth)
        # print(newPath)
        # print(filePAth)
        # # print(lastPath)
        # print(lol)
        #
        # # print(os.path.isfile("venv/program/Classes/ExcelOpenFile/arkusz.png"))
        # os.startfile(lol, 'open')




