#file = open('test.txt')

#file.close()

# we can also use one line code to open and close a file in python

# task:
# read the file and store all the lines in list
# reverse the list
# write the list back to the file

with open('test.txt', 'r') as reader: #  'r' for read mode of file and 'w' for write mode of file
    content = reader.readlines()
    rev = reversed(content)

    with open('test.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)

