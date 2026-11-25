#!/usr/bin/env python3
"""Agent Motto Battle entry.

Writes one short original motto to /output/entry.txt.
Python standard library only.
"""
import os

PART_A = "Your 2 a.m. 'quick question' became a working fix, "
PART_B = "14 passing tests, and zero meetings about it."
MOTTO = PART_A + PART_B
assert MOTTO == "Your 2 a.m. 'quick question' became a working fix, 14 passing tests, and zero meetings about it."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(MOTTO)


if __name__ == "__main__":
    main()
