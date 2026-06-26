# random accessing of binary files
# open a binary for writing and reading 
f = open('line.bin','w+b')

# now file pointer will be at 0th byte
n = f.tell()
print(n)    # displays 0

# write a string with 16 characters 
f.write(b'Python text book')

# now the file pointer moves to 16th byte
print(f.tell()) # displays 16

# move file pointer to 0th and read first 6 bytes
f.seek(0,0) # moves the pointer to the 0th byte from the file begninning
data = f.read(6)
print(data.decode())    # displays Python

# moves file pointer to 4th byte from ending 
f.seek(-4,2)
data = f.read(4)    # reads 4 bytes from there
print(data.decode())    # displays book

# colse the file 
f.close()