t = int(input())
result = []
for i in range(t):
    a, b = map(int, input().split())
    result.append([a, b])

for j in result:
    aa = j[0] % 10

    if aa == 0:
        print(10)
    elif aa in [1, 5, 6]:
        print(aa)
    elif aa in [4, 9]:
        if j[1] % 2 == 1:
            print(aa)
        else:
            print(aa*2 % 10)
    else:
        b = j[1] % 4
        if b == 0:
            print((aa**4) % 10)
        else:
            print((aa**b) % 10)
