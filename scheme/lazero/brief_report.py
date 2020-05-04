from simpleStorageR import storeAList
import re
import subprocess

with open ("piplist.log") as f:
    g=f.read()
    h=g.split("\n")[2:]
    j={}
    i=map(lambda x:re.findall(r"^[a-zA-Z0-9\._\-]+",x)[0],h)
    for x in i:
        if len(x)>1:
            msg="pip3 show "+x
            print(msg)
            ms = subprocess.check_output([msg],shell=True,executable='/data/data/com.termux/files/usr/bin/zsh')
            j.update({x:ms.decode()})
            print("processed: {}".format(x))
    storeAList(j)
    print("brief stored.")
