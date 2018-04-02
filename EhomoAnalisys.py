from matplotlib import pyplot as plt
import matplotlib.lines as mpatches
import numpy as np
from XxlSearch import GetDF

df = GetDF("Data.xlsx")
plt.plot(df["Ehomo"],df["EbindLa"], "bo")
plt.show()