n = int(input())
w = ''
z = 0
for i in range(n):
    m,o,p,q,r,s,t=input().split('-')
    u=2*int(q)+int(r)+20*int(s)+10*int(t)
    if(u>z):
        w=f'{m} {o} {p} {u}'
        z=u
print(w)