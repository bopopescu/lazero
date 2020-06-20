import os
# whatever.
i=os.getpid()
print(i)
print("this is the main lazero program.")
with open("/tmp/lazero","r") as f:
    # you can timeout this.
    i=f.read()
    print(i)
# i=input("does this work?")
# print(i)
# /dev/pts/4 ??
# can we bind it to other places? detach or something?
# it does not affect the program.
# it competes with the input.
# mkfifo???