__author__ = 'tony'
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data1 = pd.read_csv('price-of-a-dozen-eggs-19001993-i.csv')
plt.figure()
plt.plot(data1.Price)
plt.savefig('price-of-eggs-no-err')


data2 = pd.read_csv('price-of-a-dozen-eggs-19001993-i.csv')
plt.figure()
plt.plot(data2.iloc[:,1])
plt.savefig('price-of-eggs-no-err-2')