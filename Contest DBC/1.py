a,b = [int(i) for i in input().split()]

if(b <= 2):
    print('nova')
elif(b >= 97 and b <=100):
    print('cheia')
else:
    if(b <= 96 and b >= 3):
        if(b < a):
            print('minguante')
        else:
            print('crescente')