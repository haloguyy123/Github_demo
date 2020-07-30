#!/usr/bin/env python
# coding: utf-8

# In[1]:


import turtle
turtle0=turtle.Turtle()
turtle1=turtle.Turtle()
turtle2=turtle.Turtle()
turtle3=turtle.Turtle()


# In[3]:


turtle_list=[turtle0,turtle1,turtle2,turtle3]


# In[4]:


color_list=['red','blue','green','yellow']


# In[5]:


for i in range(4):
    turtle_list[i].color(color_list[i])
    turtle_list[i].penup()
    turtle_list[i].goto(-250, 100*(i-1.5))
    turtle_list[i].pendown()


# In[6]:


turtle_list[0].shape('turtle')
turtle_list[1].shape('turtle')
turtle_list[2].shape('turtle')
turtle_list[3].shape('turtle')


# In[7]:


import random
speed0=random.randint(1,10)
speed1=random.randint(1,10)
speed2=random.randint(1,10)
speed3=random.randint(1,10)


# In[8]:


speed=[speed0,speed1,speed2,speed3]


# In[10]:


for n in range(50):
    for i in range(4):
        turtle_list[i].forward(speed[i])


# In[18]:


for i in range(4):
    turtle_list[i].reset()


# In[9]:


linedrawer=turtle.Turtle()
linedrawer.penup()
linedrawer.goto(250,200)
linedrawer.right(90)
linedrawer.pendown()
linedrawer.forward(400)
linedrawer.ht()


# In[30]:


linedrawer.reset()


# In[ ]:




