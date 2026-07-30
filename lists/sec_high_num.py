l = [10,40,25,6,89,30]
h = float("-inf")
h1 = h
for i in range(len(l)):
    if l[i] > h:
        h1 = h
        h = l[i]
    elif l[i] > h1:
        h1 = l[i]
print(h1)