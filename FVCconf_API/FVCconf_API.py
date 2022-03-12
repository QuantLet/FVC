import pandas as pd
import numpy as np

#... or laoad directly 
y_true = np.load('y_true.npy')     
test_results = pd.read_pickle("results_API_test_set.pkl")


#replace 0 with NaN
test_results = test_results.replace(0, np.nan)


#count not-NaN valued in df: "/8" to get number of invalid requests
sum(test_results.count(axis=1)/8) #2388 -> 1201 invalid requests, 33% NA 

#boolean series of TRUE/FALSE for NA
NA_bool_test = test_results['anger'].isnull()

#predicition for each observation
row_max_test = test_results.idxmax(axis = 1, skipna = False)
test_results['prediction'] = row_max_test

#change into pandas format and change to integer
y_true = pd.Series(y_true.astype(int).astype(str))


#change FER labels to API labels 
#evtl schöner machen.....
true_y_test = y_true.replace('0', 'anger')
true_y_test = true_y_test.replace('1', 'disgust')
true_y_test = true_y_test.replace('2', 'fear')
true_y_test = true_y_test.replace('3', 'happiness')
true_y_test = true_y_test.replace('4', 'sadness')
true_y_test = true_y_test.replace('5', 'surprise')
true_y_test = true_y_test.replace('6', 'neutral')


#add to pandas
test_results['true'] = true_y_test
#pred_val['true'] = true_y_val


#compare two columns:
comp_test = np.where(test_results['true']== test_results['prediction']) #1470/3589 = 40.95% matches


#compare without NA rows
test_results_nadrop = test_results.dropna()
comp_test_nadrop = np.where(test_results_nadrop['true']== test_results_nadrop['prediction']) #1470/2388 = 61,56% matches



#without obs. classified as 'contempt'
test_results_contempt_drop = test_results_nadrop.drop(test_results_nadrop[test_results_nadrop.prediction == 'contempt'].index)

#18 obs classified as 'contempt, only divisor changes, correctly class. remains
comp_test_contempt_drop = np.where(test_results_contempt_drop['true'] == test_results_contempt_drop['prediction']) #1470/2370 = 62,02% matches


import pandas as pd
import matplotlib.pyplot as plt
from sklearn import metrics

#drop 'contempt'
test_results_conf = test_results_nadrop.drop(test_results_nadrop[test_results_nadrop.prediction == 'contempt'].index)

confusion = metrics.confusion_matrix(test_results_conf['true'], test_results_conf['prediction'])
index = ['anger', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral']  


df_conf = pd.DataFrame(confusion, range(7), range(7))
df_conf.columns = index
df_conf.index = index
df_conf.to_csv('confusion_API.csv')

