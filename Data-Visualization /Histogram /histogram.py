# Python program to show Histogram pyplot module

import matplotlib.pyplot as plt
import pandas as pd

# plot x
x = [10, 20, 30, 40]
plt.hist(x, bins=10)
plt.show()

# histogram

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
 
# Using numpy random function to generate random data
np.random.seed(19685689)
 
mu, sigma = 120, 30
x = mu + sigma * np.random.randn(10000)
 
# passing the histogram function
n, bins, patches = plt.hist(x, 70, histtype='bar', density=True, facecolor='pink', alpha=0.80)
 
 
plt.xlabel('Values')
plt.ylabel('Probability Distribution')
plt.title('Histogram showing Data Distribution')
plt.xlim(50, 180)
plt.ylim(0, 0.04)
plt.grid(True)
plt.show()
