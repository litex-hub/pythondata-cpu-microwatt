#!/usr/bin/env python3
import os

from litex.data.cpu import microwatt

print("Found microwatt @ version", microwatt.version_str, "(with data", microwatt.data_version_str, ")")
print()
print("Data is in", microwatt.data_location)
assert os.path.exists(microwatt.data_location)
print("Data is version", microwatt.data_version_str, microwatt.data_git_hash)
print("-"*75)
print(microwatt.data_git_msg)
print("-"*75)
print()
print("It contains:")
for root, dirs, files in os.walk(microwatt.data_location):
    dirs.sort()
    for f in sorted(files):
        path = os.path.relpath(os.path.join(root, f), microwatt.data_location)
        print(" -", path)
