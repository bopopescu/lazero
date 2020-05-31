import pynput
import time
import pyautogui
# import cv2
# while True:
# fuck.
# is this how you fucking live?
# you can do this for many shits.
# use background mouse input? come on.
# on windows there's a different story, for mouse.
# do not take it seriously. they are all experiments.
# scale those shits?
# rotate, and more.
# glob=[]
# def der(a):
#     return [(a[x][0]-a[x+1][0],a[x][1]-a[x+1][1]) for x in range(len(a)-1)]
# def calc(a):
#     r=list(map(lambda x: x[:2],a))
#     print(der(r))
def a(*b):
    # global glob
    print(time.time(),*b)
    if len(b)>2:
        p=pyautogui.screenshot(region=[b[0]-25,b[1]-25,25,25])
        # can you see the cursor?
        # use boundary-safe function to do this cropping task.
        # with mouse?
        # is my code right?
        # it is going crazy.
        # print(dir(p))
        # p.show()
        # cv2.show(p)
    # if len(glob)<10:
    #     glob.append(b)
    # else:
    #     # print(glob)
    #     print(calc(glob))
    #     glob=[]
# def a(p,*b):
#     print(time.time(),*b)
    # how to pass to another function?
    # send via network.
# try to specify the process.
# p= Process(target=)
    # send via process??
    # use pipe???
    # how to write these shits?
# with pynput.mouse.Listener(on_move=lambda x:a(p,x),on_scroll=lambda x:a(p,x),on_click=lambda x:a(p,x)) as l:
with pynput.mouse.Listener(on_move=a,on_scroll=a,on_click=a) as l:
    try:
        l.join()
    except:
        pass
    # fucking cool shit.
    # print(e)
# print(dir(pynput))
# great shit.
# but this is a huge shit.
# it takes too many shits.
# you even have scrolling!
# now you've got the data! raw data waiting for processing.
# and you can do it yourself.