for i in range(2, 101, 2):  
    print(i)
# Program to check whether a given number is prime or not
num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print(f"{num} is not a prime number")
            break
    else:
        print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")

# Program to find factorial of a number using loop
num = int(input("Enter a number: "))
fact = 1
for i in range(1, num + 1):
    fact *= i
print(f"Factorial of {num} is: {fact}")

# Program to print Fibonacci series up to N terms
N = int(input("Enter number of terms: "))
a, b = 0, 1
print("Fibonacci Series:")
for i in range(N):
    print(a, end=" ")
    a, b = b, a + b
