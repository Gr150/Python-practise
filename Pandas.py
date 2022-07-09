#!/usr/bin/env python
# coding: utf-8

# ## Getting and knwoing about the data 

# In[4]:


import pandas as pd


# In[5]:


data= pd.read_csv('uber-raw-data.csv')


# In[ ]:





# In[6]:


data= pd.read_csv('restaurants.csv')


# In[7]:


data


# In[8]:


data.shape # attribute


# In[9]:


data.info() #function


# In[10]:


data.describe()


# In[11]:


data.describe(include='all')


# In[12]:


data.isna()


# In[13]:


data.isna().sum()


# ## << DATA Understanding>>

# ### *Perform initial analysis  
# ### * Pull out insights

# ## Perform initial analysis  
# 
# * Rows= Observations/Datapoints
# * Columns= Feature/Parameters

# In[14]:


data['name'].nunique()


# In[15]:


data['position'].nunique()


# In[16]:


print(data['category'].unique())


# In[17]:


print(data['name'].unique())


# In[18]:


data['category'].nunique()


# In[19]:


data['zip_code'].nunique()


# ##  Top 5 category of restaurants has the highest ratings

# In[20]:


data.groupby(by='category')['ratings'].sum().sort_values(ascending=False).head(5)


# ###  Getting and knowing your data

# In[21]:


data1= pd.read_csv('u.user',sep= '|')


# In[22]:


data1


# In[23]:


data1.shape


# In[24]:


data1.info()


# In[25]:


data1.nunique()


# In[26]:


data1.isna().sum()


# In[27]:


data1.describe(include='all')


# In[28]:


data1.groupby(by=['gender','occupation'])['user_id'].count().sort_values(ascending= False)


# In[29]:


pd.pivot_table(data= data1,
    values='user_id',
    index='gender',
    columns='occupation',
    aggfunc = 'count')


# ## Filtering and Sorting 

# In[30]:


euro_data=pd.read_csv('Euro_2012_stats_TEAM.csv')


# In[31]:


euro_data


# In[32]:


euro_data.info()


# In[33]:


euro_data.shape


# In[34]:


euro_data.isna().sum()


# In[35]:


pd.set_option()


# ##  Get team names with yellow card and red card in descending order

# In[36]:


team_yellow= euro_data[['Team','Yellow Cards','Red Cards']]


# In[37]:


import warnings
warnings.filterwarnings(action='ignore')


# In[38]:


team_yellow.sort_values(by='Red Cards',
    axis= 0,
    ascending=False,
    inplace= True)


# In[39]:


team_yellow


# ## Filter the team with red cards

# In[40]:


Team_red=team_yellow[team_yellow['Red Cards']==1]


# In[41]:


Team_red


# In[ ]:





# In[ ]:





# ## Get teams with 1 red card and 4 yellow card 

# In[42]:


team_yellow['Red Cards']==1


# In[43]:


team_yellow['Yellow Cards']==4


# In[44]:


team_yellow[(team_yellow['Red Cards']==1) | (team_yellow['Yellow Cards']==4)]


# # Indexing and Slicing

# In[45]:


# index locator

# using iLoc and loc


# In[46]:


team_yellow


# In[47]:


euro_data.iloc[0:5,0:5] #using indexing method


# In[48]:


euro_data.iloc[8:,10:12]


# In[49]:


euro_data.loc[:10,"Shots on target":"Shooting Accuracy"] # mention the column names using loc


# In[50]:


euro_data


# ## Filter teams, penalty goal and passes 

# In[51]:


euro_data.loc[:10,['Team','Penalty goals','Passes']]


# ## Selecting the features of 0,2,4,5,10

# In[52]:


euro_data.loc[[0,2,4,5,10],['Team','Penalty goals','Passes']]


# ## Deleting a column using del (single column) or drop (multiple colum) 

# In[53]:


euro_data


#  ##  Delete column Shots off target

# In[54]:


del euro_data['Shots off target']


# In[55]:


euro_data


# ## Delete columns  , Hit Woodwork, Penalties not scored, Headed goals

# In[56]:


euro_data.drop(labels=['Hit Woodwork','Penalties not scored','Headed goals'],
    axis= 1,
    index=None,
    columns=None,)


# ## Creating series and dataframes 
# 
# ### Pandas have two dataframes
# 1D Series 
# 2D Dataframe

# In[57]:


t=[1,2,3,4,5]


# In[58]:


type(t)


# In[59]:


x=pd.Series(t)


# In[60]:


type(x)


# In[61]:


Student={'Name':['GR','SJ','AJ'],'Age':[5,10,9]}


# In[62]:


Student


# In[63]:


details=pd.DataFrame(Student)


# In[64]:


details


# In[65]:


Student1={'Name':['GR','SJ','AJ'],'Age':[50,100,15]}


# In[66]:


details=pd.DataFrame(Student1)


# In[67]:


details


# ## Apply function

# In[68]:


student=pd.read_csv('student-mat.csv')


# In[69]:


student


# In[70]:


student.info()


# In[71]:


student.isna().sum()


# In[72]:


type(student)


# ## Excercise using Lamba function- adding all the elements  in Medu,	Fedu with 2

# In[73]:


student['Medu']=student['Medu'].apply(lambda x:x+2)
student['Fedu']=student['Fedu'].apply(lambda x:x+2)


# ###  Task= Create a new column 'Eligibility' and the value will be 0 if age<17 and 1 when age>17 

# In[74]:


def new_colum(x):
    if x>17:
        return 1
    else: return 0    


# In[75]:


student['Eligibility']=student['age'].apply(new_colum) ## passing user defined function


# In[76]:


student


# In[77]:


student['Eligibility lambda']=student['age'].apply(lambda x: 1 if x>17 else 0)


# In[78]:


student


# # Merge (concat) 

# In[89]:


sales_2017=pd.read_csv('Sales Transactions-2017.csv')
sales_2017.head()


# In[93]:


sales_2017['Party'].unique()


# In[80]:


sales_2018=pd.read_csv('Sales Transactions-2018.csv')
sales_2018.head()


# In[81]:


sales_2019=pd.read_csv('Sales Transactions-2019.csv')
sales_2019.head()


# In[82]:


sales_total= pd.concat([sales_2017,sales_2018,sales_2019])


# In[83]:


sales_total.head(10)


# ### Explore- left, right, outer and inner join

# # Left Join-   returns a dataframe containing all the rows of the left dataframe.

# In[116]:


left_joined= pd.merge(sales_2018,sales_2019,on='Voucher',how='left')`


# In[117]:


left_joined


# ## Right Outer Join, is similar to the Left Outer Join. The only difference is that all the rows of the right dataframe are taken as it is and only those of the left dataframe that are common in both.

# In[120]:


Right_joined= pd.merge(sales_2018,sales_2019,on='Voucher',how='right')


# In[121]:


Right_joined


# In[ ]:





# # Outer Join- returns all those records which either have a match in the left or right dataframe. 

# # When rows in both the dataframes do not match, the resulting dataframe will have NaN for every column of the dataframe that lacks a matching row.  

#  ## We can perform Full join by just passing the how argument as ‘outer’ to the merge() function:

# In[100]:


Outer_joined= pd.merge(sales_2018,sales_2019,on='Voucher',how='outer', indicator=True)


# In[ ]:





# In[109]:


Outer_joined


# In[ ]:





# ## Inner Join- returns a dataframe with only those rows that have common characteristics. 

# ##  The merge() function in Pandas is our friend here. By default, the merge function performs an inner join. 

# ##   performed inner join on the product and Party dataframes on the ‘Voucher’ column.

# In[111]:


inner_joined= pd.merge(sales_2018,sales_2019,on='Voucher')


# In[112]:


inner_joined


# ###  Lets find out same product sold between 2018 and 2019

# In[115]:


pd.merge(sales_2018,sales_2019, how='inner',left_on=['Product'], right_on=['Product'], indicator=True)


# In[ ]:





# ### Another excercise to clean the data sales_total and it should look like below sales_clean

# In[48]:


sales_clean= pd.read_csv('Sales-Transactions-Edited.csv')


# In[50]:


sales_clean.head(40)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ## Grouping VS pivotable VS crosstab

# In[52]:


insurance=pd.read_csv('insurance.csv')


# In[53]:


insurance


# ## Find out region wise average insurance charges

# In[60]:


insurance.groupby(by=['region'])['charges'].mean().sort_values(ascending=False)


# ## Find out smoker with region wise  average insurance charges

# In[61]:


insurance.groupby(by=['region','smoker'])['charges'].mean().sort_values(ascending=False)


# In[74]:


pd.pivot_table(data=insurance,
 values=['charges'],
    index=['region'],
    columns=['smoker'],
    aggfunc='mean')


# In[78]:


pd.crosstab(index=insurance['smoker'],
    columns=insurance['region'],margins=True)  ####computes a frequency table of the factors


# In[ ]:




