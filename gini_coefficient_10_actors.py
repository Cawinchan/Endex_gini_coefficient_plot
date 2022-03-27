import numpy as np
from utils import gini,lorenz
import matplotlib.pyplot as plt

# Generation of example 10 actors with a Gini coefficient of 0.8
arr_10 = np.array(sorted([1000,600,100,5,5,2,1,1,1,1]))

lorenz_curve_10 = lorenz(arr_10)

# X values are between 0.0 to 1.0
plt.plot(np.linspace(0.0, 1.0, lorenz_curve_10.size), lorenz_curve_10, label='Lorenz_curve', marker='.')
# plot the straight line perfect equality curve
plt.title("Gini coefficient of 10 actors"+"\n"+"gini:"+str(round(gini(arr_10),2)))
plt.plot([0,1], [0,1], label='Line of ideal Decentralization')
plt.ylabel("Cumulative Percentage of Ownership")
plt.xlabel("Cumulative Percentage of Population")
plt.legend()
plt.show()