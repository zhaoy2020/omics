# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 13:20:15 2022

@author: zhao
"""
import tkinter as tk
import tkinter.ttk as ttk
import matplotlib.pyplot as plt
# 创建画布需要的库
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np

def lanuchCogInter():
    cogGUI = tk.Toplevel()
    
    # 绘图区
    pictureLbFrame=tk.LabelFrame(cogGUI,text='绘图')
    pictureLbFrame.pack(side='left')
# =============================================================================
#     绘图函数部分
# =============================================================================
    fig = Figure(figsize=(5, 4), dpi=100)
    t = np.arange(0, 3, .01)
    ax = fig.add_subplot()
    line, = ax.plot(t, 2 * np.sin(2 * np.pi * t))
    ax.set_xlabel("time [s]")
    ax.set_ylabel("f(t)")
# =============================================================================
#     绘图
# =============================================================================
    canvas = FigureCanvasTkAgg(fig, master=pictureLbFrame)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().pack(side='top', fill='both')
    
    # 参数区
    ctrLbFrame = tk.LabelFrame(cogGUI,text='参数')
    ctrLbFrame.pack(side='left',anchor='n')
    ## 数据
    dtLbFrame = tk.LabelFrame(ctrLbFrame,text='数据')
    dtLbFrame.pack(side='top',anchor='n')
    xLabel = tk.Label(dtLbFrame,text='x')
    xLabel.grid(row=1,column=0)
    xEntry = ttk.Combobox(dtLbFrame)
    xEntry.grid(row=1,column=1)
    
    yLabel = tk.Label(dtLbFrame,text='y')
    yLabel.grid(row=2,column=0)
    yEntry = ttk.Combobox(dtLbFrame)
    yEntry.grid(row=2,column=1)
    # 调参
    prLbFrame = tk.LabelFrame(ctrLbFrame,text='调参')
    prLbFrame.pack(side='top',anchor='n')
    tk.Label(prLbFrame,text='hug').grid(row=1,column=0)
    colorCombobox = ttk.Combobox(prLbFrame)
    colorCombobox.grid(row=1,column=1)
    
    tk.Label(prLbFrame,text='color').grid(row=2,column=0)
    colorCombobox = ttk.Combobox(prLbFrame)
    colorCombobox.grid(row=2,column=1)

    
    

if __name__ == "__main__":
    '''
    Main function
    '''