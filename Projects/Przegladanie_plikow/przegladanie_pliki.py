"""Program do skopiowania zdjęć z danego okresu czasu"""

import shutil
import os
import datetime
from PIL import Image, ImageFilter
import time
import shutil


# folderName=None
# dateFrom=None
# dateTo=None
# path=None
pathFrom="D:"
pathTo="D:"

datetimeFrom=datetime.date(2018,8,7)
datetimeTo=datetime.date(2018,8,9)
list=os.listdir("D")
dlugosc= len(list)
print(dlugosc)
print(list)
print(list[0])
print(int('09'))
print(int('29'))


def copyToProperFolder(pathFrom,pathTo,datetimeFrom,datetimeTo,fileList):
    newFolder=os.mkdir(pathTo)
    for item in range(0,dlugosc):
        pictureName=fileList[item]
        # print(fileList[item])
        year=int(pictureName[4:8])
        month=int(pictureName[9:10])
        day=int(pictureName[10:12])
        print("rok " + str(year))
        print("miesiac " + str(month))
        print("dzien " + str(day))
        datetimeCurrent=datetime.date(year,month,day)
        if(datetimeCurrent>=datetimeFrom and datetimeCurrent<=datetimeTo):
                lol = os.path.join(pathFrom, pictureName)
                shutil.move(lol,pathTo)
        else:
                continue



copyToProperFolder(pathFrom,pathTo,datetimeFrom,datetimeTo,list)



# if(datetime1==datetime2):
#     print("true")
# else:
#     print("nie równe")

# print(datetime1)





# f = open("D:\Moj telefon Mi 6\zdjecia\IMG_20171229_163805_BURST3.jpg", "w", -1, "utf-8")
# f.write("Jakiś tam tekst")
# f.close()
# # print(time.ctime(os.path.getctime("D:\Moj telefon Mi 6\zdjecia\IMG_20171229_163805_BURST3.jpg")))
# print(time.ctime(os.path.getmtime("D:\Moj telefon Mi 6\zdjecia\IMG_20171229_163805_BURST3.jpg")))

# def copyToProperFolder(pathFrom,pathTo,datetimeFrom,datetimeTo,fileList):
#     newFolder=os.mkdir(pathTo)
#     for item in fileList:
#         pictureName=str(fileList[item])
#         year=pictureName[4:8]
#         month=pictureName[9:10]
#         day=pictureName[11:12]
#         datetimeCurrent=datetime.date(year,month,day)
#         try:
#             if(datetimeCurrent>=datetimeFrom and datetimeCurrent<=datetimeTo):
#                 shutil.move(pathFrom,pathTo)
#             else:
#                 pass
#         except:
#             print("Zły plik")
#
#

# list=os.listdir("D:\Moj telefon Mi 6\zdjecia")
# string=list[0]
# print(string[4:8])
# print(string[8:10])
# print(string[10:12])
# # file=Image.open('D:\Moj telefon Mi 6\zdjecia\IMG_20171229_163805_BURST3.jpg')
# file=Image.
# print(file)