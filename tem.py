# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 23:46:07 2022

@author: zhao
"""
# import sys
# sys.path.append("D:\\WorkStation\\PyhtonWorkStation\\20220410-comparative\\bmp")
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 



if __name__ == "__main__":
    '''
    Main function
    '''
    df = pd.read_excel('tem.xlsx')
    
    
    def simpleFunction(a:int, b:float, c:str, *d:list, **e:dict) -> (int, int, str):
        '''
        A simple demo about the annotation style of Python function
        '''
        sumResult = a + b + len(c)
        numOFagruments = 3
        return sumResult, numOFagruments, c
    
    print(simpleFunction(1, 2.5, "hellow", ))