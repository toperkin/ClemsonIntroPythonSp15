import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_table("band.data", sep=" ", header=None)
data = data.dropna(axis=1, how='all')
plt.figure()
data.plot()
plt.savefig('pd_text_import1')


plt.figure()
data.plot(x=2)
plt.savefig('pd_text_import2')

def scale(x):
    return 27.21*x-0.3

data[1:] = data[1: ].apply(scale)

plt.figure()
data.plot(x=2, legend=False)
plt.savefig('pd_text_import3')


plt.figure()
i=0
for col in data.columns:
    if col != 2:
        if data[col].min() > -2 and data[col].max() < 3:
            if i==0:
                ax = data.plot(x=2, y=col, legend=False)
                i=1
            else:
                data.plot(x=2, y=col, legend=False, ax=ax)

plt.savefig('pd_text_import4')
