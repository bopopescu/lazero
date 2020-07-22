#!/bin/bash
# firejail --cgroup=/sys/fs/cgroup/lazero/tasks  --apparmor --disable-mnt bash
firejail --private --blacklist=/ --read-only=/home --nonewprivs --noroot --apparmor --disable-mnt bash
# what the heck is going on? why it is able to modify shits?
