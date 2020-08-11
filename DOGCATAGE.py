#!/usr/bin/env python
# coding: utf-8

# In[22]:


CAT_DOG=input("Do you own a dog or a cat?")
if CAT_DOG==str('dog'):
    Dog_age=int(input("How old is your dog?"))
    if Dog_age==1:
        print('12')
    else:
        x=Dog_age*4+16
        print(x)
if CAT_DOG==str('cat'):
    Cat_age=int(input("How old is your cat?"))
    if Cat_age==1:
        print('15')
    else:
        y=Cat_age*4+16
        print(y)

