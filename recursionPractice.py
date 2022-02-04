#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 09:29:33 2022

@author: faizhilaly
"""
#factorial
def factorial(i):
   if i == 1:
       return i
   else:
       return i*factorial(i-1)

#countdown
def countdown(i):
    if i == 0:
        print("Blastoff")
    else:
        print(i)
        countdown(i-1)

#reverse
def reverse(i):
    if len(i) == 0:
        return i
    else:
        return reverse(i[1:]) + i[0]