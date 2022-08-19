#!/usr/bin/env python
# coding: utf-8

# In[ ]:


###Dealing with missing values


# In[1]:


import pandas as pd


# In[2]:


data = pd.read_csv('/Users/kirtananambiar/Documents/Netflix/listings.csv')


# In[3]:


data.head()


# In[6]:


###Get different unique data types of each column and total of it.This is to understand how many categorical
##and how many columns are numerical.

data.dtypes.value_counts()


# In[11]:


numerical_df = data.columns[data.dtypes!='object'] 
categorical_df = data.columns[data.dtypes=='object'] 


# In[14]:


data[numerical_df].isnull().sum()


# In[15]:


data[categorical_df].isnull().sum()


# In[19]:


##Percentage of missing values categorical values
data[categorical_df].isnull().sum().sort_values(ascending=False)/len(data)


# In[20]:


###Percentage of missing values numerical
data[numerical_df].isnull().sum().sort_values(ascending=False)/len(data)


# ###Methods to handle missing values
# 1. df.dropna
# 2. df.dropna(axis=1) : Drop table if any column contains missing value in a row
# 3. df.dropna(how=all): Drop if entire row is NA
# 4. df.dropna(thresh=4): Keep if entire row  has more than 4 non NA values, else drop
# 5. df.dropna(subset=['col1','col2'])
# 
# ###Fill
# Fill with constants
# 1. df.fillna(values={'col1':"Constant", 'col2':"Constant1"})
# Fill with mean, median, or mode.
# 2. df['col1'].fillna(df['col1'].mean())
# Fill with previous or next value
# 3. df['col1'].fillna(method="bfill") :fills with next value
#  

# In[ ]:


##Univariate Analysis of categorical
1. bar graphs
2. box plots for outliers

###Mutlivariate Analysis:
1. Correlation Matrix
2. Heat Maps

