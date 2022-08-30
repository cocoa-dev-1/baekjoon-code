w = []
k = []
for j in range(2):
    for i in range(10):
        if j == 0:
            w.append(int(input()))
        else:
            k.append(int(input()))

ww = 0
kk = 0

for i in range(2):
    for j in range(3):
        if i == 0:
            ww += w.pop(w.index(max(w)))
        else:
            kk += k.pop(k.index(max(k)))

print(ww, kk)
