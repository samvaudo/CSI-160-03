#Managing data in permanent files

'''
Key methods
1. write() - writes data to a file: Overwrites data in a file
2. read() - reads data from a file: Creates a copy for presenting
3. append() - appends data to a file: (update)

If theres a situation where the programmer writes to a non-existent file, the Python interpreter will
first create the file and then writes to it

File handler: Manages the use of open(), close(), write(), read(), and append()

IF YOU HAVE AN open(), THERE MUST BE A close()
'''


'''
#Writing to a file
f1 = open('first_file.txt', 'a') #Opens in append mode
content1 = 'More data. ' #content
f1.write(content1) # adds to data
f1.close() #closes file

#Reading data from a file
f2 = open('first_file.txt', 'r') #Opens in read mode
content2 = f2.read() #Reads file
print(content2) #Prints content
f2.close() #Closes file

#Context Manager - It automatically closes any open files in a process
with open('first_file.txt','r') as f3:
    content3 = f3.read()
    print('You are reading from the file "first_file.txt"')
    print(content3)
'''

file = 'first_file.txt'
data = input('Enter data for this file:')

with open(file,'a') as f:
    f.write(data)

with open(file,'r') as f2:
    content = f2.read(5) #This can control the number of characters to output
    print(content)