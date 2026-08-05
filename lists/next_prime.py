#  print the next prime numbers in agiven list
l = list(map(int,input().split()))
for i in range(len(l)):
    n = abs(l[i]) + 1
    while True:
        prime = True
        if n < 2:
            prime = False
        else:
            for j in range(2,n):
                if n % j == 0:
                    prime = False
                    break
        if prime:
            print(n,end=" ")
            break
        n = n + 1