#!/usr/bin/env python

from time import sleep
import sys

# usage: just run the thing.
print("Firing lasers...")
for i in range(10):
    print("PEW!")
    sleep(0.5)

sys.exit(0)
