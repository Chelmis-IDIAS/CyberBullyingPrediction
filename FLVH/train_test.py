from __future__ import division
import pandas as pd
import numpy as np
import os
from sklearn.model_selection import train_test_split

directory = '/home/miley/Documents/harris formulation/tau=1_k=10'
if not os.path.exists(directory+'/train'):
    os.makedirs(directory+'/train')
if not os.path.exists(directory+'/test'):
    os.makedirs(directory+'/test')
for i in range(10)[:1]:
    data = pd.read_csv(directory+'/task_'+str(i)+'.csv')
    X = data.iloc[:, :-1]
    y = data['label'].tolist()

    x_train, x_test, y_train, y_test,= train_test_split(
        X, y, test_size=0.3, random_state=42)


    x_train['label'] = y_train
    x_test['label'] = y_test
    x_train.to_csv(directory+'/train/task_'+str(i)+'.csv',index=False)
    x_test.to_csv(directory+'/test/task_'+str(i)+'.csv',index=False)

