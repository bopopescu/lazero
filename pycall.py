from subprocess import call
# this is redirection. but where is stdin?
# making it online is required, but how do you make it online without basic knowledge?
# asking for knowledge is not wise.
# i can pass it to a file object and then just redirect it to the result!
with open("sample.log","w+") as f:
    s=["ls"]
    # s=["yes"]
    c=call(s,stdout=f,stderr=f,cwd="/bin/")
    # well, knowledge is a good thing.
    # I mean, can we do it at some temp location???
    # what does this shit believe? icons? strings? RA9?