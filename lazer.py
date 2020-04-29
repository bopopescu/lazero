from getFromDill import returnAList
import random

def reader(f):
    with open(f,"r") as f0:
        return f0.read()

r=returnAList()
r=random.choice(r)
r=reader(r)
print(r)
