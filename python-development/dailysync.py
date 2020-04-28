#!/usr/bin/env python3
import subprocess
import os
from multiprocessing import Pool

src = "../data/prod/"
dest = "../data/prod_backup/"
get_dirs = [f for f in os.walk(src)][0][1]
dirs = []
for d in get_dirs:
    dirs.append(f"{src}{d}"
def backup(directory):
    print(f"Backing up {directory}...")
    subprocess.call(["rsync", "-arq", directory, dest])

if __name__ == '__main__':
    p = Pool(len(dirs))
    p.map(backup, dirs)

