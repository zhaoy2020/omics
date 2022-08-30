# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 10:13:47 2022

@author: zhao
"""

import os

def doGomoku():
    try:
        os.popen(f'python ./scripts/Games/Gomoku.py')
    except:
        pass 
    
def doSnake():
    try:
        os.popen(f'python ./scripts/Games/Snake.py')
    except:
        pass 
    
def doFlyBrid():
    try:
        os.popen(f'cd scripts/Games/FlyBrid/ && python flappy.py')
    except:
        pass 
    
if __name__ == "__main__":
    '''
    Main function
    '''