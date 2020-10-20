#! /usr/bin/python3

from build_map import *



filename = "map1.txt"
print(f"INPUT FILE: {filename}")

forward = build_map(filename)

if forward is None:
    print("TESTCASE: build_map() returned None")
else:
    print(f"build_map() returned:")
    for k in forward.keys():
        print(f"{k}: {forward[k]}")


print()
print("TESTCASE COMPLETED")


