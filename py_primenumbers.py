#program to print prime number or not
# a = int(input())
# fc = 0
# for i in range(1,a+1):
#     if a % i == 0:
#         fc = fc + 1
# if fc == 2:
#     print("Prime number ")
# else:
#     print("Not a Prime number")


#program to print prime numbers  in given range

# a = int(input())
# b = int(input())
# for i in range(a,b+1):
#     fc = 0
#     for j in range(1,i+1):
#         if i % j == 0:
#             fc = fc + 1
#     if fc == 2:
#         print(i,end=" ")


#program to print factors of a number:
# n = int(input())
# for i in range(1,n+1):
#     if n % i == 0:
#         print(i,end=" ")
                        


#program to print a perfect square of a number

# import math
# n = int(input())
# if n <= 0:
#     print("INvalid Input")
# else:
#     root = math.isqrt(n)
#     if root * root == n:
#         print("It is a perfect square")
#     else:
#         print("Not a perfect square")



#alternative prime numbers

# n = int(input())
# ac = 0
# for i in range(1,n+1):
#     fc = 0
#     for j in range(1,i+1):
#         if i % j == 0:
#             fc = fc + 1
#     if fc == 2:
#         ac = ac + 1
#         if ac % 2 == 1:
#             print(i)


#alternative prime numbers of two inputs


# n = int(input())
# m = int(input())
# ac = 0
# for i in range(n,m+1):
#     fc = 0
#     for j in range(1,i+1):
#         if i % j == 0:
#             fc = fc + 1
#     if fc == 2:
#         ac = ac + 1
#         if ac % 2 == 1:
#             print(i)

#alternative prime numbers with commas
# a = int(input())
# b = int(input())
# al = 0
# for i in range(a,b+1):
#     fc = 0
#     for j in range(1,i+1):
#         if i % j == 0:
#             fc = fc + 1
#     if fc == 2:
#         al = al + 1
#         if al % 2 == 1:
#             if al > 1:
#                 print(end=", ")

#             print(i,end=" ")


# a = int(input())
# b = int(input())
# al = 0
# c = 0
# for i in range(a,b+1):
#     fc = 0
#     for j in range(1,i+1):
#         if i % j == 0:
#             fc = fc + 1
#     if fc == 2:
#         al = al + 1
#         if al % 2 == 1:
#             if al > 1:
#                 print(end=", ")
#             print(i,end=" ")


#prime numbers program
# n = int(input())
# for i in range(1,n+1):
#     fc = 0
#     if n % i == 0:
#         fc = fc + 1
#     if fc == 2:
#        print("Prime number")
#     else:
#         print("Not a prime number")



#prime numbers in a given range
# a = int(input())
# b = int(input()) 
# c = 0
# for i in range(a,b+1):
#     fc= 0
#     for j in range(1,i+1):
#         if i % j == 0:
#             fc = fc + 1
#     if fc == 2:
#         c = c + 1
#         if c > 1:
#             print(end=", ")
#         print(i,end=" ")


#prime numbers without using count

# a = int(input())
# b = True
# if a > 0:
#     for i in range(2,int(a**0.5)+1):
#         if a % i == 0:
#             b = False
#             break
#         if b == True and a > 1:
#             print("Prime Number")
#         else:
#             print("Not a prime number")



#sum of all the prime numbers between given values
# a = int(input())
# b = int(input())
# sum = 0
# for i in range(a+1,b):
#     fc = 0
#     for j in range(1,i+1):
#         if i % j == 0:
#             fc = fc + 1
#     if fc == 2:
#         sum = sum + i
# print(sum)

#sum of alternative prime numbers between range using comma logic
# a = int(input())
# b = int(input())
# sum = 0
# ac = 0
# if a > 0 and b > 0:
#     for i in range(a+1,b):
#         if i > 1:
#             fc = 0
#             for j in range(1,i+1):
#                 if i % j == 0:
#                     fc = fc + 1
#             if fc == 2:
#                 ac = ac + 1
#                 if ac % 2 == 1:
#                     sum = sum + i
#     print(sum)
# else:
#     print("Invalid Input")



#write a program to print all prime factors in a given number
n = int(input())
c = 0
for i in range(1,n+1):
    fc = 0
    if n % i == 0:
        for j in range(1,i+1):
            if i % j == 0:
                fc = fc + 1
        if fc == 2:
            print(i,end=" ")
            c = c + 1
            



