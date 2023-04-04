import pandas as pd
import numpy as np # linear algebra
import seaborn as sns # visualize
import matplotlib.pyplot as plt

df = pd.read_csv('archive\student-mat.csv')
df.drop(["address"], ["famsize"])



print(df)

print(df['Dalc'])
