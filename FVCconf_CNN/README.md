[<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/banner.png" width="888" alt="Visit QuantNet">](http://quantlet.de/)

## [<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/qloqo.png" alt="Visit QuantNet">](http://quantlet.de/) **FVCconf_CNN** [<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/QN2.png" width="60" alt="Visit QuantNet 2.0">](http://quantlet.de/)

```yaml

Name of Quantlet: FVCconf_CNN

Published in: Face Value of Companies

Description: "Generates confusion matrix between test set predictions of FVCConvNet and true test set values. Can be made by loading model and weights from Q-let FVCConvNet and data loader function for original data set FVCload_dataset, or by simply loading already generated predictions and true values."


Keywords: 'neural-network, estimation, empirical, optimization, descending-gradients'

Author: Sophie Burgard

Submitted: '21.11.2017'



```

### PYTHON Code
```python

import pandas as pd
import matplotlib.pyplot as plt
import sklearn.metrics


#load data, requires function load_dataset() from Q-let: FVCload_dataset 
#and original data from Kaggle's Facial Expression Recognition Competition 2013
from FVCload_dataset import load_dataset
(x_train, y_train), (x_test, y_test), (x_valid, y_valid) = load_dataset() 

# load json and create model (stored in FVCConvNet)
json_file         = open('model_CNN.json', 'r')
loaded_model_json = json_file.read()
json_file.close()

loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("weights_CNN.h5")


#generate predictions based for test set
y_pred = loaded_model.predict_classes(x_test)
np.save('y_pred ', y_pred)


#.... just or load saved array with predictions and true values
y_pred = np.load('y_pred.npy')
y_true = np.load('y_true.npy') 
index  = ['anger', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral']


#organize in confusion matrx
confusion = sklearn.metrics.confusion_matrix(y_true, y_pred)   
df_conf   = pd.DataFrame(confusion, range(7), range(7))

#name rows and columns
df_conf.columns = index
df_conf.index   =  index

#save as csv
df_conf.to_csv('confusion_CNN.csv')

```

automatically created on 2018-05-28