# import pandas as ppa
# import numpy as np
# from pandas import ExcelWriter
# from pandas import ExcelFile
import openpyxl as op

import program.Classes.Tabs.Dane as duj
import program.Classes.Dane.DaneWejsciowe as dw
import program.Classes.Dane.DaneEntalpia as de1
import program.Classes.Dane.DaneEntalpia2 as de2
import program.Classes.Dane.DaneStrumienieMasy as st
import program.Classes.Funkcje.FunkcjeIteracje as it

class ReadDataExcel():

    def __init__(self, name):
        self.name = name


    def excel(self):
      data=ppa.read_excel(r'C:\\Users\\OEM\\Desktop\\pythonExcel2.xlsx')
      df=ppa.DataFrame(data,columns=['Nazwa','Strumien','Temp'])
      df2 = ppa.DataFrame(data, columns=['Nazwa2', 'Strumien2', 'Temp2'])
      d=df['Temp'][1]
      d1=df2['Temp2'][0]
      dw._dZas.set(d)
      dw._czasNap.set(d1)

      print(d)

    def wypelnijDaneExclem(self):
        # data = ppa.read_excel(r'C:\\Users\\OEM\\Desktop\\GotowyArkuszmgr.xlsx',index_col=0,header=1,)#wazne ze header ustawia skad startujemy
        # data = ppa.read_excel(self.name, index_col=0,
        #                       header=1,dtype=str )  # wazne ze header ustawia skad startujemy
        # df = ppa.DataFrame(data, columns=['Nazwa', 'Wartość', 'Jednostka','Symbol'])
        # df2 = ppa.DataFrame(data, columns=['Nazwa', 'Temperatura pary [C]', 'Ciśnienie pary [MPa]', 'Entalpia pary [kJ/kg]'])
        #########dotad zakomentowane jest ok
        path=self.name
        wb_obj=op.load_workbook(path)
        sheet_obj=wb_obj.active
        #Dane wejściowe
        dZas=sheet_obj.cell(row=3,column=2)
        dw._dZas.set(dZas.value)

        hZas = sheet_obj.cell(row=4, column=2)
        dw._hZas.set(hZas.value)

        ilZas = sheet_obj.cell(row=5, column=2)
        dw._ilZas.set(ilZas.value)

        gestWody = sheet_obj.cell(row=6, column=2)
        dw._gestWody.set(gestWody.value)

        czasNap = sheet_obj.cell(row=7, column=2)
        dw._czasNap.set(czasNap.value)

        wd = sheet_obj.cell(row=8, column=2)
        dw._wd.set(wd.value)

        nk = sheet_obj.cell(row=9, column=2)
        dw._nk.set(nk.value)

        #Strumienie masy
        mwz = sheet_obj.cell(row=20, column=2)
        st._mwz.set(mwz.value)

        mods = sheet_obj.cell(row=21, column=2)
        st._mods.set(mods.value)

        mwtr1 = sheet_obj.cell(row=22, column=2)
        st._mwtrI.set(mwtr1.value)

        mwtr2 = sheet_obj.cell(row=23, column=2)
        st._mwtrII.set(mwtr2.value)

        mwtr3 = sheet_obj.cell(row=24, column=2)
        st._mwtrIII.set(mwtr3.value)

        mwtr4 = sheet_obj.cell(row=25, column=2)
        st._mwtrIV.set(mwtr4.value)

        mwtr5 = sheet_obj.cell(row=26, column=2)
        st._mwtrV.set(mwtr5.value)

        m1 = sheet_obj.cell(row=27, column=2)
        st._mI.set(m1.value)

        m2 = sheet_obj.cell(row=28, column=2)
        st._mII.set(m2.value)

        m3 = sheet_obj.cell(row=29, column=2)
        st._mIII.set(m3.value)

        m4 = sheet_obj.cell(row=30, column=2)
        st._mIV.set(m4.value)

        m5 = sheet_obj.cell(row=31, column=2)
        st._mV.set(m5.value)

        m6 = sheet_obj.cell(row=32, column=2)
        st._mVI.set(m6.value)

        m7 = sheet_obj.cell(row=33, column=2)
        st._mVII.set(m7.value)

        mps = sheet_obj.cell(row=34, column=2)
        st._mps.set(mps.value)

        modg = sheet_obj.cell(row=35, column=2)
        st._modg.set(modg.value)

        nwp = sheet_obj.cell(row=37, column=2)
        dw._nwp.set(nwp.value)

        nsp = sheet_obj.cell(row=38, column=2)
        dw._nsp.set(nsp.value)

        nnp = sheet_obj.cell(row=39, column=2)
        dw._nnp.set(nnp.value)

        isp = sheet_obj.cell(row=40, column=2)
        de2._isp.set(isp.value)

        inp = sheet_obj.cell(row=41, column=2)
        de2._inp.set(inp.value)

        iznp = sheet_obj.cell(row=42, column=2)
        de2._iznp.set(iznp.value)

        qwoodg = sheet_obj.cell(row=44, column=2)
        it._qwododg.set(qwoodg.value)

        ppp = sheet_obj.cell(row=45, column=2)
        it._ppp.set(ppp.value)

        pzp = sheet_obj.cell(row=46, column=2)
        it._pzp.set(pzp.value)

     # Entalpie/Temperatura
        Twz = sheet_obj.cell(row=3, column=11)
        de1._Twz.set(Twz.value)

        Tpz = sheet_obj.cell(row=4, column=11)
        de1._Tpz.set(Tpz.value)

        Tpkond = sheet_obj.cell(row=5, column=11)
        de1._Tpkond.set(Tpkond.value)

        Tods = sheet_obj.cell(row=6, column=11)
        de1._Tods.set(Tods.value)

        TSH5wyl = sheet_obj.cell(row=7, column=11)
        de1._TSH5wyl.set(TSH5wyl.value)

        THR1wlot = sheet_obj.cell(row=8, column=11)
        de1._TRH1wlot.set(THR1wlot.value)

        TRH2wyl = sheet_obj.cell(row=9, column=11)
        de1._TRH2wyl.set(TRH2wyl.value)

        Tp1 = sheet_obj.cell(row=10, column=11)
        de1._Tp1.set(Tp1.value)

        Tp2 = sheet_obj.cell(row=11, column=11)
        de1._Tp2.set(Tp2.value)

        Tp3 = sheet_obj.cell(row=12, column=11)
        de1._Tp3.set(Tp3.value)

        Tp4 = sheet_obj.cell(row=13, column=11)
        de1._Tp4.set(Tp4.value)

        Tp5 = sheet_obj.cell(row=14, column=11)
        de1._Tp5.set(Tp5.value)

        Tp6 = sheet_obj.cell(row=15, column=11)
        de2._Tp6.set(Tp6.value)

        Tp7 = sheet_obj.cell(row=16, column=11)
        de2._TpVII.set(Tp7.value)

        T1 = sheet_obj.cell(row=17, column=11)
        de2._TI.set(T1.value)

        T2 = sheet_obj.cell(row=18, column=11)
        de2._TII.set(T2.value)

        T3 = sheet_obj.cell(row=19, column=11)
        de2._TIII.set(T3.value)

        T4 = sheet_obj.cell(row=20, column=11)
        de2._TIV.set(T4.value)

        T5 = sheet_obj.cell(row=21, column=11)
        de2._TV.set(T5.value)

        T6 = sheet_obj.cell(row=22, column=11)
        de2._TVI.set(T6.value)

        T7 = sheet_obj.cell(row=23, column=11)
        de2._TVII.set(T7.value)

     #Entalpie/Cisnienie

        pwz = sheet_obj.cell(row=3, column=12)
        de1._pwz.set(pwz.value)

        ppz = sheet_obj.cell(row=4, column=12)
        de1._ppz.set(ppz.value)

        ppkond = sheet_obj.cell(row=5, column=12)
        de1._ppkond.set(ppkond.value)

        pods = sheet_obj.cell(row=6, column=12)
        de1._pods.set(pods.value)

        pSH5wyl = sheet_obj.cell(row=7, column=12)
        de1._pSH5wyl.set(pSH5wyl.value)

        pHR1wlot = sheet_obj.cell(row=8, column=12)
        de1._pRH1wlot.set(pHR1wlot.value)

        pRH2wyl = sheet_obj.cell(row=9, column=12)
        de1._pRH2wyl.set(pRH2wyl.value)

        pp1 = sheet_obj.cell(row=10, column=12)
        de1._pp1.set(pp1.value)

        pp2 = sheet_obj.cell(row=11, column=12)
        de1._pp2.set(pp2.value)

        pp3 = sheet_obj.cell(row=12, column=12)
        de1._pp3.set(pp3.value)

        pp4 = sheet_obj.cell(row=13, column=12)
        de1._pp4.set(pp4.value)

        pp5 = sheet_obj.cell(row=14, column=12)
        de1._pp5.set(pp5.value)

        pp6 = sheet_obj.cell(row=15, column=12)
        de2._pp6.set(pp6.value)

        pp7 = sheet_obj.cell(row=16, column=12)
        de2._ppVII.set(pp7.value)

        p1 = sheet_obj.cell(row=17, column=12)
        de2._pI.set(p1.value)

        p2 = sheet_obj.cell(row=18, column=12)
        de2._pII.set(p2.value)

        p3 = sheet_obj.cell(row=19, column=12)
        de2._pIII.set(p3.value)

        p4 = sheet_obj.cell(row=20, column=12)
        de2._pIV.set(p4.value)

        p5 = sheet_obj.cell(row=21, column=12)
        de2._pV.set(p5.value)

        p6 = sheet_obj.cell(row=22, column=12)
        de2._pVI.set(p6.value)

        p7 = sheet_obj.cell(row=23, column=12)
        de2._pVII.set(p7.value)


        #Entalpia/Entalpia

        iwz = sheet_obj.cell(row=3, column=13)
        de1._iwz.set(iwz.value)

        ipz = sheet_obj.cell(row=4, column=13)
        de1._ipz.set(ipz.value)

        ipkond = sheet_obj.cell(row=5, column=13)
        de1._ipkond.set(ipkond.value)

        iods = sheet_obj.cell(row=6, column=13)
        de1._iods.set(iods.value)

        iSH5wyl = sheet_obj.cell(row=7, column=13)
        de1._iSH5wyl.set(iSH5wyl.value)

        iHR1wlot = sheet_obj.cell(row=8, column=13)
        de1._iRH1wlot.set(iHR1wlot.value)

        iRH2wyl = sheet_obj.cell(row=9, column=13)
        de1._iRH2wyl.set(iRH2wyl.value)


        ip1 = sheet_obj.cell(row=10, column=13)
        de1._ip1.set(ip1.value)

        ip2 = sheet_obj.cell(row=11, column=13)
        de1._ip2.set(ip2.value)

        ip3 = sheet_obj.cell(row=12, column=13)
        de1._ip3.set(ip3.value)

        ip4 = sheet_obj.cell(row=13, column=13)
        de1._ip4.set(ip4.value)

        ip5 = sheet_obj.cell(row=14, column=13)
        de1._ip5.set(ip5.value)

        ip6 = sheet_obj.cell(row=15, column=13)
        de2._ip6.set(ip6.value)

        ip7 = sheet_obj.cell(row=16, column=13)
        de2._ipVII.set(ip7.value)

        i1 = sheet_obj.cell(row=17, column=13)
        de2._iI.set(i1.value)

        i2 = sheet_obj.cell(row=18, column=13)
        de2._iII.set(i2.value)

        i3 = sheet_obj.cell(row=19, column=13)
        de2._iIII.set(i3.value)

        i4 = sheet_obj.cell(row=20, column=13)
        de2._iIV.set(i4.value)

        i5 = sheet_obj.cell(row=21, column=13)
        de2._iV.set(i5.value)

        i6 = sheet_obj.cell(row=22, column=13)
        de2._iVI.set(i6.value)

        i7 = sheet_obj.cell(row=23, column=13)
        de2._iVII.set(i7.value)



        # s=df['Wartość'][0]
        # dw._dZas.set(s)
        # dw._hZas.set(df['Wartość'][1])
        # dw._ilZas.set(df['Wartość'][2])
        # dw._gestWody.set(df['Wartość'][3])
        # dw._czasNap.set(df['Wartość'][4])
        # dw._wd.set(df['Wartość'][5])
        # dw._nk.set(df['Wartość'][6])
        #
        # ## Entalpie/ Temperatura
        # de1._Twz.set(df2['Temperatura pary [C]'][0])
        # de1._Tpz.set(df2['Temperatura pary [C]'][1])
        # de1._Tpkond.set(df2['Temperatura pary [C]'][2])
        # de1._Tods.set(df2['Temperatura pary [C]'][3])
        # de1._TSH5wyl.set(df2['Temperatura pary [C]'][4])
        # de1._TRH1wlot.set(df2['Temperatura pary [C]'][5])
        # de1._TRH2wyl.set(df2['Temperatura pary [C]'][6])
        # de1._Tp1.set(df2['Temperatura pary [C]'][7])
        # de1._Tp2.set(df2['Temperatura pary [C]'][8])
        # de1._Tp3.set(df2['Temperatura pary [C]'][9])
        # de1._Tp4.set(df2['Temperatura pary [C]'][10])
        # de1._Tp5.set(df2['Temperatura pary [C]'][11])
        # de2._Tp6.set(df2['Temperatura pary [C]'][12])
        # de2._TpVII.set(df2['Temperatura pary [C]'][13])
        # de2._TI.set(df2['Temperatura pary [C]'][14])
        # de2._TII.set(df2['Temperatura pary [C]'][15])
        # de2._TIII.set(df2['Temperatura pary [C]'][16])
        # de2._TIV.set(df2['Temperatura pary [C]'][17])
        # de2._TV.set(df2['Temperatura pary [C]'][18])
        # de2._TVI.set(df2['Temperatura pary [C]'][19])
        # de2._TVII.set(df2['Temperatura pary [C]'][20])
        #
        # ##Entalpie/Cisnienie
        #
        # de1._pwz.set(df2['Ciśnienie pary [MPa]'][0])
        # de1._ppz.set(df2['Ciśnienie pary [MPa]'][1])
        # de1._ppkond.set(df2['Ciśnienie pary [MPa]'][2])
        # de1._pods.set(df2['Ciśnienie pary [MPa]'][3])
        # de1._pSH5wyl.set(df2['Ciśnienie pary [MPa]'][4])
        # de1._pRH1wlot.set(df2['Ciśnienie pary [MPa]'][5])
        # de1._pRH2wyl.set(df2['Ciśnienie pary [MPa]'][6])
        # de1._pp1.set(df2['Ciśnienie pary [MPa]'][7])
        # de1._pp2.set(df2['Ciśnienie pary [MPa]'][8])
        # de1._pp3.set(df2['Ciśnienie pary [MPa]'][9])
        # de1._pp4.set(df2['Ciśnienie pary [MPa]'][10])
        # de1._pp5.set(df2['Ciśnienie pary [MPa]'][11])
        # de2._pp6.set(df2['Ciśnienie pary [MPa]'][12])
        # de2._ppVII.set(df2['Ciśnienie pary [MPa]'][13])
        # de2._pI.set(df2['Ciśnienie pary [MPa]'][14])
        # de2._pII.set(df2['Ciśnienie pary [MPa]'][15])
        # de2._pIII.set(df2['Ciśnienie pary [MPa]'][16])
        # de2._pIV.set(df2['Ciśnienie pary [MPa]'][17])
        # de2._pV.set(df2['Ciśnienie pary [MPa]'][18])
        # de2._pVI.set(df2['Ciśnienie pary [MPa]'][19])
        # de2._pVII.set(df2['Ciśnienie pary [MPa]'][20])
        #
        # ##Entalpie/Entalpie
        #
        # de1._iwz.set(df2['Entalpia pary [kJ/kg]'][0])
        # de1._ipz.set(df2['Entalpia pary [kJ/kg]'][1])
        # de1._ipkond.set(df2['Entalpia pary [kJ/kg]'][2])
        # de1._iods.set(df2['Entalpia pary [kJ/kg]'][3])
        # de1._iSH5wyl.set(df2['Entalpia pary [kJ/kg]'][4])
        # de1._iRH1wlot.set(df2['Entalpia pary [kJ/kg]'][5])
        # de1._iRH2wyl.set(df2['Entalpia pary [kJ/kg]'][6])
        # de1._ip1.set(df2['Entalpia pary [kJ/kg]'][7])
        # de1._ip2.set(df2['Entalpia pary [kJ/kg]'][8])
        # de1._ip3.set(df2['Entalpia pary [kJ/kg]'][9])
        # de1._ip4.set(df2['Entalpia pary [kJ/kg]'][10])
        # de1._ip5.set(df2['Entalpia pary [kJ/kg]'][11])
        # de2._ip6.set(df2['Entalpia pary [kJ/kg]'][12])
        # de2._ipVII.set(df2['Entalpia pary [kJ/kg]'][13])
        # de2._iI.set(df2['Entalpia pary [kJ/kg]'][14])
        # de2._iII.set(df2['Entalpia pary [kJ/kg]'][15])
        # de2._iIII.set(df2['Entalpia pary [kJ/kg]'][16])
        # de2._iIV.set(df2['Entalpia pary [kJ/kg]'][17])
        # de2._iV.set(df2['Entalpia pary [kJ/kg]'][18])
        # de2._iVI.set(df2['Entalpia pary [kJ/kg]'][19])
        # de2._iVII.set(df2['Entalpia pary [kJ/kg]'][20])
        #
        #
        #
        # ##Strumienie Masy
        #
        # st._mwz.set(df['Wartość'][17])
        # st._mods.set(df['Wartość'][18])
        # st._mwtrI.set(df['Wartość'][19])
        # st._mwtrII.set(df['Wartość'][20])
        # st._mwtrIII.set(df['Wartość'][21])
        # st._mwtrIV.set(df['Wartość'][22])
        # st._mwtrV.set(df['Wartość'][23])
        # st._mI.set(df['Wartość'][24])
        # st._mII.set(df['Wartość'][25])
        # st._mIII.set(df['Wartość'][26])
        # st._mIV.set(df['Wartość'][27])
        # st._mV.set(df['Wartość'][28])
        # st._mVI.set(df['Wartość'][29])
        # st._mVII.set(df['Wartość'][30])
        # st._mps.set(df['Wartość'][31])
        # st._modg.set(df['Wartość'][32])
        #
        # ##Obliczenia
        # dw._nwp.set(df['Wartość'][34])
        # dw._nsp.set(df['Wartość'][35])
        # dw._nnp.set(df['Wartość'][36])
        # de2._isp.set(df['Wartość'][37])
        # de2._inp.set(df['Wartość'][38])
        # de2._iznp.set(df['Wartość'][39])
        # it._qwododg.set(df['Wartość'][41])
        # it._ppp.set(df['Wartość'][42])
        # it._pzp.set(df['Wartość'][43])
        #
        #









