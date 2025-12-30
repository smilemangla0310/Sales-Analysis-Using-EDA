#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


df=pd.read_csv('sales_data.csv')


# In[4]:


df.head()


# In[5]:


df.describe()


# In[6]:


df.shape


# In[7]:


df.columns


# In[8]:


df.info()


# In[9]:


df.duplicated().sum()


# In[10]:


df.isnull().sum()


# In[11]:


df['Revenue']=df['Quantity']*df['Price']


# In[12]:


df['Revenue']


# In[13]:


df.reset_index(drop=True)


# In[14]:


df.groupby('Product').sum()


# In[15]:


df.sort_values(by='Revenue',ascending=False)


# In[16]:


df.groupby('Product')['Revenue'].sum().idxmax()


# In[17]:


df['Product'].value_counts().sort_values(ascending=False)


# In[18]:


df['Revenue'].sum()


# In[19]:


df.groupby('Region')['Revenue'].sum().sort_values(ascending=False)


# In[20]:


df.groupby('Product')[['Price','Quantity']].mean()


# In[21]:


df.groupby('Product')['Revenue'].mean()


# In[22]:


df.sort_values(by='Revenue',ascending=False)


# In[23]:


df.to_csv("clean_sales_report.csv",index=False)


# In[48]:


df['Revenue'].sum()


# In[ ]:




