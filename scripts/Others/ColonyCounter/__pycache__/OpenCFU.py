# -*- coding: utf-8 -*-
"""
Created on Thu May  4 22:13:43 2023

@author: zhao
"""
# =============================================================================
# # import sys
# # sys.path.append("D:\\WorkStation\\PyhtonWorkStation\\20220410-comparative\\bmp")
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt 
# # mpl.rcParams['pdf.fonttype'] = 42 
# # plt.rc('font',family='Times New Roman')
# 
# =============================================================================
import os
import tkinter as tk
from tkinter import ttk

class OpenCFU(tk.Frame):
    '''
    OpenCFU interface
    '''
    def __init__(self, master=None):
        super().__init__(master)
        # self.pack()

        self.entrythingy = tk.Entry()
        self.entrythingy.pack()

        # Create the application variable.
        self.contents = tk.StringVar()
        # Set it to some value.
        self.contents.set("this is a variable")
        # Tell the entry widget to watch this variable.
        self.entrythingy["textvariable"] = self.contents

        # Define a callback for when the user hits return.
        # It prints the current value of the variable.
        self.entrythingy.bind('<Key-Return>', self.print_contents)
        
    def print_contents(self, event):
        print("Hi. The current entry content is:", self.contents.get())

if __name__ == "__main__":
    '''
    Main function
    '''
# =============================================================================
#     main windows
# =============================================================================
    root = tk.Tk()
    root.title('openCFU')
    root.geometry("350x300")
    
    mianWindow = OpenCFU()
    
    root.mainloop()
