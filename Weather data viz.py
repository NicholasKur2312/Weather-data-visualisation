#!/usr/bin/env python
# coding: utf-8

# ## Temperature in Melbourne Comparison

# Comparing winter temperature in Melbourne over the years. <br>
# Data is obtained from the Bureau of Meteorology government website - [link](http://www.bom.gov.au/).

# In[63]:


import pandas as pd
import numpy as np

import seaborn


# In[65]:


# this url is only for the temperature reading of Olympic Park
url = "https://reg.bom.gov.au/jsp/ncc/cdio/weatherData/av?p_nccObsCode=36&p_display_type=dataFile&p_stn_num=086038"
tables = pd.read_html(url)


# The first item in tables is a monthly average temperature for 2013-2025. <br>
# The second item in tables are monthly statistics of the temperature over the years. 
# <br><br>
# We want the first table because we are comparing temperature between the years. <br>
# The second table will be more useful if we would like to compare between months or seasons.

# In[68]:


data = tables[0]


# In[70]:


#drop irrelevant rows and columns
yearly_temp = data[37:]
yearly_temp = yearly_temp.drop(53)
yearly_temp = yearly_temp.drop(54)
yearly_temp = yearly_temp.drop(61)
yearly_temp = yearly_temp.drop("Annual", axis = 1)


# In[72]:


yearly_temp_long = pd.melt(yearly_temp, id_vars = ["Year"], value_vars = list(yearly_temp.columns.values)[1:], var_name = "Month", 
                           value_name = "Temperature")


# In[74]:


# convert values in table to int
yearly_temp_long['Year'] = pd.to_numeric(yearly_temp_long['Year']).astype('Int64')
yearly_temp_long['Temperature'] = pd.to_numeric(yearly_temp_long['Temperature']).astype('Float64')


# In[76]:


#increase size of plot
seaborn.set_theme(rc={'figure.figsize':(15, 5)})

seaborn.boxplot(data = yearly_temp_long, x = "Year", y = "Temperature")


# These are the values and plots for 2003-2024. Let us compare it to the period that is available for the same area in 1940-1961.

# In[89]:


yearly_temp_old = data[0:24]


# In[91]:


yearly_temp_old


# In[93]:


yearly_temp_old = yearly_temp_old.drop(0)
yearly_temp_old = yearly_temp_old.drop(1)
yearly_temp_old = yearly_temp_old.drop("Annual", axis = 1)


# In[95]:


# exact same steps we've done for the previous set

yearly_temp_old_long = pd.melt(yearly_temp_old, id_vars = ["Year"], value_vars = list(yearly_temp_old.columns.values)[1:], var_name = "Month", 
                           value_name = "Temperature")

# convert values in table to int
yearly_temp_old_long['Year'] = pd.to_numeric(yearly_temp_old_long['Year']).astype('Int64')
yearly_temp_old_long['Temperature'] = pd.to_numeric(yearly_temp_old_long['Temperature']).astype('Float64')


# In[103]:


seaborn.set_theme(rc={'figure.figsize':(25, 5)})

seaborn.boxplot(data = yearly_temp_old_long, x = "Year", y = "Temperature")
seaborn.boxplot(data = yearly_temp_long, x = "Year", y = "Temperature")


# From the graph, the lowest and highest temperatures for 2003-2024 are higher than for 1940-1961. While there are standout years due to Melbourne's fluctuating weather, there is a pattern in terms of increasing temperature that can be observed.

# In[ ]:




