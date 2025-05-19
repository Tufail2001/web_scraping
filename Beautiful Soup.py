#!/usr/bin/env python
# coding: utf-8

# In[33]:


from bs4 import BeautifulSoup
import requests


# In[34]:


url = "https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"


# In[35]:


page = requests.get(url)


# In[36]:


soup = BeautifulSoup(page.text, 'html')


# In[43]:


print(soup.prettify())


# In[48]:


table = soup.find_all('table')[1]


# In[49]:


table


# In[55]:


world_titles = table.find_all('th')


# In[56]:


world_table_titles = [title.text.strip() for title in world_titles]
print(world_table_titles)


# In[57]:


import pandas as pd


# In[58]:


df = pd.DataFrame(columns = world_table_titles)
df


# In[60]:


column_data = table.find_all('tr')


# In[62]:


for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    
    length = len(df)
    df.loc[length] = individual_row_data


# In[70]:


df.head()


# In[72]:


df.to_csv(r"C:\Users\HP ELITE BOOK\Desktop\midj\companies.csv", index =False)


# In[ ]:
