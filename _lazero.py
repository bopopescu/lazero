import subprocess
#import random
from storeADill import storeAList

<<<<<<< HEAD
#def reader(f):
#    with open(f,"r") as f0:
#        return f0.read()

cmd = "ls **/*.py"
ms = subprocess.check_output([cmd],shell=True,executable='/data/data/com.termux/files/usr/bin/zsh')
#print(ms)
ms=ms.decode().split("\n")[:-1]
#print(ms)
ms0=storeAList(ms)
=======
To make everything
executable, analyzable, controllable."""
s=filter(lambda x: "\n" not in x,so.split("\n"))
si=map(lambda x: "printf(\"%s\\n\");" % (x,),s)
for x in si:
    print(x)
# this is a metaprogram.
# it is strange, to launch code in debug mode.
# never seen this before.
>>>>>>> a7a3dc9a4d82ff9379bc7943cf831d3f0527d10f
