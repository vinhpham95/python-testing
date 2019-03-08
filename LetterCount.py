# Vinh Pham
# 10/11/16
# Lab 7 -  Letter Count
# Counts all the letters in a word file.

# Prompt for file_name to open
file_name = input("What is the file name?: ")
words_file = open(file_name)
all_words = ""

# Combine all lines into a giant string
for line_str in words_file:
    line_str.lower()    #Convert to lowercase to avoid dealing with upper/lower-case seperately
    all_words +=line_str

# This is how you count specific characters in a string
a_count = (all_words.count('a'))
b_count = (all_words.count('b'))
c_count = (all_words.count('c'))
d_count = (all_words.count('d'))
e_count = (all_words.count('e'))
f_count = (all_words.count('f'))
g_count = (all_words.count('g'))
h_count = (all_words.count('h'))
i_count = (all_words.count('i'))
j_count = (all_words.count('j'))
k_count = (all_words.count('k'))
l_count = (all_words.count('l'))
m_count = (all_words.count('m'))
n_count = (all_words.count('n'))
o_count = (all_words.count('o'))
p_count = (all_words.count('p'))
q_count = (all_words.count('q'))
r_count = (all_words.count('r'))
s_count = (all_words.count('s'))
t_count = (all_words.count('t'))
u_count = (all_words.count('u'))
v_count = (all_words.count('v'))
w_count = (all_words.count('w'))
x_count = (all_words.count('x'))
y_count = (all_words.count('y'))
z_count = (all_words.count('z'))

# Formality
print ('I see',a_count,'as',b_count,'bs',c_count,'cs',\
       d_count,'ds',e_count,'es',f_count,'fs',g_count,'gs',\
       h_count,'hs',i_count,'is',j_count,'js',k_count,'ks',\
       l_count,'ls',m_count,'ms',n_count,'ns',o_count,'os',\
       p_count,'ps',q_count,'qs',r_count,'rs',s_count,'ss',\
       t_count,'ts',u_count,'us',v_count,'vs',w_count,'ws',\
       x_count,'xs',y_count,'ys',z_count,'zs')

# Necessity
words_file.close()
    
