m = input()
k = input()
k=k*(len(m)//len(k)+1)
r=''
for i,j in enumerate(m):
    r+='1' if j!=k[i] else '0'
print(r)
