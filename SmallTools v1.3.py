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


from scripts.BlastGUI.Blast import lanuchBlastInter
from scripts.BlastGUI.Other import lanuchOtherInter

from scripts.GO.Idmapping import lanuchIdmappintInter

from scripts.Games.Game import doGomoku
from scripts.Games.Game import doSnake
from scripts.Games.Game import doFlyBrid



if __name__ == '__main__':
    '''main function'''
    # window = MainWindow()
    # create root window
    window = tk.Tk()
    window.title('SmallTools V1.3')
    # 窗口不可扩大
    window.geometry("300x300") # x必须小写
    # window.resizable(0,0)
    # 窗口按比例扩大, 暂时还没搞懂
    
    # 创建主菜单
    mainMenu = tk.Menu(window)
# =============================================================================
    ## 创建菜单及其子菜单
    fileMenu = tk.Menu(mainMenu,tearoff=False)
    fileMenu.add_command(label='Blast',command=lanuchBlastInter)
    fileMenu.add_command(label='Other',command=lanuchOtherInter)
    mainMenu.add_cascade(label='BlastGUI',menu=fileMenu)
    # 创建菜单
    goMenu = tk.Menu(mainMenu,tearoff=False)
    goMenu.add_command(label='idmapping',command=lanuchIdmappintInter)
    goMenu.add_command(label='interproscan')
    goMenu.add_command(label='eggnog')
    mainMenu.add_cascade(label='GO',menu=goMenu)
# =============================================================================
    # 创建菜单
    mainMenu.add_cascade(label='KEGG')
# =============================================================================
    # 创建菜单
    mainMenu.add_cascade(label='COG')
# =============================================================================
    # 创建game菜单及其子菜单，所有的游戏源码也放在scripts文件夹里面了
    gameMenu = tk.Menu(mainMenu,tearoff=False)
    gameMenu.add_command(label='五子棋',command=doGomoku)
    gameMenu.add_command(label='贪吃蛇',command=doSnake)
    gameMenu.add_command(label='小飞鸟',command=doFlyBrid)
    mainMenu.add_cascade(label='Games',menu=gameMenu)
    # 创建help菜单及其子菜单
    helpMenu = tk.Menu(mainMenu,tearoff=False)
    def doInfo():
        tk.messagebox.showinfo(title='About SmallTools',message='A small bioinformatic tool for biologier.\nVersin 1.3')
    helpMenu.add_command(label='About',command=doInfo)
    helpMenu.add_command(label='Update')
    mainMenu.add_cascade(label='Help',menu=helpMenu)
# =============================================================================

    # 菜单生效
    window.config(menu=mainMenu)
    
    # 主界面
    mainInter = tk.Frame(window)
    mainInter.pack(side='top',expand='yes',anchor='center',fill='both')
    poem = '''
    北国风光，千里冰封，万里雪飘。
    望长城内外，惟余莽莽；
    大河上下，顿失滔滔。
    山舞银蛇，原驰蜡象，欲与天公试比高。
    须晴日，看红装素裹，分外妖娆。
    江山如此多娇，引无数英雄竞折腰。
    惜秦皇汉武，略输文采；
    唐宗宋祖，稍逊风骚。
    一代天骄，成吉思汗，只识弯弓射大雕。
    俱往矣，数风流人物，还看今朝。
    '''
    tk.Label(mainInter, text=poem,justify='left').pack(side='top')
    tk.Label(mainInter, text='--毛泽东',justify='right').pack()
    
    window.mainloop()
