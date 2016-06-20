#!/bin/bash
# This script imitates `wc -l`.

# Please don't forget to make it executable or use with shell executable explicidly.

awk ' END { print "     "NR }' <&0