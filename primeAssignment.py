# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 09:13:46 2021
@author: Richard Paglia

Prime Numbers Assignment
"""

initial = 2
ending = 1000


# Python program to display all the prime numbers within an interval

# lower = 900
# upper = 1000

# print("Prime numbers between", lower, "and", upper, "are:")

for prime in range(initial, ending + 1):
    
    if prime > 1:
        for i in range(2, prime):
            if (prime % i) == 0:
                break
        else:
            print(prime, end=(', '), flush=True)

