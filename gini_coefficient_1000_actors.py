import numpy as np
from utils import gini,lorenz
import matplotlib.pyplot as plt

# Generation of example 1000 actors with a Gini coefficient of 0.9 (multiplied by 10 for ease of generation)
arr_1000 = np.array(sorted([10000, 7000, 5585,4280, 3627, 772, 715, 634, 595, 500, 360, 336, 295, 288, 280, 275, 265, 215, 212, 162, 157, 152, 148, 145, 142, 132, 130,121, 104, 94, 78, 72, 67, 64, 63, 57, 53, 45, 41, 41, 35, 30, 30,24, 19, 17, 16, 15, 13, 12, 11, 11, 8, 8, 8, 8, 7, 7, 7, 6, 6, 5, 5, 3, 3, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,1,1,1,1,1,1,1,1,1,1,1]*10))

lorenz_curve_1000 = lorenz(arr_1000)

# X values are between 0.0 to 1.0
plt.plot(np.linspace(0.0, 1.0, lorenz_curve_1000.size), lorenz_curve_1000, label='Lorenz_curve', marker='.')
# plot the straight line perfect equality curve
plt.title("Gini coefficient of 1000 actors"+"\n"+"gini:"+str(round(gini(arr_1000),2)))
plt.plot([0,1], [0,1], label='Line of ideal Decentralization')
plt.ylabel("Cumulative Percentage of Ownership")
plt.xlabel("Cumulative Percentage of Population")
plt.legend()
plt.show()