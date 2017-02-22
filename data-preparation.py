# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 05:23:21 2017

@author: parag
"""
#Data preprocessing

################# import the libraries #################
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

################# import dataset #######################

dataset = pd.read_csv('Data.csv')

############### convert to array format required by Numpy ###
#[:,:-1] means we take all rows ":"
#and all columns except for the last one ie. ",-1"
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values

###################### Missing data ###################################

####### Numerical data #####
#Here using Imputer with capital I (case-sensitive) 
#to impute missing values
from sklearn.preprocessing import Imputer

#build imputer object for sklearn preprocessing class, by entering object parameters
imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)

#apply this object to columns 2 and 3 of array X
imputer = imputer.fit(x[:, 1:3])
#apply transform method of imputer object to original array
x[:, 1:3] = imputer.transform(x[:, 1:3])

###################### Encoding Categorical data ################################
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

#Define object to create integer labels for categorical variables
#in independant features array X
labelencoder = LabelEncoder()

#Fist convert categorical labels into integer labels for features array X
x[:,0] = labelencoder.fit_transform(x[:,0])

#Next define an object to build dummy variables
#Here we are deifining the object to work with 1-d array 
#ie. feature in X with index 0
onehotencoder = OneHotEncoder(categorical_features=[0])

x = onehotencoder.fit_transform(x).toarray()

#Now converting response variable  y into integers
y = labelencoder.fit_transform(y)

#################### Splitting dataset into Test and Train #################
from sklearn.cross_validation import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=0)
