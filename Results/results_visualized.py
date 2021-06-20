from numpy import double
import pandas as pd 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm


data = pd.read_csv("final.csv") 

# Preview the first 5 lines of the loaded data 
print(data.head())
print(data.describe())

data.plot(x='trainNums', y='accuracy', style='o')
fig = plt.figure()
ax = Axes3D(fig)
ax.set_xlabel('trainNums')
ax.set_ylabel('EnergyPercentage')
ax.set_zlabel('accuracy')
ax.plot_trisurf(data.trainNums, data.energyPercentage, data.accuracy, cmap=cm.jet, linewidth=0.2)
data.plot(x='energyPercentage', y='accuracy', style='o')


plt.show()