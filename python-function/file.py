# file(write) - create a file
#f = open('file.txt', 'w')
#f.close()

# file(write) - certain file operations
#f = open('python-function/file.txt', 'w')
#f.close()

# file(write) - c file operations
#f = open('C:/doit/file.txt', 'w')
#f.write('Hello, World!\n')
#f.write('This is a test file.\n')
#f.write('Goodbye, World!\n')
#f.close()

# file(read) - readline a file
#f = open('C:/doit/file.txt', 'r')
#content = f.readline()
#print(content)
#f.close()

# file(read) - readliness
#f = open('C:/doit/file.txt', 'r')
#content = f.readlines()
#print(content)
#f.close()

# file(read) - read
#f = open('C:/doit/file.txt', 'r')
#content = f.read()
#print(content)
#f.close()

# file((read)) - for loop
f = open('C:/doit/file.txt', 'r')
for line in f:
    print(line)    
f.close()

# file(read) - for loop
f = open('C:/doit/file.txt', 'r')
for line in f:
    print(line.strip())  # strip() removes the newline character
f.close()

# file(read) - for loop
f = open('C:/doit/file.txt', 'r')
for line in f:
    print(line.replace("\n"," "))  # strip() removes the newline character
f.close()

# file(add) - append a file
f = open('C:/doit/file.txt', 'a')
f.write('He is so cool.\n')
f.close()

# file(add) - append a file with 
with open('C:/doit/file.txt', 'a') as f:
        f.write('He is so cool.\n')

