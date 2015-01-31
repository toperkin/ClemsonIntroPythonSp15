__author__ = 'tony'
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

A = pd.read_table("band.data", sep=" ")
A = A.dropna(axis=1, how='all')

print(A)

"""
genfromtxt reads in line by line. so the array is arranged by rows.
Swapping it out with the transpose is an easy way to switch the rows and columns.
"""

'''
A = A.T

fig = plt.figure()

for k in range(1, len(A)):
    plt.plot(A[0], 27.21*A[k]-0.3)

plt.title('Band')
plt.xlim([A[0].min(), A[0].max()])
fig.savefig("numpy_graphing1.png")

fig2 = plt.figure()

for k in range(1, len(A)):
    if min( 27.21*A[k]-0.3 ) > -2 and max( 27.21*A[k]-0.3 ) < 3:
        plt.plot(A[0], 27.21*A[k]-0.3)

plt.title('Band')
plt.xlim([A[0].min(), A[0].max()])

fig2.savefig("numpy_graphing2.png")
'''