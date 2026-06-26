# create a file with strings
# open the file for writing and reading data 
f = open('myfile.txt', 'w+')

print("Enter strings when you finish type @ and enter")
print('Start writing:')

while True:
    line = input()   # accept string into line
    if line == '@':
        break        # Exit loop immediately if '@' is entered
    f.write(line + '\n')

print("-"*20)
# Move file pointer back to the beginning before reading
f.seek(0)        

print("\nReading file contents:")
print(f.read())

# closing the file
f.close()