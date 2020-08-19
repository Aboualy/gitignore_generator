####  gitignore file generator/automator 
The main goal of this module/app is to help you search for and ignore annoying duplicate files in your project like .DS_Store , __pycache__ etc 

The app finds all the (predefined) unwanted files/folders and adds their paths to .gitignore if they are not present in it

  
~~~~**Project/
|-- project/
|   |-- test/
|   |   |-- __init__.py
|   |   |-- test_main.py
|   |   |-- __pycache__
|   |   |-- .DS_Store 
|
|   |-- dir1/
|   |   |-- __pycache__
|   |   |-- .DS_Store 
|
|   |-- __init__.py
|   |-- main.py
|   |-- __pycache__
|   |-- .DS_Store 
|
|-- setup.py
|-- README~~~~**

# The app will search for _pycache__ and .DS_Store paths (or any other unwated files/folders) and add them to .gitignore

The paths: 

__pycache__
.DS_Store 
dir1/__pycache__
dir1/.DS_Store 
test/__pycache__
test/.DS_Store 


.DS_Store files are created by Mac OS X to define how a folder's icons are positioned and which background image will appear

__pycache__ is a folder containing Python 3 bytecode compiled and ready to be executed

Reference for gitignore file :https://stackoverflow.com/questions/3719243/best-practices-for-adding-gitignore-file-for-python-projects