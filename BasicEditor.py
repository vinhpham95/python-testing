# Vinh Pham
# 10/11/16
# Lab 7 - Basic Editor
# Reads each line from word.txt and copy to temp.txt unless asked to change the line.

# Open appopriate files to use.
words_file = open("words.txt","r")
temp_file = open("temp.txt","w")
line_counter = 0 # To count each line; organization purposes.

# Read each line seperately and change if program receives an input.
for line_str in words_file:
    line_counter +=1
    replacement = input("What do you want to replace for line {}: {}".format(line_counter,line_str))
    if replacement == "":
        print (line_str,end="",file=temp_file)
    else: print (replacement,file=temp_file)
    replacement = ""    # Resets to no input.
    
# Necessity
words_file.close()
temp_file.close()


# This is a test code to read the temp_file.
##temp_file = open("temp.txt","r")
##for line_str in temp_file:
##    print(line_str)
##
##temp_file.close()

# Copy everything back into words_file, overwriting it.
words_file = open("words.txt","w")
temp_file = open("temp.txt","r")
for line_str in temp_file:
    print(line_str,end="",file=words_file)
words_file.close()
temp_file.close()

# This is a test code to read the finished words_file.
##words_file = open("words.txt","r")
##for line_str in words_file:
##    print(line_str)
##
##words_file.close()
