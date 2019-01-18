import tensorflow as tf
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame as DF

m = tf.constant(3.0, name='m')
c = tf.constant(1.5, name='c')
x = tf.placeholder(dtype="float32", name='x')
#Line equation

y=m*x+c
sess = tf.Session()

print("hi")
print("y = ", y.eval({x:2}, session=sess))

## Second

a = tf.constant([2, 1])
b = tf.constant(1)

print(sess.run(a + b))

# Create dataset
np.random.seed(555)

# IQ
X1 = np.random.normal(100, 15, 200).astype(int)
# Years of exp
X2 = np.random.normal(10, 4.5, 200)
# dob
X3 = np.random.normal(32, 4, 200).astype(int)
dob = np.datetime64('2017-10-31') - 365 * X3

b = 5

er = np.random.normal(0, 1.5, 200)
Y = np.array([0.3*x1 + 1.5*x2 + 0.83*x3 + b + e for x1,x2,x3,e in zip(X1,X2,X3,er)])
print(Y.size)

# Data Cleaning
cols = ['iq','years_experience','dob']
df = DF(list(zip(X1,X2,dob)), columns=cols)
print (df.describe())
# There is a negative value for year of experience
df = df[df.years_experience >= 0]
print("After cleaning \n", df.describe())

print("Date in describe: ", df.describe(include=['datetime64']))

#plotting
pd.plotting.scatter_matrix(df, figsize=(16, 9));
plt.show()
#df['income'] = Y
print(df.info())

# Heat map
plt.figure(figsize=(12, 9))
sns.heatmap(df.corr())
plt.show()