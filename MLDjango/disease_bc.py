# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 01:58:49 2018

@author: prate
"""

import numpy as np
#import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import Imputer
from sklearn.metrics import confusion_matrix





def load_dataset():
    dataset = pd.read_csv('MLDjango/wisc_bc_data.xls')
    X = dataset.iloc[:,2:].values
    y = dataset.iloc[:,1].values.reshape(569,1,)
    
    
    labelencoder = LabelEncoder()
    y[:, 0] = labelencoder.fit_transform(y[:,0])
    
    imputer = Imputer()
    imputer = imputer.fit(X[:,:])
    X[:,:] = imputer.transform(X[:,:])

    #X=preprocessing.normalize(X,norm='l1')

    #we do not need onehotencoding bcz we only have 2 values and they will be categogrized with 0 and 1,so no need,
    #and if we have 3 values like (male,female,trans) then we need onehotencoding and dont foget to take care of 
    #dummy variable trap
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
    size_y=np.size(y_train)
    y_train= y_train.reshape((1,size_y))

    size_y=np.size(y_test)
    y_test=y_test.reshape((1,size_y))
    
    #X_train=preprocessing.normalize(X_train,norm='l1')
    #aX_test=preprocessing.normalize(X_test,norm='l1')

    #use this in future
    X_train, X_test, y_train, y_test = X_train.astype(np.float64),X_test.astype(np.float64), y_train.astype(np.float64), y_test.astype(np.float64)
    return X_train.T,y_train,X_test.T,y_test


def layer_sizes(X, Y):
    
    n_x = np.size(X,axis=0) # size of input layer
    n_h = 45
    n_y = np.size(Y,axis=0) # size of output layer
    return (n_x, n_h, n_y)

def sigmoid(z):
    s = 1/(1+(1/np.exp(z)))
    return s


def initialize_parameters(n_x, n_h, n_y): 
    np.random.seed(2) # we set up a seed so that your output matches ours although the initialization is random.
    
    W1 = np.random.randn(n_h,n_x) *0.01
    b1 = np.zeros((n_h,1))
    W2 = np.random.randn(n_y,n_h) *0.01
    b2 = np.zeros((n_y,1))
   
    
    parameters = {"W1": W1,
                  "b1": b1,
                  "W2": W2,
                  "b2": b2}
    
    return parameters



def forward_propagation(X, parameters):
   
   
    W1 = parameters["W1"]
    b1 = parameters["b1"]
    W2 = parameters["W2"]
    b2 = parameters["b2"]
    
    # Implement Forward Propagation to calculate A2 (probabilities)
    Z1 =np.array(np.dot(W1,X),dtype=np.float32)+b1
    A1 = np.tanh(Z1)
    Z2 = np.array(np.dot(W2,A1),dtype=np.float32)+b2
    A2 = sigmoid(Z2)
    
    
    
    cache = {"Z1": Z1,
             "A1": A1,
             "Z2": Z2,
             "A2": A2}
    
    return A2, cache


def compute_cost(A2, Y, parameters):
    
    
    m = Y.shape[1] # number of example

    
    logprobs = np.multiply(np.log(A2),Y)+np.multiply(np.log(1-A2),(1-Y))
    cost = -np.sum(logprobs)/m
    
    cost = np.squeeze(cost)     # makes sure cost is the dimension we expect. 
                                # E.g., turns [[17]] into 17 
    
    return cost


def backward_propagation(parameters, cache, X, Y):
    
    m = X.shape[1]
    
    W1 = parameters["W1"]
    W2 = parameters["W2"]
    
    A1 = cache["A1"]
    A2 = cache["A2"]
  
    dZ2 = A2-Y
    dW2 = np.dot(dZ2,A1.T)/m
    db2 = np.sum(dZ2,axis=1,keepdims=True)/m
    dZ1 = np.dot(W2.T,dZ2)*(1 - np.power(A1, 2))

    dW1 = np.dot(dZ1, X.T) / m
    db1 = np.sum(dZ1, axis=1, keepdims=True) / m
    
    grads = {"dW1": dW1,
             "db1": db1,
             "dW2": dW2,
             "db2": db2}
    
    return grads



def update_parameters(parameters, grads, learning_rate =1.2):
   
    W1 = parameters["W1"]
    b1 = parameters["b1"]
    W2 = parameters["W2"]
    b2 = parameters["b2"]
    
    dW1 = grads["dW1"]
    db1 = grads["db1"]
    dW2 = grads["dW2"]
    db2 = grads["db2"]
   
    W1 = W1-learning_rate*dW1
    b1 = b1-learning_rate*db1
    W2 = W2-learning_rate*dW2
    b2 = b2-learning_rate*db2
    
    parameters = {"W1": W1,
                  "b1": b1,
                  "W2": W2,
                  "b2": b2}
    
    return parameters

def nn_model(X, Y, n_h, num_iterations = 10000, print_cost=False):
    
    np.random.seed(3)
    n_x = layer_sizes(X, Y)[0]
    n_y = layer_sizes(X, Y)[2]
    
   
    parameters = initialize_parameters(n_x, n_h, n_y)
    W1 = parameters["W1"]
    b1 = parameters["b1"]
    W2 = parameters["W2"]
    b2 = parameters["b2"]
    
    costs = []
   

    for i in range(0, num_iterations):
         
       
        A2, cache = forward_propagation(X, parameters)
        
        
        cost = compute_cost(A2, Y, parameters)
 
        
        grads = backward_propagation(parameters, cache, X, Y)
 
        
        parameters = update_parameters(parameters, grads, learning_rate = 0.0006)
        
        if i % 100 == 0:
            costs.append(cost)
       
        if print_cost and i % 1000 == 0:
            print ("Cost after iteration %i: %f" %(i, cost))

    return parameters,costs

def predict(parameters, X):
    A2, cache = forward_propagation(X, parameters)
    predictions = A2>0.4 #it will compare each element with 0.5 and mark it true or false based on cndition
    return predictions


def train_model():
    train_set_x_orig, train_set_y, test_set_x_orig, test_set_y = load_dataset()
    print(np.shape(train_set_x_orig),np.shape(train_set_y))

    parameters, costs = nn_model(train_set_x_orig, train_set_y, 45, num_iterations=25000, print_cost=True)

    predictions = predict(parameters, train_set_x_orig)
    print('Accuracy Train: %d' % float(
        (np.dot(train_set_y, predictions.T) + np.dot(1 - train_set_y, 1 - predictions.T)) / float(
            train_set_y.size) * 100) + '%')
    cm_train = confusion_matrix(train_set_y.astype(np.int64).T, predictions.T)
    print(cm_train)

    predictions = predict(parameters, test_set_x_orig)
    print('Accuracy Test: %d' % float(
        (np.dot(test_set_y, predictions.T) + np.dot(1 - test_set_y, 1 - predictions.T)) / float(
            test_set_y.size) * 100) + '%')

    predictions = predictions.astype(np.int64)
    cm_test = confusion_matrix(test_set_y.astype(np.int64).T, predictions.T)
    print(cm_test)
    np.save('MLDjango/myfile2.npy', parameters)

    '''
    fig = plt.figure()
    costs = np.squeeze(costs)
    plt.plot(costs)
    plt.ylabel('cost')
    plt.xlabel('iterations (per hundreds)')
    plt.title("Learning rate =0.001")
    fig.savefig('smart/static/smart/images/graph.png')
    '''




def check(X1):
    read_dictionary = np.load('MLDjango/myfile2.npy').item()
    prediction = predict(read_dictionary, X1)
    return np.squeeze(prediction)







