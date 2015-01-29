__author__ = 'tony'
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('price-of-a-dozen-eggs-19001993-i.csv')
price = pd.Series(data.Price)
ma = pd.rolling_mean(price, 10, center=True)
mstd = pd.rolling_std(price, 10, center=True)
plt.figure()
plt.plot(data.Price)
plt.fill_between(mstd.index, ma-2*mstd, ma+2*mstd, color='b', alpha=0.2)
plt.savefig('price-of-eggs')