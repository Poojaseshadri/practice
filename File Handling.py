with open('hello.txt', 'r') as file:
    content = file.read()
    print(content)
    
with open('hello.txt', 'w') as file:
    file.write('  happy days  ')
       
try:
    with open('hello.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print('File not found!')
except IOError:
    print('Error reading the file!')
    
    
with open('hello.txt', 'r') as file:
    content = file.read()
    print(content)

with open('hello.txt', 'r') as file:
    content = file.readline()
    print(content)

with open('hello.txt', 'r') as file:
    content = file.readlines()
    print(content)


with open('hello.txt', 'w') as file:
    file.write('Hello! Welcome to demofile.txt\n'
    'This file is for testing purposes.\n'
    'Good Luck!\n')
with open('hello.txt', 'w') as file:
    file.writelines('Hello! Welcome to demofile.txt\n'
    'This file is for testing purposes.\n'
    'Good Luck!\n'
    'happy\n')
try:
    with open('hello.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print('File not found!')

except IOError:
    print('Error reading the file!')
fhand =open('hello.txt')
print(fhand)