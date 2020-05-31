# i do not know shit about bradient descent.
import torch
import torch.nn as nn
import numpy as np
from confirm_shape import get_writings
import time
device = torch.device("cuda")
# total time 42.38628387451172
# you know, it is not significantly faster.
# middle is for hiddern layer dimension.
actual, o = get_writings()
# one-hot.
hotter = list(sorted(set(actual.reshape(-1).tolist())))
n_in, n_h, n_out, batch_size = o.shape[1], 25, 10, o.shape[0]


def one_hotter(am, bm):
    r = [0 for x in range(len(bm))]
    r[bm.index(am)] = 1
    return r

# one extra recommendation: when not importable, release this thing to another category: unknown.
# and when shape problem occurs, raise the exception.
def dec_one(cm, bm):
    return bm[cm.index(1)]
# i know the principles. i just hate to manually check all the shits.

model = nn.Sequential(nn.Linear(n_in, n_h), nn.ReLU(),
                      nn.Linear(n_h, n_out), nn.Sigmoid())
criterion = torch.nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)  # learning rate
x = torch.Tensor(o.tolist())
y = torch.Tensor([one_hotter(x0[0], hotter) for x0 in actual.tolist()])
# print(x.shape,y.shape)
# print(y)
y = y.to(device)
x = x.to(device)
model = model.to(device)
t = time.time()
for epoch in range(50000):
    # y = baseIV()  # very strange.
    y_pred = model(x)
    # print("prediction", y_pred)
    loss = criterion(y_pred, y)
    print("loss",loss)
    # print("epoch", epoch, "loss", loss, type(loss))
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
print("total time", time.time()-t)
