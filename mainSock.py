import socket as s
import time
sock=s.socket(s.AF_UNIX)
# print(dir(sock))
# sock.close("/tmp/lazero.sock")
sock.bind("/tmp/lazero.sock")
# time.sleep(10)
#  /dev/vcsa7  ??
# xsel is a selection manager, without copy and paste.