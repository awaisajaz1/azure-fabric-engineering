#!/usr/bin/env python
# coding: utf-8

# ## delta-streams
# 
# New notebook

# In[ ]:


# We shall check the offsets and reservoir version to actually see how new data from source table injected everytime into streaming objects for exactly once process


# ## **Create a small table**

# In[2]:


# The command is not a standard IPython magic command. It is designed for use within Fabric notebooks only.
# %%sql
# create table earthquakes_lakehouse.delta_source
# (
#     ID int,
#     NAME string
# )
# USING DELTA
# LOCATION 'Files/delta_source/src1'


# In[23]:


# The command is not a standard IPython magic command. It is designed for use within Fabric notebooks only.
# %%sql
# insert into earthquakes_lakehouse.delta_source 
# values 
# (1, 'Owais'),
# (2, 'Waqas'),
# (3, 'Asif'),
# (4, 'Kashif')


# In[5]:


# The command is not a standard IPython magic command. It is designed for use within Fabric notebooks only.
# %%sql
# SELECT * from earthquakes_lakehouse.delta_source 


# In[6]:


streaming_df = spark.readStream.table("earthquakes_lakehouse.delta_source ")


# In[18]:


# streaming_df.writeStream.format("delta")\
# .option("checkpointLocation", "Files/delta_source/chkpoint1")\
# .option("path", "Files/delta_source/trgt1")\
# .trigger(processingTime = "3 Seconds")\
# .start()

streaming_df.writeStream.format("delta")\
.option("checkpointLocation", "Tables/chkpoint1")\
.option("path", "Tables/trgt1")\
.trigger(processingTime="3 seconds")\
.start()


# In[25]:


df = spark.read.option("multiline", "true").json("Files/delta_source/trgt1/_delta_log/00000000000000000001.json")
# df now is a Spark DataFrame containing JSON data from "Files/delta_source/trgt1/_delta_log/00000000000000000001.json".
display(df)


# In[7]:


# The command is not a standard IPython magic command. It is designed for use within Fabric notebooks only.
# %%sql
# describe history earthquakes_lakehouse.delta_source 


# In[24]:


# The command is not a standard IPython magic command. It is designed for use within Fabric notebooks only.
# %%sql
# SELECT * from trgt1


# In[22]:


from delta.tables import DeltaTable

delta_table = DeltaTable.forPath(spark, "Tables/trgt1")
history_df = delta_table.history()  # Fetch version history
history_df.show(truncate=False)

