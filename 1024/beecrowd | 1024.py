#  Problema 1024
# https://www.beecrowd.com.br/judge/pt/problems/view/1024


n = int(input())

for i in range(n):
    string = list(input())
    size = len(string)
    for i, letra in enumerate(string):
        ord_letra = int(ord(letra))
        if((ord_letra >= 65 and ord_letra <= 90) or (ord_letra >= 97 and ord_letra <= 122)):
            ord_letra+=3
            string[i] = chr(ord_letra)

    string = string[::-1]

    print(''.join(string[:size//2]), end='')

    print(''.join( [ chr(int(ord(k)-1)) for k in string[size//2:] ] ))