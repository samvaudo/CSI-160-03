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

f = open('first_file.txt', 'w')
content = 'This is text data'
f.write(content)
f.close