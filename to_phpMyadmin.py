#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Import library
import pandas as pd 
from sqlalchemy import create_engine
import pyarrow.parquet as pq

# Connect to the MySQL database
my_conn=create_engine("mysql+pymysql://root:ghulam@localhost:3306/dana")

# Read Parquet Data
df = pd.read_parquet(r'D:\Dana\business.parquet', engine='pyarrow')


df["attributes"] = df["attributes"].to_json(orient='records')
df["hours"] = df["hours"].to_json(orient='records')

df.to_sql(con=my_conn,name='yelp_business',if_exists='append',index=False)

