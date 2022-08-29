n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
equal = 0

def Biggest(b):
    idx = 0
    for i in range(0, b+1):
        if a[i] > a[idx]:
            idx = i
    return idx

if a == b:
    equal += 1

for last in range(n-1, 0, -1):
    # print(last)
    idx = Biggest(last)
    if last != idx:
        a[idx], a[last] = a[last], a[idx]
        if a == b:
            equal += 1

if equal == 0:
    print("0")
else:
    print("1")