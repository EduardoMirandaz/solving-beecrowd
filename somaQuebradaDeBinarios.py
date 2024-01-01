a=input();b=[[],[],[],[],[],[],[]];
for i in a:
    [b[c].append(j) for c,j in enumerate(list(str(bin(ord(i)))[2:]))]
[print(''.join(i)) for i in b]

