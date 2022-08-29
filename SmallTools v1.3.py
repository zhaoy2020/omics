# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 12:24:09 2022

@author: ZhaoYu
@email: zhao_sy@126.com
"""

import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import tkinter.ttk as ttk

import pandas as pd
import os



def blastGUI(root):
    wsFrame = tk.LabelFrame(root,text='work station')
    wsFrame.pack(side='top')
    
    btFrame = tk.Frame(root)
    btFrame.pack(side='top')
    
    dpFrame = tk.LabelFrame(root,text='Parameters')
    dpFrame.pack(side='top')
    
    # create db path label, entry and button
    dbPathLabel = tk.Label(wsFrame,text='DBs path')
    dbPathLabel.grid(row=1, column=0)
    
    dbFilePath = tk.StringVar() # the text content of entry connect with StringVar
    dbPathEntry = tk.Entry(wsFrame, textvariable=dbFilePath)
    dbPathEntry.grid(row=1, column=1)
    
    def openDbFile():
        dbFilePath.set('')
        dbFilePath.set(tk.filedialog.askopenfilename())
    dbPathButton = tk.Button(wsFrame, text='File', command=openDbFile)
    dbPathButton.grid(row=1, column=2, sticky='w')
      
    # create query path label, entry and button
    queryPathLabel = tk.Label(wsFrame,text='Query path')
    queryPathLabel.grid(row=2, column=0)
    
    queryFilePath = tk.StringVar()
    def openQueryFile():
        queryFilePath.set('')
        queryFilePath.set(tk.filedialog.askopenfilename())
    queryPathEntry = tk.Entry(wsFrame, textvariable=queryFilePath)
    queryPathEntry.grid(row=2, column=1)
    queryPathButton = tk.Button(wsFrame, text='File', command=openQueryFile)
    queryPathButton.grid(row=2, column=2, sticky='w')
    
    # create Output path label, entry and button
    outputPathLabel = tk.Label(wsFrame,text='Output path')
    outputPathLabel.grid(row=3, column=0)
    
    outputFilePath = tk.StringVar()
    outputPathEntry = tk.Entry(wsFrame, textvariable=outputFilePath)
    outputPathEntry.grid(row=3, column=1)
    
    def openOutputFile():
        outputFilePath.set('')
        outputFilePath.set(tk.filedialog.askdirectory())
    outputPathButton = tk.Button(wsFrame, text='Dir.', command=openOutputFile)
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
    tk.Button(btFrame, text='format db', command=formatDb).grid(row=1, column=0)
    
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
    tk.Button(btFrame, text='Blast', command=doBlast).grid(row=1, column=1)
    
    def doDefaultParameters():
        cpuThreads.set('7')
        maxHsps.set('1')
        numAlignments.set('1')
        evalue.set('1e-5')
        outfmt.set('6')
        dbType.set('prot')
        blastType.set('blastp(aa/aa)')
    tk.Button(btFrame, text='Default Parameters', command=doDefaultParameters).grid(row=1, column=2)
    
    # create config of parameters
    tk.Label(dpFrame, text='CPU threads').grid(row=5, column=0)
    cpuThreads = tk.StringVar()
    cpuThreadsSpinbox = tk.Spinbox(dpFrame, from_=1, to=16, textvariable=cpuThreads)
    cpuThreadsSpinbox.grid(row=5, column=1)
    
    tk.Label(dpFrame, text='max_hsps').grid(row=6, column=0)
    maxHsps = tk.StringVar()
    max_hspsSpinbox = tk.Spinbox(dpFrame, from_=1, to=100, textvariable= maxHsps)
    max_hspsSpinbox.grid(row=6, column=1)
    
    tk.Label(dpFrame, text='num_alignments').grid(row=7, column=0)
    numAlignments = tk.StringVar()
    num_alignmentsSpinbox = tk.Spinbox(dpFrame, from_=1, to=100, textvariable=numAlignments)
    num_alignmentsSpinbox.grid(row=7, column=1)
    
    tk.Label(dpFrame, text='evalue').grid(row=8, column=0)
    evalue = tk.StringVar()
    evalueSpinbox = tk.Spinbox(dpFrame, from_=0, to=1e-3, increment=0.00001, textvariable=evalue)
    evalueSpinbox.grid(row=8, column=1)
    
    tk.Label(dpFrame, text='outfmt').grid(row=9, column=0)
    outfmt = tk.StringVar()
    outfmtSpingbox = tk.Spinbox(dpFrame, from_=0, to=8, textvariable=outfmt)
    outfmtSpingbox.grid(row=9, column=1)
    
    tk.Label(dpFrame, text='dbtype').grid(row=0, column=0)
    dbType = tk.StringVar()
    # dbtypeSpingbox = tk.Spinbox(dpFrame, values=("prot", "nucl"), textvariable=dbtype)
    # dbtypeSpingbox.grid(row=0, column=1)
    dbTypeCombobox= ttk.Combobox(dpFrame, textvariable=dbType,values=("prot", "nucl"))
    dbTypeCombobox.grid(row=0,column=1)
    
    tk.Label(dpFrame, text='blastType').grid(row=10, column=0)
    blastType = tk.StringVar()
    # blastTypeSpingbox = tk.Spinbox(dpFrame, values=("blastn(nt/nt)", "blastx(nt/aa)", 'tblastn(aa/nt)', 'blastp(aa/aa)'), textvariable=blastType)
    # blastTypeSpingbox.grid(row=10, column=1)
    blastTypeCombobox= ttk.Combobox(dpFrame, textvariable=blastType,values=("blastn(nt/nt)", "blastx(nt/aa)", 'tblastn(aa/nt)', 'blastp(aa/aa)'))
    blastTypeCombobox.grid(row=10,column=1)
    
    # create a text which display the blast program lanuch results
    logFrame = tk.Frame(root)
    logFrame.pack(side='top')
    logText = tk.Text(logFrame, width=35, height=5)
    logText.grid(row=1, column=0)
    
def game(root1):
    pass
    

if __name__ == '__main__':
    '''main function'''
    # window = MainWindow()
    # create root window
    window = tk.Tk()
    window.title('SmallTools version 2.0')
    # 窗口不可扩大
    # window.resizable(0,0)
    # 窗口按比例扩大, 暂时还没搞懂
    
    # 创建主菜单
    mainMenu = tk.Menu(window)
    ## 创建file菜单及其子菜单
    fileMenu = tk.Menu(mainMenu,tearoff=False)
    fileMenu.add_command(label='New')
    fileMenu.add_command(label='Open')
    fileMenu.add_command(label='Close')
    fileMenu.add_command(label='Quit',command=window.quit)
    mainMenu.add_cascade(label='File',menu=fileMenu)
    # 创建edit菜单
    mainMenu.add_cascade(label='Edit')
    # 创建window菜单
    mainMenu.add_cascade(label='Window')
    # 创建game菜单及其子菜单，所有的游戏源码也放在scripts文件夹里面了
    gameMenu = tk.Menu(mainMenu,tearoff=False)
    def doGomoku():
        try:
            os.popen(f'python ./scripts/game/gomoku.py')
        except:
            pass                
    gameMenu.add_command(label='五子棋',command=doGomoku)
    def doSnake():
        try:
            os.popen(f'python ./scripts/game/snake.py')
        except:
            pass                
    gameMenu.add_command(label='贪吃蛇',command=doSnake)
    def doFlyBrid():
        try:
            os.popen(f'cd scripts/game/flyBrid/ && python flappy.py')
        except:
            pass                
    gameMenu.add_command(label='小飞鸟',command=doFlyBrid)
    mainMenu.add_cascade(label='Game',menu=gameMenu)
    # 创建help菜单及其子菜单
    helpMenu = tk.Menu(mainMenu,tearoff=False)
    def doInfo():
        tk.messagebox.showinfo(title='About SmallTools',message='A small bioinformatic tool for biologier.\nVersin 1.3')
    helpMenu.add_command(label='About',command=doInfo)
    helpMenu.add_command(label='Update')
    mainMenu.add_cascade(label='Help',menu=helpMenu)
    # 菜单生效
    window.config(menu=mainMenu)


    tabControl = ttk.Notebook(window) # 创建选项卡对象
    tabControl.pack()
    # 选项卡blastGUI
    root = tk.Frame(tabControl) # 新建选项卡1
    root.pack(side='top')
    tabControl.add(root, text='BlastGUI') # 添加选项卡1至选项卡对象中
    blastGUI(root)
    # 选项卡pyGame
    root1 = tk.Frame(tabControl) # 新建选项卡2
    root1.pack(side='top')
    tabControl.add(root1,text='pyGame') # 添加选项卡2至选项卡对象中
    game(root1)
    
    window.mainloop()
