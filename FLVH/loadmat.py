from scipy.io import loadmat
import pandas as pd
mat = loadmat('w.mat')
w = pd.DataFrame(mat['W'])
# print w