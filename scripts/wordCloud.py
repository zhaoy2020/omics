# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 19:31:21 2021

@author: Bio-windows
"""

import numpy as np
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
import pandas as pd
import argparse 



def wordCloud(record_handle, picture_handle, output_file_name):
    # text = pd.read_table(record_handle)[['来源出版物', '% of 2528']].dropna().set_index('来源出版物')['% of 2528'].to_dict()
    text = pd.read_table(record_handle).iloc[:, [0, 2]].dropna()
    text = text.set_index(text.columns[0])[text.colums[1]].to_dict()
    
    
    alice_mask = np.array(Image.open(picture_handle))
    
    wc = WordCloud(background_color="white", max_words=2000, mask=alice_mask, contour_width=3, contour_color='steelblue', random_state= 1)
    # generate word cloud
    wc.generate_from_frequencies(text)
    image_colors = ImageColorGenerator(alice_mask)
    
    wc.to_file(output_file_name + '.pdf')

if __name__ == '__main__':
    '''
    process
    '''