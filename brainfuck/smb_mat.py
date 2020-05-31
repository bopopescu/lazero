from sympy import *
import numpy as np
# def ReLU(a):
#     return np.maximum(0,a)
# # wha the fuck?

# tanh?
def sigmoid(a):
    return np.matrix((1/(1+np.e**-(np.array(a))))-0.5)
# def sigmoid(a):
#     return np.matrix((1-np.e**np.array(a)/(1+np.e**np.array(a))))
#     # this value is a symbol!


def mean_squ(a):
    b = np.mean(
        list(map(lambda z: sqrt(abs(z)), [x for y in a.tolist() for x in y])))
    return b


b = np.matrix([[symbols('d{}{}'.format(x, y)) for x in range(6)]
               for y in range(5)])  # <--
b0, b1 = symbols("b0 b1")  # |
a = np.matrix([[symbols('w{}{}'.format(x, y)) for x in range(3)]
               for y in range(6)])  # |
d = np.matrix([[symbols('wf{}{}'.format(x, y))
                for x in range(1)] for y in range(3)])  # |
r = np.matrix([[symbols('r{}{}'.format(x, y)) for x in range(1)]
               for y in range(5)])  # --
# a=np.matrix([[symbols('w{}{}'.format(x,y))+b0 for x in range(5)] for y in range(6)])
# d=np.matrix([[symbols('wf{}{}'.format(x,y))+b1 for x in range(1)] for y in range(5)])
# print(b)
# what about the derivative?
# your fucking deeplearning nightmare!
# cuBLAS? LAPACK? MKL? it is all about it!
# best use some precompiled symbols first, and then dynamically load them.
# the loss func?
# it introduces the headache.
# mean square error?
c = sigmoid(b*a+b0)
c0 = sigmoid(c*d+b1)
c1 = mean_squ(c0-r)
# print(c1)
# horrible nightmare.
# print(b.shape,a.shape,d.shape,c.shape,c0.shape,r.shape)
# c2=
e = Derivative(c1, a).doit()
f = Derivative(c1, d).doit()
g = Derivative(c1, b0).doit()
# does this really work? but i have to say, that i have no fucking choice.
# # so, how do you evaluate this shit?
# # is it possible without symbols?
# # no?
# # not the same.
# i will take another.
print(e.shape, f.shape)
print(g)
# print("derivative with respect of d:{}".format(e.doit()))
# this is horrible.
# is that really the function?