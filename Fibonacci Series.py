#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n=int(input())
#write your code here
x=[0,1]

for i in range(n-2):
    x.append((x[i]+x[i+1]))

for i in range(n):
    print(x[i])

