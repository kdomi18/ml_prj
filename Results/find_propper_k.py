from numpy import double
import pandas as pd 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import seaborn as sns

data = pd.read_csv("knn_k_acc.csv") 

# Preview the first 5 lines of the loaded data 
print(data.head())

data.plot(x='knn_k', y='accuracy', style='o')
data.plot(x='knn_k', y='accuracy', style='o')
sns.set_theme(color_codes=True)
sns.regplot(x="knn_k", y="accuracy", data=data, order=2)
sns.regplot(x="knn_k", y="accuracy", data=data, order=1)

plt.show()