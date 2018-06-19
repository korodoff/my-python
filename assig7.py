# what is time tuple?
# time tuple is a useage of tuple in used for the ordering and notation of time
import time
print(time.gmtime())
# wirte a program to get format time
print(time.asctime(time.gmtime()))

import datetime
d=datetime.date.today()
print("today month is",d.month)

import datetime
d=datetime.date.today()
print("today day is",d.day)

import datetime
from datetime import date
print("6 in",date.today())

#WAP Time Using Local Time
import time
print(time.localtime())

#Find the Factorial of a Number
import math
n=int(input("enter any no "))
print("factiorial is:",math.factorial(n))

#Find the GCD of a Number
import math
n=int(input("enter any no1:"))
m=int(input("enter no 2:"))
print(math.gcd(n,m))

#Use OS package
import os
print(os.getcwd())
print(os.listdir)
print(os.environ)





