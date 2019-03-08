# Vinh Pham
# 10/4/16
# Lab 6


# Define what you are using to check.
UPPER_CASE= "ABCDEFGHIJKLMNOPQRSTUVWXYZ_"


# story = "To VERB_ONE or not to VERB_ONE: that is the NOUN_ONE:" <--- this is just an Example
# Ask user for string in proper format.
story = input("Type in a MadLib using ALL_CAPS for your variables: ")
print () # Just makes it easier to read in executed program
print ("MadLib: ",story) # Confirming
print ()


used_variables =[] # So it doesn't ask for the same variable twice.
variable ="" # For the program to recognize variables through single characters.
new_story = story # Result output

# Check letter
for char in range(0,len(story)):
    # Below are the conditions to recognize a variable.
    if story[char] in UPPER_CASE and story[char-1] in UPPER_CASE and story[char-2]== " ":
        variable = story[char-1]
        while char < len(story) and story[char] in UPPER_CASE:
            variable += story[char]
            char+=1
        if variable not in used_variables: # So it doesn't ask for same variable twice.
            used_variables.append(variable)
            replacement = input("Change {} into: ".format(variable)) #So it won't affect loop reading
            new_story = new_story.replace(variable,replacement)    
        
# Success!
print ()
print (new_story)

