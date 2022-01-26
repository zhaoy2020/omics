# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 11:03:55 2021

@author: Bio-windows
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from venn import venn
from upsetplot import generate_counts
from upsetplot import plot


if __name__ == '__main__':
    '''main function'''
    # 只能做2-6个venn图
    musicians = {
        "Members of The Beatles": {"Paul McCartney", "John Lennon", "George Harrison", "Ringo Starr"},
        "Guitarists": {"John Lennon", "George Harrison", "Jimi Hendrix", "Eric Clapton", "Carlos Santana"},
        "Played at Woodstock": {"Jimi Hendrix", "Carlos Santana", "Keith Moon"},
        "haha": {"Jimi Hendrix", "Carlos Santana"},
        "hah1": {"Jimi Hendrix", "Carlos Santana"},
        "hah2": {"Jimi Hendrix", "Carlos Santana"},
    }
venn(musicians)

    example = generate_counts()
    plot(example, show_counts='%d')
