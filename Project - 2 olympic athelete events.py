#!/usr/bin/env python
# coding: utf-8

# In[125]:


#import libraries
import pandas as pd 
import numpy as np
from matplotlib import pyplot as plt


# In[126]:


data = pd.read_csv("athlete_events.csv")
data.head()


# In[127]:


data['Medal'].value_counts()


# In[128]:


data['Medal'].isnull().sum()


# So The Null value means those who are not getting medal or Participants.
# And first we analysis with who got medal

# In[129]:


newdf = data[(data.Medal == "Gold") | (data.Medal == "Silver") | (data.Medal == "Bronze")]
newdf.sample(10)


# In[149]:


most_medal_got_country = data.Team.value_counts()[:10]
most_medal_got_country


# In[155]:


plt.barh(most_medal_got_country.index ,most_medal_got_country)
plt.show()


# So As expected United States having more no.of olympic medal and followed by france , great Britain

# In[156]:


data.Sex.value_counts()


# This represents in history how women can't participate in Olympic games .Now a days it was changed ,GOOD!
