#!/usr/bin/env python
# coding: utf-8

# # Import and Export Files
#
# # Challenge 1 - Working with CSV and Other Separated Files
#
# Import the pandas library
#
# csv files are more commonly used as dataframes. In the cell below, load the file from the URL provided using the `read_csv()` function in pandas. Starting version 0.19 of pandas, you can load a csv file into a dataframe directly from a URL without having to load the file first like we did with the JSON URL. The dataset we will be using contains informtaions about NASA shuttles.
#
# In the cell below, we define the column names and the URL of the data. Following this cell, read the tst file to a variable called `shuttle`. Since the file does not contain the column names, you must add them yourself using the column names declared in `cols` using the `names` argument. Additionally, a tst file is space separated, make sure you pass ` sep=' '` to the function.

# In[1]:


#Your pandas import here:

import pandas as pd


# In[2]:


# Run this code:

cols = ['time', 'rad_flow', 'fpv_close', 'fpv_open', 'high', 'bypass', 'bpv_close', 'bpv_open', 'class']
tst_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/statlog/shuttle/shuttle.tst'


# In[3]:


# Your code here:
##pandas.read_csv(filepath_or_buffer: Union[str, pathlib.Path, IO[~AnyStr]], sep=',', delimiter=None, header='infer', names=None, index_col=None, usecols=None, squeeze=False, prefix=None, mangle_dupe_cols=True, dtype=None, engine=None, converters=None, true_values=None, false_values=None, skipinitialspace=False, skiprows=None, skipfooter=0, nrows=None, na_values=None, keep_default_na=True, na_filter=True, verbose=False, skip_blank_lines=True, parse_dates=False, infer_datetime_format=False, keep_date_col=False, date_parser=None, dayfirst=False, cache_dates=True, iterator=False, chunksize=None, compression='infer', thousands=None, decimal=b'.', lineterminator=None, quotechar='"', quoting=0, doublequote=True, escapechar=None, comment=None, encoding=None, dialect=None, error_bad_lines=True, warn_bad_lines=True, delim_whitespace=False, low_memory=True, memory_map=False, float_precision=None)[source]

shuttle = pd.read_csv(tst_url, names = cols, sep = ' ')
shuttle


# Let's verify that this worked by looking at the `head()` function.

# In[4]:


# Your code here:
shuttle.head(10)


# To make life easier for us, let's turn this dataframe into a comma separated file by saving it using the `to_csv()` function. Save `shuttle` into the file `shuttle.csv` and ensure the file is comma separated and that we are not saving the index column.

# In[5]:


# Your code here:
## DataFrame.to_csv(self, path_or_buf=None, sep=', ', na_rep='', float_format=None, columns=None, header=True, index=True, index_label=None, mode='w', encoding=None, compression='infer', quoting=None, quotechar='"', line_terminator=None, chunksize=None, date_format=None, doublequote=True, escapechar=None, decimal='.')
shuttle.to_csv('shuttle.csv', sep=',', index=False)


# # Challenge 2 - Working with Excel Files
#
# We can also use pandas to convert excel spreadsheets to dataframes. Let's use the `read_excel()` function. In this case, `astronauts.xls` is in the same folder that contains this notebook. Read this file into a variable called `astronaut`.
#
# Note: Make sure to install the `xlrd` library if it is not yet installed.

# In[6]:


# Your code here:



astronaut = pd.read_excel("astronauts.xls")


# Use the `head()` function to inspect the dataframe.

# In[ ]:


# Your code here:


# Use the `value_counts()` function to find the most popular undergraduate major among all astronauts.

# In[ ]:


# Your code here:


# Due to all the commas present in the cells of this file, let's save it as a tab separated csv file. In the cell below, save `astronaut` as a tab separated file using the `to_csv` function. Call the file `astronaut.csv` and remember to remove the index column.

# In[ ]:


# Your code here:


# # Bonus Challenge - Fertility Dataset
#
# Visit the following [URL](https://archive.ics.uci.edu/ml/datasets/Fertility) and retrieve the dataset as well as the column headers. Determine the correct separator and read the file into a variable called `fertility`. Examine the dataframe using the `head()` function.

# In[ ]:


# Your code here:

