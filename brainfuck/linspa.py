import torch
import numpy as np
import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation
# hard to find complex parameters.
# plenty of fuck.
import seaborn as sns
import pandas as pd
# %matplotlib inline
import torch
import torch.nn as nn
from torch.autograd import Variable
# this is for jupyter.
class Lin(nn.Module):
    def __init__(self, input_dim, output_dim):
        super
m=2
c=3
x=np.random.rand(256)
noise=np.random.rand(256)/4
y=x*m+c+noise
df=pd.DataFrame()
df['x']= x
df['y']=y
x_train=x.reshape(-1,1)
# they always hide the dimension.
# print(x_train.shape,x.shape)# does not have second dimension.
y_train=y.reshape(-1,1)
# strange.
# sns.lmplot(x='x',y='y',data=df)
# plt.show()
# what the heck.
# with regression model.
# you always got options.
