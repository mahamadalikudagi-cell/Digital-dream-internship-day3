num = int(input("Enter a number: "))
if num > 0:
    print("number is positive.")
elif num < 0:
    print("number is negative.")
else:
    print("number is zero.")

# Checke the even and idd
if num % 2 == 0:
    print("number is even.")
else:
    print("number is odd.")

#largest of three number
a=int(input("enter first number:"))
b=int(input("enter second number:"))
c=int(input("enter third number:"))
if(a>=b)and(a>=c):
 print("largest number is",a)
elif(b>=a)and(b>=c):
    print("largest number is",b)
else:
    print("largest number is",c)

#check the lap year
    year=int(input("enter a year:"))
    if(year%4==0 and year%100!=0)or(year%400==0):
        print(year,"is a leap year")
    else:
        print(year,"is not a leap year")