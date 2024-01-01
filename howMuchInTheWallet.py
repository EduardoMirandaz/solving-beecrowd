n = int(input())
am=0
for i in range(n):
    inputs = input().split()
    name = inputs[0]
    amount = int(inputs[1])

    if('cent' in name):
        am+=0.01*float(name[:name.index('-')])*amount
    else:
        am+=float(name[:name.index('-')])*amount

print('${:.2f}'.format(am))

# Sample

# 4
# 20-dollar-bill 1
# 5-dollar-bill 2
# 1-dollar-bill 3
# 25-cent-coin 2