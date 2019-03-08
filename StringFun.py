#Vinh Pham
# 9/27/16
# Lab 5

# Exercise 1:Given the string "Monty Python":
# (a) Write an expression to print the first character.
# (b) Write an expression to print the last character.
# (c) Write an expression inculding len to print the last character.
# (d) Write an expression that prints "Monty".
# Exercise 2: Given the string "homebody":
# (a) Write an expression using slicing to print "home".
# (b) Write an expression using slicing to print "body".
# Exercise 3: Given a variable S containing a string of even length:
# (a) Write an expression to print out the first half of the string.
# (b) Write an expression to print out the second half of the string.
# Exercise 4:Given a variable S containing a string of odd length:
# (a) Write an expression to print the middle character.
# (b) Write an expression to print the string up to but not including the middle character
# (c) Write an expression to print the string from the middle
#      character to the end (not including the middle character).


# Exercise 1
string_1 = "Monty Python"
print (string_1[0]) 
print (string_1[-1])
print (string_1[len(string_1)-1])
print (string_1[:5])

# Exercise 2.
string_2 = "homebody"
print (string_2[0:4])
print (string_2[4:])

#Exercise 3.
s = "123456"
print (s[:int(len(s)/2)])
print (s[int(len(s)/2):])

#Exercise 4.
s = "123456789"
print (s[int(len(s)/2)])
print (s[:int(len(s)/2)])
print (s[int(len(s)/2+1):])

