import sys
import math

s = input()
a=0
for i,j in enumerate(s):
    a+= int(ord(j)) * i
print(a)