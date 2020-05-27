import numpy as np
import torch
n = np.array([1, 2, 3, 4, 2, 2, 3, 4])
d = n.reshape(-1, 4, 1)
print(d)
# compare with tensor.
t=torch.tensor(d)
# what the heck?
print(t)
t0=d.tolist()
t0=torch.tensor(t0)
print(t0)
# fuck.
y = torch.tensor([[[1.0], [0.0], [0.0], [1.0], [1.0],
                    [1.0], [0.0], [0.0], [1.0], [1.0]], [[0.5], [-0.2], [-0.5], [-0.3], [1.0],
                                                         [-0.2], [0.8], [0.5], [-0.1], [0.1]]])
print(y,y.shape)
# print(n.shape, d.shape)
# # what is the difference?
# print(n.tolist())
# print(d.tolist())
# # this is how we flattern shits? what about dict?
# # r={"1",1,"2",2}
# # holy shit. this is comprehensible. can this be tensor?
# r = {"1": 1, "2": 2, "v": {"#": 3, "s": {"##": 4}}}
# # this is a set, not a dict
# s = np.array(r)
# print(s, type(s), type(r))
# # flat.
# # this one has size one.
# f = s.tolist()
# print(f, type(f))
# holy shit.
# f=s.reshape(-1,0)
# print(f,f.shape)
# what the heck?
# v=torch.Tensor(s)
# type is object.
# print(v,type(v))
# everything numpy?
