[<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/banner.png" width="888" alt="Visit QuantNet">](http://quantlet.de/)

## [<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/qloqo.png" alt="Visit QuantNet">](http://quantlet.de/) **FVCload_dataset** [<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/QN2.png" width="60" alt="Visit QuantNet 2.0">](http://quantlet.de/)

```yaml

Name of Quantlet: FVCload_dataset

Published in: Face Value of Companies

Description: "Automizes the procedure of loading the data set and restructuring the images from one-dimensional array into two-dimensional images. Required dataset is from Kaggle's 2013 Facial Expression Recognition Competition and can be downloaded under 'https://www.kaggle.com/c/challenges-in-representation-learning-facial-expression-recognition-challenge' "


Keywords: 'neural-network, estimation, empirical, optimization, descending-gradients'

Author: Sophie Burgard

Submitted: '21.11.2017'



```

### PYTHON Code
```python

import numpy as np
import pandas as pd
import csv
import time


#set path where FER2013 dataset is stored. Dataset can be downloaded from
#https://www.kaggle.com/c/challenges-in-representation-learning-facial-expression-recognition-challenge
path = '.....'

with open(path ,'r') as f:
    df = pd.read_csv(f, delimiter = ',')
    #size public training set
    train_size = df[df.Usage == 'Training'].count().values[0]
    #size public test set
    test_size = df[df.Usage == 'PublicTest'].count().values[0]
    #size private test set
    valid_size = df[df.Usage == 'PrivateTest'].count().values[0]
    #picture dimension: 48*48 pixel
    dim = 48

#function to load competition data and reshapes to correct CNn dimension   
def load_dataset():

#predefine empty arrays for training & test split
    x_train = np.empty([train_size,dim, dim])
    x_test  = np.empty([test_size, dim, dim])
    x_valid = np.empty([valid_size, dim, dim])
    y_train = np.empty(train_size)
    y_test  = np.empty(test_size)
    y_valid = np.empty(valid_size)
    ind_train = ind_test = ind_valid = 0
    
    for i in range(0, len(df)):
        tmp = df.iloc[i,:]
        if tmp.Usage == 'Training':
            x_train[ind_train, :,:] = np.fromstring(tmp[1], dtype = 'int', sep = ' ').reshape(dim, dim)
            y_train[ind_train] = int(tmp[0])
            ind_train += 1 
        elif tmp.Usage == 'PublicTest':           
            x_test[ind_test, :,:] = np.fromstring(tmp[1], dtype = 'int', sep = ' ').reshape(dim, dim)
            y_test[ind_test] = int(tmp[0])
            ind_test += 1 
        else: #'PrivateTest': secret competition data
            x_valid[ind_valid, :,:] = np.fromstring(tmp[1], dtype = 'int', sep = ' ').reshape(dim, dim)
            y_valid[ind_valid] = int(tmp[0])
            ind_valid += 1
    return (x_train, y_train) , (x_test, y_test), (x_valid, y_valid)      
            
#to load dataset use:        
#(x_train, y_train), (x_test, y_test), (x_valid, y_valid) = load_dataset() 

```

automatically created on 2018-05-28