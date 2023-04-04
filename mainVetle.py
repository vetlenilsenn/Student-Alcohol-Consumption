import pandas as pd
import numpy as np # linear algebra
import seaborn as sns # visualize
import matplotlib.pyplot as plt

df = pd.read_csv(r'archive\student-mat.csv')
print(df)

print(df['Dalc'])
