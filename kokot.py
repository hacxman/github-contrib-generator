#!/usr/bin/python3
import os
import sys

if __name__ == "__main__":
  if len(sys.argv) < 2:
    print("file expected")
    exit(2)

  fname = sys.argv[1]
  with open(fname) as fin:
    data = fin.readlines()

