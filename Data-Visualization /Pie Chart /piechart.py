# Python program to show Pie Chart pyplot module

import matplotlib.pyplot as plt
import pandas as pd
 

# initializing the data
flowers = ['LILIES', 'SUNFLOWERS', 'DAISIES',
        'ROSES', 'VIOLETS',]
data = [23, 10, 35, 15, 12]
 
# plotting the data
plt.pie(data, labels=flowers)
 
# Adding title to the plot
plt.title("Flourist Data")
 
plt.show()
