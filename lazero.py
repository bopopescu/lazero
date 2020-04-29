so="""    -
   |               ___  __  __
  / \  |    /|  /  ___ |   |  |
 \  _\ |__ / | /__ ___ |   |__|

To make everything
executable, analyzable, controllable."""
s=filter(lambda x: "\n" not in x,so.split("\n"))
si=map(lambda x: "printf(\"%s\\n\");" % (x,),s)
for x in si:
    print(x)
# this is a metaprogram.
# it is strange, to launch code in debug mode.
# never seen this before.