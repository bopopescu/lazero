#!/bin/bash
# it is fine to dig into chars. but you name it.
mkfifo /tmp/lazero &> /dev/null
while true
do
# maim -i $(xdotool getactivewindow) -f png /tmp/lazero && sleep 1 & sleep 1 && kill $!
maim -f png /tmp/lazero && sleep 2 & sleep 2 && kill $!
# echo hello world
done