# Vinh Pham
# 9/27/16
# Lab 5

S="I had a cat named amanda when I was little"
count = 0


##for i in S:           Here is the original.
##    if i== "a":
##        count +=1
##print (count)



# Use two counters instead of 1 and set to run until last letter.
i = 0
while i < len(S):
    if S[i] == "a":
        count +=1
    i+=1
print (count)
    
