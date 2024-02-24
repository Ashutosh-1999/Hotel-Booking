#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#importing libraris


# In[4]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')


# In[ ]:


#loading the dataset


# In[5]:


df=pd.read_csv('hotel_bookings 2.csv')


# In[ ]:


#Exploratory data analysis and data cleaning


# In[6]:


df.head()


# In[7]:


df.tail()


# In[8]:


df.shape


# In[9]:


df.columns


# In[10]:


df.info()


# In[11]:


df.describe(include = 'object')


# In[12]:


for col in df.describe(include = 'object').columns:
    print(col)
    print(df[col].unique())
    print('-'*50)


# In[13]:


df.isnull().sum()


# In[14]:


df.drop(['company','agent'], axis=1 , inplace=True)
df.dropna(inplace = True)


# In[24]:


df.isnull().sum()


# In[15]:


df.describe()


# In[16]:


df['adr'].plot(kind='box')


# In[17]:


df=df[df['adr']<5000]


# In[18]:


df.describe()


# In[ ]:


#Data analysis and visualizations


# In[23]:


canceled_perc = df['is_canceled'].value_counts(normalize = True)
print(canceled_perc)

plt.figure(figsize =(5,4))
plt.title('reservation status count')
plt.bar(['not canceled','canceled'],df['is_canceled'].value_counts(), edgecolor = 'k' ,width =0.7)
plt.show()


# In[32]:


plt.figure(figsize =(8,4))
ax1 = sns.countplot(x ='hotel', hue='is_canceled' , data=df, palette= 'Blues')
legend_labels,_=ax1.get_legend_handles_labels()
plt.title('reservation status in different hotels', size=20)
plt.xlabel('hotel')
plt.ylabel('number of reservations')
plt.show()


# In[34]:


resort_hotel = df[df['hotel']== 'Resort Hotel']
resort_hotel['is_canceled'].value_counts(normalize = True)


# In[35]:


city_hotel = df[df['hotel']== 'City Hotel']
city_hotel['is_canceled'].value_counts(normalize = True)


# In[37]:


resort_hotel=resort_hotel.groupby('reservation_status_date')[['adr']].mean()
city_hotel=city_hotel.groupby('reservation_status_date')[['adr']].mean()


# In[43]:


plt.figure(figsize=(20,8))
plt.title('Average daily rate in City and Resort hotel', fontsize=30)
plt.plot(resort_hotel.index, resort_hotel['adr'], label='Resort Hotel')
plt.plot(city_hotel.index, city_hotel['adr'], label='City Hotel')
plt.legend(fontsize=20)
plt.show()


# In[49]:


df['reservation_status_date']=pd.to_datetime(df['reservation_status_date'],format= 'mixed')


# In[51]:


df['month']=df['reservation_status_date'].dt.month
plt.figure(figsize =(16,8))
ax1 = sns.countplot(x='month', hue='is_canceled', data=df , palette='bright')
legend_labels,_=ax1.get_legend_handles_labels()
plt.title('reservation status per month', size=20)
plt.xlabel('month')
plt.ylabel('number of reservations')
plt.legend(['not canceled','canceled'])
plt.show()


# In[61]:


plt.figure(figsize=(15,8))
plt.title('ADR per month', fontsize=30)
plt.bar('month','adr', data = df[df['is_canceled'] == 1].groupby('month')[['adr']].sum().reset_index())
plt.xlabel('month')
plt.ylabel('adr')
plt.show()


# In[62]:


canceled_data=df[df['is_canceled']==1]
top_10_country= canceled_data['country'].value_counts()[:10]
plt.figure(figsize=(8,8))
plt.title('Top 10 countries with reservation canceled')
plt.pie(top_10_country, autopct ='%.2f', labels=top_10_country.index)
plt.show()


# In[63]:


df['market_segment'].value_counts()


# In[64]:


df['market_segment'].value_counts(normalize = True)


# In[65]:


canceled_data['market_segment'].value_counts(normalize = True)


# In[69]:


canceled_df_adr = canceled_data.groupby( 'reservation_status_date') [['adr']].mean()
canceled_df_adr.reset_index(inplace = True)
canceled_df_adr.sort_values('reservation_status_date', inplace = True)
not_canceled_data = df[df['is_canceled'] == 0]
not_canceled_df_adr = not_canceled_data.groupby( 'reservation_status_date')[['adr']].mean()
not_canceled_df_adr.reset_index(inplace = True)
not canceled_df_adr.sort_values('reservation_status_date', inplace = True)
plt.figure(figsize = (20,6))
plt.title('Average Daily Rate')
plt.plot(not_canceled_df_adr[ 'reservation_status_date'], not_canceled_df_adr['adr'], label = 'not canceled')
plt.plot(canceled_df_adr['reservation_status_date'], canceled_df_adr['adr'], label = 'canceled')
plt.legend()


# In[73]:


canceled_df_adr = canceled_df_adr[(canceled_df_adr[ 'reservation_status_date']>'2016') & (canceled_df_adr['reservation_status_date']< '2017-09')]
not_canceled_df_adr = not_canceled_df_adr[(not_canceled_df_adr[ 'reservation_status_date']>'2016') & (not_canceled_df_adr[ 'reservation_status_date']<'2017-09')]


# In[78]:


plt. figure (figsize = (20,6))
plt. title('Average Daily Rate',fontsize=30)
plt.plot (not_canceled_df_adr['reservation_status_date'], not_canceled_df_adr['adr'], label='not canceled')
plt.plot (canceled_df_adr[ 'reservation_status_date'], canceled_df_adr['adr'], label = 'canceled')
plt.legend (fontsize = 20)
plt.show()


# In[ ]:




