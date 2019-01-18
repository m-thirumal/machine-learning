import numpy as np
import matplotlib.pyplot as plt
#Seed

np.random.seed(555)

X1 = np.random.normal(100, 15, 200).astype(int)

X2 = np.random.normal(10, 4.5, 200)

X3 = np.random.normal(32, 4, 200).astype(int)

print(X3)
#plot of X3
plt.hist(X3, 30, density=True)
plt.show()
print("-------------------------")
dob = np.datetime64('2017-10-31') - 365 * X3

print(dob)