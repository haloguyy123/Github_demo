#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
import time
print('welcome to the guess the password!')
time.sleep(1)
print('*--------------------------------------*')
time.sleep(1)
passwords=['dog123','cat123','moose123','wolf123','dolphin123']
x=random.choice(passwords)
time.sleep(1)
user_answer=input('what is your guess?')
while not (user_answer==x):
        print('wrong, try again')
        user_answer=input('What is your new guess?')
if user_answer==x:
        print('CORRECT!')

