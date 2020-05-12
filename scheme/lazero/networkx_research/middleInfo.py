import random
import networkx as nx
from getFromPickleR import returnWTF, returnFuckMe
import copy
import re
# platform for that thing to execute the code.
r2048 = returnWTF()
f2048 = [x for y in returnFuckMe() for x in y]


def catchMyError(a, b):
    try:
        a(b)
    except Exception as e:
        return e


def binaryAppendex(b):
    a = copy.copy(b)
    assert type(a) == str
    def fma(
        x): return x in "0123456789_QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm"
    a0, a1 = "", ""
    a2 = []
    for x in a:
        if fma(x):
            a0 += x
            if a1 != "":
                a2.append(a1)
                a1 = ""
        else:
            # if fma(x):
            a1 += x
            if a0 != "":
                a2.append(a0)
                a0 = ""
    if a0 != "":
        a2.append(a0)
    if a1 != "":
        a2.append(a1)
    return a2
    # just check whether the first one's type and it is done.

# remainder: str has no append a.append(y) -> a+=y


def casualCode(a):
    g = list(globals().keys())+f2048
    g0 = binaryAppendex(a)
    # execute it yourself?
    # imagine the code?
    g1 = [(x, x in g) for x in g0]
    return g1
# can't escape.
# check executable code?
# get me to the parser. get me to the highlighter. very important in developing this thing.
# but let's talk about HOW TO FIND AND USE IT.
# replace it with current shits?
# it is binary, relative.


# internal solver? yes.
# find the map. the hidden potential list.
# print(r2048)
# exec()
# learn whether executable or not?
# problem? start to delete things.
# is it str?
# exec(r2048)
c = "catchMyError(exec, r2048)"
c0 = casualCode(c)
print(c0)
# so what is the problem with this code?
# equivalent form?
c1 = exec(c)
print(c1)
# check the procedure?
# analyze the code?

# print(c,type(c))
# consider your fix.
# all fucking procedure must be declared explicitly.
# search for all consistents.
# all builtins?
# error persists.
# there is no trust.
# print(c,type(c))
# have error? solve it?
# intention?
