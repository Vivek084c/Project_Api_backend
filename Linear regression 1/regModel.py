import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


#reading the dataset
df=pd.read_csv("train.csv")
df2=pd.read_csv("test.csv")

# independet feature
X=df[["x"]]
X.head()
print(f"the shape of X is {X.shape}")

X1=df["x"]
print(f"the shape of X1 is {X1.shape}")

Xtest=df[['x']]

#for dependent feature we can have it as a series as it a 1d vector
Y=df['y']
Y.head()
Ytest=df['y']

from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
X=scaler.fit_transform(X)
Xtest=scaler.transform(Xtest)

# appling linear regression
from sklearn.linear_model import LinearRegression

regression=LinearRegression(n_jobs=-1)

regression.fit(X,Y)

