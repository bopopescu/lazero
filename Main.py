import os,sys
# whatever.
i=os.getpid()
print(i)
# print("$ echo 'foobar' > /proc/{0}/fd/0".format(os.getpid()))
print("this is the main lazero program.")
# with open("/tmp/lazero","r") as f:
# print("read :: [" + sys.stdin.readline() + "]")
print(sys.stdin.readline())
# is it a normal console?
# not working??
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