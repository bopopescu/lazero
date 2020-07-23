#!/bin/bash
docker run --rm --kernel-memory="8m" --memory-swap="16m" --cpus="0.05" --memory="16m" --memory-reservation="8m" -it --storage-opt overlayfs2.size=0.008G alpine sh
# --read-only
# if it is XFS it is way better than now.
