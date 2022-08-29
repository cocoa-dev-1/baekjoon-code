n, k = map(int, input().split())
a = list(map(int, input().split()))
change = 0

def Biggest(b):
    last = 0
    count = 0
    for i in range(0, b+1):
        if a[i] > last:
            last = a[i]
            count = i
    return last, count

for last in range(n-1, 0, -1):
    # print(last)
    big, num = Biggest(last)
    if last != num:
        a[num], a[last] = a[last], a[num]
        change += 1
    if change == k:
        break

if change < k:
    print("-1")
else:
    print(" ".join(str(e) for e in a))

