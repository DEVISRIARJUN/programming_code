#smallest digits in a given number
    # n = int(input())
    # s = 9
    # while(n > 0):
    #     r = n % 10
    #     if r < s:
    #         s = r
    #     n = n // 10
    # print(s)


#largest digits in a given number
# n = int(input())
# l = 0
# while(n > 0):
#     r = n % 10
#     if r > l:
#         l = r
#     n = n // 10
# print(l)


#perfect square in a given number
import math
n = int(input())
    root = math.isqrt
    if root * root == n:
        print(f"{n} is a perfect square")
    else:
        print(f"{n} is not a perfect square")