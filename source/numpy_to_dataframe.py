import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data_amzn = np.genfromtxt("AMZN-KO/AMZN.csv", delimiter=",")
data_ko = np.genfromtxt("AMZN-KO/KO.csv", delimiter=",")

merged = np.concatenate((data_amzn[2:,1:3], data_ko[2:,1:3]), axis=1)
df = pd.DataFrame(merged)

plt.figure()
df.plot(kind='hexbin',  x=0, y=2, gridsize=20)
plt.savefig("amzon-ko-hex")
