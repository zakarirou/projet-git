#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 17:13:09 2020

@author: zakaria
"""

a=['2','3','4','2']
b=list(map(int,a))
c=[int(x) for x in a]
d=a.map(lambda x: int(x))
a[len(a)-1]
a.reverse()

a=set([1,2,3])
b={}
c=set()
b={3,4,5}
c.add(5)
class A:
    def test(self):
        print("A")
    def __init__(self):
        self.test()
class B :
    def __init__(self):
        A.test(self)

a=A()
b=B()



"kkkkkk'
from datetime import datetime
from datetime import timedelta
#Add 1 day.
print (datetime.now() + timedelta(days=1))
#Subtract 60 seconds.
print (datetime.now() + timedelta(days=60))
#Add 2 years.
j = True
k = False
not (j and k)


a=[10,4,7,1,5,8,2,3,2]

a.sort()


import numpy as np
a=np.zeros((300,300,3))
a=a.astype(int)
















