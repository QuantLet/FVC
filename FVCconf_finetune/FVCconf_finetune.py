import pandas as pd
import matplotlib.pyplot as plt
import sklearn.metrics
import keras

#load data, requires function load_dataset() from Q-let: FVCload_dataset 
#and original data from Kaggle's Facial Expression Recognition Competition 2013
from FVCload_dataset import load_dataset
(x_train, y_train), (x_test, y_test), (x_valid, y_valid) = load_dataset() 

# load json and create model (stored in FVCConvNet)
json_file         = open('model_CNN.json', 'r')
loaded_model_json = json_file.read()
json_file.close()

loaded_model = keras.models.model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("weights_CNN.h5")


#generate predictions based for test set
y_pred = np.argmax(loaded_model.predict(x_test),axis=1)
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
df_conf.to_csv('confusion_finetune.csv')
