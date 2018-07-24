# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 11:37:12 2018

@author: prateeek
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import Imputer
from sklearn import preprocessing



def load_dataset():
    dataset = pd.read_csv('indian_liver_patient.csv')
    X = dataset.iloc[:,[1,2,3,4,5,6,8]].values
    y = dataset.iloc[:, 10].values
    
    
    labelencoder = LabelEncoder()
    X[:, 0] = labelencoder.fit_transform(X[:, 0])
    
    imputer = Imputer()
    imputer = imputer.fit(X[:,:])
    X[:,:] = imputer.transform(X[:,:])
    
    X=preprocessing.normalize(X,norm='l1')
    
    #we do not need onehotencoding bcz we only have 2 values and they will be categogrized with 0 and 1,so no need,
    #and if we have 3 values like (male,female,trans) then we need onehotencoding and dont foget to take care of 
    #dummy variable trap
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
    size_y=np.size(y_train)
    y_train= y_train.reshape((1,size_y))

    size_y=np.size(y_test)
    y_test=y_test.reshape((1,size_y))
    return X_train.T,y_train,X_test.T,y_test





def sigmoid(z):
    s = 1/(1+(1/np.exp(z)))
    return s




def initialize_with_zeros(dim):
    """
    
    Argument:
    dim -- size of the w vector we want (or number of parameters in this case)
    
    Returns:
    w -- initialized vector of shape (dim, 1)
    b -- initialized scalar (corresponds to the bias)
    """
    w = np.zeros((dim,1))
    b = 0
    
    return w, b





def propagate(w, b, X, Y):
    """
    Arguments:
    w -- weights, a numpy array of size (num_px * num_px * 3, 1)
    b -- bias, a scalar
    X -- data of size (num_px * num_px * 3, number of examples)
    Y -- true "label" vector (containing 0 if non-cat, 1 if cat) of size (1, number of examples)
    """
    
    m = X.shape[1]
    
    
    z=np.array(np.dot(w.T,X),dtype=np.float32)+b
    A = sigmoid(z) 
    
                                   # compute activation
    cost =-(np.dot(Y,np.log(A.T))+(np.dot((1-Y),np.log((1-A).T))))/m                            # compute cost

    # BACKWARD PROPAGATION (TO FIND GRAD)
    dw =np.dot(X,(A-Y).T)/m
    db = np.sum(A-Y)/m
    
    cost = np.squeeze(cost)
    
    grads = {"dw": dw,
             "db": db}
    
    return grads, cost

def optimize(w, b, X, Y, num_iterations, learning_rate, print_cost = True):
    """
    This function optimizes w and b by running a gradient descent algorithm
    
    Arguments:
    w -- weights, a numpy array of size (num_px * num_px * 3, 1)
    b -- bias, a scalar
    X -- data of shape (num_px * num_px * 3, number of examples)
    Y -- true "label" vector (containing 0 if non-cat, 1 if cat), of shape (1, number of examples)
    num_iterations -- number of iterations of the optimization loop
    learning_rate -- learning rate of the gradient descent update rule
    print_cost -- True to print the loss every 100 steps
    """
    
    costs = []
    
    for i in range(num_iterations):
        grads, cost = propagate(w, b, X, Y)
        
        # Retrieve derivatives from grads
        dw = grads["dw"]
        db = grads["db"]
        
        # update rule (≈ 2 lines of code)
        w = w-learning_rate*dw
        b = b-learning_rate*db
        
        # Record the costs
        if i % 100 == 0:
            costs.append(cost)
        
        if print_cost and i % 100 == 0:
            print ("Cost after iteration %i: %f" %(i, cost))
    
    params = {"w": w,
              "b": b}
    
    grads = {"dw": dw,
             "db": db}
    
    return params, grads, costs

def predict(w, b, X):
    '''
    Arguments:
    w -- weights, a numpy array of size (num_px * num_px * 3, 1)
    b -- bias, a scalar
    X -- data of size (num_px * num_px * 3, number of examples)
    
    Returns:
    Y_prediction -- a numpy array (vector) containing all predictions (0/1) for the examples in X
    '''
    
    m = X.shape[1]
    Y_prediction = np.zeros((1,m))
    w = w.reshape(X.shape[0], 1)
    
    
    z=np.array(np.dot(w.T,X),dtype=np.float32)+b
    A = sigmoid(z) 
    
    for i in range(A.shape[1]):
        
        # Convert probabilities A[0,i] to actual predictions p[0,i]
        if A[:,i]<=0.5:
            Y_prediction[:,i]=0
        else:
            Y_prediction[:,i]=1
        pass
    
    assert(Y_prediction.shape == (1, m))
    
    return Y_prediction

def model(X_train, Y_train, X_test, Y_test, num_iterations = 5000, learning_rate = 0.5, print_cost = False):
   
    w, b = initialize_with_zeros(X_train.shape[0])

    # Gradient descent (≈ 1 line of code)
    parameters, grads, costs =optimize(w, b, X_train, Y_train, num_iterations, learning_rate, print_cost = True)
    
    # Retrieve parameters w and b from dictionary "parameters"
    w = parameters["w"]
    b = parameters["b"]
    
    # Predict test/train set examples (≈ 2 lines of code)
    Y_prediction_test = predict(w, b, X_test)
    Y_prediction_train = predict(w, b, X_train)

    # Print train/test Errors
    print("train accuracy: {} %".format(100 - np.mean(np.abs(Y_prediction_train - Y_train)) * 100))
    print("test accuracy: {} %".format(100 - np.mean(np.abs(Y_prediction_test - Y_test)) * 100))

    
    d = {"costs": costs,
         "Y_prediction_test": Y_prediction_test, 
         "Y_prediction_train" : Y_prediction_train, 
         "w" : w, 
         "b" : b,
         "learning_rate" : learning_rate,
         "num_iterations": num_iterations}
    
    return d


train_set_x_orig, train_set_y, test_set_x_orig, test_set_y = load_dataset()




d = model(train_set_x_orig, train_set_y, test_set_x_orig, test_set_y, num_iterations = 500000, learning_rate = 0.001, print_cost = True)


costs = np.squeeze(d['costs'])
plt.plot(costs)
plt.ylabel('cost')
plt.xlabel('iterations (per hundreds)')
plt.title("Learning rate =" + str(d["learning_rate"]))
plt.show()
