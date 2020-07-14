#!/usr/bin/env python
# coding: utf-8

# In[17]:


foodfee=int(input('How much does your food cost?'))


# In[ ]:


tax=float(input('What is the tax of your state?'))


# In[1]:


tip_or_no=input('Will you leave any tips?')
x='yes'
if tip_or_no==x:
    tip=float(input('How much money will you leave?'))
else:print('Ok, the total fee is YOU MUST PAY TIP OR ELSE YOU CAN NOT LEAVE!!!')


# In[ ]:


finalbill=foodfee+tip+tax
print('Your final fee is',finalbill, 'dollars')

