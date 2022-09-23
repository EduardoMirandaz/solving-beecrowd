#  Problema 1168
# https://www.beecrowd.com.br/judge/pt/problems/view/1168

a = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
n = int(input())
out=''
while(n):
    b = 0
    for i in input():
        b+=a[int(i)]
    out+= str(b) + ' leds\n' 
    n-=1
print(out, end='')