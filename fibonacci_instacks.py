#sum of fibonacci series

# n = int(input())
# fact = 1
# sum = 1
# if n > 0:
#     print(1,end=" ")
#     for i in range(1,n+1):
#         fact = fact * i
#         sum = sum + fact
#         print("+",end=" ")
#         print(fact,end=" ")
#     print("=",end=" ")
#     print(sum)
# else:
#     print("Invalid Inputs")






# Write a program to print the Average of the Alternative Fibonacci Series in the Given Range?


# n = int(input())
# m = int(input())
# sum = 0
# count = 0
# a , b = 0 , 1
# if n > m:
#     n , m = m , n
# if n >= 0 and m >= 0:
#     ac = 0
#     while a <= m:
#         if a >= n:
#             ac = ac + 1
#             if ac % 2 == 1:
#                 sum = sum + a
#                 count = count + 1
#         c = a + b
#         a = b
#         b = c
#     if count == 0:
#         print("No Fibonacci Series Values")
#     else:
#         print("%.2f"%(sum/count))
# else:
#     print("Invalid Inputs")







#Write a program to print First N terms of Alternative Fibonacci Series?
# n = int(input())
# ac = 0
# count = 0
# a , b = 0 , 1
# if n < 0:
#     n = -(n)
# if n == 0:
#     print("Invalid Inputs")
# else:
#     for i in range(1,(n * 2)+1):
#         ac = ac + 1
#         if ac % 2 == 1:
#             count = count + 1
#             if count > 1:
#                 print(end=", ")
#             print(a,end=" ")
#         c = a + b
#         a = b
#         b = c


#Write a program to print First N terms in the Fibonacci Series?
# n = int(input())
# a , b = 0 , 1
# if n < 0:
#     n = -(n)
# if n == 0:
#     print("Invalid Inputs")
# else:
#     for i in range(1,n+1):
#         print(a,end=" ")
#         c = a + b
#         a = b
#         b = c


# Write a program to print the Average of the Fibonacci Series in Between the Given Range?

# n = int(input())
# m = int(input())
# a , b = 0 , 1
# sum = 0
# count = 0
# if n > m:
#     n , m = m , n
# if n >= 0 and m >= 0:
#     while a <= m:
#         if a >= n:
#             sum = sum + a
#             count = count + 1
#         c = a + b
#         a = b 
#         b = c
#     if count == 0:
#         print("No Fibonacci Series in given range")
#     else:
#         print("%.2f"%(sum/count))
# else:
#     print("Invalid Inputs")













#1+1+2+-----------------------  = sum



