while True:
    n = int(input())
    if n == 0:
        break
    array = []
    array_origin = []
    for _ in range(n):
        txt = input()
        array.append(txt.upper())
        array_origin.append(txt)
    array_sorted = sorted(array)
    result = array.index(array_sorted[0])
    print(array_origin[result])
