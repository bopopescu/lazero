#!/bin/bash
# firejail --cgroup=/sys/fs/cgroup/lazero/tasks  --apparmor --disable-mnt bash
firejail --apparmor --disable-mnt bash
