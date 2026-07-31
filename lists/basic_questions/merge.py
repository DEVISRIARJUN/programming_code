# 3. Write a program to merge two lists into a single list. 

l1 = [10,20,30,40,50]
l2 = [20,30,50,69,70,90,89]
# l3 = l1+ l2
# print(l3)
l1.extend(l2)
print(l1)