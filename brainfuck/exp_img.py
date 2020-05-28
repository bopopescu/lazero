registry = None
def recv(number):
    global registry
    if registry is not None:
        if number == registry:
            return number+number*1j
        else:
            r=number+registry*1j
            registry=number
            return r
    else:
        registry=number
        return number
# this is self-repeating.
px=[1,2,3,4,5,4,3,2,1]
for x in px:
    print(recv(x))