#!/usr/bin/env python
# coding: utf-8

# # Data structure
# 
# * List
# 
# * Set
# 
# * Tuple
# 
# * Dictionary
# 
# Task for the day is to explore all the funcions of list, set, tuple, dictionary

# ## List
# 
# * 1D
# * Heterogenous
# * Allows duplicates
# * Mutable
# * Indexible

# In[1]:


list_=[]


# In[2]:


type(list_)


# In[3]:


shop=[1,2,3,'Apple','Banana', 4, '%']


# In[6]:


shop[4]


# ## Set
# * Faster compared to list
# * Mutable
# * {} is used to set value
# * doesn't allow duplicate
# * Not indexable
# * heterogeneous

# In[7]:


cart= set()


# In[10]:


cart={1,2,3,4,5,6,1,2,'A','B','A'}


# In[11]:


cart


# In[12]:


type(cart)


# In[13]:


cart[1]


# In[14]:


cart.add('Z')


# In[15]:


cart


# In[16]:


cart.add(0)


# In[17]:


cart


# ### Tuple 
# * default data type for a variable is tuple
# * 1D
# * Immutable
# * Indexable 
# * heterogeneous
# * Allows duplicate

# In[22]:


cart='string','a', 'b', 1


# In[23]:


type(cart)


# In[21]:


cart[1]


# ### Dictionary 
# * 2D
# * heterogeneous
# * Mutable
# * Duplicate keys are not allowed but values are 
# * slicing not possible

# In[24]:


cart={}


# In[25]:


type(cart)


# In[28]:


cart={'data':1,'Info':2, 'K':'R'}


# In[29]:


cart.values()


# ## Explore all the functions of list, set, tuple, dictionary

# ##  List - append, clear, copy, count, extend, index, insert, pop, remove, reverse, sort

# ### -> Append

# In[2]:


txt=['A','B','C','D']


# In[3]:


txt.append('Me')


# In[4]:


txt


# ## ->Clear 

# In[5]:


txt.clear()


# In[6]:


txt


# In[ ]:





# ### copy

# In[7]:


txt=['A','B','C','D']


# In[8]:


number= txt.copy()


# In[9]:


number


# In[10]:





# ### ->Extend

# In[11]:


txt.extend(number) #//adds all the elements of an iterable (list, tuple, string etc.) to the end of the list#


# In[12]:


txt


# In[13]:


number=(5,6,8)


# In[14]:


txt.extend(number)


# In[15]:


txt


# ### ->Index :  returns the position at the first occurrence of the specified value.

# In[26]:


name=['abhi','bhav','chiru']


# In[28]:


name.index('bhav')


# In[31]:


num=['abhi',1,'bhav',2,'chiru',5,7,7,8]


# In[32]:


num.index(7)


# ## Copy

# In[20]:


name=['a','A','A','a','b','B','b']


# In[23]:


name.count('a')


# In[24]:


num=[1,5,1,4,3,4,3,5,1]


# In[25]:


num.count(1)


# ###  Insert- inserts the specified value at the specified position.

# In[42]:


txt=[1,2,3,4,5]


# In[43]:


txt.insert(4,'Inserted here')


# In[44]:


txt


# In[57]:


name=['A','B','V']


# In[58]:


name.insert(5,'Z') # there are empty values in index 3 &4, it automatically adds the value to index 3


# In[59]:


name


# In[60]:


name.index('Z')


# ### Pop - removes the element at the specified position.

# In[61]:


txt=['A',1,3,34,'B']


# In[62]:


txt.pop(2)


# In[63]:


txt


# In[64]:


num=[1,2,3,4,2,5,6,3]


# In[65]:


num.pop(5)


# In[66]:


num


# ###  remove- removes the first occurrence of the element with the specified value whereas pop removes the values pointed in the index

# In[67]:


txt=[1,3,5,7,9]


# In[69]:


txt.remove(5)


# In[70]:


txt


# In[71]:


name=['A','AB','ABC','ABCDE']


# In[72]:


name.remove('ABC')


# In[73]:


name


#  ###  reverse- reverses the sorting order of the elements.

# In[74]:


txt=['A',1,3,34,'B']


# In[75]:


txt.reverse()


# In[76]:


txt


# In[77]:


num=[1,2,3,4,7,9]


# In[80]:


num.reverse()


# In[81]:


num


# ### sort- sorts the list ascending by default.

# In[89]:


txt=[3,2,1]


# In[90]:


txt.sort()


# In[91]:


txt


# In[92]:


txt=['ABB','ACC','BAA']


# In[93]:


txt.sort(reverse=True)


# In[94]:


txt


# ## SET - 
# 
# add
# clear
# copy
# difference
# difference_update
# discard
# intersection
# intersection_update
# isdisjoint
# issubset
# issuperset
# pop
# remove
# symetric_difference
# symetric_difference_update
# union
# update

# In[1]:


data= set()


# In[2]:


data=('Info','num','txt','alphanum')


# In[3]:


type(data)


# In[4]:


data={'Info','num','txt','alphanum'}


# In[5]:


type(data)


# # Function-1 Add - Adds an element to the set

# In[7]:


data={'Info','num','txt','alphanum'}
data.add('Hexa')
print(data)


# In[9]:


num={1,2,3,4,5,6}
num.add('numbers')
print(num)


# ##  2) Clear-Removes all the elements from the set

# In[10]:


fruits = {"apple", "banana", "cherry"}

fruits.clear()

print(fruits)


# ### 3) Copy- Returns a copy of the set

# In[20]:


fruits = {"apple", "banana", "cherry"}


# In[21]:


x=fruits


# In[22]:


fruits={"apple", "banana", "cherry","orange"}


# In[23]:


x


# In[24]:


print(x)


# In[30]:


x=fruits.copy()


# In[31]:


x


# In[32]:


fruits={"apple", "banana", "cherry","orange","Kiwi"}


# In[33]:


print(x)


# ### 4) difference:Returns a set containing the difference between two or more sets & difference_update:Removes the items in this set that are also included in another, specified set

# In[34]:


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.difference(y)

print(z)


# In[38]:


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.difference_update(y)
print(z)


# In[39]:


print (x,y)


# ##  difference() method returns a new set, without the unwanted items, and the difference_update() method removes the unwanted items from the original set but doesn't return anything

# ### 5) discard- Remove the specified item

# In[40]:


fruits = {"apple", "banana", "cherry"}

fruits.discard("banana")

print(fruits)


# In[41]:


num={1,2,3,4,5}

num.discard(5)

print(num)


# ### 6) intersection : Returns a set, that is the intersection of two or more sets and intersection_update: Removes the items in this set that are not present in other, specified set(s)

# In[42]:


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)


# In[43]:


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z= x.intersection_update(y)

print(z)

print(y)

print(x)


# In[ ]:





# ### 7)isdisjoint-  method returns True if none of the items are present in both sets, otherwise it returns False.

# In[45]:


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.isdisjoint(y)

z


# In[46]:


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft"}
z = x.isdisjoint(y)
z


# ### 8)  issubset- Return True if all items in set x are present in set y

# In[47]:


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft","apple", "banana", "cherry"}
z = x.issubset(y)
z


# In[48]:


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft","apple", "banana"}
z = x.issubset(y)
z


# ###  It returns false even when one item is missing

# ###  9)issuperset- returns True if all items in set y are present in set x:

# In[49]:



x = {"google", "microsoft","apple", "banana"}
y = {"apple", "banana", "cherry"}
z = x.issuperset(y)
z


# In[50]:


x = {"google", "microsoft","apple", "banana", "cherry"}
y = {"apple", "banana", "cherry"}
z = x.issuperset(y)
z


# ###  10) pop-Removes an element from the set and remove- Removes the specified element

# In[51]:


x = {"google", "microsoft","apple", "banana", "cherry"}
z=x.pop()
z


# In[52]:


z=x.pop()
z


# ### Pop will randomly remove the element 

# In[58]:


x = {"google", "microsoft","apple", "banana", "cherry"}
x.remove("google")
print(x)


# In[60]:


x.discard("microsoft")
print(x)


# ###  Remove and discard will do the same but remove will throw an error if it cant find that element

# In[61]:


x.discard("google")


# In[62]:


x.remove("google")


# ##  11) symetric_difference- Returns a set with the symmetric differences of two sets and symetric_difference_update- inserts the symmetric differences from this set and another

# In[63]:


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)


# In[64]:


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)


# ###  12) union- Return a set containing the union of sets

# In[66]:


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
t = {"GLove", "Mango", "ant"}

z = x.union(y,t)

print(z)


# In[ ]:





# ### 13) Update - Update the set with another set, or any other iterable

# In[67]:


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.update(y)

print(x)


# # Tuple-  count , index method

# In[68]:


data= ('apple','banana',1,1)


# In[69]:


type(data)


# ## Count-  Returns the number of times a specified value occurs in a tuple

# In[70]:


data=(1,1,2,2,2,2,2,2,3,3,3,3,3,4,4,4,5)
data.count(2)


# In[72]:


data=("apple", "banana", "cherry","apple", "banana", "cherry","apple", "banana", "cherry")
data.count("apple")


# ###  Index- Searches the tuple for a specified value and returns the position of where it was found

# In[76]:


data.index("cherry")


# In[77]:


data.index(5)


# ###  method raises an exception if the value is not found.

# ## Dictionary-  clear, copy, fromkeys, get , items, keys, pop, popitem, setdefault, update, values

# In[80]:


Emp={'Name':['Gov','AJ','Jack'],'Id':[101,102,203],'age':[18,22,18]}


# In[81]:


type(Emp)


# ### 1) Clear- Remove all elements from the car list:

# In[85]:


car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(car)

car.clear()

print("After executing clear statement:",car)


# In[ ]:





# ###  2)Copy- Returns a copy of the dictionary

# In[86]:


car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.copy()

print(x)


# In[ ]:





# ###  3)Keys- Returns a list containing the dictionary's keys and fromkeys- Returns a dictionary with the specified keys and value

# In[88]:


car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["color"] = "white"

x = car.keys()

print(x)


# In[91]:


my_dict={}
y={'key1','key2','key3'}
x={0,2,3}

my_dict=dict.fromkeys(y,x)

print(my_dict)


# ### 4)get- Returns the value of the specified key

# In[92]:


car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.get("model")

print(x)


# ###  5)items- Returns a list containing a tuple for each key value pair

# In[93]:


car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.items()

print(x)


# ### 6) POP - Removes the element with the specified key and POPitem- Removes the last inserted key-value pair

# In[94]:


car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car)
car.pop("model")

print(car)


# In[95]:


car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car)
car.popitem()

print(car)


# ###  7) Setdefault- returns the value of the item with the specified key. If the key does not exist, insert the key, with the specified value, see example below

# In[100]:


car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("model1", "Bronco")

print(x)


# ###  8) update- updates the dictionary with the specified key-value pairs

# In[106]:


car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.update({"color": "White"})

print(car)


# ### 9)values- Returns a list of all the values in the dictionary

# In[107]:


car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.values()


# In[ ]:




