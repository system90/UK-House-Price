#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Dataset:
# https://data.london.gov.uk/dataset/uk-house-price-index


# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[3]:


house = pd.read_csv('House Price_by type.csv')
print(house.shape)   # Dimesions of the dataset


# In[4]:


# The whole dataset
house.head()


# In[5]:


# Find January data
# All the December months for years 1995 - 2019

houseJan = house[house['Month']=='Jan']
houseJan.head()


# In[6]:


houseJan.head()


# In[7]:


# Line Graph of Detached house prices against Year
plt.plot(houseJan['Year'], houseJan['Detached'], label='Detached')
plt.plot(houseJan['Year'], houseJan['Semi Detached'], label='Semi Detached')
plt.plot(houseJan['Year'], houseJan['Terraced'], label='Terraced')
plt.plot(houseJan['Year'], houseJan['Flat'], label='Flat')

plt.xlabel('Year')
plt.ylabel('Detached House Sale Price (£)')
plt.title('House Type prices against Year', fontsize=15)
plt.legend()


# In[8]:


# Create a new dataframe for all dates. So we can use it for a scatter plot


# In[9]:


# Scatter Plot of Detached house prices against Year

### make it for all dates

plt.scatter(houseJan['Year'], houseJan['Detached'], marker='x', alpha=1.0, s=5)   

plt.xlabel('Year')
plt.ylabel('Detached House Sale Price (£)')
plt.title('Detached house prices against Year')

