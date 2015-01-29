__author__ = 'tony'

import matplotlib.pyplot as plt
from pandas import read_csv
from pandas.tools.plotting import andrews_curves

data = read_csv('iris.data')
plt.figure()

andrews_curves(data, 'Name')

plt.savefig('andrews')