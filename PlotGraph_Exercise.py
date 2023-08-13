import pandas as pd
import numpy as np                  #import as np function for basic matlab/math calculations
import matplotlib.pyplot as plt     #import as plt function
import matplotlib                   #ignore, just to check version
print(matplotlib.__version__)       #ignore, just to check version

x = np.linspace(-20 , 20, 200)
y = np.sin(x)
plt.plot(x, y, marker="o")          #plot with markers, but does not show plot
plt.xlabel('X-axis')                #label
plt.ylabel('Y-axis')                #label
plt.title("Graph Title")            #label
plt.show()                          #show plot
