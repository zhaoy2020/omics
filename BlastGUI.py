
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 12:24:09 2022

@author: ZhaoYu
@email: zhao_sy@126.com
"""

import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

import pandas as pd
import os

# =============================================================================
# 
# class MainWindow():
#     def __init__(self):
#         self.root = tk.Tk()
#         self.root.title('BlastGUI(SmallTools version 2.0)')
#         self.root.geometry('450x350+300+200')
#         # create 
#         self.dbPathLabel = tk.Label(self.root,text='DBs path')
#         self.dbPathLabel.grid(row=1, column=0)
#         self.dbFilePath = tk.StringVar()
#         self.dbPathEntry = tk.Entry(self.root, textvariable=self.dbFilePath)
#         self.dbPathEntry.grid(row=1, column=1)
#         self.dbPathButton = tk.Button(self.root, text='Open', command=self.openDbFile)
#         self.dbPathButton.grid(row=1, column=2)
#   
#         self.root.mainloop()
# 
#     def openDbFile(self):
#         self.dbFilePath.set('')
#         self.dbFilePath.set(tk.filedialog.askopenfilename())
# 
# =============================================================================
if __name__ == '__main__':
    '''main function'''
    # window = MainWindow()
    # create root window
    root = tk.Tk()
    root.title('BlastGUI (SmallTools version 2.0)')
    
    # create db path label, entry and button
    dbPathLabel = tk.Label(root,text='DBs path')
    dbPathLabel.grid(row=1, column=0)
    
    dbFilePath = tk.StringVar() # the text content of entry connect with StringVar
    dbPathEntry = tk.Entry(root, textvariable=dbFilePath)
    dbPathEntry.grid(row=1, column=1)
    
    def openDbFile():
        dbFilePath.set('')
        dbFilePath.set(tk.filedialog.askopenfilename())
    
    dbPathButton = tk.Button(root, text='Open File', command=openDbFile)
    dbPathButton.grid(row=1, column=2, sticky='w')
      
    # create query path label, entry and button
    queryPathLabel = tk.Label(root,text='Query path')
    queryPathLabel.grid(row=2, column=0)
    
    queryFilePath = tk.StringVar()
    def openQueryFile():
        queryFilePath.set('')
        queryFilePath.set(tk.filedialog.askopenfilename())
        
    queryPathEntry = tk.Entry(root, textvariable=queryFilePath)
    queryPathEntry.grid(row=2, column=1)
    queryPathButton = tk.Button(root, text='Open File', command=openQueryFile)
    queryPathButton.grid(row=2, column=2, sticky='w')
    
    # create Output path label, entry and button
    outputPathLabel = tk.Label(root,text='Output path')
    outputPathLabel.grid(row=3, column=0)
    
    outputFilePath = tk.StringVar()
    outputPathEntry = tk.Entry(root, textvariable=outputFilePath)
    outputPathEntry.grid(row=3, column=1)
    
    def openOutputFile():
        outputFilePath.set('')
        outputFilePath.set(tk.filedialog.askdirectory())
    
    outputPathButton = tk.Button(root, text='Open Dir.', command=openOutputFile)
    outputPathButton.grid(row=3, column=2, sticky='w')
    
    def formatDb():
        makedb = "makeblastdb.exe -dbtype "+dbtype.get()+" -in "+ dbFilePath.get()+" -parse_seqids -out "+os.path.join(os.path.dirname(dbFilePath.get()),os.path.basename(dbFilePath.get()).split('.')[0])
        print("start:\n",makedb)
        
        logText.insert("end", makedb) # 在文本末尾插入字符
        logText.insert("end", '\n') # 换行骚操作
        logText.yview_moveto(1) # 定位到文本末尾
        logText.update() # 更新
        os.system(makedb)
        
        print('makedb is ok.')
        logText.insert("end", 'makedb is ok.')
        logText.insert("end", '\n')
        logText.yview_moveto(1)
        logText.update()
        tk.messagebox.showinfo(title='Blast result', message='makedb is ok.')
        
    tk.Button(root, text='format db', command=formatDb).grid(row=4, column=0)
    
    def doBlast():
        
        tem = outputFilePath.get()
        
        if outfmt.get() == '6':
            # lanuchBlast = blastType.get().split("(")[0]+" -num_threads "+cpuThreads.get()+" -query "+queryFilePath.get()+" -db "+tem+"/db"+" -out "+tem+"/results.txt"+" -max_hsps "+maxHsps.get()+" -num_alignments "+numAlignments.get()+" -evalue "+evalue.get()+" -outfmt "+"\""+outfmt.get()+" qseqid sseqid sgi stitle evalue bitscore pident qcovs length mismatch gapopen qstart qend sstart send"+"\""
            lanuchBlast = blastType.get().split("(")[0]+" -num_threads "+cpuThreads.get()+" -query "+queryFilePath.get()+" -db "+os.path.join(os.path.dirname(dbFilePath.get()),os.path.basename(dbFilePath.get()).split('.')[0])+" -out "+tem+"/results.txt"+" -max_hsps "+maxHsps.get()+" -num_alignments "+numAlignments.get()+" -evalue "+evalue.get()+" -outfmt "+"\""+outfmt.get()+" qseqid sseqid sgi stitle evalue bitscore pident qcovs length mismatch gapopen qstart qend sstart send"+"\""
        else:
            # lanuchBlast = blastType.get().split("(")[0]+" -num_threads "+cpuThreads.get()+" -query "+queryFilePath.get()+" -db "+tem+"/db"+" -out "+tem+"/results.txt"+" -max_hsps "+maxHsps.get()+" -num_alignments "+numAlignments.get()+" -evalue "+evalue.get()+" -outfmt "+outfmt.get()
            lanuchBlast = blastType.get().split("(")[0]+" -num_threads "+cpuThreads.get()+" -query "+queryFilePath.get()+" -db "+os.path.join(os.path.dirname(dbFilePath.get()),os.path.basename(dbFilePath.get()).split('.')[0])+" -out "+tem+"/results.txt"+" -max_hsps "+maxHsps.get()+" -num_alignments "+numAlignments.get()+" -evalue "+evalue.get()+" -outfmt "+outfmt.get()
        
        print(lanuchBlast)
        logText.insert("end", lanuchBlast)
        logText.insert("end", '\n')
        logText.yview_moveto(1)
        logText.update()
        os.system(lanuchBlast)
        
        # clean data sheet when outfmt is 6
        if outfmt.get() == '6':
            resultsHeader = ["qseqid", 
                             "sseqid", 
                             "sgi", 
                             "stitle", 
                             "evalue", 
                             "bitscore",
                             "pident", 
                             "qcovs", 
                             "length", 
                             "mismatch",
                             "gapopen", 
                             "qstart", 
                             "qend", 
                             "sstart", 
                             "send"]
            results = pd.read_table(tem+"/results.txt", header=None, names=resultsHeader)
            # results = pd.read_table('test/results.txt', header=None, names=resultsHeader)
            results.to_csv(tem+"/results.csv", index=None)
        else:
            pass
        
        print("Blast is ok.")
        logText.insert("end", 'Blast is ok.')
        logText.insert("end", '\n')
        logText.yview_moveto(1)
        logText.update()
        
# =============================================================================
#         rmTem = "rm "+tem+"/db* "+tem+"/log*"
#         os.system(rmTem)
# =============================================================================
        tk.messagebox.showinfo(title='Blast result', message='Blast is ok.')
        
    # create Blast
    tk.Button(root, text='Blast', command=doBlast).grid(row=4, column=1)
    
    def doDefaultParameters():
        cpuThreads.set('2')
        maxHsps.set('1')
        numAlignments.set('1')
        evalue.set('1e-5')
        outfmt.set('6')
        dbtype.set('prot')
        blastType.set('blastp(aa/aa)')
    
    tk.Button(root, text='Default Parameters', command=doDefaultParameters).grid(row=4, column=2)
    
    # create config of parameters
    tk.Label(root, text='CPU threads').grid(row=5, column=0)
    cpuThreads = tk.StringVar()
    cpuThreadsSpinbox = tk.Spinbox(root, from_=1, to=16, textvariable=cpuThreads)
    cpuThreadsSpinbox.grid(row=5, column=1)
    
    tk.Label(root, text='max_hsps').grid(row=6, column=0)
    maxHsps = tk.StringVar()
    max_hspsSpinbox = tk.Spinbox(root, from_=1, to=100, textvariable= maxHsps)
    max_hspsSpinbox.grid(row=6, column=1)
    
    tk.Label(root, text='num_alignments').grid(row=7, column=0)
    numAlignments = tk.StringVar()
    num_alignmentsSpinbox = tk.Spinbox(root, from_=1, to=100, textvariable=numAlignments)
    num_alignmentsSpinbox.grid(row=7, column=1)
    
    tk.Label(root, text='evalue').grid(row=8, column=0)
    evalue = tk.StringVar()
    evalueSpinbox = tk.Spinbox(root, from_=0, to=1e-3, increment=0.00001, textvariable=evalue)
    evalueSpinbox.grid(row=8, column=1)
    
    tk.Label(root, text='outfmt').grid(row=9, column=0)
    outfmt = tk.StringVar()
    outfmtSpingbox = tk.Spinbox(root, from_=0, to=8, textvariable=outfmt)
    outfmtSpingbox.grid(row=9, column=1)
    
    tk.Label(root, text='dbtype').grid(row=0, column=0)
    dbtype = tk.StringVar()
    dbtypeSpingbox = tk.Spinbox(root, values=("prot", "nucl"), textvariable=dbtype)
    dbtypeSpingbox.grid(row=0, column=1)
    
    tk.Label(root, text='blastType').grid(row=10, column=0)
    blastType = tk.StringVar()
    blastTypeSpingbox = tk.Spinbox(root, values=("blastn(nt/nt)", "blastx(nt/aa)", 'tblastn(aa/nt)', 'blastp(aa/aa)'), textvariable=blastType)
    blastTypeSpingbox.grid(row=10, column=1)
    
    # create a text which display the blast program lanuch results
    logFrame = tk.Frame(root)
    logFrame.grid(row=11, column=0, rowspan=2, columnspan=3)
    logText = tk.Text(logFrame, width=50, height=5)
    logText.grid(row=0, column=0)
    
    
    root.mainloop()
