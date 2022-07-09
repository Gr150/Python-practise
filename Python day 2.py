#!/usr/bin/env python
# coding: utf-8

# ## Chapter 4 Functions and loops

# ### Types of functions
# * Anonymous
# 
# * userdefined
# 
# * Builtin

# ### User defined function 

# ### define function- Positional argument

# In[5]:


def add_2(a,b): #argument
    return a+b  #function terminaton


# In[6]:


add_2(5,6)


# ### Default parameter

# In[7]:


def team_details(Id, name, gender, company='Excelr' ):
    print('****************Team A*******************')
    print('ID is:', Id)
    print('name is:', name)
    print('gender is:', gender)
    print('company is:', company)
    return


# In[8]:


team_details(0o1, 'GR', 'M', 'IBM')


# In[9]:


team_details(0o2, 'GR', 'M')


# ### Variable length argument

# In[10]:


def team_details(Id, name, gender, *company ):
    print('****************Team A*******************')
    print('ID is:', Id)
    print('name is:', name)
    print('gender is:', gender)
    print('company is:', company)
    return


# In[11]:


team_details(0o1, 'GR', 'M', 'IBM', 'ABC', 'DEF')


# ### Variable length and keyword argument

# In[12]:


def team_details(Id, gender,*name, **company ):
    print('****************Team A*******************')
    print('ID is:', Id)
    print('name is:', name)
    print('gender is:', gender)
    print('company is:', company)
    return


# In[13]:


team_details(0o1, 'M','GR', 'MR','MA', 'M', company1= 'IBM', company2='ABC', company3='DEF')


# ## Loops

# In[14]:


for i in range(1,5):
    print(i)


# In[15]:


for i in range(1,15,3):
    print(i)


# ### Function within for loop 

# In[16]:


def for_test(a,b):
    for i in range(a,b,2):
        print("The numbers are", i)
        


# In[17]:


for_test(1, 10)


# ## Conditional logic

# ## 1) compare value

# In[18]:


5==5


# In[19]:


5!=5


# In[20]:


5>6


# In[21]:


6>5


# ## Logical operators
# 
# * And operator 
# * OR operator
# * Not operator
# * IN operator

# In[30]:


x=int(input('enter the value of x:'))


# In[31]:


x<6 and x>2


# In[32]:


x<6 or x>2


# In[33]:


not(x<6 and x>2)


# In[25]:


data='ghfhshash'
x='a'

x in data


# In[26]:


x='z'
x in data


# In[ ]:





# ### Challenge to find factors of a number
# 1) Get an input from user
# 2) if user_input= 10, factor numbers are 1, 2,5, 10

# In[34]:


num= int(input("Enter the number:"))


# In[35]:


num= int(input("Enter the number:"))
for i in range (1,num+1):
    if num % i == 0:
        print(i)
    
        


# ###  Break out of problem

# In[29]:


for i in range (0,20):
    print(i)
    if i==15:
        break
        print('It has been stopped')##anything after break wont be printed 


# In[38]:


for i in range (0,20):
    print(i)
    if i==15:
         print('It has been stopped')## anything before break will definitely print
         break
       


# # Assignment - 2
# 
# Submit 2 examples for each module.
# 
# . while loop
# 
# . for loop
# 
# . if else
# 
# _ if elif else
# 
# . user defined functions without for loop, if loop
# . user defined functions with for loop
# 
# . user defined functions with for loop and if loop
# . break
# 
# . continue
# 
# . for loop with in operator
# 
# . for loop with if statement
# 
# . for loop with not in operator
# 
# . if with in operator
# 
# . if with not in operator
# 

# ## while loop- can execute a set of statements as long as a condition is true.

# In[31]:


i=5
while i<20:
    print(i)
    i=i+1
    


# In[55]:


y=int(input('Enter a number'))
while y<15:
    print(y)
    y=y+1


# In[33]:


i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)


# In[34]:


i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")


# ## For loop 

# In[35]:


Name=['Dan, Mark,Jim']


# In[36]:


for i in Name:
    print(i)


# In[37]:


Name=('Dan, Mark,Jim')
for i in Name:
    print(i)


# ## if else

# In[38]:


x='Code'
y=input('Please enter Code:')

if x == y:
    print('Code matches')
else:
        print('Code mismatch')


# In[39]:


x=['World','Planet', 'Star']
if x[0]== 'World':
    print('True')
else:
    print('Incorrect')


# ## If elsif else

# In[40]:


Names=['Apple','Ant','Orange']
if Names[0]=='apple':
    print(Names[0])
elif Names[1]=='fruit':
    print(Names[1])
else:
    print(Names[2])


# In[41]:


a = 33
b = 44
c = 55 
if b > a and b>c:
  print("b is greater than a but lesser than c")
elif a == b and b < c:
  print("a and b are equal")
else :
  print("All a, b and c are Unequal")


# ## User defined functions with if loop
# 

# In[42]:


def my_function():
   i in range (1,10)
   print(i)
   

    


# In[43]:


i=10
if i>8:
    my_function()


# In[44]:


def txt(x):
    if x>5:
        result=x+1
        print(result)
    else:
        result=x
    return result
   
        


# In[45]:


txt(6)


# In[46]:


def txt(x):
    k=5
    result=k+txt(x-1)
    return result


# In[ ]:


txt(5)


# ## ## User defined functions with for loop
# 

# In[84]:


def looping():
    for i in range (0,10):
        print(i)


# In[85]:


looping()


# ## user defined functions with for loop and if loop

# In[88]:


for i in range (1,20):
    if i==5:
        my_func()


# In[86]:


def my_func():
    print("My function was called")


# ## Break 

# In[4]:


for i in range(15):
    if i>10:
        break
    print(i)


# In[7]:


i=1
while i<10:
    print(i)
    if i==7:
        break
    i+=1


# ## Continue - this will end the current iteration in a for loop (or a while loop), and continues to the next iteration.

# In[10]:


for i in range(10):
    if i==5:
        continue
    print(i)


# In[39]:


i=1
for i in range(100):
    while i==50:
        continue
    print(i)


# ## for loop with in operator

# In[19]:


for x in "India":
    print(x)


# In[20]:


names=["AB","BC","CD","EF"]
for i in names:
    print(i)


# ## for loop with if statement- Break the loop if the name has any vowel

# In[43]:


Name=input(print('Enter the name:'))
for i in Name:
    if (i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
        break
    print(i)


# ##  for loop with not in operator

# In[51]:


plant=['Tree','Air','Shelter','Human']
harmful='Human'

for x  in harmful:
    if harmful not in plant:
        print(plant)
else: print(harmful)


# In[54]:


y=[1,2,55,66,77]
x=[66,7,8,9]

for x in y:
    if x not in y:
        print('Values doesnt match')
else: print('Values match')


# ##  if with in operator

# In[59]:


y=('Spring')


# In[60]:


Climate=['Spring','Rainy','Summer','Winter']


# In[62]:


if y in Climate:
    print('Expected Weather')
else: print('Unexpected Weather')    


# In[82]:


y=(2)
number=(1,2,3,4,5)

if y in number:
    print('Numbers found')
else: print('numbers not found')


# ##  if with not in operator

# In[83]:


y=('Summer')
Climate=['Spring','Rainy','Summer','Winter']
if y not in Climate:
    print('Unexpected Weather')
else: print('expected Weather')  


# In[ ]:


num=()


# In[ ]:





# In[ ]:





# In[ ]:




