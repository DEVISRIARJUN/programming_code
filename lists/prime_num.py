# print the prime numbers in a given list

l = list(map(int,input().split()))
c = 0
for i in l:
    if i > 1:
        prime = True
        for j in range(2,i):
            if i % j == 0:
                prime = False
                break
        if prime:
            print(i,end=" ")
            c = c + 1
if c == 0:
    print("No Prime Numbers")




# if input ----->    18 15 7 93 11 6 31 9    -------- > output : 7 11 31