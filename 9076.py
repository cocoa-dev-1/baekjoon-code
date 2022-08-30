T = int(input())

a = []

for i in range(T):
    n = list(map(int, input().split()))
    a.append(n)

for j in a:
    j.pop(j.index(max(j)))
    j.pop(j.index(min(j)))
    if (max(j) - min(j)) >= 4:
        print("KIN")
    else:
        print(sum(j))
