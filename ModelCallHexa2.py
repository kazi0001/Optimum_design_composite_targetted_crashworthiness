# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 12:49:16 2020

@author: KK14839
"""



# load and evaluate a saved model
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import tensorflow as tf
from array import *
from tensorflow import keras
from sklearn.metrics import mean_squared_error
from keras.callbacks import EarlyStopping 
from keras.callbacks import ModelCheckpoint




# load model
loaded_model = tf.keras.models.load_model('my_model_WGR2')
# summarize model.
loaded_model.summary()
loaded_model.get_weights()
# load dataset
dataset = pd.read_excel('WGR1b.xlsx')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values
# evaluate the model
score = loaded_model.evaluate(X, y, verbose=0)

#Developed ANN model check for 60 and 65 degree
y_pred60 = loaded_model.predict(np.array([[0.57,	0.35,	0.62,	0.58,	0.98,	3.48]]))
y_pred65 = loaded_model.predict(np.array([[0.65,	0.39,	0.59,	0.67,	0.97,	3.57]]))

# Maximum angle using developed ANN
y_predmax = loaded_model.predict(np.array([[0.65,	1.306,	0.94,	1.2,	1.18,	5.45]]))

# Need to find 63 degree 

par1=0.57
par2=0.35
par3=0.59
par4=0.58
par5=0.97
par6=3.48

for par6 in np.arange(3.48,3.57,.01):
     for par5 in np.arange(0.97, 0.98,.01):
          for par4 in np.arange(0.58, 0.67,.01):
              for par3 in np.arange(0.59, 0.62,.01):
                  for par2 in np.arange(0.35,0.39,.01):
                      for par1 in np.arange(0.57,0.65,.01):
                        y_pred63 = loaded_model.predict(np.array([[par1, par2, par3, par4, par5, par6]]))
                        list1 = [np.float64(y_pred63),par1, par2, par3, par4, par5, par6]
                        print(list1)
            
                        # x=open("pred63b.txt",'a')
                        # print(list1, file=x)
                        # x.close
                        
                        # list1=list1+list1
                        
                        
                        # list1=np.append(list1,list1)
                        
                        
                        # finallist = np.append(list1, list1, axis=1).reshape( ,7)
                        
                        
                                               
                        # # Create a Pandas dataframe from some data.
                        # df = pd.DataFrame({'Data': [finallist]})

                        # # Create a Pandas Excel writer using XlsxWriter as the engine.
                        # writer = pd.ExcelWriter('pandas_simple.xlsx', engine='xlsxwriter')

                        # # Convert the dataframe to an XlsxWriter Excel object.
                        # df.to_excel(writer, sheet_name='Sheet1')

                        # # Close the Pandas Excel writer and output the Excel file.
                        # writer.save()
                        
                        

    #                 y_pred63 = loaded_model.predict(np.array([[par1, par2, par3, par4, par5, par6]]))
    #                 list2 = [np.float64(y_pred63),par1, par2, par3, par4, par5, par6]

    #             y_pred63 = loaded_model.predict(np.array([[par1, par2, par3, par4, par5, par6]]))
    #             list3 = [np.float64(y_pred63),par1, par2, par3, par4, par5, par6]
                
    #         y_pred63 = loaded_model.predict(np.array([[par1, par2, par3, par4, par5, par6]]))
    #         list4 = [np.float64(y_pred63),par1, par2, par3, par4, par5, par6]

    #     y_pred63 = loaded_model.predict(np.array([[par1, par2, par3, par4, par5, par6]]))
    #     list5 = [np.float64(y_pred63),par1, par2, par3, par4, par5, par6]

    # y_pred63 = loaded_model.predict(np.array([[par1, par2, par3, par4, par5, par6]]))
    # list6 = [np.float64(y_pred63),par1, par2, par3, par4, par5, par6]






    












