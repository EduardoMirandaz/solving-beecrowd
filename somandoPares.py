n = input()
m = [int(i) if not(int(i) % 2) else 0 for i in input().split()]
print(sum(m))