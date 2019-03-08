# Vinh Pham
# 9/27/16
# Lab 5 - Spam

import random
choice = input("Please choose from the following: turkey, ham, rice, eggroll: ")

before = random.randint(0,3)
after = random.randint(0,3)
print (before*"SPAM ",choice,after*"SPAM ")
