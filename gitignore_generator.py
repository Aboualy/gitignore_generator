#!/usr/bin/env python
# coding: utf-8

import os

"""

The main goal of this module is to help you ignore annoying duplicate files in your project like .DS_Store , __pycache__ etc 
The function below will follow all unwanted files/dirs and add their paths to  .gitignore if they are not present in it

.DS_Store files are created by Mac OS X to define how a folder's icons are positioned and which background image will appear
__pycache__ is a folder containing Python 3 bytecode compiled and ready to be executed

"""


def ignoring_annoying_files_dirs():
    tobe_ignored = ['.DS_Store','__pycache__','.ipynb_checkpoints', '.idea']
    currdir_path = os.path.abspath(os.curdir)
    root = os.path.abspath(os.curdir)
    ignored_paths = []
    exclude = set(['venv'])
    for path, subdirs, files in os.walk(root):
        for subdir in subdirs:
            if tobe_ignored.__contains__(subdir):
                full_path = os.path.join(path, subdir)
                ig_subdirs = os.path.relpath(full_path, currdir_path)
                # If you prefer a forward slash (/) at the end of the folder name
                ignored_paths.append(ig_subdirs + '/')
                # otherwise
                ignored_paths.append(ig_subdirs)
        subdirs[:] = [d for d in subdirs if d not in exclude]
        for name in files:
            if tobe_ignored.__contains__(name):
                full_path = os.path.join(path, name)
                ig_files = os.path.relpath(full_path, currdir_path)
                ignored_paths.append(ig_files)

    mode = 'r+' if os.path.exists(currdir_path + '/.gitignore') else 'a+'
    with open('.gitignore', mode) as f:
        lines =[i.replace('\n','') for i in f.readlines()]
        ignoredfiles = set(ignored_paths) - set(lines)
        if ignoredfiles is not None:
        #nline = "\n" + '# automatically generated lines ' "\n"
            f.write("\n")
            [f.write("{}\n".format(i)) for i in ignoredfiles]


ignoring_annoying_files_dirs()