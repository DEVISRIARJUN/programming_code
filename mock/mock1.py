#printing like 1,A,@,1,A,@

# a=int(input())
# if a == 0:
#     print("Zero")
# else:
#     a=abs(a)
#     c=0
#     for i in range(1,a+1):
#         c=c+1
#         if c>1:
#             print(end=", ")
#         if i%3==1:
#             print(1,end="")
#         elif i%3==2:
#             print("A",end="")
#         else:
#             print("@",end="")
#     print()



# 2)athemetic calculations using the switch case


# a=int(input())
# b=int(input())
# op=input()
# match op:
#     case "+":
#         print(a+b)
#     case "-":
#         print(a-b)
#     case "*":
#         print(a*b)
#     case "/":
#         print(a/b)



#3)celcius to fahrenheit

# n=int(input())
# c=(n*9/5)+32
# print(f"{c}F")


#4)fahrenheit to celcius

# n=int(input())
# f=(n-32)*5/9
# print(f"{f}C")



# write a program to perform all these tasks
# a.     Store a number in a variable
# b.    If value is not in range (100-1000) prints WRONG NUMBER else follows the steps
# c.     Check even or odd
# d.    If even divide the number by 3 and print the remainder
# e.     If odd divide the number by 2 and print the remainder.


# n=int(input())
# if n>=100 and n<=1000:
#     if n%2==0:
#         n=n%3
#         print(n)
#     else:
#         n=n%2
#         print(n)

# n=int(input())
# n1=int(input())
# for i in range(n,n1+1):
#     if i%2==0:
#         print(i,end=" ")


# n=int(input())
# l=[]
# for i in range(1,n+1):
#     l.append("A,B")    #A,B,A,B,A,B,A,B
# print(",".join(l))


# n=int(input())
# n1=int(input())
# if n%2==0:
#     n=n+2
# else:
#     n=n+1
# for i in range(n,n1+1,4):
#     print(i,end=" ")        #12 14 18.....

# a=int(input())
# b=int(input())
# l=[]
# if a>b:
#     for i in range(a,b-1,-1):
#         l.append(f"{i}@{i-1}")
# else:
#     for i in range(a,b+1):
#         l.append(f"{i}@{b+1}")  
# print(",".join(l))               #10@9,9@8,8@7,7@6,6@5,5@4,4@3,3@2,2@1,1@0,0@-1,-1@-2,-2@-3,-3@-4,-4@-5,-5@-6




# a=int(input())
# b=int(input())
# if a>b:
#     a,b=b,a
# for i in range(a,b+1):
#     if i == b:
#         print(f"{i}*{i+1}",end="")
#     else:
#         print(f"{i}*{i+1}",end=",")
# print()
# for i in range(a,b+1):
#     if i == b:
#         print(i*(i+1),end="")
#     else:
#         print(i*(i+1),end=",")



# n=int(input())
# n1=int(input())
# c=0
# if n%2==1:
#     n=n+1
# else:
#     for i in range(n,n1+1,4):    
#         if i%2==0:
#             c=c+1
#             if c>1:
#                 print(end=", ")
#             print(i,end="")       #10,14,18,22......


# a=int(input())
# b=int(input())
# sum=0
# for i in range(a+1,b):
#     if i%2==0:
#         sum=sum+i
# print(sum)


# n = int(input())
# c = 0
# for i in range(1,n+1):
#     c=c+1
#     if c > 1:
#         print(end=", ")
#     if  i % 3 == 0:
#         print("factor of three",end="")
#     else:
#         print(i,end="")


# n=float(input())
# n1=float(input())
# c=0
# while round(n,1) <= n1:
#     c=c+1
#     if c>1:
#         print(end=",")
#     print(f"{n:.1f}^2",end=" ")
#     n=n+0.2
# print(".")                     #10.7^2 ,10.9^2 ,11.1^2 ,11.3^2 ,11.5^2 ,11.7^2 ,11.9^2 ,12.1^2 .





# if input is 10 and -5

# output will be 10@9,9@8,8@7,7@6,6@5,5@4,4@3,3@2,2@1,1@0,0@-1,-1@-2,-2@-3,-3@-4,-4@-5,-5@-6

# a=int(input())
# b=int(input())
# c=0
# if a>b:
#     for i in range(a,b-1,-1):
#         c=c+1
#         if c>1:
#             print(end=",")
#         print(f"{i}@{i-1}",end="")
# else:
#     for i in range(a,b+1):
#         c=c+1
#         if c>1:
#             print(end=",")
#         print(f"{i}@{i+1}",end="")




# a=int(input())
# b=int(input())
# c=0
# if a>b:
#     for i in range(a,b-1,-1):
#         c=c+1
#         if c>1:
#             print(end=", ")
#         if i<0:
#             print(f"({i*5})",end="")
#         else:
#             print(i*5,end="")
# else:
#     for i in range(a,b+1):
#         c=c+1
#         if c>1:
#             print(end=", ")
#         if i<0:
#             print(f"({i*5})",end="")
#         else:
#             print(i*5,end="")




        

# a=int(input())
# b=int(input())
# c=0
# if a<0 and b<0:
#     print("Invalid Inputs")
# else:
#     for i in range(a,b+1):
#         fc = 0
#         for j in range(1,i+1):
#             if i%j==0:
#                 fc=fc+1
#         if fc==2:
#             c=c+1
#             if c>1:
#                 print(end=", ")
#             print(i,end="")



# prime number without using factor count

# a=int(input())
# b=True
# for i in range(2,int(a**0.2)+1):
#     if a%i==0:
#         b=False
#         break
#     if b==True and a>1:
#         print("primenumber")
#     else:
#         print("not a prime number")


# n=int(input())
# n1=int(input())
# c=0
# ac=0
# if n>0 and n1>0:
#     for i in range(n,n1+1):
#         fc=0
#         for j in range(1,i+1):
#             if i%j==0:
#                 fc=fc+1
#         if fc==2:
#             ac=ac+1
#             if ac%2==1:
#                 c=c+1
#                 if c>1:
#                     print(end=", ")
#                 print(i,end="")              #9, 37, 43, 53, 61, 71, 79, 89



# n=int(input())
# s=9
# if n>0:
#     while n>0:
#         r=n%10
#         if s<r:
#             s=r
#         n=n//10
#     print(f"smallest digit is {2}")
# else:
#     print("Invalid Input")    #smallest digit in agiven number



# n=int(input())
# l=0
# if n>0:
#     while n>0:
#         r=n%10
#         if r>l:
#             l=r
#         n=n//10
#     print(f"largest digit is {l}")
# else:
#     print("Invalid Input")


# n=int(input())
# c=0
# if n>0:
#     rev=0
#     t=n
#     while t>0:
#         r=t%10
#         rev=rev*10+r
#         t=t//10
#     while rev>0:
#         r=rev%10
#         rev=rev//10
#         c=c+1
#         if c>1:
#             print(end=" + ")
#         print(r,end="")              #input:25689  ----->2 + 5 + 6 + 8 + 9




# n=int(input())
# c=0
# sum=0
# if n>0:
#     for i in range(1,n+1):
#         sum=sum+i
#         c=c+1
#         if c==1:
#             print("sum of 'N' natural numbers is",end=" ")
#         if c>1:
#             print(end=" + ")
#         print(i,end="")
#     print(f" = {sum}.")



# a=int(input())
# b=int(input())
# c=0
# if a<0 or b<0:
#     print("No Palindrome Values")
# else:
#     if a>b:
#         a,b=b,a
#     for i in range(a+1,b):
#         rev=0
#         t=i
#         while i>0:
#             r=i%10
#             rev=rev*10+r
#             i=i//10
#         if t==rev:
#             c=c+1
#             if c>1:
#                 print(end=", ")
#             print(t,end=" ")
#     if c==0:
#         print("No Plaindrome values")



# n=int(input())
# m=int(input())
# cou=0
# a=0
# b=1
# sum=0
# if n>=0 and m>=0:
#     if n>m:
#         n,m=m,n
#     while a<=m:
#         if a>=n:
#             # print(a,end=" ")
#             sum=sum+a
#             cou=cou+1
#         c=a+b
#         a=b
#         b=c
#     if c==0:
#         print("No Fibonacci Series Values")
#     else:
#         print("%.2f"%(sum/cou))



# n=int(input())
# sum=1
# fact=1
# print(1,end="")
# for i in range(1,n+1):
#     fact=fact*i
#     sum=sum+fact
#     print("+",end="")
#     print(fact,end="")
# print(f"={sum}")


# n=int(input())
# ac=0
# count=0
# a,b=0,1
# if n==0:
#     print("Invalid Input")
# else:
#     n=abs(n)
#     for i in range(1,(n*2)+1):
#         ac=ac+1
#         if ac%2==1:
#             count=count+1
#             if count>1:
#                 print(end=", ")
#             print(a,end="")
#         c=a+b
#         a=b
#         b=c



# n1=int(input())
# n2=int(input())
# n3=int(input())
# if n1<=0 and n2<=0 or n2<=0 and n3<=0 or n3<=0 and n1<=0:
#     print("Invalid Inputs")
# else:
#     l=min(n1,n2,n3)
#     for i in range(l,0,-1):
#         if n1%i==0 and n2%i==0 and n3%i==0:
#             print(i)
#             break



# n1=int(input())
# n2=int(input())
# n3=int(input())
# if n1<=0 and n2<=0 or n2<=0 and n3<=0 or n3<=0 and n1<=0:
#     print("Invalid Inputs")
# else:
#     l=max(n1,n2,n3)
#     k=l
#     while True:
#         if l%n1==0 and l%n2==0 and l%n3==0:
#             print(l)
#             break
#         l=l+k



# n = int(input())
# n1 = int(input())
# if n <= 0 and n1 <= 0:
#     print("Invalid Row and Column Values")
# elif n <= 0:
#     print("Invalid Row Value")
# elif n1 <= 0:
#     print("Invalid Column Value")
# else:
#     c = 1
#     for i in range(1,n+1):
#         for j in range(1,n1+1):
#             if j > 1:
#                 print("*",end="")
#             print(c,end="")
#             c = c + 1
#         print()




a=int(input())
b=int(input())
for i in range(1,a+1):
    sum=0
    for j in range(1,i+1):
        print(b,end=" ")
        sum=sum+a
        b=b+2
        


            

