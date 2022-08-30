n = int(input())
a = []

for i in range(n):
    a.append(int(input()))

for j in range(n):
    print(a.pop(a.index(min(a))))
