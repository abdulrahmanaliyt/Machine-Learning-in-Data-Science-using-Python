# copying an image into a file 
# open the files in binary mode 
f1 = open("E:\\Git coding\ML in DS with Python\Python Basics\\11. Data Storage in Files\Peacock.jpg",'rb')
f2 = open('newPeacock.jpg','wb')

# read bytes from f1 and write into f2
byte = f1.read()
f2.write(byte)

# close the files 
f1.close()
f2.close()
