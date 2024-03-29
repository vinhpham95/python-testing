# Vinh Pham
# 11/8/16
# Lab 10

speech = "to be or not to be"
speech_list = speech.split()

word_count_dict = {}

for word in speech_list:
    if word in word_count_dict:
        word_count_dict[word] += 1
    else:
        word_count_dict[word] = 1

# print(word_count_dict)

#####

def add_word(word, word_count_dict):
    '''Update the word frequency: word is the key, frequency is the value.'''
    if word in word_count_dict:
        word_count_dict[word] += 1
    else:
        word_count_dict[word] = 1


#######


import string
def process_line(line, word_count_dict):
    '''Process the line to get lowercase words to add to the dictionary.'''
    line = line.strip()
    word_list = line.split()
    for word in word_list:
        # ignore the '--' that is in the file
        if word not in ['--', 'a', 'the', 'and', 'it']:
            word = word.lower()
            word = word.strip()
            # get commas, periods and other punctuation out as well
            word = word.strip(string.punctuation)
            add_word(word, word_count_dict)

#####


def pretty_print(word_count_dict):
    '''Print nicely from highest to lowest frequency.'''
    # create a list of tuples, (value, key)
    # value_key_list = [(val,key) for key,val in d.items()]
    value_key_list=[]
    for key,val in word_count_dict.items():
        value_key_list.append((val,key))
    # sort method sorts on list's first element, the frequency. 
    # Reverse to get biggest first
    value_key_list.sort(reverse=True)
    # value_key_list = sorted([(v,k) for k,v in value_key_list.items()], reverse=True)
    file1 = open("gettyanalysis.txt","w")
    print('{:11s}{:11s}'.format('Word', 'Count'),file=file1)
    print('_'*21,file=file1)
    for val,key in value_key_list:
        if val >2:
            print('{:12s}  {:<3d}'.format(key,val),file=file1)
    file1.close()

####

def main ():
    word_count_dict={}
    gba_file = open('gettysburg.txt','r')
    for line in gba_file:
        process_line(line, word_count_dict)
    print('Length of the dictionary:',len(word_count_dict))
    pretty_print(word_count_dict)









