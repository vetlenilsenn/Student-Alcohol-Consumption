import pandas as pd
import numpy as np # linear algebra
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
import matplotlib.pyplot as plt


#Reading our csv file and saving it to "df"
df = pd.read_csv('archive\student-mat.csv')

#Dropping collums we will not need
df.drop(["school", "address", "famsize", "reason", "Medu", "Fedu", "Mjob", "Fjob", "traveltime", "famsup", "paid", "activities", "nursery"], axis=1, inplace=True)
print(df)

"""
Data we have desited to keep and use:
sex - student's sex (binary: 'F' - female or 'M' - male)
age - student's age (numeric: from 15 to 22)
Pstatus - parent's cohabitation status (binary: 'T' - living together or 'A' - apart)
guardian - student's guardian (nominal: 'mother', 'father' or 'other')
studytime - weekly study time (numeric: 1 - <2 hours, 2 - 2 to 5 hours, 3 - 5 to 10 hours, or 4 - >10 hours)
failures - number of past class failures (numeric: n if 1<=n<3, else 4)
schoolsup - extra educational support (binary: yes or no)
higher - wants to take higher education (binary: yes or no)
internet - Internet access at home (binary: yes or no)
romantic - with a romantic relationship (binary: yes or no)
famrel - quality of family relationships (numeric: from 1 - very bad to 5 - excellent)
freetime - free time after school (numeric: from 1 - very low to 5 - very high)
goout - going out with friends (numeric: from 1 - very low to 5 - very high)
Dalc - workday alcohol consumption (numeric: from 1 - very low to 5 - very high)
Walc - weekend alcohol consumption (numeric: from 1 - very low to 5 - very high)
health - current health status (numeric: from 1 - very bad to 5 - very good)
absences - number of school absences (numeric: from 0 to 93)

These grades are related with the course subject, Math or Portuguese:
G1 - first period grade (numeric: from 0 to 20)
G2 - second period grade (numeric: from 0 to 20)
G3 - final grade (numeric: from 0 to 20, output target)
"""

#Dropping all values that are NA
df.dropna(inplace=True)

#Combine weekdays alcohol consumption with weekend alcoho consumption to find total alcohol consumption
df = df.assign(drinksTotal=df['Dalc'] + df['Walc'])

#Placing all the people that does drink alcohol in one column
df = df.assign(doesDrink=df["drinksTotal"]>=1)

print(df)

print(df['doesDrink'].value_counts())

print("hei")

features = ["Dalc", "Walc"]
X = df.loc[:, features]
y = df.loc[:, ['drinksTotal']]

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0, train_size = .75)

reg = DecisionTreeRegressor(max_depth = 2, random_state = 0)

reg.fit(X_train, y_train)
reg.predict(X_test[0:10])
X_test.head(1)