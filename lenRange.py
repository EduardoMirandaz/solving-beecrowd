n = int(input())
if(n<500):
    print(len(range(n, 1000-n)))
else:
    print('-'+str(len(range(1000-n, n))))
    