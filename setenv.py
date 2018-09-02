#!/usr/bin/env python3
# Purpose: Read config and set in the environment
# See also: https://docs.aws.amazon.com/cli/latest/topic/config-vars.html
# Usage:
#    Run ./setenv.py then copy-paste output to terminal
#    eval `python3 ./setenv.py` is not working, did it ever?

print('export LC_ALL="{}"'.format('en_US.UTF-8'))
print('export LANG="{}"'.format('en_US.UTF-8'))
