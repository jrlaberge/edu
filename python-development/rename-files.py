#!/usr/bin/env python3

import sys
import subprocess
import re

def rename_files(directory, old_string, new_string):
    proc = subprocess.run(['find', directory, '-type', 'f', '-name', f"*{old_string}*"], stdout=subprocess.PIPE)
    files = proc.stdout.decode().split()
    counter = 0
    for file in files:
        subprocess.run(['mv', file, file.replace(old_string, new_string)])
        print(file)
        counter += 1
    print(f"{counter} files renamed successfully")

rename_files('.', old_string = sys.argv[1], new_string = sys.argv[2])
