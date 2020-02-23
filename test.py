#!/usr/bin/env python3
import os

from litex.data.cpu import microwatt

print("Found microwatt @ version", microwatt.version_str, "("+microwatt.git_hash+")")
print("Data is in", microwatt.data_location)
assert os.path.exists(microwatt.data_location)
print("It contains:\n -", end=" ")
print("\n - ".join(os.listdir(microwatt.data_location)))