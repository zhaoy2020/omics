# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 13:17:29 2022
@author: zhao
"""
import os

if __name__ == "__main__":
    '''
    Main function
    '''
    
    for num in range(62):
        # print(f'{num:02}')
        cmd = 'ascp -QT -l 300m -i ~/miniconda3/envs/aspera/etc/asperaweb_id_dsa.openssh anonftp@ftp.ncbi.nlm.nih.gov:/blast/db/v5/nr.'+f'{num:02}'+'.tar.gz  ./nr'
        print(cmd)
        os.popen(cmd)
