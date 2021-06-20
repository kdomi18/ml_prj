from numpy import double
import pandas as pd 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import seaborn as sns

data = pd.read_csv("nF_acc.csv") 

# Preview the first 5 lines of the loaded data 
print(data.head())

data.plot(x='nrFeatures', y='accuracy', style='o')
data.plot(x='nrFeatures', y='accuracy', style='o')
sns.set_theme(color_codes=True)
sns.regplot(x="nrFeatures", y="accuracy", data=data, order=2)
sns.regplot(x="nrFeatures", y="accuracy", data=data, order=1)
# sns.regplot(x="nrFeatures", y="accuracy", data=data, order=3)

plt.show()