# -*- coding: utf-8 -*-
"""Titanic-LogisticRegression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kc0Ic3_AcR6LrIdJ3AIONxYWxwc0XRN-
"""

from google.colab import drive
drive.mount('/content/drive')

cd /content/drive/MyDrive/Logistic_Regression

# Commented out IPython magic to ensure Python compatibility.
# data analysis and wrangling
import pandas as pd
import numpy as np
import random as rnd
# visualization
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
# %matplotlib inline
# machine learning
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import RFECV
from sklearn.metrics import classification_report

Train_df = pd.read_csv('TitanicDataTrain.csv')
Test_df = pd.read_csv('TitanicDataTest.csv')

Train_df.head()

column_names = Train_df.columns.values
print(column_names)

Train_df.drop(["PassengerId", "Name", "Ticket", "Cabin"], axis = 1, inplace = True)

Test_df.drop(["PassengerId", "Name", "Ticket", "Cabin"], axis = 1, inplace = True)

Train_df.info()





column_names = Train_df.columns.values
print(column_names)



Train_df[column_names].isnull().sum()

Test_column_names = Test_df.columns.values
print(Test_column_names)

Test_df[Test_column_names].isnull().sum()

Age_mode = Train_df["Age"].mode().iloc[0]

Train_df["Age"].fillna(Age_mode, inplace = True)
Train_df[column_names].isnull().sum()

Embarked_mode = Train_df["Embarked"].mode().iloc[0]
Train_df["Embarked"].fillna(Embarked_mode, inplace = True)
Train_df[column_names].isnull().sum()

Age_mode_test = Test_df["Age"].mode().iloc[0]
Test_df["Age"].fillna(Age_mode_test, inplace = True)
Fare_mode_test = Test_df["Fare"].mode().iloc[0]
Test_df["Fare"].fillna(Fare_mode_test, inplace = True)
Test_df[Test_column_names].isnull().sum()

Train_df.dtypes

Train_df["Sex"].value_counts()



Train_df["Sex"] = Train_df["Sex"].map({"male": 0, "female": 1}).astype(int)



print(Train_df["Sex"].value_counts())

Train_df["Embarked"].value_counts()

Train_df["Embarked"] = Train_df["Embarked"].map({"S": 1, "C": 2, "Q": 3}).astype(int)
print(Train_df["Embarked"].value_counts())

Test_df.dtypes

Test_df["Sex"].value_counts()

Test_df["Sex"] = Test_df["Sex"].map({"male": 0, "female": 1}).astype(int)

Test_df["Embarked"].value_counts()

Test_df["Embarked"] = Test_df["Embarked"].map({"S": 1, "C": 2, "Q": 3}).astype(int)
print(Test_df["Embarked"].value_counts())

sns.heatmap(Train_df.corr(), annot = True)

X_train_data = Train_df.drop("Survived", axis = 1)
y_train_data = Train_df["Survived"]
x_test_data = Test_df

rfecv = RFECV(estimator=LogisticRegression(solver='liblinear'), min_features_to_select=1, step=1, cv=6, scoring='accuracy')
rfecv.fit(X_train_data, y_train_data)
print("Optimal number of features: %d" % rfecv.n_features_)
print('Selected features: %s' % list(X_train_data.columns[rfecv.support_]))
# Plot number of features VS. cross-validation scores
plt.figure(figsize=(10,6))
plt.xlabel("Number of features selected")
plt.ylabel("Cross validation score (nb of correct classifications)")
plt.plot(range(1, len(rfecv.grid_scores_) + 1), rfecv.grid_scores_)
plt.show()

X_train, X_val, y_train, y_val = train_test_split(X_train_data, y_train_data, test_size = 0.2)
print("Shape of X_train", X_train.shape, "\nShape of y_train", y_train.shape)
print("Shape of X_val", X_val.shape, "\nShape of y_val", y_val.shape)

print(y_val)

model = LogisticRegression(max_iter = 10000)
param_grid = dict()
param_grid['solver'] = ['newton-cg', 'lbfgs', 'liblinear', 'sag', 'saga']

grid = GridSearchCV(model, param_grid, refit = True)
grid.fit(X_train, y_train)

print("Best params: ", grid.best_params_)

model = LogisticRegression(solver = "sag", max_iter = 2000)
model.fit(X_train, y_train)
accuracy = round(model.score(X_train, y_train) * 100, 2)
print("Training Accuracy of loictic regression:", accuracy, "\n")

model = LogisticRegression(solver = "lbfgs", max_iter = 20)
model.fit(X_train, y_train)
accuracy = round(model.score(X_train, y_train) * 100, 2)
print("Training Accuracy of logictic regression:", accuracy, "\n")

model = LogisticRegression(solver = "newton-cg", max_iter = 100)
model.fit(X_train, y_train)
accuracy = round(model.score(X_train, y_train) * 100, 2)
print("Training Accuracy of logictic regression:", accuracy, "\n")



model = LogisticRegression(solver = "saga", max_iter = 2000)
model.fit(X_train, y_train)
accuracy = round(model.score(X_train, y_train) * 100, 2)
print("Training Accuracy of logictic regression:", accuracy, "\n")

model = LogisticRegression(solver = "liblinear", max_iter = 10)
model.fit(X_train, y_train)
accuracy = round(model.score(X_train, y_train) * 100, 2)
print("Training Accuracy of logictic regression:", accuracy, "\n")

model = LogisticRegression(solver = "newton-cg", max_iter = 2000)
model.fit(X_train, y_train)
accuracy = round(model.score(X_train, y_train) * 100, 2)
print("Training Accuracy of logictic regression:", accuracy, "\n")

print("In validation Dataset, Total number of People:", len(y_val))
print("Actual Result in validation dataset")
print("Survived", sum(y_val!=0))
print("Not Survived", sum(y_val==0))

y_pred = model.predict(X_val)
print("\nPrediction of Logistic Regression")
print("Survived", sum(y_pred!=0))
print("Not Survived", sum(y_pred==0))

print("=========Classification report=======")
print(classification_report(y_val, y_pred))

y_pred = model.predict(x_test_data)
print("In Test Dataset, Total Number of People:", len(y_pred))
print("Survived", sum(y_pred!=0))
print("Not Survived", sum(y_pred==0))

sorted(Test_df.columns.values)

Sex_dict = {'1': 'female',
            '0': 'male'}
Embarked_dict = {"1" : "S",
               "2" : "C",
               "3" : "Q"}
Sex_keys = list(Sex_dict.keys())
Sex_vals = list(Sex_dict.values())

Embarked_keys = list(Embarked_dict.keys())
Embarked_vals = list(Embarked_dict.values())

Test_df.columns.values

print("Please fill in the information of the person you want to predict")
Age = input("Enter Age:")
Embarked = input("Enter Port of Embarkation:")
Fare = input("Enter Fare:")
Parch = input("Enter Number of parents:")
Sex = input("Enter Sex:")
Pclass = input("Enter Ticket class:")
SibSp = input("Enter number of siblings:")

custom_test_list = []
custom_test_list.append(int(Pclass))
Sex_ids = Sex_keys[Sex_vals.index(Sex)]
custom_test_list.append(int(Sex_ids))
custom_test_list.append(float(Age))
custom_test_list.append(int(SibSp))
custom_test_list.append(int(Parch))
custom_test_list.append(float(Fare))
Embarked_ids = Embarked_keys[Embarked_vals.index(Embarked)]
custom_test_list.append(int(Embarked_ids))

print(custom_test_list)

custom_test M= np.array([custom_test_list])
y_pred = model.predict(custom_test)
print("Y predict: ", y_pred)
print()

if y_pred == 0:
  print("This person will die.")
else:
  print("This person will survive.")

print()
print()

#True Positive: prediction == 1 and true label is 1
TruePositive = np.sum(np.logical_and(y_pred == 1, y_val == 1))

#True Negative: prediction == 0 and true label is 0
TrueNegative = np.sum(np.logical_and(y_pred == 0, y_val == 0))

#False Positive: prediction == 1 and true label is 0
FalsePositive = np.sum(np.logical_and(y_pred == 1, y_val == 0))

#False Negative: prediction == 0 and true label is 1
FalseNegative = np.sum(np.logical_and(y_pred == 0, y_val == 1))