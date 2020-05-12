import random
import networkx as nx
from getFromPickleR import returnWTF, returnFuckMe
from does_it_have_string import checkEval, eat
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
# always instant need. always. not some unpackable shits, not manuals to be read.
# this is what REAL SHIT IS.

def checkMajorLink(a):
    assert type(a) == list
    l = len(a)
    l0 = [int(x[1]) for x in a]
    l1 = sum([l1[x*2] for x in range(l//2)])
    l2 = sum(l0) - l1
    return l1 > l2

# it is not about the code.
# create custom networks.
# based on natural language?
# maybe. as my comment says.
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
# think about it. think about the infrastructure of this computer.
# so what is the problem with this code?
# equivalent form?
# c1 = eval(c)
c1=checkEval(c)(c)
# this is great.
# it is getting weird.
c2 = str(c1)
c3 = type(c1)
print(c2,c3)
# we are gettings things here.
# build a graph?
# that is an error. consider the fix.
# check the procedure?
# analyze the code?
# check major link.

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
