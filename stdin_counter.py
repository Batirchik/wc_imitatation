#!/usr/bin/env python
# This script imitates `wc -l`.

import sys

# Lets print with the same indent as `wc -l` does!
print " "*5 + "%s" % len(sys.stdin.readlines())


"""
For huge files please consider to read line by line.

line_count = 0
for line in sys.stdin:
    line_count += 1
print " "*5 + "%s" % line_count
"""
