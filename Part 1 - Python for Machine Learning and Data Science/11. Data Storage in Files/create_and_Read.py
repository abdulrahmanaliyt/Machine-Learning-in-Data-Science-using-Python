# Open file in w+ mode (Write + Read)
f = open('myfile.txt', 'w+')

user_text = input('Enter text: ')
f.write(user_text)

# Move file pointer back to the beginning (index 0) before reading
f.seek(0)

# Now reading will work properly
print("Reading file contents:")
print(f.read(8))

f.close()