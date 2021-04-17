import tkinter.filedialog
import sys
import wget as wg
import inspect as ins

# tkinter.filedialog.asksaveasfilename()
# tkinter.filedialog.asksaveasfile()
# tkinter.filedialog.askopenfilename()
# tkinter.filedialog.askopenfile()
# tkinter.filedialog.askdirectory()
# tkinter.filedialog.askopenfilenames()
# tkinter.filedialog.askopenfiles()


import tkinter as tk
from tkinter import filedialog as fd
from tkinter.filedialog import asksaveasfile
import os as os


class FileDialog():
    def __init__(self):
        pass

    def callback(self):
        name = fd.askopenfilename(title="Select a File", filetype=(("Excel", "*.xlsx"), ("Excel", "*.xls")))
        return name

    def callback2(self):
        # f=open('arkusz.png')
        # fd.askopenfile('arkusz.png')
        # file=open('r',"arkusz.png")
        # file = fd.asksaveasfile(filetypes=file)
        # fd.askopenfile(initialfile='arkusz.png')
        # name=fd.askopenfile('r',initialfile='venv/program/Classes/HelperClass/arkusz.png')
        # fd.asksaveasfile('r',initialfile=name)
        #f=open('/FileDialog.py/arkusz.png')
        nazaw=os.getcwd()
        # classPAth=ins.getfile(FileDialog.__class__)
        # classPAth=os.path.abspath(sys.modules[FileDialog.__module__].__file__)
        # filePAth=('Classes/ExcelOpenFile/pythonExcel2.xlsx')
        filePAth = ('Classes/ExcelOpenFile/Formularz.xlsx')
        print(nazaw)
        # path = 'D:\\KursAI\\pythonprojects\\venv\\magisterka_version2\\venv\\program\\Classes\\ExcelOpenFile\\pythonExcel2.xlsx'
        newPath=nazaw[:-4]
        # lastPath=newPath+filePAth
        lol=os.path.join(newPath,filePAth)
        print(newPath)
        print(filePAth)
        # print(lastPath)
        print(lol)

        # print(os.path.isfile("venv/program/Classes/ExcelOpenFile/arkusz.png"))
        os.startfile(lol, 'open')

         # print(os.fspath())
         # fd.askdirectory()






    # errmsg = 'Error!'
# tk.Button(text='Click to Open File',
#         command=callback).pack(fill=tk.X)
# tk.mainloop()
