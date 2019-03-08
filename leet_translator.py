# Vinh Pham
# 11/8/16
# Lab 10, leet_translator
# Create 2 functions that translate leet to eng and eng to leet.


def leet_to_eng(dict_input,leet):
    """Translates leet to english"""
    return dict_input[leet] #Format for returning the value.

def eng_to_leet(dict_input,eng):
    """Translates english to leet"""
    for key,val in dict_input.items(): #Runs through the keys and respective values
        if val == eng: # When definition matches the value
            return key 
                       
def main(): #Testing purposes
    """Main program"""
    my_dict ={'y':'why', 'r':'are', 'u':'you', 'l8':'late'} 
    print (leet_to_eng(my_dict,'y'))    
    print (eng_to_leet(my_dict,'why'))
