import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

price = pd.Series(np.random.randn(150).cumsum(), index=pd.date_range('2000-1-1', periods=150, freq='B'))
ma = pd.rolling_mean(price, 20)
mstd = pd.rolling_std(price, 20)
plt.figure()
plt.plot(ma.index, ma, 'b')
plt.fill_between(mstd.index, ma-2*mstd, ma+2*mstd, color='b', alpha=0.2)
plt.savefig('line_w_error')