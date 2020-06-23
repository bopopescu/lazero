from subprocess import call

# this is redirection. but where is stdin?
# making it online is required, but how do you make it online without basic knowledge?
# asking for knowledge is not wise.
with open("sample.log","w+") as f:
    s=["ls"]
    c=call(s,stdout=f,stderr=f,cwd="/bin/")
    # well, knowledge is a good thing.