a = []

for i in range(9):
    a.append(int(input()))

b = sum(a)

for i in range(9):
    for j in range(i+1, 9):
        if b - (a[i]+a[j]) == 100:
            one, two = a[i], a[j]
            break

a.remove(one)
a.remove(two)

for i in sorted(a):
    print(i)
