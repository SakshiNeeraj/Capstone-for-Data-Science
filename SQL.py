#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[11]:


ChicagoCensusData=pd.read_csv("ChicagoCensusData.csv")
ChicagoCensusData.head(2)


# In[47]:


ChicagoCrimeData=pd.read_csv("ChicagoCrimeData.csv")
ChicagoCrimeData.head(2)
ChicagoCrimeData.columns


# In[39]:


ChicagoPublicSchools=pd.read_csv("ChicagoPublicSchools.csv")
ChicagoPublicSchools.head(2)
ChicagoPublicSchools.columns


# In[9]:


get_ipython().system('pip install pandasql')
from pandasql import sqldf


# In[10]:


query = "SELECT COUNT (*) FROM ChicagoCrimeData"
result = sqldf(query, globals())
print(result)


# In[12]:


query = "SELECT Community_Area_Name FROM ChicagoCensusData WHERE Per_Capita_Income < 11000"
result = sqldf(query, globals())
print(result)


# In[23]:


query = "SELECT CASE_NUMBER FROM ChicagoCrimeData WHERE DATE > '2005-01-01'"
result = sqldf(query, globals())
print(result)


# In[31]:


query = "SELECT * FROM ChicagoCrimeData WHERE PRIMARY_TYPE='KIDNAPPING'"
result = sqldf(query, globals())
print(result)


# In[38]:


query = "SELECT PRIMARY_TYPE FROM ChicagoCrimeData WHERE LOCATION_DESCRIPTION='SCHOOL'"
result = sqldf(query, globals())
print(result)


# In[43]:


query = "SELECT AVG(SAFETY_SCORE) AS AverageSafetyScore FROM ChicagoPublicSchools"
result = sqldf(query, globals())
print(result)


# In[44]:


query = "SELECT Community_Area_Name FROM ChicagoCensusData ORDER BY PERCENT_HOUSEHOLDS_BELOW_POVERTY DESC LIMIT 5"
result = sqldf(query, globals())
print(result)


# In[46]:


query = "SELECT Community_Area_Number, COUNT(*) AS CrimeCount FROM ChicagoCrimeData GROUP BY Community_Area_Number ORDER BY CrimeCount DESC LIMIT 1"
result = sqldf(query, globals())
print(result)


# In[49]:


query = '''
    SELECT Community_Area_Name
    FROM ChicagoCensusData
    WHERE HARDSHIP_INDEX = (
        SELECT MAX(HARDSHIP_INDEX)
        FROM ChicagoCensusData
    )
'''
result = sqldf(query, globals())
print(result)


# In[52]:


query = '''
    SELECT Community_Area_Name
    FROM ChicagoCensusData NATURAL JOIN ChicagoCrimeData
    WHERE Community_Area_Number = (
        SELECT Community_Area_Number
        FROM (
            SELECT Community_Area_Number, COUNT(*) AS CrimeCount
            FROM ChicagoCrimeData
            GROUP BY Community_Area_Number
        ) AS subquery
        ORDER BY CrimeCount DESC
        LIMIT 1
    )
'''
result = sqldf(query, globals())
print(result)


# In[ ]:




