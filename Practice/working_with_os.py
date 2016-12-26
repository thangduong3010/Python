import os
from os import path
import shutil

def main():
    #print(os.name)
    if path.exists(r"F:\Github\Python\Practice\Files\data\file3.txt"):
        src = path.realpath(r"F:\Github\Python\Practice\Files\data\file3.txt")

        head, tail = path.split(src)
        print("Path: {}".format(head))
        print("Tail: {}".format(tail))

        # make a backup
        dst = src + ".bak"
        # make a copy
        shutil.copy(src, dst)


if __name__ == "__main__":
    main()