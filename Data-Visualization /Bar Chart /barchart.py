# Python program to show Bar Chart pyplot module

import matplotlib.pyplot as plt
import pandas as pd

# Reading the tips.csv file
x = [10, 20, 30, 40]
y = [10, 29, 45, 22]

# plotting the data
plt.bar(x, y)

# Adding title to the plot
plt.title("Bar Chart")

# Adding label on the y-axis
plt.ylabel('y axis')

# Adding label on the x-axis
plt.xlabel('x axis')

plt.show()
