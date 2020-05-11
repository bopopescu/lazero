from getFromPickleR import returnList
from simpleStorageR import storeWTF
# this is the exact step: mimic our operation
# PREDICT OUR OPERATION
# PREDICT MORE
# RUN ALONE
# MAKE SURE WE, THE HUMAN BEINGS, THE MAJOR LEAGUES, ARE RIGHTFUL.
# JUST LIKE OUR RIGHT HAND TEACHING LEFT HAND.
r=returnList()
# print(type(r))
l=list(r.keys())
# {'code_exec': [], 'link_cap': [], 'equation': False, 'class_name': False, 'curly_bracket': [], 'round_bracket': [], 'square_bracket': []}
r0=[]
for x in l:
    p = r[x]['code_exec']
    if p != []:
        r0.append(p)
# print(r0)
storeWTF(r0)