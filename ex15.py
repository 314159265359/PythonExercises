#Print contents of file after inputting filename from command line

from sys import argv # bring in argv feature-module

script, filename = argv # assign script and filename as the 2 arguments

txt = open(filename) # open file and assign to a variable

print "Here's your file %r:" % filename # prints message and filename
print txt.read() # perform read on file held by variable and print

# Print contents of file after prompting user for filename
print "Type the filename again:"
file_again = raw_input("> ") # uses prompt symbol and assigns input to var

txt_again = open(file_again) #new name of file taken from user not argv

print txt_again.read()

txt.close() # closing files by using assigned file variable
txt_again.close()

### FYI ###
#after entering Python:
#filename = 'ex15_sample.txt'
#txt = open(filename)
#print txt.read()
# ----view contents ----
#quit()

