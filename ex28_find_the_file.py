# Write a function find that gets as input a path to a folder. Within this folder (and all of its subfolders), there is file with the content 's3cr3t' in it. Once you found the correct file based on its content, return the file path
#
# You must use the os library.

import os

def find(path):
    # return the file path of the file that contains 's3cr3t'

    for root, dirs, files in os.walk(path):
        for file in files:
                with open(os.path.join(root, file)) as currf:
                    for line in currf:
                        if 's3cr3t' in line:
                            return os.path.join(root, file)

    pass