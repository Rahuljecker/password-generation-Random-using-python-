#!/usr/bin/env python
# coding: utf-8

# In[31]:


import string as s
from random  import *


ch=s.ascii_letters+s.punctuation+s.digits

password="".join(choice(ch)for x in range(randint(8,16)))
print(password)


# In[ ]:





# In[ ]:





# In[ ]:




