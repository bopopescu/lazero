# import random
# what is this random for?
# randomly select shits, and yinject them
def radrepl(a, b, f=0):
    assert f >= 0 and type(f) == int and f <= len(a)
    # s0=[x for x in a]
    def r0(x): return r'{}'.format(x)
    sf = []
    for r in range(len(s)-f+1):
        for z in b:
            sx = r''.join([r0(s[:r]), r0(z), r0(s[r+f:])])
            sf.append(sx)
    return sf

# i do not want to learn any fucking c code.
# i just want to fuck.
# let the mean value be that value.
# solve the matrix?
# (x+(1)y+(2)z+...+[2q]d)/(x+y+z+...+d)=q
# nothing here!
# when talk about recursive matters, my computer usually slows the hell down.
# raw instincts.
# learn syntax rules? you can find it by some function discovery.
# count, replace.
s = r"""print(f"\033[1m\033[92m=======")"""
# reverse the order? you need discovery!
# maybe only partial reverse, but not all!
# other shits need for discovery and collection.
# alter things.
# s0 = set(s)
# print(s0)  # we've got raw shits, beyond manupulation.
# this works.
# s1 = str(s)
# sx = ["happy"]
# also consider zero. for insertion.
# that's how we do the job.
# consider len(a) for replace.
sx=[""]
# want to replace? just do it.
# works for all shit.
r = radrepl(s, sx, 5)
for x in r:
    print(x, type(x))
# print(s1)
# eval(s1)
# to alter things at char level.
# they complie octave code beforehand.
