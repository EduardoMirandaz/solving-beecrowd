#  Problema 1141
# https://www.beecrowd.com.br/judge/pt/problems/view/1141

def max_thread(l, v):
    for i in range(len(l)):


out = ''
while(True):
    n = int(input())
    if(not n): break
    l = []
    [l.append(input()) for i in range(n)]
    l = sorted(list(set(l)))
    max_seq_l = []
    [max_seq_l.append(max_thread(l,0))]
    print(max_seq_l)
