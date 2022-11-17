import matplotlib.pyplot as plt
import numpy as numpy 
import pandas as pd
from pandas.plotting import scatter_matrix
from sklearn.datasets import load_wine

data = load_wine()
wine = pd.DataFrame(data.data, columns=data.feature_names)
scatter_matrix(wine.iloc[:,[0,5]])
plt.savefig("plot.png")
plt.show()