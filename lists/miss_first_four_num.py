#missing of the first four smallest numbers in agiven list

l = [6,81,7,15,11,37,23,13,27,16]
k = min(l) + 1
c = 0
while True:
    if k not in l:
        print(k,end=" ")
        c = c + 1
    if c == 4:
        break
    k = k + 1
