import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

b = int(input())
p = int(input())
r = int(input())
t = int(input())
a = p*r*t

if(a == b):
    print('Just enough bread')
elif(a<b):
    print('Enough bread')
else:
    print('Not enough bread')

    