normal_sum=0
complex_sum=0
n = int(input())
for i in range(n):
    c = input()[:-1]
    m = c.rfind('-')

    op = m if m!=-1 else c.rfind('+')

    normal_sum += int(c[:op])
    complex_sum += int(c[op:])

print('sum')
print(f'{normal_sum}{"+" if complex_sum > 0 else ""}{complex_sum}i')
print('square')
print(f'{normal_sum**2 - complex_sum**2}{"+" if complex_sum*normal_sum >= 0 else ""}{2*complex_sum*normal_sum}i')


# Example:
# 3
# 0+1i
# -2-3i
# 4+5i