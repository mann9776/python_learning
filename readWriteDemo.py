file = open('test.txt')

#  read all the contents of the file
#print(file.read(5)) # passing parameter read n number of characters

#print(file.readline()) # read one single line at a time
#print(file.readline())

#  print line by line using readline method

#line = file.readline()

#while line!="":
#    print(line)
#    line = file.readline()

# readlines put all the lines in an array

for line in file.readlines():
    print(line)

file.close()
