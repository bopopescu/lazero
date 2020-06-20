import fcntl
import sys
import termios
# https://unix.stackexchange.com/questions/48103/construct-a-command-by-putting-a-string-into-a-tty/48221
# i really have to tear it off to get the essense of machine.
# it is unknown numbers. just like that.
# what the fuck. all the same.
# what about some sort of screen command?
# xdotool
# expect??
# quit it.
# that really works.
# but it is still hard to get content from windows???
with open('/dev/pts/0', 'w') as fd:
    # with open('/proc/71043/fd/0', 'w') as fd:
    for char in "\x01d":
        fcntl.ioctl(fd, termios.TIOCSTI, char)
        # it works. you can do some util.
        # io control on file descripters? what about windows?
        # forget about it. all we need is concentration.