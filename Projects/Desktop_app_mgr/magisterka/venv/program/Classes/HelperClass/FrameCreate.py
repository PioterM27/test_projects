import tkinter as tk
from tkinter import ttk
from tkinter import *

class FrameCreate(Frame):
     def __init__(self, framex, topic, row, column):
         super(FrameCreate, self).__init__()
         self.framex = framex
         self.topic = topic
         self.row = row
         self.column = column

     def frameCreate(val):
         var2 = Frame(val.framex, width=500, height=310, bd=8, relief="sunken")
         var2.grid(row=val.row, column=val.column)
         varTopic = Label(var2, width=45, bd=2, relief="sunken", text=val.topic,font=("Helvetica", 8))
         varTopic.grid(row=val.row-1, column=val.column, columnspan=10, pady=4)
         return (var2)