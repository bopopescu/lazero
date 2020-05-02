def checkSingle(a):
    d=dir(eval(a) if type(a)== str else a)
    return d

def combine(a):
    a0=checkSingle(a)
    a1=list(map(lambda x:".".join(a,x),a0))
    return a1

def typecheck(a):
    d=type(eval(a) if type(a)== str else a)
    return d

def typeBatch(a):
    d=combine(a)
    d0=list(map((x,typecheck(x)),d))
    return d0

