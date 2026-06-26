import os
import sys

# Accept file name from keyboard
filename = input("Enter the filename to open: ")

# Check if the file exists on the disk
if os.path.isfile(filename):
    print(f"\n--- Contents of '{filename}' ---")
    with open(filename, 'r') as f:
        print(f.read())
else:
    print(f"Error: The file '{filename}' does not exist.")
    # Terminate the program cleanly
    sys.exit()