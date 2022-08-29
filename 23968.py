n, k = map(int, input().split())
a = list(map(int, input().split()))

change_count = 0

for i in range(n-1, 0, -1):
    for j in range(0, i):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            change_count += 1
            if change_count == k:
                print(a[j], a[j+1])

if change_count < k:
    print("-1")