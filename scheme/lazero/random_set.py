def export_sets(a,window_size):
    print(a)
    assert type(window_size)==int and window_size>1
    assert type(a) in [list,str] and len(a)>2
    return [frozenset(a[x:x+window_size]) for x in range(len(a)-window_size)]

def meta_sets(a,window_size,evolution=0):
    assert type(evolution)==int and evolution >=0
    a0=export_sets(a,window_size)
    if evolution ==0:
        return a0
    else:
        return meta_sets(a0,window_size,evolution-1)
