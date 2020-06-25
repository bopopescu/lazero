#!/bin/bash
echo -e '#include <stdio.h>\nint main(){printf("this is the main lazero program.\\\n");}'>/dev/shm/sample.c && command c /dev/shm/sample.c && rm /dev/shm/sample.c