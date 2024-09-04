#!/usr/bin/env python
# coding: utf-8

# What are (is?) data?
# Code: Representing types of data on computers

# In[ ]:


## create variables of different types (classes)

# data numerical (here as a list)
numdata = [ 1, 7, 17, 1717 ]

# character / string
chardata = 'xyz'

# double-quotes also fine
strdata = "x"

# boolean (aka logical)
logitdata = True # notice capitalization!

# a list can be used like a MATLAB cell
listdata = [ [3, 4, 34] , 'hello' , 4 ]

# dict (kindof similar to MATLAB structure)
dictdata = dict()
dictdata['name'] = 'Mike'
dictdata['age'] = 25
dictdata['occupation'] = 'Nerdoscientist'


# In[ ]:


# let's see what the workspace looks like
get_ipython().run_line_magic('whos', '')


# In[ ]:


# clear the Python workspace
get_ipython().run_line_magic('reset', '-sf')


# In[ ]:




