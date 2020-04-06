#!/usr/bin/env python3
import os

from litex.data.cpu import microwatt

print("Found microwatt @ version", microwatt.version_str, "("+microwatt.git_hash+")")
print("Data is in", microwatt.data_location)
assert os.path.exists(microwatt.data_location)
print("It contains:")
for root, dirs, files in os.walk(microwatt.data_location):
    dirs.sort()
    for f in sorted(files):
        path = os.path.relpath(os.path.join(root, f), microwatt.data_location)
        print(" -", path)
