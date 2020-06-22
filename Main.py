import os,sys
# whatever.
import time
i=os.getpid()
print(i)
# you can generate two locks: .rlock, .wlock.
# the only solution is to put pid inside the lock.
# print("$ echo 'foobar' > /proc/{0}/fd/0".format(os.getpid()))
print("this is the main lazero program.")
# with open("/tmp/lazero","r") as f:
# print("read :: [" + sys.stdin.readline() + "]")
k=5
while k>=0:
    s=sys.stdin.readline()
    if len(s)==0:
        print("dummy!")
    # print(s,len(s))
    else:
        print(s)
    # empty string? can we check it??
    # this has a lock there.
    # print("dummy!")
    time.sleep(0.5)
    k-=1
# is it a normal console?
# not working??
# does not work.
# does that work????
#     # you can timeout this.
#     i=f.read()
# i can send bytes.
#     print(i)
# i=input("does this work?")
# import os, sys
# if __name__ == "__main__":
    # print("Try commands below")
    # while True:
        # pass
# print(i)
# /dev/pts/4 ??
# can we bind it to other places? detach or something?
# it does not affect the program.
# it competes with the input.
# mkfifo???
# multiple output??