#Combining argv and raw_input works as long as
# you enter correct number arguments on command line
from sys import argv

#script = raw_input("Call me a name ")
first = raw_input("First item please? ")
second = raw_input("Second? ")
#third = raw_input("Third? ")
#script, first, second, third = argv
script, third = argv


print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third


