#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


# In[2]:


sns.set()


# In[3]:


# Wczytaj dane HR_dirty_data.txt

filename = 'HR_dirty_data.txt'
data_location = 'dane/'
HR_dirty_data = pd.read_csv(data_location + filename, sep=';')


# In[4]:


HR_dirty_data


# In[5]:


HR_dirty_data.describe()


# In[6]:


sum(HR_dirty_data['last_evaluation'] > 1)  # 2


# In[7]:


HR_dirty_data['last_evaluation'] > 1


# In[8]:


HR_dirty_data[HR_dirty_data.last_evaluation > 1]


# In[9]:


# Usunmy te wartosci (nie cale rekordy, tylko wartosci dla tej jednej kolumny)

mask = HR_dirty_data['last_evaluation'] > 1
HR_dirty_data.loc[mask, 'last_evaluation'] = np.nan


# In[10]:


sum(HR_dirty_data['last_evaluation'] > 1)


# In[11]:


HR_dirty_data.loc[10, :]


# In[12]:


HR_dirty_data.describe()


# In[13]:


# Sprawdzmy ile jest wartosci powyzej 100

sum(HR_dirty_data['number_project'] > 10)  # 1


# In[14]:


# Usunmy tę jedna wartosc, analogicznie jak w przypadku last_evaluation

mask = HR_dirty_data['number_project'] > 100
HR_dirty_data.loc[mask, 'number_project'] = np.nan


# In[15]:


HR_dirty_data.describe()


# In[16]:


# Teraz maksymalna wartosc to 30, sprawdzmy histogram...

plt.hist(HR_dirty_data['number_project'].dropna())
plt.ylabel('Number of projects')
plt.show()


# In[17]:


# Usunmy na chwile wartosc <= 8

HR_dirty_data_tmp = HR_dirty_data.loc[HR_dirty_data['number_project'] > 8, :]
plt.hist(HR_dirty_data_tmp['number_project'].dropna())
plt.show()


# In[18]:


# ok, a wiec mamy jedna wartosc = 30, mozemy przyjac, ze zostala ona wprowadzona
# blednie, usunmy te wartosc

mask = HR_dirty_data['number_project'] == 30
HR_dirty_data.loc[mask, 'number_project'] = np.nan


# In[19]:


HR_dirty_data.describe()


# In[20]:


# Sprawdzmy rozklad zmiennej time_spend_company (widzimy maksymalna podejrzana wartosc 10)

plt.hist(HR_dirty_data['time_spend_company'].dropna())
plt.show()


# In[21]:


mask = HR_dirty_data['Work_accident'] < 0
HR_dirty_data.loc[mask, 'Work_accident'] = np.nan

mask = HR_dirty_data['left'] < 0
HR_dirty_data.loc[mask, 'left'] = np.nan

mask = HR_dirty_data['promotion_last_5years'] < 0
HR_dirty_data.loc[mask, 'promotion_last_5years'] = np.nan


# In[22]:


mask = HR_dirty_data['Work_accident'] > 1
HR_dirty_data.loc[mask, 'Work_accident'] = np.nan


# In[23]:


HR_dirty_data.describe()


# In[24]:


# Sprawdzmy teraz czy nie pominelismy jakis wartosci odstajacych przy pomocy box plot
# sprawdzamy tylko zmienne ciagle, tj. number_project, average_montly_hours, time_spend_company

plt.boxplot(HR_dirty_data['number_project'].dropna(), sym='k.')

# sym-'k.' dodany w celu zmiany oznaczenia dla wartosci odstajacych
# jezeli modul seaborn jest zaimportowany to matplotlib nie pokazuje ich uzywajac domyslnego symbolu

plt.ylabel('Number of projects')
plt.show()


# In[25]:


HR_dirty_data.describe()


# In[26]:


plt.boxplot(HR_dirty_data['average_montly_hours'].dropna(), sym='k.')
plt.ylabel('Average montly hours')
plt.show()


# In[27]:


plt.boxplot(HR_dirty_data['time_spend_company'].dropna(), sym='k.')
plt.ylabel('Time spent in the company')
plt.show()


# In[28]:


HR_dirty_data.describe()


# In[29]:


sns.boxplot(HR_dirty_data['number_project'])


# In[30]:


sns.boxplot(HR_dirty_data['average_montly_hours'])


# In[31]:


sns.boxplot(HR_dirty_data['time_spend_company'])


# In[32]:


HR_dirty_data.info()


# In[33]:


HR_dirty_data['sales'].unique()


# In[34]:


HR_dirty_data.columns


# In[35]:


# Po pierwsze usunmy wszystkie białe znaki

HR_dirty_data['sales'] = HR_dirty_data['sales'].str.replace(" ", "")


# In[36]:


HR_dirty_data.sales.value_counts()


# In[37]:


sales_map = {'hrr': 'hr', 'saless': 'sales', 'Tech': 'technical', 'tech': 'technical', 'it': 'IT'}


# In[38]:


#sales_map = {'hrr': 'hr', 'saless': 'sales', 'Tech': 'technical', 'tech': 'technical', 'it': 'IT'}

HR_dirty_data["sales"].replace(sales_map, inplace=True)
HR_dirty_data['sales'].value_counts()


# In[39]:


type(sales_map)


# In[40]:


# salary #

HR_dirty_data['salary'].unique()


# In[41]:


HR_dirty_data['salary'] = HR_dirty_data['salary'].str.replace(" ", "")
HR_dirty_data['salary'].value_counts()


# In[42]:


salary_map = {'mediu': 'medium', 'Medium': 'medium'}
HR_dirty_data['salary'].replace(salary_map, inplace=True)
HR_dirty_data['salary'].value_counts()


# In[43]:


HR_dirty_data.info()


# In[44]:


HR_dirty_data_no_nan = HR_dirty_data.dropna()
HR_dirty_data_no_nan.info()


# In[45]:


# W naszym zbiorze wariancje zmiennych nie są zbyt dużę, zastem mozemy wybrac zarowno srednia
# jak i mediane, zastapmy braki danych srednimi
# oczywiscie nic nie stoi na przeszkodzie, aby uzyc mediany
# Wczesniej jednak, braki wartosci dla zmiennych logicznych (o wartosciach 0/1)
# zastapimy czesciej wystepujaca wartoscia
# zmienne logiczne to: Work_accident, left, promotion_last_5years

columns = ['Work_accident', 'left', 'promotion_last_5years']
HR_dirty_data_no_nan2 = HR_dirty_data.copy()
HR_dirty_data_no_nan2[columns] = HR_dirty_data_no_nan2[columns].fillna(HR_dirty_data_no_nan2.mode().iloc[0])


# In[46]:


HR_dirty_data_no_nan2.describe(include='all')


# In[47]:


HR_dirty_data_no_nan2.info()


# In[48]:


HR_dirty_data_no_nan2 = HR_dirty_data_no_nan2.fillna(HR_dirty_data_no_nan2.mean().round(2))
HR_dirty_data_no_nan2.isnull().sum()


# In[49]:


# Zauwazmy, ze zmienne tekstowe wciaz maja braki danych
# w takim przypadku, jednym ze sposobow jest stworzenie nowej kategorii
# dla braku danych

HR_dirty_data_no_nan2["sales"].fillna('no_information', inplace=True)
HR_dirty_data_no_nan2["salary"].fillna('no_information', inplace=True)


# In[50]:


HR_dirty_data_no_nan2.sales.value_counts()


# In[51]:


HR_dirty_data_no_nan2.info()


# In[52]:


HR_dirty_data_no_nan2.describe()


# In[53]:


HR_dirty_data.describe()


# In[54]:


# Zapisz oczyszczone dane

HR_dirty_data_no_nan2.to_csv(data_location + 'HR_cleaned.txt', index=False, sep=';')

