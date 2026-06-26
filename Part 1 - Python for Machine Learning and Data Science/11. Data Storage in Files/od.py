# # Method 1: The Modern Way (pathlib)
# # pathlib treats file paths as objects rather than just strings, making it very clean and easy to read.
#_______________________________________________________

# from pathlib import Path

# # Get the current working directory
# current_dir = Path.cwd()

# print(f"Contents of {current_dir}:\n")

# # Iterate through all items in the directory
# for item in current_dir.iterdir():
#     # Check if it's a directory or a file to format the output nicely
#     item_type = "[DIR]" if item.is_dir() else "[FILE]"
#     print(f"{item_type} {item.name}")


#----------------------------------------------

# Method 2: The Classic Way (os.listdir)
# If you are working with older codebases, you will frequently see the os module used. os.listdir() returns a simple list of strings representing the names of the files and folders.
#_______________________________________________________________________________
# import os

# # Get the current working directory path
# current_dir = os.getcwd()

# print(f"Contents of {current_dir}:\n")

# # Get a list of all files and folders
# dir_contents = os.listdir(current_dir)

# for item in dir_contents:
#     print(item)
    
#----------------------------------------------
# Method 3: The Detailed Way (Using os.walk)
# If you don't just want the current directory, but also want to look inside every single subfolder (recursively), you can use os.walk.
#______________________________________________
# import os

# # Walks through the current directory, its subdirectories, and files
# for root, dirs, files in os.walk('.'):
#     print(f"Current Folder: {root}")
#     print(f"Subdirectories: {dirs}")
#     print(f"Files: {files}")
#     print("-" * 20)

#------------------------------------------------
# Method 4
#_______________________________
import os

# Walks through the current directory, its subdirectories, and files
for dirpath, dirnames, filenames in os.walk('.'):
    print('Current path:',dirpath)
    print('Directories:',dirnames)
    print('Files:',filenames)
    print()