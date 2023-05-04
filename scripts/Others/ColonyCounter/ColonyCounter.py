# -*- coding: utf-8 -*-
"""
Created on Thu May  4 18:26:47 2023

@author: zhao
"""

import tkinter as tk
import tkinter.ttk as ttk
import matplotlib.pyplot as plt

# 创建画布需要的库
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
import pandas as pd

def lanuchColonyCounterInter():
    GUI = tk.Toplevel()
    
    # 绘图区
    pictureLbFrame=tk.LabelFrame(GUI,text='绘图')
    pictureLbFrame.pack(side='left')
# =============================================================================
#     绘图函数部分
# =============================================================================
    fig = Figure(figsize=(5, 4), dpi=100)
    # ax = fig.add_subplot()
    # t = np.arange(0, 3, .01)
    # line, = ax.plot(t, 2 * np.sin(2 * np.pi * t))
    # ax.set_xlabel("time [s]")
    # ax.set_ylabel("f(t)")
# =============================================================================
#     绘图
# =============================================================================
    canvas = FigureCanvasTkAgg(fig, master=pictureLbFrame)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().pack(side='top', fill='both')
    
    # 参数区
    ctrLbFrame = tk.LabelFrame(GUI,text='参数')
    ctrLbFrame.pack(side='left',anchor='n')
    ## 数据
    dtLbFrame = tk.LabelFrame(ctrLbFrame,text='数据')
    dtLbFrame.pack(side='top',anchor='n')
    tk.Label(dtLbFrame,text='Data').grid(row=1,column=0)
    
    dataPath = tk.StringVar()
    dtEntry = tk.Entry(dtLbFrame,textvariable=dataPath)
    dtEntry.grid(row=1,column=1)
    def openData():
        dataPath.set(tk.filedialog.askopenfilename())
    dtButton = tk.Button(dtLbFrame,text='File',command=openData)
    dtButton.grid(row=1,column=2)
    tk.Label(dtLbFrame,text='Sep').grid(row=2,column=0)
    
    dataType = tk.StringVar()
    dtCombobox = ttk.Combobox(dtLbFrame,textvariable=dataType,values=("tsv", "csv","excel"))
    dtCombobox.grid(row=2,column=1)
    
    def doRead():
        global df
        try:
            if dataType.get() == 'tsv':
                df = pd.read_table(dataPath.get())
            elif dataType.get() == 'csv': 
                df = pd.read_csv(dataPath.get())
            elif dataType.get() == 'excel':
                df = pd.read_excel(dataPath.get())
            else:
                tk.messagebox.showerror(title='Error',message='请确认文本格式')
        except:
            tk.messagebox.showerror(title='Error',message='格式错误')
        print(df)
        xCombobox['values'] = tuple(df.columns)
        yCombobox['values'] = tuple(df.columns)
    readButton = tk.Button(dtLbFrame,text='Read',command=doRead)
    readButton.grid(row=2,column=2)
    
    
    # 调参
    prLbFrame = tk.LabelFrame(ctrLbFrame,text='调参')
    prLbFrame.pack(side='top',anchor='n')
    
    xLabel = tk.Label(prLbFrame,text='x')
    xLabel.grid(row=1,column=0)
    xCombobox = ttk.Combobox(prLbFrame)
    xCombobox.grid(row=1,column=1)
    
    yLabel = tk.Label(prLbFrame,text='y')
    yLabel.grid(row=2,column=0)
    yCombobox = ttk.Combobox(prLbFrame)
    yCombobox.grid(row=2,column=1)
    
    tk.Label(prLbFrame,text='hug').grid(row=3,column=0)
    colorCombobox = ttk.Combobox(prLbFrame)
    colorCombobox.grid(row=3,column=1)
    
    tk.Label(prLbFrame,text='color').grid(row=4,column=0)
    colorCombobox = ttk.Combobox(prLbFrame)
    colorCombobox.grid(row=4,column=1)
    def doClear():
        fig.clf()
        fig.canvas.draw()
    tk.Button(prLbFrame,text='Clear',command=doClear).grid(row=5,column=0)
    def doDraw():
        fig.clf()
        ax = fig.add_subplot()
        t = np.arange(0, 3, .01)
        line, = ax.plot(t, 2 * np.sin(2 * np.pi * t))
        ax.set_xlabel("time [s]")
        ax.set_ylabel("f(t)")
        fig.canvas.draw() # 注意，此步很重要        
    tk.Button(prLbFrame,text='Draw',command=doDraw).grid(row=5,column=1)
    def doDemo():
        fig.clf()
        ax = fig.add_subplot()
        t = np.arange(0, 3, .01)
        line, = ax.plot(t, 10 * np.sin(2 * np.pi * t))
        ax.set_xlabel("time [s]")
        ax.set_ylabel("f(t)")
        fig.canvas.draw() # 注意，此步很重要  
    tk.Button(prLbFrame,text='Demo',command=doDemo).grid(row=5,column=2)

    
    

if __name__ == "__main__":
    '''
    Main function
    '''