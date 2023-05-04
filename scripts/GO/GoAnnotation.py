# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 19:44:37 2022

@author: zhao
"""
# import sys
# sys.path.append("D:\\WorkStation\\PyhtonWorkStation\\20220410-comparative\\bmp")
import numpy as np
import pandas as pd
import gzip



if __name__ == "__main__":
    
    # 整理blast结果
    '''
    筛选blast结果
    输入格式为：outfmt 7
    '''
    headInfo = ["query acc.ver","subject acc.ver","% identity","alignment length","mismatches","gap opens","q. start","q. end","s. start","s. end","evalue","bit score"]
    blast = pd.read_table('query/sp_results.txt', header=None, comment='#', names=headInfo)
    '''
    ascending 表示：升序
    query acc.ver 升序
    bit score 降序
    按照query acc.ver进行去重复，保留‘first’，即最佳比对结果    
    '''
    blastFilted = blast.sort_values(by=['query acc.ver', 'bit score'], ascending=[True, False]).drop_duplicates(subset=['query acc.ver'], keep='first')
    
    
    # 用with读取idmapping.tb.gz并创建临时的缓存字典，否则数据太大无法短时间读取
    # (1) UniProtKB accession
    # (2) UniProtKB ID
    # (3) EntrezGene
    # (4) RefSeq
    # (5) NCBI GI number
    # (6) PDB
    # (7) Pfam
    # (8) GO
    # (9) PIRSF
    # (10) IPI
    # (11) UniRef100
    # (12) UniRef90
    # (13) UniRef50
    # (14) UniParc
    # (15) PIR-PSD accession
    # (16) NCBI taxonomy
    # (17) MIM
    # (18) UniGene
    # (19) Ensembl
    # (20) PubMed ID
    # (21) EMBL/GenBank/DDBJ
    # (22) EMBL protein_id
    
    tem = {} # tem:dict {"UniProtKB accession":"GO"}
    with gzip.open('idmapping.tb.gz', 'r') as idmapping:
        for line in idmapping:
            lsplit = line.rstrip().split("\t")
            if lsplit[7]:
                tem[lsplit[0]] = lsplit[7] # lsplit[0]->UniProtKB accession
    
    def annotation(ac):
        key = ac.split(".")[0]
        if key in tem.keys():
            return tem[key]
        else:
            return np.nan
                    
    blastFilted['GO'] = blastFilted['subject acc.ver'].apply(annotation)
    blastFilted.to_csv('GO_results.csv', index=None) # 输出结果文件
    
    
