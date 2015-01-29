__author__ = 'tony'

import pandas as pd
import datetime
import random
import matplotlib.pyplot as plt
import pylab as pl
import numpy as np

plt.figure()

df = pd.DataFrame(np.random.randn(1000, 2), columns=['a', 'b'])
df['b'] = df['b'] + np.arange(1000)
df.plot(kind='hexbin', x='a', y='b', gridsize=25)
plt.savefig('hex_scatter.png')


# http://economistry.com/2013/07/easy-data-visualization-with-google-charts-and-a-csv/
data = pd.read_csv('kzn1993.csv')
df2 = pd.DataFrame(data, columns=['meaneduc', 'cm_16_exp'])
df2.plot(kind='hexbin', x='meaneduc', y='cm_16_exp', gridsize=35)
plt.savefig('hex_scatter2.png')
