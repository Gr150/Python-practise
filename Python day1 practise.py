#!/usr/bin/env python
# coding: utf-8

# # Chapter 1 - Hello world

# In[167]:


print("Welcome to python programming")


# ### When to use ',", " " " quotes

# In[168]:


print ('welcome to my session')


# In[169]:


print ("welcome to govardhan's session")


# In[170]:


print ("""He started the class with this statemnt, "Hello everyone, welcome to my class".""")


# ### 1.b creating a variable

# In[16]:


scores= 10,20,122,50,60,70,80


# In[17]:


len(scores)


# In[18]:


scores[2:]


# # Chapter 2 String and String method

# ## Different data types in python
# * Integer- numbers without decimal value
# 
# * Float- numbers with decimal value
# 
# * String- characters or values enclosed within quotes

# In[19]:


score_int= 2536


# In[25]:


type(score_int)


# In[27]:


score_float= 35.22


# In[28]:


type(score_float)


# In[30]:


score_string= "It's a six"


# In[31]:


type (score_string)


# ### 2.1 Concatenation, indexing and slicing

# In[32]:


f_name= 'Govardhan'
l_name= 'Reddy'


# In[33]:


print(f_name + ' G ' + l_name) #concatenation


# ### Indexing

# In[51]:


Title='Python programming is fun'


# In[53]:


Title[:]


# In[54]:


Title[0:]


# In[55]:


len(Title)


# In[57]:


Title[:25]


# In[58]:


Title[:-19]


# In[62]:


Title[7:25]


# ## Manipulate strings with methods

# In[46]:


Name_1='Jack'
Name_2='Tom'
Name_3='Chris  moy'


# In[41]:


print(Name_1.capitalize())


# In[42]:


print(Name_1.lower())


# In[43]:


print(Name_1.upper())


# In[47]:


print(Name_3)


# ###  Task 1 - Get 2 example for string methods  ***
# 
# capitalize
# casefold
# center
# count
# encode
# endswith
# expandtabs
# find
# format
# format_map
# index
# isalnum
# isalpha
# isascii
# isdecimal
# isdigit
# isidentifier
# islower
# isnumeric
# isprintable
# isspace
# istitle
# isupper
# join
# ljust
# 
# 
# lower
# lstrip
# maketrans
# partition
# removeperfix
# removesuffix
# replace
# rfind
# rindex
# rjust
# rpartition
# rsplit
# rstrip
# split
# splitlines
# startswith
# strip
# swapcase
# title
# translate
# upper
# zfill 

# ### 1 capitalize

# In[68]:


data='what a great city'
text='awesome'


# In[69]:


print(data.capitalize())


# In[71]:


print(text.capitalize())


# ### 2) casefold- Returns the lower case string.

# In[73]:


txt= 'WhAT A Shot'


# In[74]:


print(txt.casefold())


# In[75]:


case2='HOLY MOLY'


# In[76]:


print(case2.casefold())


# ### 3) center- The center() method returns a new centered string of the specified length, which is padded with the specified character. The deafult character is space.

# In[84]:


ctr='Welcome to Python'


# In[85]:


len(ctr)


# In[88]:


print(ctr.center(24,'>'))


# In[89]:


ctr2='Its a wonderful day'


# In[90]:


print(ctr.center(30,'*'))


# ### 4) count- count of substring

# In[92]:


print(ctr.count('Welcome'))


# In[93]:


cnt= 'The the tHe thE THE ThE'
print (cnt.count('the'))


# In[95]:


cnt1= 'one one one one one'
print(cnt1.count('one'))


# In[97]:


cnt2= 1,1,1,1,1


# In[99]:


print(cnt2.count(1))


# ### 5) encode- Encode the string using the codec registered for encoding.
# 

# In[101]:


print(cnt.encode())


# In[105]:


enc="Chris @t the p@rt*&$#"
print(enc.encode())


# ### 6) endswith-  returns True if a string ends with the specified suffix (case-sensitive), otherwise returns False.

# In[108]:


print(enc.endswith('#'))


# In[111]:


txt=('This is to check the last sentence')
print(txt.endswith('last sentence'))


# ### 7) expandtabs- returns a string with all tab characters \t replaced with one or more space, depending on the number of characters before \t and the specified tab size.

# In[113]:


txt=('there is a \tspace here')
print(txt.expandtabs())


# In[115]:


txt=('We are adding 8 spaces here \t <-')
print (txt.expandtabs(8))


# ###  8) find- method returns an index of the first occurence only. It returns -1 if a substring is not found.

# In[117]:


print(txt.find('adding'))


# In[121]:


print(txt.find('a',4,20))


# In[122]:


print(txt.find('z'))


# ### 9) format -method formats the specified value(s) and insert them inside the string's placeholder '{ }'.

# In[128]:


Format='{this} which has to be edited'
print(Format.format(this='I have written'))


# In[129]:


txt='{name} is very {feeling} because the temperature is -{temp}'


# In[136]:


print(txt.format(name="Tom",feeling="sad",temp = 3))


# ### 10) format_map

# In[ ]:


print(txt.format_map())


# In[ ]:


(/Need, to, work, on, it)


# In[ ]:





# ### 11) index- returns the index of the first occurence of a substring in the given string. It is same as the find() method except that if a substring is not found, then it raises an exception.

# In[140]:


txt='A black bird is flying'


# In[144]:


print(txt.find('A'))


# In[145]:


print(txt.index('A'))


# In[146]:


print(txt.find('z'))


# In[147]:


print(txt.index('z'))


# ### 12) isalnum- returns True if all characters in the string are alphanumeric (either alphabets or numbers). If not, it returns False.

# In[148]:


txt='Ab123456@#$'


# In[150]:


print(txt.isalnum())


# In[151]:


txt='asGSASG123456'


# In[152]:


print(txt.isalnum())


# In[153]:


txt='       '


# In[154]:


print(txt.isalnum())


# ### 13)isalpha- method returns True if all characters in a string are alphabetic (both lowercase and uppercase) and returns False if at least one character is not an alphabet. The whitespace, numerics, and symbols are considered as non-alphabetical characters.

# In[163]:


txt="Its a wonderful day"


# In[164]:


print(txt.isalpha())


# In[165]:


txt="Iamacoder"


# In[166]:


print(txt.isalpha())


# ### 14)isascii-returns True if the string is empty or all characters in the string are ASCII.

# In[167]:


txt='A@$%^&*'


# In[168]:


print(txt.isascii())


# In[169]:


txt='123456'


# In[170]:


print(txt.isascii())


# ### 15) isdecimal- returns True if all characters in a string are decimal characters. If not, it returns False.

# In[171]:


txt='1,2,3,4,5,6'


# In[173]:


print(txt.isdecimal())


# In[176]:


txt='12345'


# In[177]:


print(txt.isdecimal())


# In[180]:


txt='1523.54'


# In[181]:


print(txt.isdecimal())


# ### 16) isdigit- returns True if all characters in a string are digits or Unicode char of a digit. If not, it returns False.

# In[182]:


txt='12345'


# In[183]:


print(txt.isdigit())


# In[184]:


txt='ABCD'


# In[185]:


print(txt.isdigit())


# ### 17) isidentifier-  checks whether a string is valid identifier string or not. It returns True if the string is a valid identifier otherwise returns False.

# ### A valid identifier string can only contain uppercase or lowercase alphabats A to Z, underscore, digits 0 to 9, and must start with an alphabats or an underscore.

# In[186]:


identi=('Abcd_0123')


# In[187]:


print(identi.isidentifier())


# In[190]:


identi=('_abcd12345')


# In[191]:


print(identi.isidentifier())


# In[192]:


identi=('$_abcd12345')


# In[193]:


print(identi.isidentifier())


# ### 18) islower- checks whether all the characters of a given string are lowercased or not. It returns True if all characters are lowercased and False even if one character is uppercase.

# In[194]:


txt=('abcdefgh')


# In[195]:


print(txt.islower())


# In[196]:


txt=('Abcdefgh')


# In[197]:


print(txt.islower())


# 
# ### 19) isnumeric- checks whether all the characters of the string are numeric characters or not. It will return True if all characters are numeric and will return False even if one character is non-numeric.

# In[199]:


txt=('123456789')


# In[200]:


print(txt.isnumeric())


# In[201]:


txt=('123456789a')


# In[202]:


print(txt.isnumeric())


# ### 20) isprintable- returns True if all the characters of the given string are Printable(alphabets, numerical values, symbols, and empty string). It returns False even if one character is Non-Printable('\n', '\t', '\r', '\x16', '\xlf', ).

# In[203]:


txt=('Hello world')


# In[204]:


print(txt.isprintable())


# In[205]:


txt=('Hello\nworld')


# In[206]:


print(txt.isprintable())


# ### 21) isspace-returns True if all the characters of the given string are whitespaces. It returns False even if one character is not whitespace.

# In[208]:


txt=('     ')


# In[210]:


print(txt.isspace())


# In[211]:


txt=('\n\t')


# In[212]:


print(txt.isspace())


# In[213]:


txt=('Hey Hi')


# In[214]:


print(txt.isspace())


# ### 22)istitle-checks whether each word's first character is upper case and the rest are in lower case or not. It returns True if a string is titlecased; otherwise, it returns False. The symbols and numbers are ignored.

# In[223]:


txt1= 'Good morning'


# In[224]:


print(txt1.istitle())


# In[225]:


txt2='Good Morning'


# In[227]:


print(txt2.istitle())


# #### 23)isupper- checks whether all the characters of a given string are uppercase or not. It returns True if all characters are uppercase and False even if one character is not in uppercase.

# In[228]:


txt='ABCDEFG'


# In[229]:


print(txt.isupper())


# In[230]:


txt='Abcdefgh'


# In[232]:


print(txt.isupper())


# ### 24) join returns a string, which is the concatenation of the string (on which it is called) with the string elements of the specified iterable as an argument.

# In[237]:


sep='+'
name=('Tom karan jack')
print(sep.join(name))


# In[238]:


sep='+'
name=('Tom karan jack')
print(name.join(sep))


# In[239]:


sep='+'
name=['Tom', 'karan', 'jack']
print(sep.join(name))


# In[241]:


sep='****'
name=('Tom', 'karan', 'jack')
print(sep.join(name))


# ###  25) ljust- returns the left justified string with the specified width. If the specified width is more than the string length, then the string's remaining part is filled with the specified fill char. The default fill char is a space. str.ljust(width, fillchar)

# In[242]:


txt=("It was an amazing movie")


# In[245]:


print(txt.ljust(30))


# In[247]:


print(txt.ljust(30,'#'))


# In[248]:


print(txt.ljust(3,'#'))


# In[252]:


print(txt.ljust(25,'#'))


# ### 26) lower- method returns the copy of the original string wherein all the characters are converted to lowercase. If no uppercase characters present, it returns the original string.

# In[1]:


txt='An Apple a Day keeps the doctor AWAY'


# In[2]:


print(txt.lower())


# In[3]:


txt='ABCDEFGHIJKL'


# In[4]:


print(txt.lower())


# ### 27)lstrip-returns a copy of the string by removing leading characters specified as an argument. By default, it removes leading whitespaces if no argument passed.

# In[6]:


txt='  It was a great day'


# In[7]:


print(txt.lstrip())


# In[11]:


txt='  It was a great day'


# In[20]:


print(txt.lstrip('It '))


# ### 28) maketrans and 29) translate- returns a mapping table that maps each character in the given string to the character in the second string at the same position. This mapping table is used with the translate() method, which will replace characters as per the mapping table. 

# In[21]:


text="Excelr"


# In[27]:


make_trans=text.maketrans('E','X')


# In[28]:


print(make_trans)


# In[31]:


trans=text.translate(make_trans)


# In[32]:


print(trans)


# In[33]:


text="Parallel universe"


# In[40]:


text_trans=text.maketrans('universe', 'esrevinu')


# In[37]:


print(text_trans)


# In[41]:


trans=print(text.translate(text_trans))


# ### 30)partition-splits the string at the first occurrence of the specified string separator sep argument and returns a tuple containing three elements, the part before the separator, the separator itself, and the part after the separator.

# In[42]:


text="That's fantastic"


# In[43]:


print(text.partition(' '))


# In[48]:


text="That's a fantastic award"


# In[51]:


print(text.partition('a'))


# In[54]:


print(text.partition(''))


# ### 31) removeprefix-Return a str with the given prefix string removed if present.

# In[55]:


print(text.removeprefix("That's"))


# In[56]:


print(text.removeprefix('T'))


# ###  32)removesuffix- Return a str with the given suffix string removed if present.

# In[57]:


print(text.removesuffix('s'))


# In[59]:


print(text.removesuffix('award'))


# In[60]:


print(text.removesuffix('d'))


# In[61]:


print(text.removesuffix('fantastic'))


# ### 33)replace-Return a copy with all occurrences of substring old replaced by new.
# 

# In[63]:


text='A very fantastic subject'


# In[68]:



print(text.replace('A',"It's a"))


# In[69]:


text='Dark night'


# In[70]:



print(text.replace('Z',"It's a"))


# In[71]:


print(text.replace('n',"It's a"))


# ### 34)rfind - Returns an integer value indicating an index of the last occurence of the specified substring.
#     

# In[78]:


text="lets find"


# In[79]:


print(text.rfind('lets'))


# In[80]:


print(text.rfind(' '))


# ### 35) rindex- is same as the rfind() that returns the index of the last occurence of a substring in the given string. However, unlike the rfind() method, it raises ValueError if the substring is not found.

# In[81]:


text="lets find INDEX"


# In[82]:


print(text.rfind('Z'))


# In[83]:


print(text.rindex('Z'))


# ### 36) rjust returns the right justified string with the specified width. If the specified width is more than the string length, then the string's remaining part is filled with the specified fill char.

# In[84]:


text='See here'


# In[86]:


print(text.rjust(15,'>'))


# In[87]:


text="I couldn't See here"


# In[89]:


print(text.rjust(25,'>'))


# ### 37)rpartition- splits the string at the last occurrence of the specified string separator sep argument and returns a tuple containing three elements, the part before the separator, the separator itself, and the part after the separator. 

# In[90]:


text='Every dog has its day'


# In[91]:


print(text.rpartition('a'))


# In[92]:


print(text.rpartition('s'))


# ### 38) split and 39) rsplit- The split() method splits the string from the specified separator and returns a list object with string elements. 

# ### The only difference between the split() and rsplit() is when the maxsplit parameter is specified. If the maxsplit parameter is specified, then the rsplit() method starts splitting a string from the right side (from the last character), whereas the split() method starts splitting from the left side (from the first character). 

# In[100]:


text=('a,b,c,d,e,@f,g,h')


# In[101]:


print(text.split('@'))


# In[102]:


print(text.rsplit('@'))


# In[103]:


text=('a,b,c,d,e,@f,@g,@h')


# In[104]:


print(text.split('@',2))


# In[105]:


print(text.rsplit('@',2))


# ### 40) strip and 41) rstrip- The strip() method returns a copy of the string by removing both the leading and the trailing characters. By default, it removes leading whitespaces if no argument passed.
# 
# 

# ### The rstrip() method returns a copy of the string by removing the trailing characters specified as argument.

# In[106]:


text='remove the ego'


# In[107]:


print(text.strip('ego'))


# In[108]:


print(text.rstrip('ego'))


# In[110]:


text='hell is hell'


# In[111]:


print(text.strip('hell'))


# In[112]:


print(text.rstrip('hell'))


# ### 42) splitlines- splits the string at line boundaries and returns a list of lines in the string. 

# In[124]:


txt='''First line
Second line
third line'''


# ### triple ''' is used to define a multi-line string.

# In[125]:


print(txt.splitlines())


# In[129]:


txt='C#\nJava\npython\nC++'


# In[130]:


print(txt)


# In[128]:


print(txt.splitlines())


# ### 43) startswith  returns True if a string starts with the specified prefix. If not, it returns False. 

# In[131]:


txt='Robert is a good man'


# In[133]:


print(txt.startswith('Robert'))


# In[134]:


print(txt.startswith('Robert',0,6))


# In[135]:


print(txt.startswith('Robert',0,7))


# In[136]:


print(txt.startswith('is',7,10))


# ### 44)swapcase- returns a copy of the string with uppercase characters converted to lowercase and vice versa.

# In[138]:


txt='DAY at BANGALORE iS SuPerb'


# In[139]:


print(txt.swapcase())


# In[140]:


txt='DATA IS THE NEW OIL'


# In[141]:


print(txt.swapcase())


# In[142]:


txt='seriously!'


# In[143]:


print(txt.swapcase())


# ###  45)title- returns a string where each word starts with an uppercase character, and the remaining characters are lowercase. If the word contains a number or a symbol, the first letter after that will be converted to upper case.

# In[144]:


txt='this is to test the title command'


# In[145]:


print(txt.title())


# In[146]:


txt='12three'


# In[148]:


print(txt.title())


# In[149]:


txt='12 Three'


# In[150]:


print(txt.title())


# ### 46)upper-  returns a string in the upper case.

# In[153]:


txt='this was lower case'


# In[154]:


print(txt.upper())


# In[155]:


txt='numbers dont affect 123'


# In[156]:


print(txt.upper())


# ###  47) zfill- returns a copy of the string with '0' characters padded to the left. It adds zeros (0) at the beginning of the string until the length of a string equals the specified width parameter.

# In[157]:


txt='lenghty'


# In[161]:


print(txt.zfill(5))


# In[162]:


print(txt.zfill(10))


# In[163]:


txt='-100'


# In[164]:


print(txt.zfill(5))


# In[165]:


print(txt.zfill(10))


# In[166]:


txt='#50'
print(txt.zfill(5))


# ### Interacting with User input

# In[115]:


user_inout= input('Enter your name: ')


# In[121]:


print('The first two letter of username is: ',user_inout[0:2])


# ### Excercise to get an input and print it 

# In[122]:


user_input= input('Enter your name: ')
print('The full name is:', user_input)


# In[ ]:




