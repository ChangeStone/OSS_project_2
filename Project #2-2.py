#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

def sort_dataset(dataset_df):
    dataset_df = dataset_df.sort_values(by='year',ascending=True)
    dataset_df = dataset_df.reset_index(drop=True)
    return dataset_df

def split_dataset(dataset_df):
    dataset_df.loc[:,'salary'] *= 0.001
    
    X = dataset_df.drop(columns='salary', axis=1)
    Y = dataset_df['salary']
    
    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,train_size=1718,shuffle=False)
    
    return X_train,X_test,Y_train,Y_test

def extract_numerical_cols(dataset_df):
    dataset_df = dataset_df.loc[:,['age','G','PA','AB','R','H','2B','3B','HR','RBI','SB','CS','BB','HBP','SO','GDP','fly','war']]
    return dataset_df

def train_predict_decision_tree(X_train, Y_train, X_test):
    Y_train = Y_train.astype(int)
    dt_cls = DecisionTreeClassifier()
    dt_cls.fit(X_train,Y_train)
    return dt_cls.predict(X_test)

def train_predict_random_forest(X_train, Y_train, X_test):
    Y_train = Y_train.astype(int)
    rf_cls = RandomForestClassifier()
    rf_cls.fit(X_train,Y_train)
    return rf_cls.predict(X_test)

def train_predict_svm(X_train, Y_train, X_test):
    Y_train = Y_train.astype(int)
    svm_pipe = make_pipeline(
    StandardScaler(),
    SVC()
    )
    svm_pipe.fit(X_train,Y_train)
    return svm_pipe.predict(X_test)

def calculate_RMSE(labels, predictions):
    result = np.sqrt(np.mean((predictions-labels)**2))
    return result

if __전환석__=='__main__':
	#DO NOT MODIFY THIS FUNCTION UNLESS PATH TO THE CSV MUST BE CHANGED.
	data_df = pd.read_csv('2019_kbo_for_kaggle_v2.csv')
	
	sorted_df = sort_dataset(data_df)	
	X_train, X_test, Y_train, Y_test = split_dataset(sorted_df)
	
	X_train = extract_numerical_cols(X_train)
	X_test = extract_numerical_cols(X_test)

	dt_predictions = train_predict_decision_tree(X_train, Y_train, X_test)
	rf_predictions = train_predict_random_forest(X_train, Y_train, X_test)
	svm_predictions = train_predict_svm(X_train, Y_train, X_test)
	
	print ("Decision Tree Test RMSE: ", calculate_RMSE(Y_test, dt_predictions))	
	print ("Random Forest Test RMSE: ", calculate_RMSE(Y_test, rf_predictions))	
	print ("SVM Test RMSE: ", calculate_RMSE(Y_test, svm_predictions))

