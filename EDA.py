#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure, show
import seaborn as sns
# import scikitplot as skplt


# In[2]:


data = pd.read_csv('/Users/kirtananambiar/Documents/Netflix/netflix_titles.csv')


# In[3]:


data.head()


# In[4]:


##getting info 
data.info()
data.shape


# In[5]:


##Finds statistics for numerical columns
data.describe()


# In[6]:


##Finds unique values sum in each column
data.nunique() 


# In[7]:


#checking for missing values
data.isnull().sum()


# In[8]:


categorical =  data.columns[data.dtypes=='object']
numerical = data.columns[data.dtypes!='object']


# In[9]:


categorical = categorical.drop(['director','cast','title','date_added','description'])


# In[10]:


categorical


# In[11]:


numerical


# In[12]:


fig1, ax1 = plt.subplots()
ax1.set_title('Basic Plot')
ax1.boxplot(data['release_year'])


# In[200]:


###Netflix majority content is from the year 2018 and 75% content are post 2013
print(data['release_year'].mode())
print(data['release_year'].median())
print(data.release_year.quantile([0.25,0.5,0.75]))


# In[103]:


##Type of content vs release years
temp = data.groupby(["release_year","rating"], as_index=False).agg(
    
    count = ("rating", "count"),
    
).sort_values('count', ascending=False)
#data.groupby(["release_year","listed_in"], as_index=False)[["listed_in"]].mean()


# In[104]:


temp.nunique()


# In[107]:


###Rating vs year 
##Graph show TV-MA content is max in netflix
f, ax = plt.subplots(figsize=(10, 7))
sns.lineplot(data=temp, x='release_year', y='count', hue="rating")


# In[115]:


##Overall rating
temp4 = data.groupby('rating', as_index=False).agg(count=('rating','count')).sort_values('count', ascending=False)
sns.barplot(data=temp4, y = 'rating',x = 'count' )


# In[57]:



##Max content is of type of  movie
data['type'].value_counts()


# In[63]:


##Type vs release_year

temp1 = data.groupby(['release_year','type'], as_index=False).agg(
        count= ('type','count')).sort_values('release_year')
temp1.head()


# In[65]:


f,ax = plt.subplots(figsize=(10,7))

sns.lineplot(data=temp1, x='release_year',y='count',hue='type')


# In[80]:


##Which country produced the max content and how it grew with years
temp2 = data.groupby(['release_year','country'], as_index=False).agg(
count=('country','count')).sort_values('release_year')

f,ax = plt.subplots(figsize=(20,7))
s = sns.lineplot(data=temp2, x='release_year',y='count', hue='country')
sns.move_legend(s, "upper left", title='Country')
plt.show()


# In[95]:



###Top 20 country's producing content
plt.figure(figsize=(6, 15))

temp3 = data.groupby('country', as_index=False).agg(count=('country','count')).sort_values(by='count', ascending=False)

sns.scatterplot(data=temp3.head(20), x='count', y='country')


# In[122]:


###Top 20 genres 

temp5 = data.groupby('listed_in', as_index=False).agg(count= ('listed_in','count')).sort_values('count',ascending=False)
f,ax = plt.subplots(figsize=(10,7))
sns.barplot(data=temp5.head(20), x='count',y='listed_in')


# In[144]:


###Top 20 genres VS type

temp6 = data.groupby(['listed_in','type'], as_index=False).agg(count= ('listed_in','count')).sort_values(['count','type'],ascending=False)
f,ax = plt.subplots(figsize=(20,7))
sns.lineplot(data=temp6.head(20), x='count',y='listed_in', hue='type')



# In[156]:


###Top genre for TV show

plt.figure(figsize=(20,8))
temp7= data[data['type']=="TV Show"].groupby('listed_in',as_index=False).agg(count=('listed_in','count')).sort_values('count',ascending=False)
#t = data[data["type"]=="TV Show"]["listed_in"].value_counts()[:20]
sns.barplot(data=temp7.head(20), x='count', y='listed_in')




# In[157]:


###Top genre for movie


plt.figure(figsize=(20,8))
temp7= data[data['type']=="Movie"].groupby('listed_in',as_index=False).agg(count=('listed_in','count')).sort_values('count',ascending=False)
#t = data[data["type"]=="TV Show"]["listed_in"].value_counts()[:20]
sns.barplot(data=temp7.head(20), x='count', y='listed_in')


# In[ ]:


Inferences:
    
    
    1.Netflix majority content is from the year 2018 and 75% content are post 2013.
    2.Maximum content is of rating TV-MA in netflix.
    3.Netflix contains more movies than TV-shows and then trend shows movies to be growing with time.
    4.US, India, UK, Japan etc are the countries that produced the max content in Netflix.
    5.Documentaries, Stand-up Comedy are the most common genres in Netflix content.
    6.Most common genre for TV-shows is Kids-TV and for type Movie is Documentaries.
    

