#  Problema 1120
# https://www.beecrowd.com.br/judge/pt/problems/view/1120
out = ''
while(True):
    a, b = input().split()
    if(a == '0' and b == '0'): break
    sub = b.replace(a, '')
    [int(i) for i in sub]
    if(len(set(sub)) == 1 and sub[0] == '0'):
        out+='0\n'
    else:
        out += str(int(sub)) if len(sub)>=1 else '0'
        out += '\n'
print(out, end='')