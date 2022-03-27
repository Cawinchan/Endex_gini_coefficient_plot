import numpy as np
import matplotlib.pyplot as plt

# Generation of 1000 actors with a Gini coefficient of 0.9 (multiplied by 10 for ease of generation)
arr_1000 = np.array(sorted([10000, 7000, 5585,4280, 3627, 772, 715, 634, 595, 500, 360, 336, 295, 288, 280, 275, 265, 215, 212, 162, 157, 152, 148, 145, 142, 132, 130,121, 104, 94, 78, 72, 67, 64, 63, 57, 53, 45, 41, 41, 35, 30, 30,24, 19, 17, 16, 15, 13, 12, 11, 11, 8, 8, 8, 8, 7, 7, 7, 6, 6, 5, 5, 3, 3, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,1,1,1,1,1,1,1,1,1,1,1]*10))
arr_10 = np.array(sorted([1000,600,100,5,5,2,1,1,1,1]))

def gini(arr):
    count = arr.size
    coefficient = 2 / count
    indexes = np.arange(1, count + 1)
    weighted_sum = (indexes * arr).sum()
    total = arr.sum()
    constant = (count + 1) / count
    return coefficient * weighted_sum / total - constant

def lorenz(arr):
    scaled_prefix_sum = arr.cumsum() / arr.sum()
    return np.insert(scaled_prefix_sum, 0, 0)

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