
import program.Classes.Funkcje.FunkcjeIteracjeNN as r

class ZmienneDoIteracji():
    # def __init__(self, tab, itNbr):
    #     self.tab = tab
    #     self.itNbr = itNbr

    def stworzZmienne(self,n):
        mainTab=[
         r.tabIwz[n],
         r.tabMps[n],
         tabMI[n],
         tabMII[n],
         tabMIII[n],
         tabMIV[n],
         tabMV[n],
         tabMVI[n],
         tabMVII[n],
         tabMwt[n],
         tabMsp[n],
         tabMnp[n],
         tabMznp[n],
         tabIskzm[n],
         tabIskXN2[n],
         tabIskXN3[n],
         tabIskXN3A[n],
         tabIskXN4[n],
         tabIskXN5 [n],
         tabIwodODG [n],
         tabIpz [n],
         tabIskXW1[n],
         tabMwz[n],
         tabIskXW2[n],
         tabIskXW3[n]
        ]
        mainTab[tabIskXW2][0]=4
        print(mainTab[tabIskXW2][0])