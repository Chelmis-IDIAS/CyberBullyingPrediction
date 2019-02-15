from __future__ import division
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge,LogisticRegression,Lasso
from sklearn.metrics import r2_score
from sklearn import metrics
from scipy.io import loadmat
from sklearn.ensemble import RandomForestClassifier
for fold in range(1,4):
    tau = 1
    mat = loadmat('tau=1_k=10_step=2/W/fold_'+str(fold)+'/W_1000_new.mat')
    w = pd.DataFrame(mat['W'])
    lg = Lasso()
    eval = []
    R2 = []
    R2_Lasso = []
    for t in range(10):
        data_lg = pd.read_csv('tau=1_k=10_step=2/test/fold_' + str(fold) + '/task_' + str(t) + '.csv')
        x_lg = data_lg.iloc[:, 1:-2]
        y_lg = data_lg['label'].tolist()
        lg.fit(x_lg, y_lg)
        data = pd.read_csv('tau=1_k=10_step=2/test/fold_' + str(fold) + '/task_' + str(t) + '.csv')
        X = data.iloc[:, 1:-2]
        y = data['label'].tolist()
        lg_y = lg.predict(X)
        # print the predicted y of each task
        print lg_y