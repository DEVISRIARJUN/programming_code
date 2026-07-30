l = [10,15,20,13,8,9,80]
s = float("inf")
s2 = s1 = s
for i in range(len(l)):
    if l[i] < s:
        s1 = s
        s2 = s1
        s = l[i]
    elif l[i] < s2:
        s2 = l[i]
    elif l[i] < s1:
        s1 = l[i]
print(s1)