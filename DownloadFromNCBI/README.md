# 简述
# 在线安装aspera
```shell
conda install aspera-cli
```
# 本地安装aspera
## 先从anaconda下载aspera-cli:https://anaconda.org/HCC/aspera-cli/files
```shell
conda install aspera-cli-3.9.6-h5e1937b_0.tar.bz2i
```

# 使用
```python
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
```

