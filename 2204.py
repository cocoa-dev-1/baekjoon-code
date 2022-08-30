li = []

# 32

while True:
    n = int(input())
    if n == 0:
        break
    last = ""
    for _ in range(n):
        b = input()
        a = b.upper()
        if len(last) == 0:
            last = b
            continue
        if len(last) >= len(b):
            for i in range(len(last)):
                if len(b) < i:
                    last = b
                if last[i] == a[i]:
                    continue
                last = last if ord(last[i]) < ord(a[i]) else b
                break
    li.append(last)

for i in li:
    print(i)
