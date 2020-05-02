from getLinkage import reinforce
with open("baidu.log") as f:
    f0=f.read()
    m=reinforce(f0,50)
    print(m)
