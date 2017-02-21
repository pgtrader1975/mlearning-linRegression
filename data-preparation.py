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

################ Missing data #####################

#Here using Imputer with capital I (case-sensitive) 
#to impute missing values
from sklearn.preprocessing import Imputer

#build imputer object for sklearn preprocessing class, by entering object parameters
imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)

#apply this object to columns 2 and 3 of array X
imputer = imputer.fit(x[:, 1:3])
#apply transformation to original array
x[:, 1:3] = imputer.transform[:, 1:3]
