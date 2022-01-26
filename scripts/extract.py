# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 18:26:02 2021

提取序列模块

@author: Bio-windows
"""


import pandas as pd
from Bio import SeqIO


def extract(db_handle, extract_list_handle):
    '''从fasta数据库中，按要求提取序列
        db_handle:数据库的位置
        extract_list_handle:要提取的序列列表
        函数最终返回的的含有SeqRecord类的列表
    '''
    
    extract_list = pd.read_table(extract_list_handle, header=None)
            
    store = [] # 临时存放Bio.SeqRecord对象
    
    num = 0 # 计数
    
    for rec in SeqIO.parse(db_handle, format='fasta'):
        for rec_extr in extract_list[0].values:
            if rec.name == rec_extr:
                num = num + 1 # 序号和计数
                print('提取', rec.name, num)
                if rec: # 判断rec是否为空，不为空则添加到store列表中，表示成功提取
                    store.append(rec)
    return store 


if __name__ == '__main__':
    '''main function'''
# =============================================================================
# #如下例子
    # db_handle = 'D:/workstations/Python_Proj/20210126-effectors/db/bacillus_subtilis_GLB191-201011.faa'
#     extract_list_handle = 'D:/workstations/Python_Proj/20210126-effectors/overlap/six_result_venn.cdg1.and.cdg2.and.solution.and.total.common.16.txt'
# =============================================================================
