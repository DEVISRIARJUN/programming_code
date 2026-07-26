# n = int(input())
# rev = 0
# t = n
# while n > 0:
#     r = n % 10
#     sum = sum * 10 + r
#     n = n // 10
# if rev == t:
#     print("Palindrome ")
# else:
#     print("Not a Palindrome")


# Write a program to find Average of all Palindrome Numbers in the Range?
# a = int(input())
# b = int(input())
# a = abs(a)
# b = abs(b)
# if a == 0 or b == 0:
#     print("INVALID Inputs")
# elif a > b:
#     print("Given Inputs are Swapped")
# else:
#     c = 0
#     sum = 0
#     for i in range(a,b+1):
#         rev = 0
#         t = i
#         while i > 0:
#             r = i % 10
#             rev = rev * 10 + r
#             i = i // 10
#         if rev == t:
#             sum = sum + t
#             c = c + 1
#     if c == 0:
#         print("No Palindrome Values")
#     else:
#         print("%.2f"%(sum/c))
            



#Write A Program to check the Given Number is Perfect Square or not?
# import math
# n = int(input())
# n = abs(n)
# if n == 0:
#     print("Zero")
# else:
#     root = math.isqrt(n)
#     if root * root == n:
#         print("Given Number is Perfect Square.")
#     else:
#         print("Given Number is Not a Perfect Square.")



#  Write a program to check Given Number is Palindrome or Not.

# n = int(input())
# if n == 0:
#     print("InvAlid Input")
# else:
#     rev = 0
#     t = n
#     while n > 0:
#         r = n % 10
#         rev = rev * 10 + r
#         n = n // 10
#     if t == rev:
#         print("Palindrome")
#     else:
#         print("Not a Plaindrome")


#    Write a program to the check if the Given Number is a Palindrome or not and if it is a palindrome then Print PALINDROME, else Print the Reverse Value of a Given Number ?

# n = int(input())
# if n == 0:
#     print("Zero")
# if n >= 0:
#     rev = 0
#     t = n
#     while n > 0:
#         r = n % 10
#         rev = rev * 10 + r
#         n = n // 10
#     if rev == t:
#         print("Given Number is Palindrome")
#     else:
#         print(f"Reverse of a Given Number is {rev}")



#    Write a program to print Alternative Palindrome Numbers in the Given Range?

# a = int(input())
# b = int(input())
# if a <= 0 and b <= 0:
#     print("InvAlid InPUts")
# else:
#     ac = 0
#     c = 0
#     if a > b:
#         a , b = b , a
#     for i in range(a,b+1):
#         rev = 0
#         t = i
#         while i > 0:
#             r = i % 10
#             rev = rev * 10 + r
#             i = i // 10
#         if rev == t:
#             ac = ac + 1
#             if ac % 2 == 1:
#                 if ac > 1:
#                     print(end=", ")
#                 print(t,end="")
#                 c = c + 1
#     if c == 0:
#         print("No Plaindrome Values")
#     else:
#         print(".")


#   Write a program to Print the Reverse of a Given Number?


# n = int(input())
# n = abs(n)
# if n < 0:
#     print("InValid Inputs")
# else:
#     rev = 0
#     t = n
#     while n > 0:
#         r = n % 10
#         rev = rev * 10 + r
#         n = n // 10
#     print(rev)


#  Write a program to print all Palindrome Numbers between the Given Numbers?

# a = int(input())
# b = int(input())
# if a < 0 or b < 0:
#     print("Invalid Inputs")
# else:
#     if a > b:
#         a , b = b , a
#     c = 0
#     for i in range(a+1,b):
#         rev = 0
#         t = i
#         while t > 0:
#             r = t % 10
#             rev = rev * 10 + r
#             t = t // 10
#         if rev == i:
#             print(i)
#             c = c + 1
#     if c == 0:
#         print("No Plaindrome Values")


#  Write a program to swap the two given numbers.

# a = int(input())
# b = int(input())
# a , b = b , a
# print(a)
# print(b)


#   Write a program to print the Sum of all Alternative Palindrome Numbers Between the Given Numbers?

# a = int(input())
# b = int(input())
# a = abs(a)
# b = abs(b)
# if a == 0 or b == 0:
#     print("Invalid Inputs")
# else:
#     sum = 0
#     ac = 0
#     c = 0
#     if a > b:
#         a , b = b , a
#     for i in range(a+1,b):
#         t = i
#         rev = 0
#         while i > 0:
#             r = i % 10
#             rev = rev * 10 + r
#             i = i // 10
#         if rev == t:
#             ac = ac + 1
#             if ac % 2 == 1:
#                 sum = sum + t
#                 c = c + 1
#                 if c == 1:
#                     print(f"Sum of alternative palinrome numbers between {a} adn {b} is ",end="")
#                 if c > 1:
#                     print(" + ",end="")
#                 print(t,end="")
#     if c == 0:
#         print("No palindromes")
#     else:
#         print(f" = {sum}.")


# a = int(input())
# b = int(input())
# a = abs(a)
# b = abs(b)
# if a == 0 or b == 0:
#     print("Invalid Inputs")
# else:
#     if a > b:
#         a , b = b , a
#     sum = 0
#     c = 0
#     for i in range(a+1,b):
#         t = i
#         rev = 0
#         while i > 0:
#             r = i % 10
#             rev = rev * 10 + r
#             i = i // 10
#         if t == rev:
#             sum = sum + t
#             c = c + 1
#     if c == 0:
#         print("No palindromes")
#     else:
#         print(sum)


# n = int(input())
# if n == 0:
#     print("Invalid Input")
# elif n < 0:
#     print("Sorry you have entered negtive values")
# else:
#     sum = 0
#     for i in range(1,n+1):
#         sum = sum + i
#         print(i,end="")
#         if i < n:
#             print(" + ",end="")
#     print(" = ",sum)



# n = int(input())
# sum = 0
# c = 0
# if n == 0:
#     print("InvaLid Input.")
# elif n < 0:
#     print("Sorry! you have Entered Negative Values.")
# else:
#     for i in range(1,n+1):
#         sum = sum + i
#         c = c + 1
#         if c == 1:
#             print("Sum of 'N' Natural Numbers is ",end="")
#         if c > 1:
#             print(end=" + ")
#         print(i,end="")
#     print(f" = {sum}.")


# n = int(input())
# c = 0
# if n > 0:
#     rev = 0
#     t = n
#     while t > 0:
#         r = t % 10
#         rev = rev * 10 + r
#         t = t // 10
#     while rev >0:
#         r = rev % 10
#         rev = rev // 10
#         c = c + 1
#         if c > 1:
#             print(" + ",end="")
#         print(r,end="")
#     print(".")




# n = int(input())
# sum = 0
# c = 0
# if n == 0:
#     print("InvaLid Input.")
# elif n < 0:
#     print("Sorry you have entered negative values")
# else:
#     for i in range(1,n+1):
#         sum = sum + i
#         c = c + 1
#         if c == 1:
#             print("Sum of 'N' Natural numbers is ",end="")
#         if c > 1:
#             print(end=" + ")
#         print(i,end="")
#     print(f" = {sum}.")
    
