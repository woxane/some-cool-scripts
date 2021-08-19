#!/usr/bin/python3

import subprocess
import os 

files = subprocess.check_output(["ls"]).decode().splitlines()

mkv = [i[:-4] for i in files if i[-3:] == "mkv"]
srt = [i[:-4] for i in files if i[-3:] == "srt"]

for i in range(0,len(mkv)) :
    print(srt[i])
    print(mkv[i])
    os.rename(srt[i]+".srt", mkv[i]+".srt")
