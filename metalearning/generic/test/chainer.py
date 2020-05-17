keyboard=[['q','w','e','r','t','y','u','i','o','p'],['a','s','d','f','g','h','j','k','l'],['z','x','c','v','b','n','m']]
def returnNear(a):
    b=[]
    for x in range(3):
        if a in keyboard[x]:
            b=[x,keyboard[x].index(a),len(keyboard[x])-1]
            break
    if x==0:
        if b[1]!=b[2]:
            return (keyboard[0][b[1]+1],)
        else:
            return False
    if x==1:
        if b[1]!=b[2]:
            return (keyboard[1][b[1]+1],*keyboard[0][b[1]:b[1]+2])
        else:
            return (*keyboard[0][b[1]:b[1]+2],)
    if x==2:
            if b[1]!=b[2]:
                return (keyboard[1][b[1]+1],*keyboard[1][b[1]:b[1]+3])
            else:
                return (*keyboard[0][b[1]:b[1]+3],)

def curse():
    for k0 in range(ord("a"),ord("z")+1):
        r=returnNear(chr(k0))
        print(chr(k0),r if r!= False else "nothing")

curse()
